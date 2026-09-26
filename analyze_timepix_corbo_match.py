#!/usr/bin/env python3
"""
Cluster TimePix hits and compare cluster times to GPIO/CORBO trigger timestamps.

Default settings target the no-target TimePix/TDAQ run from the logbook:
TDAQ run 1787081424, TimePix measurement_9..measurement_23, GPIO2 = CORBO
falling edge.
"""

from __future__ import annotations

import argparse
import csv
import re
from collections import deque
from dataclasses import dataclass
from pathlib import Path
from statistics import median


@dataclass(frozen=True)
class Hit:
    pix: int
    toa: int
    ftoa: int
    tot: float
    x: int
    y: int
    time_ns: float


@dataclass(frozen=True)
class Cluster:
    measurement_id: int
    cluster_id: int
    size: int
    time_s: float
    min_time_s: float
    max_time_s: float
    duration_ns: float
    total_tot: float
    x_mean: float
    y_mean: float


class DSU:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, item: int) -> int:
        while self.parent[item] != item:
            self.parent[item] = self.parent[self.parent[item]]
            item = self.parent[item]
        return item

    def union(self, left: int, right: int) -> None:
        root_left = self.find(left)
        root_right = self.find(right)
        if root_left == root_right:
            return
        if self.rank[root_left] < self.rank[root_right]:
            root_left, root_right = root_right, root_left
        self.parent[root_right] = root_left
        if self.rank[root_left] == self.rank[root_right]:
            self.rank[root_left] += 1


def parse_start_unix(path: Path) -> float:
    pattern = re.compile(r"^# Start of measurement - unix time:\s*([0-9]+(?:\.[0-9]+)?)")
    with path.open("r", encoding="utf-8", errors="replace") as handle:
        for line in handle:
            match = pattern.match(line.strip())
            if match:
                return float(match.group(1))
            if not line.startswith("#"):
                break
    raise ValueError(f"No TimePix start timestamp found in {path}")


def read_hits(path: Path) -> list[Hit]:
    hits: list[Hit] = []
    with path.open("r", encoding="utf-8", errors="replace") as handle:
        for line in handle:
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            fields = stripped.split()
            if len(fields) < 4:
                continue
            pix = int(fields[0])
            toa = int(fields[1])
            ftoa = int(fields[2])
            tot = float(fields[3])
            x = pix % 256
            y = pix // 256
            time_ns = toa * 25.0 - ftoa * 1.5625
            hits.append(Hit(pix=pix, toa=toa, ftoa=ftoa, tot=tot, x=x, y=y, time_ns=time_ns))
    return sorted(hits, key=lambda item: item.time_ns)


def read_triggers(path: Path, event_code: int) -> list[float]:
    triggers: list[float] = []
    with path.open("r", encoding="utf-8", errors="replace") as handle:
        for line in handle:
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            fields = stripped.split()
            if len(fields) < 2:
                continue
            try:
                code = int(fields[0])
                time_s = float(fields[1])
            except ValueError:
                continue
            if code == event_code:
                triggers.append(time_s)
    return sorted(triggers)


def cluster_hits(
    hits: list[Hit],
    measurement_id: int,
    time_window_ns: float,
    min_pixels: int,
    time_reference: str,
) -> list[Cluster]:
    dsu = DSU(len(hits))
    active_by_pixel: dict[tuple[int, int], deque[tuple[float, int]]] = {}

    for idx, hit in enumerate(hits):
        cutoff = hit.time_ns - time_window_ns
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                key = (hit.x + dx, hit.y + dy)
                queue = active_by_pixel.get(key)
                if not queue:
                    continue
                while queue and queue[0][0] < cutoff:
                    queue.popleft()
                for _, other_idx in queue:
                    dsu.union(idx, other_idx)

        own_queue = active_by_pixel.setdefault((hit.x, hit.y), deque())
        own_queue.append((hit.time_ns, idx))

    groups: dict[int, list[int]] = {}
    for idx in range(len(hits)):
        groups.setdefault(dsu.find(idx), []).append(idx)

    clusters: list[Cluster] = []
    for indices in groups.values():
        if len(indices) < min_pixels:
            continue
        cluster_hits_ = [hits[idx] for idx in indices]
        min_time_ns = min(hit.time_ns for hit in cluster_hits_)
        max_time_ns = max(hit.time_ns for hit in cluster_hits_)
        total_tot = sum(hit.tot for hit in cluster_hits_)
        weighted_time_ns = sum(hit.time_ns * hit.tot for hit in cluster_hits_) / total_tot if total_tot else min_time_ns
        if time_reference == "earliest":
            cluster_time_ns = min_time_ns
        elif time_reference == "latest":
            cluster_time_ns = max_time_ns
        elif time_reference == "weighted":
            cluster_time_ns = weighted_time_ns
        else:
            raise ValueError(f"Unsupported cluster time reference: {time_reference}")
        clusters.append(
            Cluster(
                measurement_id=measurement_id,
                cluster_id=0,
                size=len(cluster_hits_),
                time_s=cluster_time_ns / 1e9,
                min_time_s=min_time_ns / 1e9,
                max_time_s=max_time_ns / 1e9,
                duration_ns=max_time_ns - min_time_ns,
                total_tot=total_tot,
                x_mean=sum(hit.x for hit in cluster_hits_) / len(cluster_hits_),
                y_mean=sum(hit.y for hit in cluster_hits_) / len(cluster_hits_),
            )
        )

    clusters.sort(key=lambda item: item.time_s)
    return [
        Cluster(
            measurement_id=cluster.measurement_id,
            cluster_id=idx,
            size=cluster.size,
            time_s=cluster.time_s,
            min_time_s=cluster.min_time_s,
            max_time_s=cluster.max_time_s,
            duration_ns=cluster.duration_ns,
            total_tot=cluster.total_tot,
            x_mean=cluster.x_mean,
            y_mean=cluster.y_mean,
        )
        for idx, cluster in enumerate(clusters)
    ]


def nearest_delta_seconds(value: float, sorted_values: list[float]) -> float | None:
    if not sorted_values:
        return None
    lo = 0
    hi = len(sorted_values)
    while lo < hi:
        mid = (lo + hi) // 2
        if sorted_values[mid] < value:
            lo = mid + 1
        else:
            hi = mid
    candidates = []
    if lo < len(sorted_values):
        candidates.append(sorted_values[lo] - value)
    if lo > 0:
        candidates.append(sorted_values[lo - 1] - value)
    return min(candidates, key=abs)


def count_matches(values: list[float], references: list[float], window_s: float) -> int:
    count = 0
    for value in values:
        delta = nearest_delta_seconds(value, references)
        if delta is not None and abs(delta) <= window_s:
            count += 1
    return count


def count_values_in_windows(values: list[float], starts: list[float], window_s: float) -> tuple[int, int, int]:
    """Return windows with >=1 value, total values in windows, and values in overlapping windows."""
    if not values or not starts:
        return 0, 0, 0
    windows_with_value = 0
    total_values = 0
    values_in_overlapping_windows = 0
    value_idx = 0
    n_values = len(values)
    for start in starts:
        end = start + window_s
        while value_idx < n_values and values[value_idx] < start:
            value_idx += 1
        scan_idx = value_idx
        count = 0
        while scan_idx < n_values and values[scan_idx] <= end:
            count += 1
            scan_idx += 1
        if count:
            windows_with_value += 1
            total_values += count
            if count > 1:
                values_in_overlapping_windows += count
    return windows_with_value, total_values, values_in_overlapping_windows


def offset_histogram(
    clusters: list[float],
    triggers: list[float],
    search_window_s: float,
    bin_width_s: float,
) -> tuple[float | None, int, list[tuple[float, int]]]:
    if not clusters or not triggers:
        return None, 0, []
    bins: dict[int, int] = {}
    lo = 0
    hi = 0
    n_clusters = len(clusters)
    for trigger in triggers:
        low_edge = trigger - search_window_s
        high_edge = trigger + search_window_s
        while lo < n_clusters and clusters[lo] < low_edge:
            lo += 1
        if hi < lo:
            hi = lo
        while hi < n_clusters and clusters[hi] <= high_edge:
            hi += 1
        for cluster_time in clusters[lo:hi]:
            delta = cluster_time - trigger
            bin_index = round(delta / bin_width_s)
            bins[bin_index] = bins.get(bin_index, 0) + 1
    if not bins:
        return None, 0, []
    best_bin, best_count = max(bins.items(), key=lambda item: item[1])
    hist = sorted((bin_index * bin_width_s, count) for bin_index, count in bins.items())
    return best_bin * bin_width_s, best_count, hist


def shifted_match_count(cluster_times: list[float], triggers: list[float], offset_s: float, window_s: float) -> int:
    shifted_clusters = [cluster_time - offset_s for cluster_time in cluster_times]
    return count_matches(triggers, shifted_clusters, window_s)


def binned_counts(values: list[float], start_s: float, end_s: float, bin_width_s: float) -> list[int]:
    if end_s <= start_s:
        return []
    n_bins = int((end_s - start_s) / bin_width_s) + 1
    counts = [0] * n_bins
    for value in values:
        if value < start_s or value >= end_s:
            continue
        idx = int((value - start_s) / bin_width_s)
        if 0 <= idx < n_bins:
            counts[idx] += 1
    return counts


def pearson(left: list[int], right: list[int]) -> float | None:
    if len(left) != len(right) or len(left) < 2:
        return None
    mean_left = sum(left) / len(left)
    mean_right = sum(right) / len(right)
    num = sum((a - mean_left) * (b - mean_right) for a, b in zip(left, right))
    den_left = sum((a - mean_left) ** 2 for a in left)
    den_right = sum((b - mean_right) ** 2 for b in right)
    if den_left <= 0 or den_right <= 0:
        return None
    return num / (den_left * den_right) ** 0.5


def lagged_correlation(
    cluster_times: list[float],
    triggers: list[float],
    bin_width_s: float,
    max_lag_s: float,
) -> tuple[float | None, float | None, int]:
    if not cluster_times or not triggers:
        return None, None, 0
    start_s = min(cluster_times[0], triggers[0])
    end_s = max(cluster_times[-1], triggers[-1])
    cluster_counts = binned_counts(cluster_times, start_s, end_s, bin_width_s)
    trigger_counts = binned_counts(triggers, start_s, end_s, bin_width_s)
    if not cluster_counts or not trigger_counts:
        return None, None, 0
    max_lag_bins = int(max_lag_s / bin_width_s)
    best_corr: float | None = None
    best_lag_bins = 0
    for lag in range(-max_lag_bins, max_lag_bins + 1):
        if lag < 0:
            left = cluster_counts[-lag:]
            right = trigger_counts[: len(left)]
        elif lag > 0:
            left = cluster_counts[: -lag]
            right = trigger_counts[lag:]
        else:
            left = cluster_counts
            right = trigger_counts
        corr = pearson(left, right)
        if corr is None:
            continue
        if best_corr is None or corr > best_corr:
            best_corr = corr
            best_lag_bins = lag
    return best_lag_bins * bin_width_s, best_corr, len(cluster_counts)


def parse_measurement_ids(value: str) -> list[int]:
    if ".." in value:
        left, right = value.split("..", 1)
        return list(range(int(left), int(right) + 1))
    return [int(part) for part in value.split(",") if part.strip()]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", type=Path, default=Path("dataTimePix"))
    parser.add_argument("--measurements", default="9..23")
    parser.add_argument("--event-code", type=int, default=1)
    parser.add_argument("--cluster-time-window-ns", type=float, default=200.0)
    parser.add_argument("--min-pixels", type=int, default=2)
    parser.add_argument(
        "--cluster-time-reference",
        choices=["earliest", "weighted", "latest"],
        default="earliest",
        help="Which cluster time to compare to GPIO/CORBO timestamps.",
    )
    parser.add_argument("--match-windows-us", default="1,5,10,25,50,100,250,500,1000")
    parser.add_argument("--offset-search-window-us", type=float, default=2000.0)
    parser.add_argument("--offset-bin-us", type=float, default=5.0)
    parser.add_argument("--correlation-bin-ms", default="1,5,10,50,100")
    parser.add_argument("--correlation-max-lag-ms", type=float, default=1000.0)
    parser.add_argument("--busy-window-us", default="50,100,200,300,500")
    parser.add_argument("--output-clusters", type=Path, default=Path("timepix_no_target_clusters.csv"))
    parser.add_argument("--output-summary", type=Path, default=Path("timepix_no_target_corbo_summary.csv"))
    parser.add_argument("--output-offsets", type=Path, default=Path("timepix_no_target_offset_scan.csv"))
    args = parser.parse_args()

    measurement_ids = parse_measurement_ids(args.measurements)
    match_windows_s = [float(item) * 1e-6 for item in args.match_windows_us.split(",") if item.strip()]
    offset_search_window_s = args.offset_search_window_us * 1e-6
    offset_bin_s = args.offset_bin_us * 1e-6
    correlation_bin_widths_s = [
        float(item) * 1e-3 for item in args.correlation_bin_ms.split(",") if item.strip()
    ]
    correlation_max_lag_s = args.correlation_max_lag_ms * 1e-3
    busy_windows_s = [float(item) * 1e-6 for item in args.busy_window_us.split(",") if item.strip()]

    all_clusters: list[Cluster] = []
    all_cluster_times: list[float] = []
    all_trigger_times: list[float] = []
    summary_rows: list[dict[str, object]] = []

    for measurement_id in measurement_ids:
        hit_path = args.data_dir / f"measurement_{measurement_id}.txt"
        trigger_path = args.data_dir / f"measurement_{measurement_id}_trigger.txt"
        start_unix = parse_start_unix(hit_path)
        hits = read_hits(hit_path)
        triggers = read_triggers(trigger_path, args.event_code)
        clusters = cluster_hits(
            hits,
            measurement_id,
            args.cluster_time_window_ns,
            args.min_pixels,
            args.cluster_time_reference,
        )

        cluster_times = [cluster.time_s for cluster in clusters]
        deltas = [
            nearest_delta_seconds(cluster.time_s, triggers)
            for cluster in clusters
        ]
        deltas = [delta for delta in deltas if delta is not None]

        row: dict[str, object] = {
            "measurement_id": measurement_id,
            "start_unix": f"{start_unix:.6f}",
            "hits": len(hits),
            "clusters": len(clusters),
            "trigger_count": len(triggers),
            "cluster_to_trigger_ratio": f"{len(clusters) / len(triggers):.6f}" if triggers else "",
            "median_nearest_trigger_delta_us": f"{median(deltas) * 1e6:.3f}" if deltas else "",
            "median_abs_nearest_trigger_delta_us": f"{median(abs(delta) for delta in deltas) * 1e6:.3f}" if deltas else "",
        }
        for window_s in match_windows_s:
            label = f"clusters_within_{window_s * 1e6:.0f}us"
            row[label] = count_matches(cluster_times, triggers, window_s)
            trigger_label = f"triggers_with_cluster_within_{window_s * 1e6:.0f}us"
            row[trigger_label] = count_matches(triggers, cluster_times, window_s)
        for bin_width_s in correlation_bin_widths_s:
            lag_s, corr, n_bins = lagged_correlation(cluster_times, triggers, bin_width_s, correlation_max_lag_s)
            label_base = f"corr_{bin_width_s * 1e3:.0f}ms"
            row[f"{label_base}_best_lag_ms"] = f"{lag_s * 1e3:.3f}" if lag_s is not None else ""
            row[f"{label_base}_pearson"] = f"{corr:.6f}" if corr is not None else ""
            row[f"{label_base}_bins"] = n_bins
        for window_s in busy_windows_s:
            windows_with_value, total_values, multi_values = count_values_in_windows(cluster_times, triggers, window_s)
            label_base = f"busy_{window_s * 1e6:.0f}us"
            row[f"{label_base}_corbos_with_cluster"] = windows_with_value
            row[f"{label_base}_clusters_in_windows"] = total_values
            row[f"{label_base}_extra_clusters_in_multi_cluster_windows"] = multi_values
        summary_rows.append(row)

        all_clusters.extend(clusters)
        all_cluster_times.extend(cluster_times)
        all_trigger_times.extend(triggers)

    args.output_clusters.parent.mkdir(parents=True, exist_ok=True)
    with args.output_clusters.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "measurement_id",
                "cluster_id",
                "size",
                "time_s",
                "min_time_s",
                "max_time_s",
                "duration_ns",
                "total_tot",
                "x_mean",
                "y_mean",
            ],
        )
        writer.writeheader()
        for cluster in all_clusters:
            writer.writerow(
                {
                    "measurement_id": cluster.measurement_id,
                    "cluster_id": cluster.cluster_id,
                    "size": cluster.size,
                    "time_s": f"{cluster.time_s:.12f}",
                    "min_time_s": f"{cluster.min_time_s:.12f}",
                    "max_time_s": f"{cluster.max_time_s:.12f}",
                    "duration_ns": f"{cluster.duration_ns:.3f}",
                    "total_tot": f"{cluster.total_tot:.3f}",
                    "x_mean": f"{cluster.x_mean:.3f}",
                    "y_mean": f"{cluster.y_mean:.3f}",
                }
            )

    total_row: dict[str, object] = {
        "measurement_id": "TOTAL",
        "start_unix": "",
        "hits": sum(int(row["hits"]) for row in summary_rows),
        "clusters": len(all_clusters),
        "trigger_count": len(all_trigger_times),
        "cluster_to_trigger_ratio": f"{len(all_clusters) / len(all_trigger_times):.6f}" if all_trigger_times else "",
        "median_nearest_trigger_delta_us": "",
        "median_abs_nearest_trigger_delta_us": "",
    }
    for window_s in match_windows_s:
        label = f"clusters_within_{window_s * 1e6:.0f}us"
        total_row[label] = sum(int(row[label]) for row in summary_rows)
        trigger_label = f"triggers_with_cluster_within_{window_s * 1e6:.0f}us"
        total_row[trigger_label] = sum(int(row[trigger_label]) for row in summary_rows)
    for bin_width_s in correlation_bin_widths_s:
        lag_s, corr, n_bins = lagged_correlation(
            sorted(all_cluster_times),
            sorted(all_trigger_times),
            bin_width_s,
            correlation_max_lag_s,
        )
        label_base = f"corr_{bin_width_s * 1e3:.0f}ms"
        total_row[f"{label_base}_best_lag_ms"] = f"{lag_s * 1e3:.3f}" if lag_s is not None else ""
        total_row[f"{label_base}_pearson"] = f"{corr:.6f}" if corr is not None else ""
        total_row[f"{label_base}_bins"] = n_bins
    for window_s in busy_windows_s:
        windows_with_value, total_values, multi_values = count_values_in_windows(
            sorted(all_cluster_times),
            sorted(all_trigger_times),
            window_s,
        )
        label_base = f"busy_{window_s * 1e6:.0f}us"
        total_row[f"{label_base}_corbos_with_cluster"] = windows_with_value
        total_row[f"{label_base}_clusters_in_windows"] = total_values
        total_row[f"{label_base}_extra_clusters_in_multi_cluster_windows"] = multi_values
    summary_rows.append(total_row)

    args.output_summary.parent.mkdir(parents=True, exist_ok=True)
    with args.output_summary.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(summary_rows[0]))
        writer.writeheader()
        writer.writerows(summary_rows)

    offset_s, offset_peak_count, offset_hist = offset_histogram(
        sorted(all_cluster_times),
        sorted(all_trigger_times),
        offset_search_window_s,
        offset_bin_s,
    )
    with args.output_offsets.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["offset_us", "count"])
        writer.writeheader()
        for delta_s, count in offset_hist:
            writer.writerow({"offset_us": f"{delta_s * 1e6:.3f}", "count": count})

    print(f"Measurements: {args.measurements}")
    print(f"Hits: {total_row['hits']}")
    print(f"Clusters: {total_row['clusters']} (min_pixels={args.min_pixels}, time_window_ns={args.cluster_time_window_ns:g})")
    print(f"Cluster time reference: {args.cluster_time_reference}")
    print(f"CORBO trigger timestamps: {total_row['trigger_count']}")
    print(f"Cluster/CORBO ratio: {total_row['cluster_to_trigger_ratio']}")
    if offset_s is not None:
        print(
            f"Best cluster-minus-CORBO offset: {offset_s * 1e6:.3f} us "
            f"(histogram peak count {offset_peak_count}, bin {args.offset_bin_us:g} us)"
        )
    for window_s in match_windows_s:
        label = f"clusters_within_{window_s * 1e6:.0f}us"
        print(f"{label}: {total_row[label]}")
        trigger_label = f"triggers_with_cluster_within_{window_s * 1e6:.0f}us"
        print(f"{trigger_label}: {total_row[trigger_label]}")
        if offset_s is not None:
            shifted = shifted_match_count(sorted(all_cluster_times), sorted(all_trigger_times), offset_s, window_s)
            print(f"triggers_with_cluster_within_{window_s * 1e6:.0f}us_after_offset: {shifted}")
    for bin_width_s in correlation_bin_widths_s:
        label_base = f"corr_{bin_width_s * 1e3:.0f}ms"
        print(
            f"{label_base}: lag {total_row[f'{label_base}_best_lag_ms']} ms, "
            f"pearson {total_row[f'{label_base}_pearson']}, bins {total_row[f'{label_base}_bins']}"
        )
    for window_s in busy_windows_s:
        label_base = f"busy_{window_s * 1e6:.0f}us"
        print(
            f"{label_base}: CORBO windows with cluster "
            f"{total_row[f'{label_base}_corbos_with_cluster']}/{total_row['trigger_count']}, "
            f"clusters in windows {total_row[f'{label_base}_clusters_in_windows']}"
        )
    print(f"Wrote {args.output_clusters}")
    print(f"Wrote {args.output_summary}")
    print(f"Wrote {args.output_offsets}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
