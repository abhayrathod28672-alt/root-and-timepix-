#!/usr/bin/env python3
"""
Match TimePix TrackLab measurements to BL4S TDAQ ROOT runs.

TDAQ ROOT files are expected to be named with the TDAQ run number, where the
run number is the Unix start time, for example 1786800039.root.  The end time is
computed from the scaler channel-15 1 MHz clock, including 32-bit counter wraps.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import math
import os
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path


U32_MODULUS = 2**32
DEFAULT_ROOT = "/Users/berare/ROOT/latest_stable/root-build/bin/root"
RUN_START_TOLERANCE_SECONDS = 180.0


@dataclass(frozen=True)
class TDAQRun:
    root_file: Path
    run_number: int
    start_unix: float
    elapsed_seconds: float
    end_unix: float
    entries: int
    scaler_branch: str
    wraps: int
    first_count: int
    last_count: int
    status: str


@dataclass(frozen=True)
class TimePixMeasurement:
    measurement_file: Path
    trigger_file: Path | None
    measurement_id: str
    start_unix: float
    trigger_end_unix: float | None
    max_trigger_seconds: float | None


def iso_utc(unix_time: float | None) -> str:
    if unix_time is None or math.isnan(unix_time):
        return ""
    return dt.datetime.fromtimestamp(unix_time, tz=dt.timezone.utc).isoformat()


def numeric_root_files(root_dir: Path) -> list[Path]:
    return sorted(
        path
        for path in root_dir.glob("*.root")
        if re.fullmatch(r"\d+", path.stem)
    )


def parse_timepix_start(path: Path) -> float | None:
    pattern = re.compile(r"^# Start of measurement - unix time:\s*([0-9]+(?:\.[0-9]+)?)")
    with path.open("r", encoding="utf-8", errors="replace") as handle:
        for line in handle:
            match = pattern.match(line.strip())
            if match:
                return float(match.group(1))
            if not line.startswith("#"):
                break
    return None


def parse_trigger_max_seconds(path: Path) -> float | None:
    max_seconds: float | None = None
    with path.open("r", encoding="utf-8", errors="replace") as handle:
        for line in handle:
            if not line.strip() or line.startswith("#"):
                continue
            fields = line.split()
            if len(fields) < 2:
                continue
            try:
                seconds = float(fields[1])
            except ValueError:
                continue
            max_seconds = seconds if max_seconds is None else max(max_seconds, seconds)
    return max_seconds


def measurement_id(path: Path) -> str:
    match = re.fullmatch(r"measurement(?:_(\d+))?", path.stem)
    if not match:
        return path.stem
    return match.group(1) or "0"


def read_timepix_measurements(data_dir: Path) -> list[TimePixMeasurement]:
    measurements: list[TimePixMeasurement] = []
    for path in sorted(data_dir.glob("measurement*.txt")):
        if path.stem.endswith("_trigger"):
            continue
        start_unix = parse_timepix_start(path)
        if start_unix is None:
            continue
        mid = measurement_id(path)
        trigger = path.with_name(f"measurement_{mid}_trigger.txt") if mid != "0" else path.with_name("measurement_trigger.txt")
        if not trigger.exists():
            trigger = path.with_name(f"{path.stem}_trigger.txt")
        if not trigger.exists():
            trigger = None
        max_trigger_seconds = parse_trigger_max_seconds(trigger) if trigger else None
        measurements.append(
            TimePixMeasurement(
                measurement_file=path,
                trigger_file=trigger,
                measurement_id=mid,
                start_unix=start_unix,
                trigger_end_unix=start_unix + max_trigger_seconds if max_trigger_seconds is not None else None,
                max_trigger_seconds=max_trigger_seconds,
            )
        )
    return sorted(measurements, key=lambda item: item.start_unix)


def root_macro_text() -> str:
    return r'''
#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <set>
#include <string>
#include <vector>
#include "TBranch.h"
#include "TFile.h"
#include "TObjArray.h"
#include "TString.h"
#include "TTree.h"

static std::string shell_quote(const std::string& value) {
  std::string out = "'";
  for (char c : value) {
    if (c == '\'') out += "'\\''";
    else out += c;
  }
  out += "'";
  return out;
}

static std::vector<std::string> discover_scaler_prefixes(TTree* tree) {
  std::set<std::string> prefixes;
  TObjArray* branches = tree->GetListOfBranches();
  for (int i = 0; i < branches->GetEntries(); ++i) {
    std::string name = branches->At(i)->GetName();
    const std::string suffix = "_ch15";
    if (name.size() <= suffix.size() || name.substr(name.size() - suffix.size()) != suffix) continue;
    std::string prefix = name.substr(0, name.size() - suffix.size());
    bool has_all = true;
    for (int ch = 0; ch < 16; ++ch) {
      std::string candidate = prefix + "_ch" + std::to_string(ch);
      if (!tree->GetBranch(candidate.c_str())) {
        has_all = false;
        break;
      }
    }
    if (has_all) prefixes.insert(prefix);
  }
  std::vector<std::string> result(prefixes.begin(), prefixes.end());
  std::stable_sort(result.begin(), result.end(), [](const std::string& a, const std::string& b) {
    bool as = TString(a).Contains("Scaler", TString::kIgnoreCase);
    bool bs = TString(b).Contains("Scaler", TString::kIgnoreCase);
    if (as != bs) return as > bs;
    return a < b;
  });
  return result;
}

void extract_scaler_runs(const char* list_path, const char* out_path, const char* requested_branch) {
  std::ifstream input(list_path);
  std::ofstream out(out_path);
  out << "root_file\trun_number\tentries\tscaler_branch\twraps\tfirst_count\tlast_count\telapsed_seconds\tstatus\n";

  std::string file_path;
  while (std::getline(input, file_path)) {
    if (file_path.empty()) continue;
    std::string base = file_path;
    size_t slash = base.find_last_of("/");
    if (slash != std::string::npos) base = base.substr(slash + 1);
    size_t dot = base.find(".root");
    std::string run = dot == std::string::npos ? base : base.substr(0, dot);

    TFile file(file_path.c_str(), "READ");
    if (file.IsZombie()) {
      out << file_path << "\t" << run << "\t0\t\t0\t0\t0\t0\topen_failed\n";
      continue;
    }

    TTree* tree = dynamic_cast<TTree*>(file.Get("RAWdata"));
    if (!tree) {
      out << file_path << "\t" << run << "\t0\t\t0\t0\t0\t0\tmissing_RAWdata\n";
      continue;
    }

    std::string branch_name = requested_branch ? requested_branch : "";
    if (branch_name.empty()) {
      std::vector<std::string> prefixes = discover_scaler_prefixes(tree);
      if (prefixes.empty()) {
        out << file_path << "\t" << run << "\t" << tree->GetEntries() << "\t\t0\t0\t0\t0\tmissing_scaler_ch15\n";
        continue;
      }
      branch_name = prefixes.front() + "_ch15";
    }

    TBranch* branch = tree->GetBranch(branch_name.c_str());
    if (!branch) {
      out << file_path << "\t" << run << "\t" << tree->GetEntries() << "\t" << branch_name << "\t0\t0\t0\t0\tmissing_requested_branch\n";
      continue;
    }

    uint32_t value = 0;
    tree->SetBranchStatus("*", 0);
    tree->SetBranchStatus(branch_name.c_str(), 1);
    tree->SetBranchAddress(branch_name.c_str(), &value);

    Long64_t entries = tree->GetEntries();
    if (entries <= 0) {
      out << file_path << "\t" << run << "\t0\t" << branch_name << "\t0\t0\t0\t0\tempty_tree\n";
      continue;
    }

    uint64_t wraps = 0;
    uint32_t previous = 0;
    uint32_t first = 0;
    uint32_t last = 0;
    bool have_previous = false;
    for (Long64_t i = 0; i < entries; ++i) {
      tree->GetEntry(i);
      if (!have_previous) {
        first = value;
        previous = value;
        have_previous = true;
      } else if (value < previous) {
        ++wraps;
      }
      previous = value;
      last = value;
    }

    uint64_t elapsed_us = wraps * 4294967296ULL + last;
    out << file_path << "\t" << run << "\t" << entries << "\t" << branch_name << "\t"
        << wraps << "\t" << first << "\t" << last << "\t" << (elapsed_us / 1000000.0)
        << "\tok\n";
  }
}
'''


def extract_tdaq_runs(root_files: list[Path], root_exe: Path, scaler_branch: str | None) -> list[TDAQRun]:
    if not root_files:
        return []
    with tempfile.TemporaryDirectory(prefix="match_timepix_tdaq_") as tmp:
        tmpdir = Path(tmp)
        list_path = tmpdir / "roots.txt"
        macro_path = tmpdir / "extract_scaler_runs.C"
        out_path = tmpdir / "tdaq.tsv"
        list_path.write_text("\n".join(str(path) for path in root_files) + "\n", encoding="utf-8")
        macro_path.write_text(root_macro_text(), encoding="utf-8")

        branch_arg = scaler_branch or ""
        command = [
            str(root_exe),
            "-l",
            "-b",
            "-q",
            f"{macro_path}(\"{list_path}\",\"{out_path}\",\"{branch_arg}\")",
        ]
        result = subprocess.run(command, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode != 0:
            raise RuntimeError(
                "ROOT scaler extraction failed.\n"
                f"Command: {' '.join(command)}\n"
                f"stdout:\n{result.stdout}\n"
                f"stderr:\n{result.stderr}"
            )

        runs: list[TDAQRun] = []
        with out_path.open("r", encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle, delimiter="\t")
            for row in reader:
                path = Path(row["root_file"])
                try:
                    run_number = int(row["run_number"])
                except ValueError:
                    continue
                elapsed = float(row["elapsed_seconds"])
                runs.append(
                    TDAQRun(
                        root_file=path,
                        run_number=run_number,
                        start_unix=float(run_number),
                        elapsed_seconds=elapsed,
                        end_unix=float(run_number) + elapsed,
                        entries=int(row["entries"]),
                        scaler_branch=row["scaler_branch"],
                        wraps=int(row["wraps"]),
                        first_count=int(row["first_count"]),
                        last_count=int(row["last_count"]),
                        status=row["status"],
                    )
                )
        return sorted(runs, key=lambda item: item.start_unix)


def overlap_seconds(a0: float, a1: float | None, b0: float, b1: float) -> float:
    if a1 is None:
        return 0.0
    return max(0.0, min(a1, b1) - max(a0, b0))


def choose_match(timepix: TimePixMeasurement, runs: list[TDAQRun]) -> tuple[TDAQRun | None, str, float, float]:
    ok_runs = [run for run in runs if run.status == "ok"]
    if not ok_runs:
        return None, "no_ok_tdaq_runs", 0.0, math.nan

    near_run_starts = [
        run
        for run in ok_runs
        if abs(timepix.start_unix - run.start_unix) <= RUN_START_TOLERANCE_SECONDS
    ]
    if near_run_starts:
        run = min(near_run_starts, key=lambda item: abs(timepix.start_unix - item.start_unix))
        overlap = overlap_seconds(timepix.start_unix, timepix.trigger_end_unix, run.start_unix, run.end_unix)
        return run, "near_tdaq_start", overlap, timepix.start_unix - run.start_unix

    overlaps = []
    for run in ok_runs:
        overlap = overlap_seconds(timepix.start_unix, timepix.trigger_end_unix, run.start_unix, run.end_unix)
        if overlap > 0:
            overlaps.append((overlap, abs(timepix.start_unix - run.start_unix), run))
    if overlaps:
        best_overlap, _, best_run = min(overlaps, key=lambda item: (-item[0], item[1], item[2].start_unix))
        return best_run, "overlap", best_overlap, timepix.start_unix - best_run.start_unix

    containing = [run for run in ok_runs if run.start_unix <= timepix.start_unix <= run.end_unix]
    if containing:
        run = min(containing, key=lambda item: abs(timepix.start_unix - item.start_unix))
        return run, "timepix_start_inside_tdaq", 0.0, timepix.start_unix - run.start_unix

    nearest = min(ok_runs, key=lambda run: min(abs(timepix.start_unix - run.start_unix), abs(timepix.start_unix - run.end_unix)))
    if timepix.start_unix < nearest.start_unix:
        gap = timepix.start_unix - nearest.start_unix
    elif timepix.start_unix > nearest.end_unix:
        gap = timepix.start_unix - nearest.end_unix
    else:
        gap = 0.0
    return nearest, "nearest_no_overlap", 0.0, gap


def write_matches_csv(path: Path, timepix_rows: list[TimePixMeasurement], runs: list[TDAQRun]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "timepix_measurement_id",
        "timepix_file",
        "timepix_trigger_file",
        "timepix_start_unix",
        "timepix_start_utc",
        "timepix_trigger_end_unix",
        "timepix_trigger_end_utc",
        "tdaq_run_number",
        "tdaq_root_file",
        "tdaq_start_unix",
        "tdaq_start_utc",
        "tdaq_end_unix",
        "tdaq_end_utc",
        "tdaq_elapsed_seconds",
        "tdaq_scaler_branch",
        "tdaq_scaler_wraps",
        "tdaq_entries",
        "match_method",
        "overlap_seconds",
        "timepix_start_minus_tdaq_start_seconds",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for timepix in timepix_rows:
            run, method, overlap, delta_start = choose_match(timepix, runs)
            writer.writerow(
                {
                    "timepix_measurement_id": timepix.measurement_id,
                    "timepix_file": str(timepix.measurement_file),
                    "timepix_trigger_file": str(timepix.trigger_file or ""),
                    "timepix_start_unix": f"{timepix.start_unix:.6f}",
                    "timepix_start_utc": iso_utc(timepix.start_unix),
                    "timepix_trigger_end_unix": f"{timepix.trigger_end_unix:.6f}" if timepix.trigger_end_unix is not None else "",
                    "timepix_trigger_end_utc": iso_utc(timepix.trigger_end_unix),
                    "tdaq_run_number": run.run_number if run else "",
                    "tdaq_root_file": str(run.root_file) if run else "",
                    "tdaq_start_unix": f"{run.start_unix:.6f}" if run else "",
                    "tdaq_start_utc": iso_utc(run.start_unix if run else None),
                    "tdaq_end_unix": f"{run.end_unix:.6f}" if run else "",
                    "tdaq_end_utc": iso_utc(run.end_unix if run else None),
                    "tdaq_elapsed_seconds": f"{run.elapsed_seconds:.6f}" if run else "",
                    "tdaq_scaler_branch": run.scaler_branch if run else "",
                    "tdaq_scaler_wraps": run.wraps if run else "",
                    "tdaq_entries": run.entries if run else "",
                    "match_method": method,
                    "overlap_seconds": f"{overlap:.6f}",
                    "timepix_start_minus_tdaq_start_seconds": f"{delta_start:.6f}" if not math.isnan(delta_start) else "",
                }
            )


def write_tdaq_summary_csv(path: Path, runs: list[TDAQRun]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "run_number",
        "root_file",
        "start_unix",
        "start_utc",
        "end_unix",
        "end_utc",
        "elapsed_seconds",
        "entries",
        "scaler_branch",
        "wraps",
        "first_count",
        "last_count",
        "status",
    ]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for run in runs:
            writer.writerow(
                {
                    "run_number": run.run_number,
                    "root_file": str(run.root_file),
                    "start_unix": f"{run.start_unix:.6f}",
                    "start_utc": iso_utc(run.start_unix),
                    "end_unix": f"{run.end_unix:.6f}",
                    "end_utc": iso_utc(run.end_unix),
                    "elapsed_seconds": f"{run.elapsed_seconds:.6f}",
                    "entries": run.entries,
                    "scaler_branch": run.scaler_branch,
                    "wraps": run.wraps,
                    "first_count": run.first_count,
                    "last_count": run.last_count,
                    "status": run.status,
                }
            )


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tdaq-dir", type=Path, default=Path("."), help="Directory containing numeric TDAQ .root files.")
    parser.add_argument("--timepix-dir", type=Path, default=Path("dataTimePix"), help="Directory containing TrackLab measurement .txt files.")
    parser.add_argument("--output", type=Path, default=Path("timepix_tdaq_matches.csv"), help="CSV path for TimePix-to-TDAQ matches.")
    parser.add_argument("--tdaq-summary", type=Path, default=Path("tdaq_run_times.csv"), help="CSV path for computed TDAQ run intervals.")
    parser.add_argument("--root-exe", type=Path, default=Path(os.environ.get("ROOT_EXE", DEFAULT_ROOT)), help="Path to the ROOT executable.")
    parser.add_argument("--scaler-branch", default=None, help="Optional explicit scaler branch, for example Scaler0_ch15.")
    parser.add_argument("--max-roots", type=int, default=None, help="Debug option: process only the first N ROOT files.")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    root_files = numeric_root_files(args.tdaq_dir)
    if args.max_roots is not None:
        root_files = root_files[: args.max_roots]
    if not root_files:
        print(f"No numeric .root files found in {args.tdaq_dir}", file=sys.stderr)
        return 2
    if not args.timepix_dir.exists():
        print(f"TimePix directory does not exist: {args.timepix_dir}", file=sys.stderr)
        return 2

    timepix_rows = read_timepix_measurements(args.timepix_dir)
    if not timepix_rows:
        print(f"No TimePix measurements with start timestamps found in {args.timepix_dir}", file=sys.stderr)
        return 2

    runs = extract_tdaq_runs(root_files, args.root_exe, args.scaler_branch)
    write_tdaq_summary_csv(args.tdaq_summary, runs)
    write_matches_csv(args.output, timepix_rows, runs)

    ok_runs = sum(1 for run in runs if run.status == "ok")
    matched = 0
    nearest = 0
    for timepix in timepix_rows:
        _, method, _, _ = choose_match(timepix, runs)
        matched += method in {"overlap", "timepix_start_inside_tdaq", "near_tdaq_start"}
        nearest += method == "nearest_no_overlap"

    print(f"TDAQ runs processed: {len(runs)} ({ok_runs} ok)")
    print(f"TimePix measurements processed: {len(timepix_rows)}")
    print(f"Matched by overlap/start-inside/near-start: {matched}")
    print(f"Nearest-only matches: {nearest}")
    print(f"Wrote {args.output}")
    print(f"Wrote {args.tdaq_summary}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
