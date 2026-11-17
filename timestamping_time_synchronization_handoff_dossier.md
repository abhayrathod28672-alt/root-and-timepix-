# Timepix3–Katherine–TDAQ timestamping handoff dossier

## Purpose of this dossier

This document is a self-contained handoff for another AI or analyst who must continue the Timepix3–Katherine–TDAQ synchronization and CEX analysis. It records the experiment context, the user’s requirements and corrections, the evidence actually inspected, the equipment and diagrams, the observations, the reasoning basis for each decision, the rejected assumptions, the complete analysis procedure, the unresolved questions, and the external references.

It is intentionally more detailed than a normal analysis note. The reader should be able to start with no knowledge of the experiment and understand both the simple story and the technical implementation.

## Important transparency boundary

The user asked for the assistant’s “thought process.” I cannot provide hidden private chain-of-thought or internal deliberation. Instead, this dossier provides the useful scientific equivalent:

- all externally checkable observations;
- the exact files and evidence sources;
- explicit assumptions;
- calculations;
- hypotheses versus facts;
- reasons for accepting or rejecting an interpretation;
- failed/dead-end approaches;
- unresolved items;
- reproducible algorithms and commands.

Nothing in this dossier should be treated as a fact merely because it is written in a previous note. Each important statement is classified.

## Evidence labels

Use these labels throughout the dossier and the appended guide:

- **[L]**: logbook or diagram fact.
- **[N]**: notebook, software configuration, or explicit user configuration statement.
- **[R]**: fact read directly from ROOT output.
- **[M]**: fact read directly from a TrackLab measurement/trigger file.
- **[E]**: external documentation or published reference.
- **[I]**: physics/electronics inference derived from evidence.
- **[U]**: unresolved; do not fill in by guessing.

A statement can have more than one label, for example `[R][I]` when a ROOT count supports an electronics interpretation.

---

# 1. Request and conversation history

## 1.1 Original scientific objective

The user asked for a complete technically accurate guide to timestamping and CEX analysis using:

- the August logbook;
- the sixth Timepix/TDAQ/CORBO notebook;
- the ROOT output;
- TrackLab measurement files;
- TrackLab trigger/GPIO files;
- matching and diagnostic scripts;
- QDC/ECAL calibration files;
- electronics diagrams and photographs;
- external Katherine, TrackLab, Timepix3, and timing references.

The guide had to explain the entire chain from physical detector signals through NIM logic, trigger formation, CORBO, TDAQ, scalers, TDCs, QDC gates, ECAL data, Katherine GPIO timestamps, Timepix3 timestamps, offline matching, and CEX selection.

The user specifically wanted technical terms explained in plain language, preferably in parentheses at first use.

## 1.2 User corrections that must control the interpretation

The user supplied several corrections and standing requirements:

1. **Actual clock:** the scaler clock used in the experiment was **1 MHz**. The original 1 kHz plan was abandoned because the beam rate could exceed approximately 1,000 particles/s.
2. **GPIO history:** the sixth notebook contains the historical GPIO information.
3. **GPIO consistency:** the user states that the same GPIO arrangement was used for every run.
4. **Recorded edge:** the user states that the recorded synchronization edge was the **leading edge**.
5. Do not infer a GPIO channel or CORBO wiring from photographs.
6. Validate GPIO and edge information against the notebook, measurement files, trigger files, and documented wiring.
7. Do not fabricate ROOT branch names, TDC units, GPIO channels, event IDs, or Timepix/Katherine timestamp semantics.
8. Do not use ROOT entry order, filename order, nominal run start, or file-writing time as physical event time.
9. Do not assign SPIDR-specific timestamp features to Katherine/TrackLab unless verified.
10. Use the attached ROOT text output; search for the missing `txt2root-1.C` rather than assuming its contents.
11. Explain clocks, signal delays, wire propagation, module delays, TDAQ delay, TDC LSB, QDC timing, NIM/VME timing, and synchronization.
12. If a photograph is unclear, call the interpretation tentative and validate it against documentation.
13. The analysis is high importance; false or unverified claims are forbidden.
14. The proton may physically be recorded before or after ECAL photons; determine the order from geometry, beta, and calibrated electronics/detector delays rather than assuming.
15. A no-target run can calibrate synchronization and quantify accidentals/backgrounds/material effects, but cannot alone prove target CEX.
16. The final guide must classify statements as logbook/diagram, notebook/user configuration, ROOT-derived, measurement-file, external documentation, inference, or unresolved.
17. The user wants the full explanation directly in chat, not only in a file.

## 1.3 Latest user request

The user then requested a beginner-friendly explanation because the amount of information had become overwhelming. The explanation was reorganized from basic concepts upward.

The current request is to produce a much more detailed handoff file containing everything useful for another AI: the instructions, reasoning basis, observations, equipment, photos, clocks, challenges, resources, previous prompts/requirements, and all technical and nontechnical context.

This dossier is the response to that request. It includes an expanded handoff section followed by the detailed timestamping/CEX guide.

---

# 2. Repository and workspace context

The repository is the project `root-and-timepix-`.

The intended working branch is:

```text
arena/01a0a9cf-root-and-timepix
```

The repository root is:

```text
/home/user/root-and-timepix-
```

The important artifact names and their roles are listed below. Some files are on the repository’s `origin/main` tree even when they are not checked out in the minimal working branch; an analyst should use `git ls-tree -r origin/main` and `git show origin/main:<path>` when necessary.

## 2.1 ROOT data and ROOT output

```text
1787536596.root
```

This file in the checkout is only a 133-byte Git-LFS pointer, not the binary ROOT file. Git LFS was not available in the earlier inspection, so the binary could not be opened locally.

The corresponding text dump is named in the repository as:

```text
"1787536596.root".txt
```

A raw copy was previously downloaded to:

```text
/tmp/root_output.txt
```

The text dump contains the output of ROOT commands including `t->Print()` and scaler `t->Scan()` commands. It is sufficient to establish the tree/branch schema and the scaler endpoint values, but it cannot replace the binary for arbitrary event-by-event TDC analysis.

## 2.2 Notebook and scripts

Important files on `origin/main`:

```text
6-TimePix_TDAQ_CORBO_Matching.ipynb
vertopal.com_6-TimePix_TDAQ_CORBO_Matching.txt
match_timepix_tdaq.py
analyze_timepix_corbo_match.py
```

`match_timepix_tdaq.py`:

- reads Timepix measurement start Unix times;
- reads trigger-file relative times;
- discovers or uses a scaler branch, normally `Scaler0_ch15`;
- treats the run filename as a Unix start-time convention;
- reads cumulative scaler values event by event;
- counts 32-bit counter wraps;
- computes a coarse run endpoint.

`analyze_timepix_corbo_match.py`:

- parses Timepix hits;
- computes `time_ns = toa*25.0 - ftoa*1.5625`;
- clusters adjacent pixels in time and space;
- reads trigger codes;
- compares clusters against CORBO trigger timestamps;
- scans offsets and matching windows;
- computes rate correlations and busy-window statistics.

## 2.3 TrackLab files

The current checked-out data block contains:

```text
measurement_5187.txt through measurement_5201.txt
measurement_5187_trigger.txt through measurement_5201_trigger.txt
```

The current trigger files show TrackLab 1.6.0 and chip ID `K8-W0036` for the active data block.

## 2.4 Diagrams and crops

Relevant rendered images include:

```text
p3_0_X1.png
p3_1_X2.png
p2_0_X0.png
logic_left.png
logic_center.png
logic_trigger_high.png
vme.png
```

These are diagram renderings/crops, not independent electronic configuration files. Their labels are useful evidence, but an ambiguous wire must not be promoted to a hardware fact without written documentation or a configuration export.

## 2.5 Existing guide

```text
timestamping_guide_readable.md
```

This handoff dossier is intended to be the broader context document. The readable guide contains the operational timestamping and CEX method and is appended after the handoff-specific sections in this file.

---

# 3. Run 1787536596: the central worked example

## 3.1 Logbook metadata

The August logbook records:

```text
Run:              1787536596
Beam:             +4 GeV
Beamfile:         <019>
Trigger:          S0S1FS0FS1
Target:           no target / background
Started:          24-Aug-2026 03:56:36 local
Finished:         24-Aug-2026 04:10:10 local
Number of events: 91,274
DESY position:    H=35.165, V=1.278
```

These are `[L]` logbook facts.

The Unix run number corresponds approximately to:

```text
24-Aug-2026 01:56:36 UTC
```

The filename/run number is useful for finding the corresponding measurement files. It is not a per-event timestamp. `[L][I]`

## 3.2 ROOT facts

The supplied ROOT text output confirms:

```text
Tree: RAWdata
Entries: 91,274
```

The ROOT output shows scaler branches:

```text
Scaler0_ch0 through Scaler0_ch15
```

It shows TDC channels 0–31 with count/multiplicity branches and separate leading/trailing arrays.

The first and last scan values were:

| entry | ch10 | ch11 | ch12 | ch15 |
|---:|---:|---:|---:|---:|
| 0 | 1 | 1 | 1 | 3,884,549 |
| 91,273 | 281,094 | 247,387 | 91,274 | 810,801,268 |

These are `[R]` facts.

## 3.3 Interpretation of the endpoint values

The value of `Scaler0_ch15` is compatible with a 1 MHz free-running clock:

```text
810,801,268 ticks / 1,000,000 ticks/s
= 810.801268 s
```

The difference between final and initial snapshots is:

```text
810,801,268 - 3,884,549
= 806,916,719 ticks
= 806.916719 s at 1 MHz
```

The final value is closer to the logbook duration than the first-to-last difference because the clock may have started before the first stored ROOT entry. The exact scaler-origin convention is not fully proven by the text dump. `[R][I][U]`

The strong interpretation is:

```text
actual clock = 1 MHz
old 1 kHz label = stale/planning label
```

The user’s configuration statement and the ROOT count independently agree. `[N][R]`

Channel 12 ends at 91,274, exactly equal to the ROOT-entry count. Together with the diagram label `CORBO`, this strongly supports:

```text
Scaler0_ch12 = accepted CORBO/event count
```

The full binary should still be scanned to verify that it increments once per stored event, rather than relying only on endpoints. `[L][R][I][U]`

---

# 4. Equipment inventory and roles

## 4.1 Timepix3

Timepix3 is a data-driven hybrid pixel detector. Each pixel can record a threshold crossing and provide:

- pixel position;
- coarse time of arrival, ToA;
- fine time of arrival, FToA;
- time over threshold, ToT.

A charged particle can produce multiple adjacent pixel hits. Those hits are later grouped into a cluster.

Timepix3 is not automatically a proton detector. It records a charged-particle response. Proton identification requires geometry, timing, energy-loss/ToT information, and/or kinematics. `[E][I]`

## 4.2 Katherine Gen2

The user states that the pictured Katherine Gen2 is the exact readout used for the data. `[N]`

External Katherine Gen2 documentation describes a readout system with:

- support for multiple chipboard configurations;
- two sensor inputs;
- high-voltage bias capability up to approximately ±1 kV;
- Ethernet and USB communication;
- four GPIO ports;
- programmable 50-ohm termination;
- external-trigger timestamping using an internal TDC;
- insertion of external trigger events into the common pixel data stream.

These are platform capabilities from external documentation. They do not prove which physical GPIO port was used in this specific run. `[E][U]`

## 4.3 TrackLab

TrackLab controls Katherine over supported communication interfaces and can configure GPIO functions. `[E]`

The current measurement header includes:

```text
Software: TrackLab 1.6.0
Chip ID: K8-W0036
Readout mode: Data-Driven Mode
Detector mode: ToA & ToT
```

For one current file, the header also contains:

```text
Bias voltage A: 150.39 V
Bias voltage B: -0.52 V
THL: 1508 (0.790 V)
Sensor temperature: 62.1 °C
Readout temperature: 37.3 °C
```

These values are file-header facts for that measurement, not automatically constants for every measurement. `[M]`

## 4.4 NIM electronics

NIM modules provide fast logic operations:

- discrimination;
- coincidence;
- AND/OR logic;
- delay;
- fan-in/fan-out;
- pulse shaping;
- trigger formation.

They are the fast logic layer between the detector pulses and the VME/TDAQ system. `[L][I]`

## 4.5 VME/TDAQ

The VME system receives accepted triggers and stores detector information in ROOT. It contains or connects to:

- TDC modules;
- QDC modules;
- scaler inputs;
- trigger/event logic;
- detector readout electronics.

The ROOT `RAWdata` tree is the storage representation of the acquired data. ROOT itself does not create a physical event clock. `[R][I]`

## 4.6 TDC

A TDC is a time-to-digital converter. It converts the arrival time of a logic edge into a digital code.

The supplied ROOT schema includes:

```text
leading edges
trailing edges
per-channel multiplicity counts
```

The diagram labels TDC0 channels 0–15 as beam and DWC discriminator channels. Channels 16–31 exist in the ROOT schema but are not identified by the supplied diagram. `[L][R][U]`

## 4.7 QDC and ECAL

A QDC is a charge-to-digital converter. It integrates a detector pulse over a gate and converts the integrated charge into an ADC value.

The ECAL uses QDC values for energy reconstruction. The QDC value itself is not an independent precise arrival timestamp.

The sequence is approximately:

```text
accepted trigger
    -> QDC gate delay
    -> gate opens
    -> ECAL pulse integrated
    -> gate closes
    -> conversion/readout
    -> ROOT value stored
```

The QDC calibration JSON/CSV files provide channel-dependent energy calibration. They do not provide the TDC timing LSB. `[R][M][U]`

---

# 5. What the photographs and diagrams show

## 5.1 Main logic diagram: `p3_0_X1.png`

The main rendered diagram is divided into:

```text
Detectors | NIM Units | VME Units
```

The detector side shows:

- C0;
- C1;
- S0;
- S1;
- FS0;
- FS1;
- S2;
- S3;
- DWC0;
- DWC1;
- calorimeter channels.

The NIM side shows discriminator outputs and logic. The C0/C1 path includes a coincidence condition with an inverted C1 input, visually representing a C0-and-not-C1 pion-like condition. The S0/S1/FS0/FS1 signals feed the main fourfold trigger logic. `[L]`

The diagram labels:

```text
EVTTRIG
BUSY
CORBO
```

and shows CORBO being routed toward the VME system.

The VME side shows three main groups:

```text
CORBO / TDC0
QDC
Scaler
```

The scaler labels include `EVTTRG`, `CORBO`, `FS0&FS1`, and the old `1 kHz` text at channel 15. The old clock label is contradicted by the user’s configuration statement and by the ROOT values. `[L][N][R]`

## 5.2 Patch-panel diagram: `p3_1_X2.png`

The patch-panel/module layout shows:

- coincidence modules 0–3;
- fan-in/fan-out modules;
- `SCINCOINC` signals;
- `EVTTRG`;
- `BUSY`;
- `CORBO`;
- `TDC0`;
- `QDC0`;
- scaler connections;
- discriminator channels;
- 50-ohm termination symbols.

The lower annotation reads approximately:

```text
S0S1FS0FS1 = ALLSCINC
S0S1 = SCINC0INC
```

The patch layout supports the existence of the trigger and fanout paths, but it does not establish the current Katherine GPIO number. `[L][U]`

## 5.3 Logic crops: `logic_left.png` and `logic_center.png`

The logic crops make the following labels clearer:

- C0/C1 discriminator branch;
- S0/S1/FS0/FS1 discriminator branch;
- fourfold S0S1FS0FS1 logic;
- EVTTRIG;
- BUSY;
- CORBO;
- TDC0 channel labels.

The logic-center crop shows two CORBO-area connection points. It is not sufficient by itself to establish which connection was routed to which GPIO or which edge polarity was configured. `[L][U]`

## 5.4 Experimental layout: `p2_0_X0.png`

The experimental-layout diagram shows the beam traveling from left to right through an arrangement of upstream detectors, beam instrumentation, the target/table region, calorimeter modules, and Timepix-related equipment.

It is a schematic layout. It does not provide a complete surveyed path length for the proton and photon timing calculation. `[L][U]`

## 5.5 Electronics photographs

The uploaded electronics photographs show the general rack and module environment, including:

- NIM logic modules;
- VME electronics;
- discriminator/coincidence hardware;
- QDC-related hardware;
- readout equipment;
- patch/rack cabling;
- the Katherine/Timepix readout context.

They are useful for identifying the general equipment classes and confirming that the experiment used conventional NIM/VME logic and a Katherine readout. They do not, by themselves, establish:

- exact cable endpoints;
- exact GPIO number;
- edge polarity;
- TDC channel assignment;
- cable length;
- module delay setting;
- TDC LSB.

The correct rule is:

```text
use photographs for context;
use diagrams/configuration exports/measurements for exact wiring.
```

---

# 6. Timepix measurement observations

## 6.1 Current file headers

The current files identify:

```text
Software: TrackLab 1.6.0
Chip ID: K8-W0036
Detector mode: ToA & ToT
Readout mode: Data-Driven Mode
```

The trigger file header for `measurement_5189_trigger.txt` is:

```text
Event code 1: evttrgcorbofall
Event code 2: evttrg
Event code 4: evttrgcorbolead
```

## 6.2 Current measurement start times

The active block begins approximately as follows:

```text
measurement_5189: 1787536593.820 UTC
measurement_5190: 1787536655.031 UTC
measurement_5191: 1787536716.245 UTC
...
measurement_5201: 1787537328.372 UTC
```

The last trigger in measurement 5201 occurs at approximately 47.590 seconds after that file’s start, giving an end near:

```text
1787537375.962 UTC
```

This is earlier than the logbook end of the TDAQ run. `[M][L]`

## 6.3 Current trigger counts

For measurement files 5189–5201 combined:

```text
code 1, CORBO falling: 83,270
code 4, CORBO leading: 83,270
code 2, EVTTRG:        222,047
```

The equal code-1 and code-4 counts are consistent with paired leading/falling edges for the same CORBO pulse stream. `[M][I]`

## 6.4 Edge separation

For adjacent code-4/code-1 pairs:

```text
median separation ≈ 120.83 ns
range             ≈ 116.67–137.50 ns
```

This supports the interpretation that code 4 is the leading edge and code 1 is the trailing/falling edge of a logic pulse. `[M][I]`

The same edge separation should not be silently included twice in the synchronization offset.

---

# 7. Sixth notebook observations and conflict handling

The sixth notebook is titled:

```text
TimePix - TDAQ - CORBO Matching Guide
```

It explains:

- Timepix measurement files;
- trigger companion files;
- the Unix measurement start time;
- the `pix`, `toa`, `ftoa`, `tot` hit format;
- the Timepix timestamp conversion;
- trigger event codes;
- file matching to TDAQ runs;
- scaler channel 15 as a 1 MHz clock;
- clustering and CORBO matching;
- the no-target reference run;
- rate correlations;
- busy-window scans;
- scaler-rate comparisons.

However, the current repository notebook text says that the older no-target run `1787081424` used only GPIO2 and the CORBO falling edge/code 1. That is a historical example and not evidence that the current 4 GeV block uses the falling edge.

The user’s explicit configuration statement says:

```text
same GPIO arrangement for every run;
leading edge is the recorded synchronization edge.
```

The current measurement-file headers independently show code 4 as the leading edge. The correct current analysis is therefore:

```text
use code 4 for leading-edge synchronization;
keep code 1 for a falling-edge cross-check;
do not infer the physical GPIO port from photographs.
```

The exact physical GPIO port remains unresolved unless a configuration export is provided. `[N][M][U]`

---

# 8. Existing analysis-script observations

## 8.1 `match_timepix_tdaq.py`

The script documents the intended TDAQ matching model:

- ROOT files are named using the run number;
- the run number is treated as a Unix start time;
- `RAWdata` is opened;
- a scaler channel ending in `_ch15` is discovered or selected;
- scaler values are read event by event;
- 32-bit wraps are counted;
- the final clock count gives a coarse elapsed time;
- Timepix file start/end intervals are compared with TDAQ intervals.

This is a file-overlap and coarse-timing tool. It does not, by itself, prove event-by-event physical matching. `[N][I]`

## 8.2 `analyze_timepix_corbo_match.py`

The script:

- reads Timepix hits;
- calculates `25 ns*ToA - 1.5625 ns*FToA`;
- sorts hits by time;
- clusters 8-neighbour pixels within a configurable window;
- calculates earliest/latest/ToT-weighted cluster time;
- reads trigger event codes;
- finds nearest trigger differences;
- scans fixed offsets;
- counts clusters in busy windows;
- calculates binned rate correlations.

Its default comments refer to the older example `1787081424` and GPIO2/CORBO falling. That default should not be copied blindly to the current run. `[N][U]`

## 8.3 Existing no-target analysis results

The notebook’s worked no-target example used:

```text
TDAQ run: 1787081424
Timepix measurements: 9–23
GPIO: older example, code 1/falling edge
```

The notebook reports approximately:

```text
Timepix cluster count: 45,359
CORBO trigger count:   approximately 39,930
```

It reports strong binned rate correlations:

```text
10 ms bins:   correlation ≈ 0.916
50 ms bins:   correlation ≈ 0.943
100 ms bins:  correlation ≈ 0.948
500 ms bins:  correlation ≈ 0.943
```

It also reports an approximate 200 µs busy/readout comparison window. These are useful control-run observations, not final event-by-event proof. `[N][I]`

The notebook’s scaler comparison for that older background block was approximately:

```text
FS0FS1:              130,149
EVTTRG:              111,198
CORBO:                47,399
TDAQ entries:         47,400
Timepix clusters:     45,359
```

Approximate ratios were:

```text
Timepix clusters / EVTTRG ≈ 0.408
Timepix clusters / CORBO  ≈ 0.957
CORBO / EVTTRG            ≈ 0.426
```

These show that Timepix and CORBO can follow the same beam structure while still having different counts due to coverage, efficiency, dead time, acceptance, and clustering choices. `[N][I]`

---

# 9. Calibration-file observations

The files named:

```text
august_normal_trigger_calibration_constants.csv
august_fs_tdc_calibration_constants.csv
august_normal_trigger_calibration_points.csv
august_fs_tdc_calibration_points.csv
```

are QDC/energy calibration outputs despite the presence of `tdc` in one filename. They contain fields such as:

```text
qdc_channel
slope_mev_per_adc
offset_mev
adc_at_1gev
adc_at_2gev
adc_at_3gev
```

They should not be interpreted as a TDC-LSB calibration. `[M][U]`

The QDC calibration is useful for ECAL energy reconstruction, but separate TDC timing documentation is still required for precision timing. `[M][I]`

---

# 10. Search for `txt2root-1.C`

The sixth notebook explains the convention:

```text
x = pix % 256
y = pix / 256
time_ns = toa * 25.0 - ftoa * 1.5625
```

The exact `txt2root-1.C` file was not found in the repository tree during inspection. An exact public copy was also not found by searching for the filename. The current notebook and analysis script are therefore the active evidence for the conversion formula.

The original macro should be recovered if any of these need to be verified:

- Timepix counter rollover handling;
- sign convention for FToA;
- whether timestamps are extended by the exporter;
- whether frame start is added in the macro or later;
- whether pixel data are reordered;
- how trigger association is encoded.

Do not infer SPIDR-specific extended timestamp fields from the generic Timepix3 literature. Katherine/TrackLab must be checked independently. `[N][E][U]`

---

# 11. Main challenges and rejected assumptions

## 11.1 Missing ROOT binary

The local ROOT file is a Git-LFS pointer. Without the binary, arbitrary event-by-event TDC values cannot be read. The text dump resolves the branch/schema and scaler endpoint questions but not the final TDC-unit question.

## 11.2 Stale 1 kHz label

The old diagram label caused an apparent 1 kHz/1 MHz conflict. The user corrected it, and the ROOT values support the user’s correction. The actual run analysis must use 1 MHz.

## 11.3 Leading versus falling edge

The old notebook example says falling edge for an older no-target configuration. Current TrackLab files explicitly contain both edge labels. The current leading-edge stream is code 4. The old and current examples must not be merged without run context.

## 11.4 GPIO channel ambiguity

A photograph or diagram crop may show a CORBO-related connector, but it does not prove the physical Katherine GPIO number. Use the configuration export or documented wiring.

## 11.5 TDC unit ambiguity

TDC branches are integer arrays. Integer storage does not reveal the physical time unit. The TDC LSB remains unresolved.

## 11.6 File coverage mismatch

The Timepix block does not cover all of the ROOT run. Therefore Timepix trigger counts should not be expected to equal 91,274.

## 11.7 High-rate matching ambiguity

Nearest-time matching can assign one Timepix cluster to more than one TDAQ event. Use one-to-one or monotonic sequence assignment and mark ambiguous candidates.

## 11.8 No-target limitation

A no-target run is excellent for calibration and backgrounds but cannot prove that a target CEX reaction occurred.

## 11.9 Proton/photon ordering

A proton is usually slower than a photon, but detector distances and electronics offsets matter. The sign of the measured difference cannot be interpreted before calibration.

## 11.10 File time versus physical time

ROOT entry order, filename order, packet arrival time, and file-writing time are not physical event timestamps.

---

# 12. Evidence ledger

| Statement | Classification | Evidence/reason |
|---|---|---|
| Run 1787536596 is +4 GeV, no target | [L] | August logbook |
| Run has 91,274 entries | [R] | ROOT `RAWdata` output |
| Actual clock is 1 MHz | [N][R] | user configuration + channel-15 values |
| Old 1 kHz label is stale | [L][N][R][I] | diagram versus user/root evidence |
| Scaler ch12 is CORBO | [L][R][I] | diagram label + endpoint equals entries |
| Scaler ch11 is EVTTRG | [L] | August diagram |
| TDC leading/trailing branches exist | [R] | ROOT branch printout |
| TDC LSB | [U] | not in supplied output |
| TDC channel 0–15 map | [L] | rendered diagram |
| TDC channel 16–31 names | [U] | no supplied map |
| TrackLab code 4 is CORBO leading | [M] | trigger-file header |
| TrackLab code 1 is CORBO falling | [M] | trigger-file header |
| Same GPIO arrangement every run | [N] | explicit user statement |
| Physical GPIO number | [U] | not in current export/photo evidence |
| Timepix formula | [N][E] | notebook/script and Timepix3 references |
| QDC calibration values | [M] | calibration CSV/JSON files |
| QDC is not a precise timestamp | [I] | QDC operating principle |
| Current exact CEX event matches | [U] | not independently validated |
| No-target run cannot prove CEX | [I][L] | physics/control-sample logic |

---

# 13. Recommended instructions for another AI

The next AI should follow these rules:

1. Start by reading this dossier before interpreting any new files.
2. Treat the actual scaler frequency as 1 MHz.
3. Use the August scaler map, especially ch11=EVTTRG and ch12=CORBO.
4. Use code 4 as the current CORBO leading-edge stream.
5. Keep code 1 as the falling-edge diagnostic stream.
6. Treat the user’s same-GPIO/leading-edge statement as configuration metadata.
7. Do not claim the physical GPIO number without a configuration export.
8. Do not claim a TDC LSB without documentation or calibration data.
9. Do not use ROOT entry order or file-writing time as physical event time.
10. Use the no-target run for synchronization/background calibration only.
11. Do not claim target CEX from the no-target run.
12. Use target-in data for the final CEX signal.
13. Calibrate the complete Timepix–TDAQ offset using many common triggers.
14. Avoid double-counting cable/module delays.
15. Separate physical time, fixed hardware offset, event-building latency, and file-writing latency.
16. Keep every ambiguous event rather than forcing a match.
17. Report unresolved items explicitly.

---

# 14. Handoff prompt for another AI

The following prompt can be given to another AI together with this dossier:

> You are continuing a high-importance Timepix3–Katherine–TDAQ synchronization and CEX analysis. Read the entire handoff dossier first. Do not reveal private chain-of-thought; instead provide evidence-labelled reasoning, reproducible calculations, explicit assumptions, and unresolved items. The actual scaler clock is 1 MHz; the old diagram label 1 kHz is stale planning information. The August scaler map is ch10=FS0&FS1, ch11=EVTTRG, ch12=CORBO, ch15=1 MHz actual clock. The current TrackLab trigger files define code 4 as `evttrgcorbolead`, code 1 as `evttrgcorbofall`, and code 2 as `evttrg`; use code 4 for leading-edge synchronization. The user states that the same GPIO arrangement was used for every run and the recorded synchronization edge was leading, but the physical GPIO number must not be inferred from photographs. Run 1787536596 is a +4 GeV no-target/background run with 91,274 ROOT entries. The ROOT text output gives the RAWdata schema, scaler endpoint values, and TDC leading/trailing branch schema but not TDC sample values or TDC LSB. Do not fabricate TDC units, event IDs, or Timepix/Katherine semantics. Do not use ROOT entry order, filename order, nominal run start, or file-writing time as physical event time. Explain all clocks, NIM/VME logic, discriminators, coincidence, EVTTRG, BUSY, CORBO, GPIO, scaler, TDC, QDC, ECAL, cable/module delays, TDAQ delay, LSB, physical time, fixed offsets, event-building latency, and file-writing time. Provide the full reproducible matching workflow and the target/no-target CEX selection, and state exactly what remains unresolved.

---

# 15. Short plain-language summary

Two independent systems watched the same beam:

```text
TDAQ/VME/ECAL system
Timepix3/Katherine system
```

The TDAQ recorded accepted events in ROOT.

Timepix recorded pixel hits and external GPIO timestamps.

The accepted trigger was called CORBO.

The actual free-running scaler clock was 1 MHz, meaning one clock count every microsecond.

The current Timepix trigger files identify code 4 as the CORBO leading edge and code 1 as the falling edge.

The synchronization task is to measure the stable time difference between the code-4 Timepix timestamp and the corresponding TDAQ event/trigger timestamp.

Cable and electronics delays are part of that measured offset unless explicitly removed first.

The scaler is useful for coarse timing. The TDC and Timepix timestamps are needed for finer timing.

A no-target run can calibrate the timing and measure backgrounds, but only target-in data can establish a target CEX signal.

# Timepix3–Katherine–TDAQ timestamping and CEX-analysis guide

**Scope.** This is the run-specific guide for the August 2026 BL4S setup, with `1787536596` as the worked example. It combines the logbook and diagrams, the sixth Timepix/TDAQ notebook, the ROOT text dump, the TrackLab exports, the analysis scripts, the available calibration files, and the electronics photographs.

This document is deliberately evidence-labelled. The labels mean:

- **[L] logbook/diagram fact** — written run record or a label/wire in the supplied diagram.
- **[N] notebook or user configuration statement** — notebook text, software configuration, or an explicit configuration statement supplied by the user.
- **[R] ROOT-derived fact** — directly visible in the supplied ROOT `t->Print()`/`t->Scan()` output.
- **[M] measurement-file fact** — directly visible in a TrackLab measurement or trigger export.
- **[E] external documentation** — manufacturer, software, ASIC, or published timing reference.
- **[I] physics/electronics inference** — a conclusion derived from the facts, not a literal label in a file.
- **[U] unresolved item** — information that is not present in the supplied files and must not be silently guessed.

Where a conclusion uses more than one kind of evidence, each relevant label is shown. A statement marked **[I]** is useful for analysis, but is not itself a hardware fact.

---

## 1. Executive conclusion

**[N][R] The scaler clock used for the actual experiment was 1 MHz, not 1 kHz.** The old `1 kHz` text in the diagram is a planning/stale label. The user states that the initial 1 kHz plan was abandoned because the beam rate could exceed about 1,000 particles/s. The ROOT values independently support 1 MHz: the channel-15 count reaches `810,801,268` during this approximately 814 s run, which is the correct order for a 1 MHz counter and impossible for a 1 kHz counter unless the label and the meaning of the branch were wrong.

**[M] The current TrackLab trigger exports contain separate edge streams.** Their headers define event code 4 as `evttrgcorbolead` and event code 1 as `evttrgcorbofall`. In the supplied current files, code 4 precedes code 1 by a median of approximately `120.83 ns`, with values quantized between about `116.67 ns` and `137.50 ns`. Therefore, when the requested reference is the leading edge, use code 4. Code 1 is the falling-edge companion, not the same timestamp.

**[N][M] The user’s current configuration statement is that the same GPIO arrangement was used for every run and that the recorded synchronization edge was the leading edge.** I treat that as configuration metadata. The repository copy of the sixth notebook still contains a run-specific note saying that the older 3 GeV no-target example used only GPIO2 and recorded the CORBO falling edge. That notebook wording must not be cited as proof that the current 4 GeV files use the falling edge. The current export headers objectively identify the leading-edge stream as code 4. The exact physical Katherine SMA/GPIO port for the current run is not established by the photographs or by the current trigger-file header. **[U]**

**[R][L] Run `1787536596` is a no-target/background run.** It has a 4 GeV positive beam, beamfile `<019>`, trigger condition `S0S1FS0FS1`, 91,274 ROOT entries, and the logbook start and finish times `24-Aug-2026 03:56:36` to `04:10:10` local time. It is appropriate for synchronization, background, and accidental studies. It cannot by itself prove CEX on a target.

**[U] The guide is sufficient to implement the complete synchronization and CEX workflow, but not to report a final nanosecond TDC offset.** The supplied ROOT text dump gives the TDC branch schema but does not give the TDC sample values, TDC reference frequency, or hardware TDC LSB. The physical GPIO port and the exact ECAL timing observable are also not fully documented in the supplied files. Those facts are required before publishing a final absolute proton–photon timing result.

---

## 2. Run-specific data audit

### 2.1 Run metadata

| Item | Value | Evidence |
|---|---:|---|
| TDAQ run | `1787536596` | [L] run log; [R] filename convention in the analysis script |
| Beam | `+4 GeV` | [L] |
| Beamfile | `<019>` | [L] |
| Target | no target/background | [L] |
| Trigger condition | `S0S1FS0FS1` | [L] |
| Logbook start | 24-Aug-2026 03:56:36 local | [L] |
| Logbook finish | 24-Aug-2026 04:10:10 local | [L] |
| ROOT tree | `RAWdata` | [R] |
| ROOT entries | `91,274` | [R] |
| DESY position | approximately `H=35.165`, `V=1.278` | [L] |

The local time in the August CERN logbook is two hours ahead of UTC. Thus the run filename/start convention gives approximately `1787536596` Unix seconds, or `24-Aug-2026 01:56:36 UTC`. The filename is useful for identifying the run and for coarse file matching; it is not a per-event physical timestamp. **[L][I]**

### 2.2 The actual scaler evidence for 1 MHz

The supplied ROOT scan is:

| ROOT entry | `Scaler0_ch10` | `Scaler0_ch11` | `Scaler0_ch12` | `Scaler0_ch15` |
|---:|---:|---:|---:|---:|
| first shown, entry 0 | 1 | 1 | 1 | 3,884,549 |
| last entry 91,273 | 281,094 | 247,387 | 91,274 | 810,801,268 |

**[R]** These are the exact first/last values visible in the supplied text output. The ROOT branch definitions show `Scaler0_ch0` through `Scaler0_ch15`, all stored as unsigned 32-bit integer leaves (`/i`).

For channel 15:

```text
last value / 1,000,000 = 810.801268 s
last - first             = 806,916,719 counts
(last - first)/1e6       = 806.916719 s
```

**[R][I]** A count rate of 1 MHz is consistent with the approximately 810.8 s counter value and with the roughly 814 s logbook interval. A 1 kHz clock would produce only about 814,000 counts, not about 810 million counts. The difference between the logbook duration and the counter-derived interval is a start/stop/reference issue: the first stored ROOT event is not necessarily the instant at which the run clock was reset, and the logbook times are recorded to coarse seconds. It is not evidence for 1 kHz.

The analysis script uses the final channel-15 count as the run elapsed time and includes 32-bit counter wraps. That is valid only if the counter origin is known to be aligned with the run start. For event-to-event timing within one file, use the difference between two channel-15 snapshots; for an absolute run endpoint, validate the counter origin against the logbook start and an independent timing pulse. **[N][I][U]**

A 32-bit 1 MHz counter wraps after:

```text
2^32 / 1e6 = 4294.967296 s = 71.5828 min.
```

Therefore a longer run must be unwrapped by detecting a downward step and adding `2^32`. Run `1787536596` does not reach one wrap. **[R][I]**

### 2.3 Current scaler map

The August diagram labels the scaler inputs as follows:

| Scaler channel | Signal in the diagram | Role |
|---:|---|---|
| 0 | discriminator C0 | C0 discriminator count |
| 1 | discriminator C1 | C1 discriminator count |
| 2 | discriminator S0 | S0 count |
| 3 | discriminator S1 | S1 count |
| 4 | discriminator FS0 | FS0 count |
| 5 | discriminator FS1 | FS1 count |
| 6 | discriminator S2 | S2 count |
| 7 | discriminator S3 | S3 count |
| 8 | scintillator coincidence & C0 | coincidence rate |
| 9 | scintillator coincidence & C1 | coincidence rate |
| 10 | FS0 & FS1 | fiber/scintillator coincidence |
| 11 | EVTTRG | pre-accept/event-trigger logic count |
| 12 | CORBO | busy-vetoed/accepted trigger count |
| 13 | AV1 & AH1 discriminator | DWC/beam condition |
| 14 | AV0 & AH0 discriminator | DWC/beam condition |
| 15 | diagram says 1 kHz | actual configured/reference clock is 1 MHz |

The diagram is the source of the names. The current ROOT endpoints provide a useful consistency check: `Scaler0_ch12` finishes at `91,274`, exactly the number of ROOT entries, whereas channel 11 finishes at `247,387`. **[L][R][I]** This strongly indicates that channel 12 is the accepted CORBO/event stream for this run and channel 11 is the higher-rate EVTTRG stream. The full binary should still be used to verify that channel 12 increments once for every entry and never skips an accepted event. **[U]**

Do not use the generic student notebook’s older `Scaler0_ch12 = EVTTRG` wording for this August run. It is inconsistent with the August diagram and with the current run’s endpoint counts. **[L][R][U]**

### 2.4 ROOT schema actually available

The ROOT text dump shows:

- `RAWdata`, with 91,274 entries. **[R]**
- QDC branches for the calorimeter channels, including raw ADC values and overflow/under-threshold/valid flags. **[R]**
- `TDC0_ch0` through `TDC0_ch31`, with per-channel multiplicity branches and separate leading and trailing arrays. **[R]**
- `Scaler0_ch0` through `Scaler0_ch15`, cumulative unsigned 32-bit values. **[R]**
- no named event/time branch was visible in the supplied `t->Print("*Trig*")`, `t->Print("*Event*")`, or `t->Print("*Time*")` sections. **[R]**

For each TDC channel `n`, the schema is of the form:

```text
NTDC0_chN
TDC0_chN[NTDC0_chN]
NTDC0_chN_leading
TDC0_chN_leading[NTDC0_chN_leading]
NTDC0_chN_trailing
TDC0_chN_trailing[NTDC0_chN_trailing]
```

The supplied diagram labels TDC0 channels 0–15 as:

```text
0  C0       1  C1       2  S0       3  S1
4  FS0      5  FS1      6  S2       7  S3
8  DWC0 L   9  DWC0 R  10  DWC0 U  11  DWC0 D
12 DWC1 L  13  DWC1 R  14  DWC1 U  15  DWC1 D
```

The root schema has channels 16–31 as well, but their hardware names are not in the supplied diagram. Do not assign those channels to CORBO or an ECAL without a patch-panel/configuration record. **[L][R][U]**

---

## 3. GPIO and edge convention

### 3.1 What the current measurement files say

For example, `measurement_5189_trigger.txt` has these headers:

```text
# Event code 1: evttrgcorbofall
# Event code 2: evttrg
# Event code 4: evttrgcorbolead
```

The first data records are:

```text
2  1.62704414167
4  1.62704415833
1  1.62704427917
```

The trigger times are seconds after the measurement start. The code-4 leading edge appears before the code-1 falling edge. This is a measurement-file fact, not a visual inference. **[M]**

Across measurement files 5189–5201, the totals are:

```text
code 1, CORBO falling edge: 83,270
code 4, CORBO leading edge: 83,270
code 2, EVTTRG:             222,047
```

The code-4/code-1 edge separation has a median of about 120.83 ns. It is therefore appropriate to use code 4 when comparing a leading-edge timestamp, and to use code 1 only when the TDAQ timestamp is explicitly a falling edge. Mixing code 4 on one side with code 1 on the other adds the pulse width to the fitted offset. **[M][I]**

The files begin at `measurement_5189` Unix time `1787536593.820`, about 2.180 s before the ROOT run start, and the supplied block ends at approximately `1787537375.962`, about 34 s before the logbook run finish. Thus the Timepix block is an overlap, not a complete copy of the TDAQ run. Its 83,270 edge pairs should not be expected to equal the 91,274 ROOT entries. **[M][L][I]**

### 3.2 Notebook wording and the current correction

The current repository version of the sixth notebook describes the older no-target reference run `1787081424` as “only GPIO2” recording “CORBO falling edge,” with event code 1 used in that example. **[N]** The current 4 GeV TrackLab files have both explicit leading and falling event-code streams, and the user’s configuration statement says the historical arrangement was the same for every run and the synchronization edge was leading. **[N][M]**

The safe analysis rule is:

1. treat the user’s explicit current configuration statement as the intended run metadata;
2. use the actual TrackLab event-code header to choose the edge (`4` for leading, `1` for falling);
3. do not infer a physical GPIO number from a photograph;
4. preserve both edge streams so that a 120 ns polarity/edge mistake can be diagnosed;
5. if the physical port number is required in a publication, obtain the Katherine/TrackLab configuration export or a wiring record. **[N][M][U]**

The current trigger-file headers do not name “GPIO2”; they name the logical event codes. Thus they prove the exported edge semantics, but not the physical SMA port. **[M][U]**

---

## 4. Full signal path in words

The following is the documented/inferred signal chain. It is written from the detectors toward the two DAQ systems.

### 4.1 Beam detectors and NIM logic

1. A beam particle crosses the upstream beam counters and the fiber/scintillator detectors. C0, C1, S0, S1, FS0, FS1, S2, and S3 produce analog detector pulses. **[L]**
2. NIM discriminators convert those analog pulses into standardized logic pulses. A discriminator is a threshold device: it emits a logic transition when the detector pulse crosses the chosen threshold. **[L][I]**
3. C0 and C1 provide a Cherenkov-based beam-particle condition. The diagram shows C0 as the counter that can respond to `e, μ, π` and C1 as the `e, μ` condition; a C0-and-not-C1 coincidence is therefore a pion-like beam discriminator in the trigger logic. This is a beam-PID inference, not a complete event-by-event pion identification. **[L][I]**
4. The current run’s main trigger condition is the fourfold `S0 ∧ S1 ∧ FS0 ∧ FS1`. The NIM coincidence/logic modules form the required coincidences, and `EVTTRG` is the event-trigger logic output. **[L]**
5. `BUSY` is the readout-dead-time signal (a veto indicating that the TDAQ is not ready to accept another event). The diagram and sixth notebook describe `CORBO` as the event-trigger condition combined with the busy veto, conventionally represented as `EVTTRG ∧ ¬BUSY`. The exact active-high/active-low electrical polarity at each module must be taken from the module configuration, not guessed from the symbol. **[L][N][I]**
6. The accepted CORBO pulse is fanned out. One copy is used by the VME TDAQ as the event/accept condition, one is counted by scaler channel 12, and a copy is sent through the documented cable/patch path to the Katherine GPIO for Timepix external-event timestamping. The exact physical GPIO connector is unresolved in the supplied material. **[L][N][U]**

### 4.2 VME TDAQ branch

After CORBO is accepted:

```text
CORBO accept
    ├── create one RAWdata event / readout transaction
    ├── snapshot cumulative scaler channels
    ├── latch TDC leading/trailing hits in the event window
    └── open or gate the QDC/ECAL charge integration
```

The ROOT entry is a storage record associated with an accepted TDAQ event. It is not automatically the time of the beam particle. The cumulative scaler values in that record give a coarse time reference and trigger counts; the TDC arrays give edge information for the channels actually connected to TDC0. **[R][I]**

### 4.3 TDC branch

A TDC (time-to-digital converter, an instrument that turns an input logic edge into a digital time code) receives discriminator outputs. The diagram explicitly maps the beam/scintillator and DWC discriminator channels to TDC0 channels 0–15. The root schema stores leading and trailing arrays separately, so a pulse width can be formed when both edges exist:

```text
pulse_width = (trailing_code - leading_code) × TDC_LSB
```

The TDC timestamp is only physically interpretable after the reference edge, epoch/rollover behavior, units, and channel wiring are known. **[R][U]**

### 4.4 QDC and ECAL branch

A QDC (charge-to-digital converter, an ADC that integrates charge in a gate) integrates the ECAL pulse during a trigger-relative gate and stores a calibrated or raw charge/energy value. The QDC gate has a start delay, a gate width, a conversion time, and a readout time. The amplitude is useful for energy reconstruction, but the value of a QDC channel is not an independent photon arrival timestamp. **[L][R][I]**

Use the QDC calibration JSON/CSV files to convert ADC values to energy. Use the QDC valid/overflow/under-threshold flags to reject unusable measurements. Do not use ROOT write order or the time at which the QDC conversion finished as the photon interaction time. **[R][I]**

### 4.5 Katherine Gen2 / Timepix3 branch

The beam particle produces threshold-crossing hits in the Timepix3 pixel matrix. The Timepix3 ASIC records pixel position, ToA (time of arrival), FToA (fine time of arrival), and ToT (time over threshold, a charge-like pulse-width quantity). TrackLab writes pixel hits to the measurement text file and external event timestamps to the trigger companion file. **[M][E]**

Katherine Gen2 documentation describes external-trigger timestamping with an internal TDC, four GPIO ports, programmable termination, and injection of external trigger events into the common pixel data stream. TrackLab documentation describes Katherine control and GPIO pin-function configuration. These are capabilities of the hardware/software platform; they do not by themselves prove which GPIO was used in this experiment or how the current text exporter names every event. **[E][U]**

---

## 5. The separate time bases

There is no single universal timestamp in the supplied files. Keep these clocks separate.

### 5.1 Timepix3 pixel time

The conversion used by the sixth notebook and `analyze_timepix_corbo_match.py` is:

```text
τ_pixel_ns = 25.0 ns × ToA - 1.5625 ns × FToA
```

The absolute time reconstructed from a measurement file is:

```text
t_pixel_abs = measurement_start_Unix + τ_pixel_ns / 1e9
```

The 25 ns coarse period comes from the 40 MHz ToA clock and the nominal 1.5625 ns fine period from the 640 MHz FToA refinement. **[N][E]** The formula gives digitization coordinates; it is not a guarantee that the detector system has 1.5625 ns physical accuracy. Pixel threshold time walk, pixel-to-pixel offsets, sensor response, clock phase, readout behavior, and calibration all contribute. **[E][I]**

The supplied `txt2root-1.C` macro itself was not found in the repository, and an exact public copy was not found by searching for its filename. The convention above is nevertheless present in the sixth notebook and analysis script and is consistent with the published Timepix3 ToA/FToA description. The macro should be recovered if the exporter’s rollover or sign convention needs to be proven. **[N][E][U]**

### 5.2 TrackLab GPIO event time

For a trigger row with relative time `τ_GPIO_s`:

```text
t_GPIO_abs = measurement_start_Unix + τ_GPIO_s
```

This is a Katherine/TrackLab timestamp of the selected GPIO edge in the exported time domain. It is not automatically the instant of the particle’s interaction at the target. It includes the physical signal path up to the GPIO, the GPIO input threshold/logic delay, and the Katherine timestamp reference. **[M][E][I]**

### 5.3 TDAQ scaler clock

For entry `i`, a coarse TDAQ time can be constructed from channel 15:

```text
τ_scaler_i = unwrap(Scaler0_ch15[i]) / 1e6 seconds
```

For a time relative to the first stored event, use:

```text
τ_scaler_relative_i = unwrap(ch15[i] - ch15[first]) / 1e6 seconds
```

For an absolute run time, use `ch15[i]/1e6` only after validating the counter origin against the run start. The scaler has a 1 µs count bin. It is excellent for coarse overlap, rate, spill structure, and event-order checks; it is not a nanosecond timestamp. **[R][N][I][U]**

### 5.4 TDC time

For a TDC code `q`:

```text
t_TDC = t_reference + q × TDC_LSB + epoch correction + channel offset
```

The exact `TDC_LSB`, reference, epoch/rollover convention, and absolute meaning of the arrays are not in the supplied ROOT text dump. Do not write `t_TDC = code × 1 ns`, `25 ps`, or any other unit until the VME TDC documentation or a calibration-pulse measurement confirms it. **[R][U]**

### 5.5 QDC conversion and file-writing time

The time at which a QDC conversion completes, the time at which a VME event is built, the time at which a UDP/USB packet is received, and the time at which a ROOT or TXT record is written are transport/storage times. They are not the physical hit time. **[I]**

---

## 6. Physical time, fixed offsets, latency, and file time

A useful model for a timestamp from channel `k` is:

```text
t_record,k = t_phys
            + t_flight,k
            + d_sensor,k
            + d_discriminator,k
            + d_cable,k
            + d_logic,k
            + d_module,k
            + q_clock,k
```

where:

- `t_phys` is the physical interaction or particle crossing time;
- `t_flight,k` is the particle/photon flight time to detector `k`;
- `d_sensor,k` is sensor/shaping/threshold delay;
- `d_discriminator,k` is threshold-crossing delay and time walk;
- `d_cable,k` is cable propagation delay;
- `d_logic,k` is coincidence, fan-in/fan-out, gate, and veto delay;
- `d_module,k` is a fixed delay in a discriminator, delay unit, TDC input, QDC gate, GPIO input, or readout module;
- `q_clock,k` is quantization and clock-phase error.

After the timestamp has been made, there can be additional terms:

```text
L_build       = event-building/buffering/transport latency
L_file        = file-writing or packet-storage latency
```

Those terms affect when software receives or writes the record, not `t_phys`. **[I]**

### 6.1 Is cable/module delay part of “TDAQ delay”?

It can be, but the phrase “TDAQ delay” is ambiguous. Define it before using it. A good definition is:

```text
D_TDAQ(path, reference) = time from the chosen physical reference edge
                           to the TDAQ timestamp for that path.
```

With that definition, cable propagation, discriminator delay, logic-module delay, fan-out delay, and TDC input delay before the latch are included in `D_TDAQ`. A delay unit intentionally inserted before the latch is also included. **[I]**

A fixed delay is useful for synchronization because it is stable and can be calibrated. It is not useful as an unverified absolute correction simply because it appears on a photograph or in a nominal module label. Measure the complete path, or fit its constant offset using a common pulse. **[I][U]**

### 6.2 Avoiding double counting

Use one of these two approaches, not both:

**Measured-offset approach:**

```text
t_TP_corrected = t_TP_raw + fitted_offset
```

The fitted offset already contains the stable difference in cable, module, logic, sensor, and timestamp delays along the two measured paths. Do not add those same nominal cable/module delays again.

**Component-budget approach:**

```text
fitted_residual = measured_difference
                  - (known cable + module + logic contributions)
```

Here the known contributions are explicitly removed before interpreting the residual. Keep a table showing exactly which terms were subtracted.

A path delay before the hardware timestamp belongs in the calibration offset. Event-building latency and file-writing latency occur after the timestamp and must not be subtracted as detector delays. **[I]**

### 6.3 What delay matters for which analysis?

| Quantity | Useful for synchronization? | Use in physical TOF? |
|---|---|---|
| common CORBO cable delay | yes, as a fixed offset | remove only by calibrated path difference |
| discriminator threshold delay | yes, if stable; correct time walk if amplitude varies | yes, after calibration |
| coincidence/fan-out propagation | yes | include in measured trigger offset |
| QDC gate start delay | links charge integration to trigger | not a photon timestamp by itself |
| TDC channel offset | yes | subtract/calibrate per channel |
| TDC quantization | sets granularity | include in uncertainty |
| event-building latency | no, after timestamp | never use as TOF correction |
| network/USB/UDP latency | no, unless a hardware timestamp is absent and only rate matching is intended | never call it detector flight time |
| file-writing time | no | never use as particle time |

---

## 7. What the TDC LSB means

The LSB (least-significant bit) is the smallest digital time bin represented by one increment of a TDC code. If a TDC has `LSB = 100 ps`, adjacent codes represent 100 ps nominal intervals. It does **not** mean that every measured time is accurate to 100 ps.

For an ideal uniform quantizer, the RMS quantization contribution is approximately:

```text
σ_quantization = LSB / sqrt(12)
```

The real uncertainty is more like:

```text
σ_total^2 = σ_quantization^2
          + σ_detector_jitter^2
          + σ_discriminator_jitter^2
          + σ_timewalk^2
          + σ_clock_phase^2
          + σ_cable/module_variation^2
          + σ_calibration^2
```

This is why “TDC LSB” and “timing accuracy” must be reported separately. **[I]**

For this experiment:

- the scaler LSB is 1 µs because the actual reference is 1 MHz; **[N][R]**
- Timepix3’s nominal fine bin is 1.5625 ns, with a 25 ns coarse ToA clock; **[E]**
- the TrackLab trigger rows visibly have a finer numerical grid, but the formal Katherine GPIO timestamp LSB is not established by the text exports alone; **[M][U]**
- the VME TDC LSB is not established by the supplied ROOT text output; **[U]**
- a QDC ADC LSB is a charge/energy bin, not a time bin. **[I]**

The TDC LSB is still valuable even when the final accuracy is worse: it determines the histogram binning, the minimum resolvable digital difference, the quantization uncertainty, and whether a fitted offset is being over-reported with too many digits. **[I]**

---

## 8. File matching and event matching

### 8.1 Stage A: catalogue files

For each Timepix measurement file, record:

```text
measurement_id
measurement start Unix time
chip ID
number of pixel rows
number of trigger rows
counts for event codes 1, 2, and 4
last trigger time
```

For each ROOT file, record:

```text
run number from filename
RAWdata entries
branch inventory
first/last Scaler0_ch15
first/last Scaler0_ch11 and ch12
number of scaler wraps
run endpoint estimate
beam/target metadata
```

Use UTC Unix times for the first file join. Do not use filename order, ROOT entry order, or file-writing time as event time. **[I][R][M]**

For run `1787536596`, the supplied overlapping block is measurement files 5189–5201. Files 5187 and 5188 have headers but no trigger rows in the current workspace, so they should not be counted as synchronized event data. **[M]**

### 8.2 Stage B: construct the TDAQ event table

With the real ROOT file, loop over `RAWdata` entries and save:

```text
root_entry
ch15_raw
ch15_unwrapped
coarse_tdaq_s = ch15_unwrapped / 1e6
ch10_raw
ch11_raw
ch12_raw
all QDC values and validity flags
all NTDC0_chN values
all leading/trailing TDC arrays
```

Treat `root_entry` only as a row locator. If the full scan confirms that `ch12` increments once per entry, add:

```text
accepted_trigger_index = ch12_unwrapped - ch12_first
```

as a derived sequence number. Label it as a derived trigger index, not as a native event ID. **[R][I][U]**

### 8.3 Stage C: construct the Timepix table

For each pixel row:

```text
x = pix % 256
y = pix // 256
τ_pixel_ns = 25.0*toa - 1.5625*ftoa
t_pixel_abs = measurement_start_Unix + τ_pixel_ns/1e9
```

For each trigger row:

```text
t_trigger_abs = measurement_start_Unix + trigger_relative_seconds
```

Keep code 4 and code 1 in separate columns. Pair them only when their separation is physically plausible; do not silently replace a leading edge with a falling edge. **[N][M]**

### 8.4 Stage D: form Timepix particle clusters

Cluster hits after reconstructing timestamps, using spatial adjacency and a scanned time-adjacency window. The existing analysis uses 8-neighbour pixel adjacency, a 200 ns first-pass cluster window, and a configurable earliest/weighted/latest cluster time. Those are analysis choices, not hardware constants. **[N][I]**

For every cluster save:

```text
measurement_id
cluster_id
first/last pixel time
chosen cluster time
x/y centroid
pixel count
sum and maximum ToT
cluster duration
```

Use the earliest hit for a leading-edge comparison only after checking threshold/time-walk effects. A ToT-weighted time can be useful for a cluster centroid, but it is not automatically the physical particle entrance time. **[I]**

### 8.5 Stage E: calibrate Timepix–TDAQ timing

Use the no-target run as a synchronization/control sample:

1. Convert code-4 leading-edge times to Unix seconds. **[M]**
2. Convert TDAQ channel-15 snapshots to coarse Unix-relative times. **[R]**
3. Restrict to the real overlap interval. **[M][L]**
4. Scan a broad offset and compute a cross-correlation or trigger-rate correlation. **[I]**
5. Fit a clock scale and offset:

   ```text
   t_TP = a + b*t_TDAQ
   ```

   where `a` is the fixed offset and `b` detects relative clock drift. **[I]**
6. If the ROOT TDC contains the corresponding CORBO edge, replace the 1 µs scaler timestamp with that TDC time for the final fit. **[U]**
7. Inspect residuals versus time, measurement file, trigger rate, and ToT. A stable narrow residual distribution is required before applying the calibration to target runs. **[I]**

The existing approximately 200 µs busy/readout comparison window is a useful scan point, not a validated physical resolution. Scan at least 10, 50, 100, 200, and 500 µs, and report the residual distribution and accidental rate for each. **[N][I]**

### 8.6 Stage F: assign clusters to events without forcing matches

For each TDAQ event, generate all Timepix clusters inside the calibrated event window. Then:

- use a one-to-one assignment when the hardware event model supports it;
- use the smallest calibrated residual only when the candidate is unique;
- mark an event ambiguous when two clusters/triggers are comparably plausible;
- keep unmatched Timepix clusters and unmatched TDAQ events for efficiency/accidental studies;
- never assign an event merely because two files overlap in wall-clock time.

At high rate, independent nearest-neighbour matching can assign the same cluster to multiple triggers. A global monotonic assignment or a sequence-alignment method is safer when only a common trigger stream is available. **[I]**

### 8.7 If the TDAQ has no CORBO TDC record

The current diagrams clearly show CORBO as a trigger/fanout signal, but the supplied TDC channel map does not identify a CORBO TDC channel. If no ROOT branch stores a CORBO edge or trigger timestamp, then:

- the 1 MHz scaler gives a coarse event time and event order;
- the Timepix code-4 stream gives a high-resolution external-trigger time on the Katherine side;
- exact event-by-event correspondence must be established by sequence alignment, known trigger acceptance, and residual validation;
- if trigger loss/prescaling cannot be quantified, only a statistical rate correlation is proven, not every individual match. **[L][R][M][U][I]**

---

## 9. ECAL/QDC synchronization

The ECAL QDC records charge integrated in a trigger-relative gate. The correct event-level association is therefore:

```text
accepted CORBO event
    -> QDC gate opens after a known trigger/gate delay
    -> ECAL pulse is integrated during the gate
    -> QDC value is read out and stored in the same RAWdata event
```

The QDC value should be joined to the TDAQ event using the event/accept record, not using the time at which the QDC conversion finished. **[R][I]**

For timing, use one of the following, in descending order of authority:

1. an ECAL TDC edge branch with documented channel and LSB; **[U]**
2. a calibrated ECAL discriminator edge in TDC0; **[L][R][U]**
3. the accepted trigger plus a measured QDC gate delay, with a timing uncertainty equal to the gate/shape uncertainty; **[I][U]**
4. never the ROOT write timestamp or row order. **[I]**

Use the QDC calibration files to obtain photon/shower energies, reject `OF`, `UT`, and invalid channels, and identify bad/unstable calorimeter channels. The August calibration notes contain channel-specific issues; do not assume all 16 channels have identical calibration quality. **[M][L]**

For a two-photon candidate, calculate:

```text
m_γγ² = 2 E1 E2 (1 - cos θ12)
```

where the photon directions come from the ECAL geometry and a target/vertex hypothesis. A two-cluster mass near the neutral-pion mass is necessary for a π0 candidate but is not alone proof of a CEX event. **[I]**

---

## 10. CEX analysis recipe

The exact reaction channel must be stated in the analysis metadata. The following is the generic selection for a charge-exchange hypothesis with a neutral-pion/photon system and a recoil proton.

### 10.1 Build a good-event sample

Require:

- a valid TDAQ/`RAWdata` event; **[R]**
- accepted CORBO/live trigger, with BUSY and trigger logic interpreted consistently; **[L][R]**
- valid QDC values for the ECAL channels used; **[R]**
- required beam-detector/TDC hits; **[L][R]**
- no corrupted or overflowed event record. **[R]**

### 10.2 Identify the incoming beam

Use the beam scintillator/fiber conditions and the calibrated C0/C1 Cherenkov logic. A raw scaler subtraction such as `C0-C1` is a rate diagnostic, not automatically an event-by-event pion label, because the scaler channels are ungated cumulative discriminator counts and may have different efficiencies/dead time. **[L][I]**

### 10.3 Reconstruct ECAL photon candidates

For each accepted event:

1. calibrate QDC ADC to energy;
2. reject invalid/overflow/under-threshold channels;
3. form spatially contiguous ECAL showers;
4. choose photon-like clusters and apply energy thresholds;
5. form all two-cluster combinations;
6. calculate `m_γγ` and the direction-to-target constraint;
7. retain a π0 candidate only after timing and accidental checks. **[I]**

### 10.4 Reconstruct a charged/proton candidate

Use the Timepix cluster/track and, where available, DWC TDC information:

- require a calibrated Timepix–TDAQ event association;
- require a track direction compatible with a vertex in the target region;
- use cluster shape, ToT/energy-loss information, and downstream geometry;
- use time of flight and momentum/kinematic constraints for proton PID (particle identification);
- do not call every Timepix cluster a proton. **[I]**

### 10.5 CEX candidate and background definition

A CEX candidate should satisfy, in one matched event:

```text
incoming beam condition
+ target-compatible interaction vertex
+ two photon-like ECAL showers
+ m_γγ compatible with π0
+ proton-like charged track/cluster
+ calibrated timing
+ kinematic closure
```

Use missing momentum/four-momentum and the appropriate nuclear-target recoil model. For a nuclear target, include Fermi motion, binding, and the residual nucleus; do not apply a free-neutron equation without checking the target composition. **[I]**

The no-target run measures beam-through, detector material, accidental Timepix–ECAL combinations, and other backgrounds. Normalize it using accepted trigger count/live time and compare spatial, timing, and energy distributions. It cannot by itself establish that a target CEX reaction occurred. A target-in excess over the no-target/empty-target and off-time sideband backgrounds is required. **[L][I]**

---

## 11. Which arrives first: recoil proton or ECAL photons?

Do not decide this from ROOT entry order, Timepix file order, or a nominal “TDAQ delay.” The physical comparison is:

```text
Δt_observed = t_Timepix_proton - t_ECAL_photon
```

The expected detector-arrival difference for a candidate with vertex-to-detector path lengths `L_p` and `L_γ` is approximately:

```text
Δt_expected_physical = L_p/(β_p c) - L_γ/c
```

The measured difference contains detector/electronics offsets:

```text
Δt_observed = Δt_expected_physical
            + (offset_Timepix - offset_ECAL)
            + calibration residual
```

For an outgoing proton with `β_p < 1`, the proton takes longer than a photon over the same distance. But the Timepix and ECAL path lengths, detector locations, trigger paths, thresholds, and calibrated offsets can reverse the observed ordering. The supplied layout is schematic and the current files do not provide a validated ECAL timestamp plus complete path-length survey and offsets. Therefore the final proton-before/proton-after statement is **[U]** until those quantities are inserted into the equation.

A correct determination is:

1. obtain the target vertex and detector coordinates;
2. calculate `L_p` and `L_γ` for the candidate geometry;
3. estimate `β_p` from the kinematic/proton hypothesis;
4. measure the Timepix–ECAL offset with a common beam/reference sample;
5. compare corrected data to `Δt_expected_physical`; and
6. report the residual and uncertainty, not only the sign. **[I]**

---

## 12. Minimal implementation pseudocode

```python
# TDAQ side
for i in range(rawdata.GetEntries()):
    rawdata.GetEntry(i)
    ch15 = unwrap(rawdata.Scaler0_ch15)
    t_tdaq_coarse_s = ch15 / 1_000_000.0
    accepted_index = rawdata.Scaler0_ch12 - ch12_first  # only after full-scan validation
    save_tdaq_event(i, t_tdaq_coarse_s, accepted_index,
                    qdc_values_and_flags(), tdc_leading_trailing_arrays())

# Timepix side
for measurement in measurements:
    t0 = parse_unix_start(measurement)
    for pix, toa, ftoa, tot in pixel_rows(measurement):
        t_hit_s = t0 + (25.0*toa - 1.5625*ftoa) * 1e-9
        save_hit(t_hit_s, pix % 256, pix // 256, tot)
    for code, relative_s in trigger_rows(measurement):
        save_trigger(t0 + relative_s, code)

# Synchronization
leading = triggers[code == 4]
tdaq = tdaq_events_with_valid_coarse_times
calibration = fit_offset_and_optional_drift(leading, tdaq,
                                             windows_us=[10, 50, 100, 200, 500])

# Event matching
for event in tdaq_events:
    candidates = clusters_in_calibrated_window(event, calibration)
    assign_unique_or_mark_ambiguous(event, candidates)

# Physics
for event in matched_events:
    photons = reconstruct_ecal_photon_clusters(event)
    pi0s = photon_pairs_near_pi0_mass(photons)
    protons = timepix_tracks_with_proton_hypothesis(event)
    select_cex_candidates(pi0s, protons, timing_and_kinematic_cuts)
```

The actual ROOT implementation must use the binary file or a complete value dump. The current 133-byte `.root` in the checkout is only a Git-LFS pointer; the supplied text dump is sufficient for schema and scaler endpoint facts, but not for arbitrary event-by-event TDC extraction. **[R][U]**

---

## 13. Required validation products before publication

Produce and retain these tables:

### TDAQ event table

```text
run
root_entry
ch15_raw
ch15_unwrapped
coarse_tdaq_time
ch10/ch11/ch12
accepted_trigger_index (derived, if validated)
QDC values and validity flags
TDC multiplicities and leading/trailing arrays
```

### Timepix hit/cluster table

```text
run
measurement_id
pixel x/y
raw ToA/FToA/ToT
absolute pixel time
cluster ID/time/size/shape
```

### GPIO table

```text
run
measurement_id
code-2 EVTTRG time
code-4 CORBO leading time
code-1 CORBO falling time
lead-to-fall separation
```

### Synchronization table

```text
run
reference edge
TDAQ reference channel
fitted offset
clock scale/drift
residual median/RMS/quantiles
candidate multiplicity
accidental rate
```

### CEX table

```text
run
event/trigger index
ECAL photon energies and directions
m_γγ
Timepix cluster/track
Δt observed
Δt expected
proton PID variables
kinematic residuals
classification: unmatched / accidental / background / CEX candidate
```

The minimum extra information needed for a final numerical nanosecond claim is:

1. TDC values for a representative ROOT scan and the VME TDC model/reference or a known calibration-pulse measurement; **[U]**
2. the Katherine/TrackLab GPIO configuration export or documented wiring if the physical SMA number must be stated; **[U]**
3. ECAL timing edge/gate definition and a path-length survey for the proton–photon ordering; **[U]**
4. the original `txt2root-1.C` if its rollover/export convention differs from the notebook/script formula. **[U]**

---

## 14. External references

1. **Katherine Gen2.** P. Burian et al., “Katherine Generation 2: advanced readout system for Timepix3 detectors,” *JINST* 20 (2025) C06077, DOI [10.1088/1748-0221/20/06/C06077](https://doi.org/10.1088/1748-0221/20/06/C06077). The paper describes the Gen2 GPIO interface, external-trigger timestamping with an internal TDC, and injection of external trigger events into the common pixel data stream. A searchable copy is also available as result [1](https://www.researchgate.net/publication/393115372_Katherine_Generation_2_advanced_readout_system_for_Timepix3_detectors). **[E]**
2. **TrackLab.** M. Farkaš et al., “Track Lab: extensible data acquisition software for fast pixel detectors, online analysis and automation,” arXiv:2310.08974. The paper documents TrackLab control of Katherine readouts and configuration of GPIO pin functions: [3](https://arxiv.org/html/2310.08974v2). **[E]**
3. **Timepix3 ToA/FToA/ToT.** J. B. et al., “PymePix: A python library for SPIDR readout of Timepix3,” arXiv:1905.07999. It describes 40 MHz/25 ns ToA, 640 MHz/1.5625 ns FToA, ToT, timestamp extension, and trigger association: [1](https://arxiv.org/html/1905.07999) and [2](https://arxiv.org/pdf/1905.07999). This is a SPIDR reference; SPIDR-specific export fields must not be attributed to Katherine unless verified. **[E]**
4. **Timepix3 ASIC.** Poikela et al., “Timepix3: a 65K channel hybrid pixel readout chip with simultaneous ToA/ToT and integrated TDC,” *JINST* 9 (2014) C05013: [publication link](https://iopscience.iop.org/article/10.1088/1748-0221/9/05/C05013). **[E]**
5. **Timepix3 data sheet.** AdvaPIX TPX3 datasheet with ToA/FToA/ToT conventions: [PDF](https://advacam.com/content/uploads/2023/10/APXT3M-Xxx201030-AdvaPIX-TPX3-Datasheet-2023-10-03.pdf). **[E]**
6. **External synchronization and offset correction.** Burian et al., “Enhanced Readout System for Timepix3-Based Detectors in Large-Scale Scientific Facilities,” *Sensors* 25 (2025) 1860: [PMC11946098](https://pmc.ncbi.nlm.nih.gov/articles/PMC11946098/). It is a related system, not evidence for the exact BL4S wiring; it is useful for the general practice of measuring cable/PLL/feedback delays and applying offline offsets. **[E]**
7. **Independent detector timestamp alignment.** ESS timing/alignment reference: [timestamping paper](https://inspirehep.net/files/78d297b837202f0b9254919a86bf36ac). **[E]**
8. **External Timepix3 synchronization.** Timepix3 synchronization to an external facility trigger: [published reference](https://iopscience.iop.org/article/10.1088/1361-6455/ac6b6b). **[E]**

The external references explain instrument capabilities and general timing practice. The logbook, diagrams, notebook/configuration statements, ROOT output, and TrackLab files remain the authority for this experiment’s actual wiring, clock choice, edge selection, and branch semantics.

---

# 16. Scaler snapshot/capture semantics — important unresolved timing question

## Direct answer

The supplied ROOT output does **not** establish whether `Scaler0_ch15`, or the other scaler channels, is:

1. latched in hardware on an accepted CORBO trigger and then read out later; or
2. read from a continuously running/live counter during the event-readout process; or
3. sampled by some intermediate event-builder/firmware operation at a fixed point after the trigger.

Therefore the following details are currently **[U] unresolved**:

- whether the scaler values are captured on CORBO or another trigger;
- whether the capture is on the leading or falling edge;
- whether the capture is before or after BUSY changes state;
- whether all 16 scaler channels are latched simultaneously;
- whether the values in one ROOT entry are hardware-simultaneous or only stored together after sequential VME reads.

## What is actually known

The ROOT tree contains `Scaler0_ch0` through `Scaler0_ch15` as scalar unsigned-integer branches, and every ROOT entry contains one value for each branch. **[R]** This proves that the event builder stored one scaler value per channel alongside the event record. It does **not** prove when the hardware sampled the counters.

`Scaler0_ch15` behaves like a continuously running 1 MHz counter, because its cumulative value grows throughout the run and reaches approximately 810 million counts. **[R][N]** A free-running counter can still have a hardware-latched snapshot: the counter continues counting, while a separate latch register freezes its value at the trigger edge. The words “free-running counter” and “latched snapshot” are therefore not opposites.

The fact that `Scaler0_ch12` ends at 91,274, matching the number of ROOT entries, supports the interpretation that channel 12 counts accepted CORBO events. **[L][R][I]** It does not prove that channel 15 was latched by the same CORBO edge.

The diagram shows the CORBO and scaler signal roles, but it does not show the scaler module’s capture command, latch timing, edge polarity, or readout protocol. **[L][U]** The analysis scripts use the scaler values but contain no firmware-level evidence about the capture mechanism. **[N][U]**

## Why the distinction matters

If scalers are latched on CORBO, then for event `i`:

```text
Scaler0_ch15[i] ≈ the 1 MHz count at the selected CORBO capture edge
```

The value is a coarse event timestamp, with 1 microsecond granularity plus a fixed phase/offset.

If scalers are read live during event readout, then:

```text
Scaler0_ch15[i] ≈ the counter value when the scaler register was read
```

The value contains an additional delay that can depend on:

- trigger logic delay;
- BUSY assertion;
- TDC/QDC conversion;
- event size;
- VME bus ordering;
- readout load;
- firmware/event-builder scheduling.

If the 16 channels are read sequentially from live counters, the values in one ROOT entry may not be simultaneous. The later-read channels would contain slightly later counts, although the difference may be small compared with the 1 microsecond clock period.

## Most likely architecture, but not yet a fact

A common DAQ architecture is:

```text
free-running counters
        |
        | accepted trigger edge
        v
hardware latch captures all counters
        |
        v
VME/event builder reads the frozen latch values
        |
        v
ROOT entry stores all scaler values
```

This architecture would make all scaler channels simultaneous at the hardware capture instant while allowing them to be read out later. It is a plausible engineering design, but it must not be presented as the actual BL4S implementation until the scaler-module documentation, firmware, or a timing test confirms it. **[I][U]**

## Which edge would capture a latched snapshot?

The current evidence does not identify the capture edge.

Possible candidates include:

- the leading edge of CORBO;
- the falling edge of CORBO;
- the EVTTRG edge before BUSY veto;
- an internal event-accept pulse generated after the CORBO logic;
- a VME/event-builder sampling command.

The TrackLab files establish that code 4 is the current Timepix CORBO leading-edge stream and code 1 is the falling-edge stream. **[M]** They do not prove which of those edges, if either, captures the VME scaler block.

A fixed approximately 120 ns difference between a Timepix leading-edge timestamp and a TDAQ scaler-derived time could be caused by:

- the scaler being latched on the falling edge;
- a fixed trigger/cable/module path delay;
- the scaler being sampled after the leading edge;
- a combination of these.

Therefore an offset alone cannot identify the capture edge unless the trigger path and TDC reference are independently known.

## Are all scaler channels captured simultaneously?

The current ROOT file proves only that all scaler values are stored in the same `RAWdata` event record. **[R]** It does not prove simultaneous hardware capture.

To claim simultaneous capture, one of the following is needed:

1. scaler-module documentation stating that all channels are latched together;
2. firmware/source code showing a common latch command;
3. a calibration test feeding known simultaneous or deliberately delayed pulses into multiple scaler channels;
4. an event-by-event relationship to a TDC/reference edge that is independent of VME readout order.

## Recommended tests

### Test 1: identify the hardware

Find the exact scaler module model, firmware version, and configuration. Obtain the manual or source documentation for:

- latch-on-trigger behavior;
- trigger input used for latching;
- leading/falling edge selection;
- whether scaler inputs are gated or free-running;
- whether the module has a common snapshot register;
- VME readout order and latency.

### Test 2: correlate channel 15 with an independent trigger edge

If the ROOT file contains a TDC channel for CORBO or a documented trigger edge, calculate:

```text
Delta_i = Scaler0_ch15[i] / 1e6 - t_CORBO_TDC[i]
```

Check whether `Delta_i` is:

- constant and independent of event size/rate;
- shifted by approximately 120 ns when comparing leading versus falling edges;
- correlated with event-building/readout load.

A stable offset supports a trigger-latched or fixed-delay interpretation, but does not alone prove the latch circuit.

### Test 3: vary event size and readout load

Compare scaler timing against a reference for:

- ordinary events;
- events with different TDC multiplicities;
- events with different QDC occupancy;
- low-rate and high-rate periods;
- different run lengths.

If the scaler-to-trigger residual changes with readout load, live readout or event-builder sampling is possible. If it remains fixed, hardware latch or a fixed sampling point is more likely.

### Test 4: simultaneous channel test

Feed a known pulser or split reference pulse into several scaler inputs. If the scaler channels are latched simultaneously, the derived count transitions should correspond to the same reference pulse. If the channels are read live and sequentially, controlled rate/phase tests may reveal ordering differences.

### Test 5: inspect the complete ROOT event values

With the binary ROOT file, inspect:

```text
Scaler0_ch10
Scaler0_ch11
Scaler0_ch12
Scaler0_ch15
```

for every entry, not only the first and last entries. Verify:

- monotonicity;
- increments of channel 12;
- repeated scaler values;
- differences between adjacent entries;
- whether channel 15 changes in a way consistent with one common event timestamp.

This still cannot prove latch timing by itself, but it can reveal inconsistencies or readout-order effects.

## Correct wording for the current analysis

Until the hardware capture semantics are documented, use:

> `Scaler0_ch15` is a cumulative 1 MHz counter whose value is stored in each `RAWdata` event. It provides a coarse event-time coordinate. The supplied files do not establish whether the stored value is a hardware-latched snapshot at the CORBO edge or a live counter read during event readout; the capture edge and cross-channel simultaneity remain to be verified from scaler-module documentation or a dedicated timing test.

Do **not** write:

> `Scaler0_ch15` is definitely latched on the leading edge of CORBO.

That statement is not proven by the current ROOT text output.
