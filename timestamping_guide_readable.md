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
