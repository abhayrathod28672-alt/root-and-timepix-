
----
---
title: Logbook BL4S 2026, August Part I
tags: BL4S, Logbook, 2026, August Part I
---

# Logbook BL4S 2026, August Part I

:::warning
### Run Planning 

#### Calibration runs of the calorimeters
-1 GeV, -2 GeV, -3 GeV, Trigger S0&S1
:::danger
this is is not complete, and can be wrong! we love your enthusiasm but please don't make edits on the logbook without supervision of your SS.
- [x] CAL0; 1786782465 , 1786787514 , 1786788903
- [x] CAL1;  1786800039, 1786799056, 1786798201 
- [x] CAL2;  1786781408, 1786780617, 1786779710
- [x] CAL4; 1786657998, 1786662364, 1786660965
- [x] CAL5;  1786794828, 1786796090,  1786797061
- [x] CAL7; 1786836376 , 1786837396, 1786838309
- [x] CAL8;  1786714515, 1786713224, 1786711761 
- [x] CAL9;  1786741940, 1786739830, 1786726168
- [x] CAL10; 1786793439, 1786791937, 1786790499
- [x] CAL11; 1786747305, 1786746501, 1786745756  
- [x] CAL12; 1786801341, 1786802590 , 1786803907
- [x] CAL13; 1786743090, 1786744038, 1786744833
- [x] CAL14; 1786748346, 1786750147, 1786750887
- [x] CAL17: 1786807867,  1786806354,1786805198 
- [x] CAL18; 1786864539, 1786840283,1786839384 
- [x] CAL19; 1786723178, 1786724681, 1786725412
:::
#### Pedestal runs of the calorimeters
Fake signal as trigger
:::info
cal0 should be taken as ch16, not as ch0.
- [x] HV ON, Trigger BUSY & AH1&AV1, Fake signal on DWC1 : 1786828994
- [x] HV OFF, Trigger BUSY & AH1&AV1, Fake signal on DWC1 : 1786829188
:::
#### Calibration of the clustering algorithm 
Trigger S0&S1&FS0&FS1
For central two calorimeters, move the DESY table 1 2 3 4 5 cm at 1 2 3 GeVs and observe the clustering code. 
- [x] CAL4
- [ ] CAL18

#### Physics Runs
- [ ] Trigger S0&S1&FS0&FS1. At 1.5, 2.0, 2.5, 3 GeV, with graphite of 1 and 3 cm thickness we should get data with lead glass calorimeters at 50 cm TBC for other energies than the 3 GeV.


:::
:::success
Experimental Layout

Distances are to be measured
![](https://codimd.web.cern.ch/uploads/upload_26b445b590f0d213c6ddbcdc19742d37.png)
:::
:::success
VME Scheme


![](https://codimd.web.cern.ch/uploads/upload_6c374d2cdd03f41068d9520370be95a8.png)

:::

:::success
NIM Scheme

![](https://codimd.web.cern.ch/uploads/upload_111f7819522b3584bcf3918b1e791eae.png)
:::

### CAL CONFIGURATIONS:
-------------------------------------------------
:::success
CAL10 |  CAL5  |   CAL1  |  CAL12
-----------------------------------
CAL17  | CAL4  |  CAL18 |  CAL7
---------------------------------
CAL0   | CAL2  | CAL14  | CAL11
---------------------------------
CAL8  |  CAL19 |CAL9   | CAL13
------------------------------
:::
### DESY Positioning For Calibration Measurements:

- CAL 4: H:31.472   V: -3.696
    - CAL 17: H: 21.699 V: -3.696
    - CAL 18: H: 41.754 V: -3.384
    - CAL 7: H: 51.774 V: -3.439
    - CAL 12: H: 52.219 V: -13.080
    - CAL 1: H: 42.114 V: -12.986
    - CAL 5: H: 31.854 V: -12.986
    - CAL 10: H: 21.688 V: -13.168
    - CAL 0: H: 21.059 V: 6.423
    - CAL 2: H: 31.196 V: 6.335
    - CAL 14: H: 41.417 V: 6.395
    - CAL 11: H: 51.396 V: 6.274
    - CAL 13 H: 51.396 V: 15.766
    - CAL 9: H: 41.542 V: 15.943
    - CAL 19: H: 31.509 V: 15.943
    - CAL 8: H: 21.094 V: 16.233
    
-------------------------------------
### Run Draft
- Run **<run number>** : **<beam momentum> GeV beam, collimators at <setting>, <YES/NO TARGET>, <purpose>**

    - beamfile: **<000>**
    - beam momentum: **<+3/-3/+5>** GeV
    - Trigger Condition: **<S0S1 / S0S1FS0FS1 / other>**
    - Event rate from CESAR: approx **<value>** events/spill
    - Trigger rate from TDAQ: approx **<value>** events/spill
    - XCET44: pressure **<value>** bar, events **<value>**, gas **CO2**
    - XCET48: pressure **<value>** bar, events **<value>**, gas **CO2**
    - Run started: **<time>, <day>**
    - Run finished: **<time>,<day>**
    - Number of events: ****
    - Target position: **<position / ->**
    - Target material thickness: **<C, W, Fe / 30 mm>**
    - DESY Table position: **
    - **Observation**:
    

## 24.08.2026

:::danger
    
This run is quite short in terhms of total numbre of events, after we have started to the run we went inside to make some changings for MMs.    
    
- Run **1787523716** : **4 GeV beam** 
    - beamfile: **<019>**
    - beam momentum: **+4** GeV
    - Trigger Condition: **S0S1FS0FS1**
    - Event rate from CESAR: approx **150899** events/spill
    - Trigger rate from TDAQ: approx **1.4k** events/spill
    - XCET44: pressure **7.998** bar, events **107130**, gas **CO2**
    - XCET48: pressure **1.103** bar, events **3092**, gas **CO2**
    - Run started: **24-Aug-2026 00:21:56**
    - Run finished: **24-Aug-2026 00:38**
    - Number of events: **20k?**
    - Target position: **49 cm from the yellow**
    - Target material thickness: **3 cm C**
    - DESY Table position: *H: 35.165, V:1.278 ###center of the calorimeters.*
    - **Observation**:things look ok, only maybe some particles are hitting with 4 GeV indeed. 
    
::::
   
:::info
Again 3 cm Graphite but more dataa
::: 
     

     
- Run **1787526649** : **4 GeV beam** 
    - beamfile: **<019>**
    - beam momentum: **+4** GeV
    - Trigger Condition: **S0S1FS0FS1**
    - Event rate from CESAR: approx **150899** events/spill
    - Trigger rate from TDAQ: approx **1.4k** events/spill
    - XCET44: pressure **7.998** bar, events **107130**, gas **CO2**
    - XCET48: pressure **1.103** bar, events **3092**, gas **CO2**
    - Run started: **24-Aug-2026 01:10:49**
    - Run finished: ** 24-Aug-2026 02:24:08**
    - Number of events: **444741**
    - Target position: **49 cm from the yellow**
    - Target material thickness: **3 cm C**
    - DESY Table position: *H: 35.165, V:1.278 ###center of the calorimeters.*
    - **Observation**:things look ok, only maybe some particles are hitting with 4 GeV indeed.  

    
:::info
We are switcginf 3 cm Aluminium 
:::  
 
    
 - Run **1787532112** : **4 GeV beam** 
    - beamfile: **<019>**
    - beam momentum: **+4** GeV
    - Trigger Condition: **S0S1FS0FS1**
    - Event rate from CESAR: approx **150899** events/spill
    - Trigger rate from TDAQ: approx **1.4k** events/spill
    - XCET44: pressure **7.998** bar, events **107130**, gas **CO2**
    - XCET48: pressure **1.103** bar, events **3092**, gas **CO2**
    - Run started: **24-Aug-2026 02:41:52 **
    - Run finished: ** 24-Aug-2026 03:51:09 **
    - Number of events: **459871**
    - Target position: **49 cm from the yellow**
    - Target material thickness: **3 cm alu**
    - DESY Table position: *H: 35.165, V:1.278 ###center of the calorimeters.*
    - **Observation**:things look ok, only maybe some particles are hitting with 4 GeV indeed.  

:::info
background run at 4 GeV
:::  
 
- Run **1787536596** : **4 GeV beam, background run** 
    - beamfile: **<019>**
    - beam momentum: **+4** GeV
    - Trigger Condition: **S0S1FS0FS1**
    - Event rate from CESAR: approx **150899** events/spill
    - Trigger rate from TDAQ: approx **1.4k** events/spill
    - XCET44: pressure **7.998** bar, events **107130**, gas **CO2**
    - XCET48: pressure **1.103** bar, events **3092**, gas **CO2**
    - Run started: **24-Aug-2026 03:56:36 **
    - Run finished: ** 24-Aug-2026 04:10:10 **
    - Number of events: **91274**
    - Target position: **49 cm from the yellow**
    - Target material thickness: **no target**
    - DESY Table position: *H: 35.165, V:1.278 ###center of the calorimeters.*
    - **Observation**:bkg run, we hope timepix matches. 
:::info
we will now switch to the 3 cm tungsten target.  
:::

 - Run **1787538016** : **4 GeV beam, physics run 3 cm tungsten** 
    - beamfile: **<019>**
    - beam momentum: **+4** GeV
    - Trigger Condition: **S0S1FS0FS1**
    - Event rate from CESAR: approx **150899** events/spill
    - Trigger rate from TDAQ: approx **1.4k** events/spill
    - XCET44: pressure **7.998** bar, events **107130**, gas **CO2**
    - XCET48: pressure **1.103** bar, events **3092**, gas **CO2**
    - Run started: **24-Aug-2026 04:20:16**
    - Run finished: ** 24-Aug-2026 05:04:47**
    - Number of events: **300768**
    - Target position: **49 cm from the yellow**
    - Target material thickness: **3 cm W**
    - DESY Table position: *H: 35.165, V:1.278 ###center of the calorimeters.*
    - **Observation**:phys run, 3 cm tungsten

:::info
we've now switched to 1.2 cm of copper.  
:::
    
 - Run **1787541067** : **4 GeV beam, physics run 1.2 cm Cu** 
    - beamfile: **<019>**
    - beam momentum: **+4** GeV
    - Trigger Condition: **S0S1FS0FS1**
    - Event rate from CESAR: approx **150899** events/spill
    - Trigger rate from TDAQ: approx **1.4k** events/spill
    - XCET44: pressure **7.998** bar, events **107130**, gas **CO2**
    - XCET48: pressure **1.103** bar, events **3092**, gas **CO2**
    - Run started: **24-Aug-2026 05:11:07**
    - Run finished: **24-Aug-2026 05:56:13**
    - Number of events: **300463**
    - Target position: **49 cm from the yellow**
    - Target material thickness: **1.2 cm Cu**
    - DESY Table position: *H: 35.165, V:1.278 ###center of the calorimeters.*
    - **Observation**:phys run, 1.2 cm Cu.
    
:::info
 this should be the final run of the 4 GeV beam, we also have the bkg run. the remaining runs are 3 GeV bkg (increase the XCET48 to 2 bar), 3 GeV 5 cm graphite, 4 GeV 4 cm Alu, (increase the XCET48 to 4 bar and XCET44 to 8-9 bar.) 1.8 GeV bkg run. We also actually need a run that measures the cherenkovs at the same pressure. I believe we cannot do this one.
:::
    
    
  - Run **1787544111** : **3 GeV beam,background run no target, ** 
    - beamfile: **<008>**
    - beam momentum: **+3** GeV
    - Trigger Condition: **S0S1FS0FS1**
    - Event rate from CESAR: approx **112391** events/spill
    - Trigger rate from TDAQ: approx **1.4k** events/spill
    - XCET44: pressure **7.998** bar, events **82539**, gas **CO2**
    - XCET48: pressure **1.991** bar, events **6086**, gas **CO2**
    - Run started: **24-Aug-2026 06:01:51**
    - Run finished: **24-Aug-2026 06:21:58**
    - Number of events: **77534**
    - Target position: **49 cm from the yellow**
    - Target material thickness: **BACKGROUND RUN FOR 3 GeV**
    - DESY Table position: *H: 35.165, V:1.278 ###center of the calorimeters.*
    - **Observation**: aLL OKAY
   
    
:::info
We are  switcing to 3 GeV runs to complete data set   4 cm ALU 
:::    
    
   - Run **1787545748** : **3 GeV beam, 4m alu run, ** 
    - beamfile: **<008>**
    - beam momentum: **+3** GeV
    - Trigger Condition: **S0S1FS0FS1**
    - Event rate from CESAR: approx **117706** events/spill
    - Trigger rate from TDAQ: approx **1.4k** events/spill
    - XCET44: pressure **7.998** bar, events **84932**, gas **CO2**
    - XCET48: pressure **1.991** bar, events **6416**, gas **CO2**
    - Run started: **24-Aug-2026 07:20:55**
    - Run finished: ** *24-Aug-2026 *
    - Number of events: ****
    - Target position: **49 cm from the yellow**
    - Target material thickness: **4 CM GRAPHITE**
    - DESY Table position: *H: 35.165, V:1.278 ###center of the calorimeters.*
    - **Observation**: aLL OKAY 
    
    
    
        
   - Run **1787545748** : **3 GeV beam, 4Cm GRAPHITE, ** 
    - beamfile: **<008>**
    - beam momentum: **+3** GeV
    - Trigger Condition: **S0S1FS0FS1**
    - Event rate from CESAR: approx **112391** events/spill
    - Trigger rate from TDAQ: approx **1.4k** events/spill
    - XCET44: pressure **7.998** bar, events **82539**, gas **CO2**
    - XCET48: pressure **1.991** bar, events **6086**, gas **CO2**
    - Run started: **24-Aug-2026 06:29:08**
    - Run finished: ** *24-Aug-2026 08:12:00*
    - Number of events: **117800**
    - Target position: **49 cm from the yellow**
    - Target material thickness: **4 CM ALU**
    - DESY Table position: *H: 35.165, V:1.278 ###center of the calorimeters.*
    - **Observation**: aLL OKAY 
    

1787552171 1.8 gEv BKG RUN WITH THE COLLIMATORS AT +- 50, AND CHERENKOVS AT 9 AND 4 BAR. 
    24-Aug-2026 08:16:11
    24-Aug-2026 09:35:04 23645
:::success  
END OF TESTBEAMMM
:::
## 23.08.2026    
:::info
after fondue, we have finished the calibration runs. 
:::
- Run **1787444130** : **1.8 GeV beam,  collimator XCHV011 used to be at -8 but we have it at 50.036 and XCHV012 USED TO BE AT -8 BUT WE HAVE IT AT 50.052, XCHV014 USED TO BE AT -8 BUT IS AT 50.017,XCHV015 used to be at -8 but is at 50.084, XCHV027 used to be at -20 but is at 49.987  , 1cm Graphite/c target, purpose: PHYSICS RUNS**

    - beamfile: **018**
    - beam momentum: **1.8** GeV
    - Trigger Condition: **S0S1FS0FS1**
    - Event rate from CESAR: approx **19180** events/spill
    - Trigger rate from TDAQ: approx **150** events/spill
    - XCET44: pressure **7.991** bar, events **13347**, gas **CO2**
    - XCET48: pressure **3.991** bar, events **1704**, gas **CO2**
    - Run started: ****
    - Run finished: ****
    - Number of events: ****
    - Target position: **40 cm from ecal**
    - Target material thickness: **Graphite 1cm**
    - DESY Table position: H: 35.170 V:1.276**
    - **Observation**: it is just so so so so so low.
    
- Run **1787473551** : **1.8 GeV beam,  collimator XCHV011 used to be at -8 but we have it at 50.036 and XCHV012 USED TO BE AT -8 BUT WE HAVE IT AT 50.052, XCHV014 USED TO BE AT -8 BUT IS AT 50.017,XCHV015 used to be at -50.263 but is at 50.084, XCHV027 used to be at -20 but is at 49.987  , 1cm Al target, purpose: PHYSICS RUNS**

    - beamfile: **018**
    - beam momentum: **1.8** GeV
    - Trigger Condition: **S0S1FS0FS1**
    - Event rate from CESAR: approx **18385** events/spill
    - Trigger rate from TDAQ: approx **160** events/spill
    - XCET44: pressure **7.991** bar, events **12788**, gas **CO2**
    - XCET48: pressure **3.991** bar, events **1626**, gas **CO2**
    - Run started: **23-Aug-2026 10:25:51**
    - Run finished: **13:32:15**
    - Number of events: **71808**
    - Target position: **40 cm from ecal**
    - Target material thickness: **Aluminium 1cm**
    - DESY Table position: H: 35.170 V:1.276**
    - **Observation**: we don't know, everything is working. Asta needs a bit of time with the beam, we turned on the smol cute run again, the beamfile is 1787484825 ,start time : 23-Aug-2026 13:33:45, stop time: 23-Aug-2026 13:54:17 and event count: 3649.
    
    
Now we want to do the 4 GeV runs, for this, for the alignment, we will go to the center of cal14, we will also lower the cherenkovs.


The changes that we made till now :D
    


| From                    | To             | New Length | Previous len |
| ----------------------- | -------------- | ---------- | ------------ |
| Below fan (left BP)     | Cal 19         | 47.3       | 47.1         |
| Top of fan              | Cal 02         | 47.1       | 46.7         |
| BP right top of the box | Cal 07         | 46.3       | 46.1         |
| Katheriene box DS       | Cal 11         | 40.1       | 39.9         |
| Top of time pix         | Cal 14         | 49.3       | 49.3         |
| Target                  | Cal 02         | 50.1       | 49.9         |
| Timepix DS              | Yellow slab DS | 63.32      | 63.15        |
        

Now what we did inside :D
    We aligned the center of the timepix to good precision (maybe :D ) and then we started the run but forgot to align the FS but as a good experimentalist (yup) we did completed that too :D and then we started our run :D
    

  - Run **1787489827** : **4 GeV beam,  2 cm W target , purpose:PHYSICS RUNS** 
    - beamfile: **<019>**
    - beam momentum: **+4** GeV
    - Trigger Condition: **S0S1FS0FS1**
    - Event rate from CESAR: approx **66564** events/spill
    - Trigger rate from TDAQ: approx **1k** events/spill
    - XCET44: pressure **7.998** bar, events **46584**, gas **CO2**
    - XCET48: pressure **1.103** bar, events **1204**, gas **CO2**
    - Run started: **23-Aug-2026 14:57:07**
    - Run finished: **23-Aug-2026 16:25:15**
    - Number of events: **221352**
    - Target position: **49 cm from the yellow**
    - Target material thickness: **2 cm W**
    - DESY Table position: *H: 35.165, V:1.278 ###center of the calorimeters.*
    - **Observation**:we stopped at 200k. 
    
    
:::info
We changed the target to 2.42 cm of copper in the beam area 
:::
- Run **1787495722** : **4 GeV beam,  2.2 cm copper target , purpose:PHYSICS RUNS** 
    - beamfile: **<019>**
    - beam momentum: **+4** GeV
    - Trigger Condition: **S0S1FS0FS1**
    - Event rate from CESAR: approx **66564** events/spill
    - Trigger rate from TDAQ: approx **1k** events/spill
    - XCET44: pressure **7.998** bar, events **46584**, gas **CO2**
    - XCET48: pressure **1.103** bar, events **1204**, gas **CO2**
    - Run started: **23-Aug-2026 16:35:22**
    - Run finished: **23-Aug-2026 17:59:30**
    - Number of events: **216422**
    - Target position: **49 cm from the yellow**
    - Target material thickness: **2.4 cm Cu**
    - DESY Table position: *H: 35.165, V:1.278 ###center of the calorimeters.*
    - **Observation**:we stopped at 216k.     
:::info
we've changed the target to 1 cm of alu, which should help both teams we hope, for the team attopion since the stats are a bit more important we will wait a bit lon on this one. 
:::
    
- Run **1787502393** : **4 GeV beam,  1 cm aluminium target , purpose:PHYSICS RUNS we've hopened the collimators for more particles,  collimator numbers are 11 12 14 15, and they were at +-20, now they are at +-40.** 
    - beamfile: **<019>**
    - beam momentum: **+4** GeV
    - Trigger Condition: **S0S1FS0FS1**
    - Event rate from CESAR: approx **150899** events/spill
    - Trigger rate from TDAQ: approx **1.4k** events/spill
    - XCET44: pressure **7.998** bar, events **107130**, gas **CO2**
    - XCET48: pressure **1.103** bar, events **3092**, gas **CO2**
    - Run started: **23-Aug-2026 18:26:33**
    - Run finished: **23-Aug-2026 20:45:04**
    - Number of events: **502489**
    - Target position: **49 cm from the yellow**
    - Target material thickness: **1 cm Al**
    - DESY Table position: *H: 35.165, V:1.278 ###center of the calorimeters.*
    - **Observation**:things look ok, only maybe some particles are hitting with 4 GeV indeed.
    
:::info
we will switch to 1 cm graphite.
:::
    
- Run **1787514996** : **4 GeV beam** 
    - beamfile: **<019>**
    - beam momentum: **+4** GeV
    - Trigger Condition: **S0S1FS0FS1**
    - Event rate from CESAR: approx **150899** events/spill
    - Trigger rate from TDAQ: approx **1.4k** events/spill
    - XCET44: pressure **7.998** bar, events **107130**, gas **CO2**
    - XCET48: pressure **1.103** bar, events **3092**, gas **CO2**
    - Run started: **23-Aug-2026 21:56:36**
    - Run finished: **24-Aug-2026 00:13:45**
    - Number of events: **500218**
    - Target position: **49 cm from the yellow**
    - Target material thickness: **1 cm C**
    - DESY Table position: *H: 35.165, V:1.278 ###center of the calorimeters.*
    - **Observation**:things look ok, only maybe some particles are hitting with 4 GeV indeed.   
    
:::info
We will switch to 3 cm Graphite target @4 GeV
:::
  
    
## 2026.08.22 
    
  - Run **1787368460** : **3 GeV beam,  1.2 cm Cu target , purpose:PHYSICS RUNS**
    - beamfile: **<008>**
    - beam momentum: **+3** GeV
    - Trigger Condition: **S0S1FS0FS1**
    
    - XCET44: pressure **2.0** bar, events **5110**, gas **CO2**
    - XCET48: pressure **4.0** bar, events **88488**, gas **CO2**
    - Run started: **22-Aug-2026 05:14:20**
    - Run finished: **22-Aug-2026 10:10:18**
    - Number of events: **610399**
    - Target position: **45cm from the bosch profiles**
    - Target material thickness: **1.2 cm Copper**
    - DESY Table position: *H: 35.167, V:1.278 ###center of the calorimeters.*
    - **Observation**:We stoped and restarted the run. We had no beam so we checked the HVs, but there wasn't an issue with them. Later we took the beam stoper off, which fixed the beam. Timepix didn't record till around 10:00:00.
    
:::info
When we came to the control center the Timepix wasn't working. There was a communication issue. After fixing the computer, we reseted the Timepix by unpluging it and counting to 10. After pluging it back we checked the PC again, but the issue wasn't fixed. So we closed the firewall which fixed the issue.
:::
    
:::info
Close the firewall after restarting the PC for Timepix to work.    
:::    

  - Run **1787387158** : **3 GeV beam,  1.2 cm Cu target , purpose:PHYSICS RUNS**
    - beamfile: **<008>**
    - beam momentum: **+3** GeV
    - Trigger Condition: **S0S1FS0FS1**
    
    - XCET44: pressure **2.0** bar, events **4981**, gas **CO2**
    - XCET48: pressure **4.0** bar, events **91412**, gas **CO2**
    - Run started: **22-Aug-2026 10:25:58**
    - Run finished: **22-Aug-2026 10:56:11**
    - Number of events: **61340**
    - Target position: **45cm from the bosch profiles**
    - Target material thickness: **1.2 cm Copper**
    - DESY Table position: *H: 35.167, V:1.278 ###center of the calorimeters.*

:::info
Changed the target from 1.2 cm Copper to 2.4 cm Copper. We wanted 3 cms, but we didn't have enough Copper targets to do so.
:::

  - Run **1787390563** : **3 GeV beam,  2.4 cm Cu target , purpose:PHYSICS RUNS**
    - beamfile: **<008>**
    - beam momentum: **+3** GeV
    - Trigger Condition: **S0S1FS0FS1**
    
    - XCET44: pressure **2.0** bar, events **5110**, gas **CO2**
    - XCET48: pressure **4.0** bar, events **92486**, gas **CO2**
    - Run started: **22-Aug-2026 11:22:43**
    - Run finished: **22-Aug-2026 14:22:12**
    - Number of events: **402046**
    - Target position: **45cm from the bosch profiles**
    - Target material thickness: **2.4 cm Copper**
    - DESY Table position: *H: 35.167, V:1.278 ###center of the calorimeters.*
    
    observation: looks okay!Due to QDC change calorimeters must be realigned and re-calibrated
    
    
**REALIGNMENT AND RE-CALIBRATION OF THE CALORIMETERS**
DESY TABLE MOVEMENTS/LOCATIONS:
    
    CAL 18
- Horizontal = 41.405
- Vertical = -3.650
    
    
    CAL 7
- Horizontal = 51.384
- Vertical = -3.705
    
    CAL 4
- Horizontal = 29.195
- Vertical = -3.617
    
    CAL 17
- Horizontal = 19.074
- Vertical = -3.437
    

    We have the center locations of CAL 18, 7, 4, 17. Batteries in laser needs to be replaced. So we will get the centers of the other calorimeters later. We will proceed with caliberation runs for the 4 calorimeters now. We have decided to re-do the caliberation for all the ECals but only for 1 energy, 2GeV 
    
    
    - Run **1787407961** : **2 GeV electron beam,  no target , purpose:Calibration Run for CAL 17**
    - beamfile: **<001>**
    - beam momentum: **2** GeV
    - Trigger Condition: **S0S1**
    
    - XCET44: pressure **2.0** bar, events **5575**, gas **CO2**
    - XCET48: pressure **4.0** bar, events **5751**, gas **CO2**
    - Run started: **22-Aug-2026 16:12:41**
    - Run finished: **22-Aug-2026 16:18:48**
    - Number of events: **22034**
    - DESY Table position: *H: 19.074, V:-3.437 ###center of the calorimeter 17.*
    
    observation: It was centered at 2200, and it made us scared if it hits to the maximum value at 3 GeV. that's why we will tke 3 spill run with 3 gev beamfile.
    

        - Run **1787408396** : **3 GeV electron beam,  no target , purpose:Calibration Run for CAL 17**
    - beamfile: **<002>**
    - beam momentum: **3** GeV
    - Trigger Condition: **S0S1**
    
    - XCET44: pressure **2.0** bar, events **6107**, gas **CO2**
    - XCET48: pressure **4.0** bar, events **6445**, gas **CO2**
    - Run started: **22-Aug-2026 16:19:56**
    - Run finished: **22-Aug-2026 16:21:38**
    - Number of events: **7051**
    - DESY Table position: *H: 19.074, V:-3.437 ###center of the calorimeter 17.*
    observation: It looked okay, not going beyond 4000. 
    
    
Continuing with the caliberation runs.
    
    
        - Run **1787408731** : **2 GeV electron beam,  no target , purpose:Calibration Run for CAL 4**
    - beamfile: **<001>**
    - beam momentum: **2** GeV
    - Trigger Condition: **S0S1**
    
    - XCET44: pressure **2.0** bar, events **5345**, gas **CO2**
    - XCET48: pressure **4.0** bar, events **5388**, gas **CO2**
    - Run started: **22-Aug-2026 16:25:31**
    - Run finished: **22-Aug-2026 16:31:30**
    - Number of events: **20372**
    - DESY Table position: *H: 29.196, V:-3.616 ###center of the calorimeter 4.*
    observation: It looked okay, centered around 2100.
    
    
     - Run **1787409242** : **2 GeV electron beam,  no target , purpose:Calibration Run for CAL 7**
    - beamfile: **<001>**
    - beam momentum: **2** GeV
    - Trigger Condition: **S0S1**
    
    - XCET44: pressure **2.0** bar, events **5345**, gas **CO2**
    - XCET48: pressure **4.0** bar, events **5388**, gas **CO2**
    - Run started: **22-Aug-2026 16:34:02**
    - Run finished: **22-Aug-2026 16:40:29**
    - Number of events: **21964**
    - DESY Table position: *H: 51.386, V:-3.704 ###center of the calorimeter 7.*
    observation: Looked okay centered around 2000.
    
    
    - Run **1787409712** : **2 GeV electron beam,  no target , purpose:Calibration Run for CAL 18**
    - beamfile: **<001>**
    - beam momentum: **2** GeV
    - Trigger Condition: **S0S1**
    
    - XCET44: pressure **2.0** bar, events **5345**, gas **CO2**
    - XCET48: pressure **4.0** bar, events **5388**, gas **CO2**
    - Run started: **22-Aug-2026 16:41:52**
    - Run finished: **22-Aug-2026 16:47:33**
    - Number of events: **20382**
    - DESY Table position: *H: 41.404, V:-3.652 ###center of the calorimeter 18.*
    
    - Observation: cal14 is centered at 1800. 
    
    Going in for getting the centers of the other calorimeters.

CAL 14
- Horizontal = 41.394
- Vertical = 6.108
    
CAL 11
- Horizontal = 50.994
- Vertical = 6.108
    
CAL 2
- Horizontal = 29.071
- Vertical = 6.102

CAL 0
- Horizontal =19.050
- Vertical = 6.189

CAL 8
- Horizontal =19.218
- Vertical =16.065
    
CAL 19
- Horizontal = 29.326
- Vertical = 16.036

CAL 9
- Horizontal =41.407
- Vertical = 15.991

CAL 13
- Horizontal =51.343
- Vertical = 15.833

CAL 12
- Horizontal = 52.037
- Vertical = -13.346
    
CAL 1
- Horizontal =42.162
- Vertical = -13.261
    
CAL 5
- Horizontal =29.727
- Vertical = -13.126

CAL 10
- Horizontal = 19.601
- Vertical = -13.057
    
we will continue will cal10. 
     
    - Run **1787414494** : **2 GeV electron beam,  no target , purpose:Calibration Run for CAL 10**
    - beamfile: **<001>**
    - beam momentum: **2** GeV
    - Trigger Condition: **S0S1**
    
    - XCET44: pressure **2.0** bar, events **5345**, gas **CO2**
    - XCET48: pressure **4.0** bar, events **5388**, gas **CO2**
    - Run started: **22-Aug-2026 18:01:34**
    - Run finished: **22-Aug-2026 18:08:34**
    - Number of events: **25352**
    - DESY Table position: *H: 19.601, V:-13.057 ###center of the calorimeter 10.*
    - Observation: cal10 is centered at 1700. 

    - Run **1787414978** : **2 GeV electron beam,  no target , purpose:Calibration Run for CAL 5**
    - beamfile: **<001>**
    - beam momentum: **2** GeV
    - Trigger Condition: **S0S1**
    
    - XCET44: pressure **2.0** bar, events **5345**, gas **CO2**
    - XCET48: pressure **4.0** bar, events **5388**, gas **CO2**
    - Run started: **22-Aug-2026 18:09:38**
    - Run finished: **22-Aug-2026 18:12**
    - Number of events: **x**
    - DESY Table position: *H: 28.726, V:-13.122 ###center of the calorimeter 5.*
    - Observation: cal5 is centered at 2100. 

    - Run **1787415228** : **2 GeV electron beam,  no target , purpose:Calibration Run for CAL 5**
    - beamfile: **<001>**
    - beam momentum: **2** GeV
    - Trigger Condition: **S0S1**
    
    - XCET44: pressure **2.0** bar, events **5345**, gas **CO2**
    - XCET48: pressure **4.0** bar, events **5388**, gas **CO2**
    - Run started: **22-Aug-2026  18:13:48**
    - Run finished: **22-Aug-2026 18:19:18**
    - Number of events: **20211**
    - DESY Table position: *H: 29.730, V:-13.122 ###center of the calorimeter 5.*
    - Observation: cal5 is centered at 2100. 

    - Run **1787415623** : **2 GeV electron beam,  no target , purpose:Calibration Run for CAL 1**
    - beamfile: **<001>**
    - beam momentum: **2** GeV
    - Trigger Condition: **S0S1**
    
    - XCET44: pressure **2.0** bar, events **5345**, gas **CO2**
    - XCET48: pressure **4.0** bar, events **5388**, gas **CO2**
    - Run started: **22-Aug-2026  18:20:23**
    - Run finished: **22-Aug-2026 18:26:19**
    - Number of events: **22000**
    - DESY Table position: *H: 42.163, V:-13.257 ###center of the calorimeter 1.*
    - Observation: cal1 is centered at 1600. 
    
    - Run **1787416044** : **2 GeV electron beam,  no target , purpose:Calibration Run for CAL 12**
    - beamfile: **<001>**
    - beam momentum: **2** GeV
    - Trigger Condition: **S0S1**
    
    - XCET44: pressure **2.0** bar, events **5345**, gas **CO2**
    - XCET48: pressure **4.0** bar, events **5388**, gas **CO2**
    - Run started: **22-Aug-2026  18:27:24**
    - Run finished: **22-Aug-2026 18:33:32**
    - Number of events: **x**
    - DESY Table position: *H: 52.036, V:-13.346 ###center of the calorimeter 12.*
    - Observation: cal12 is centered at 1200. 
    
    - Run **1787416522** : **2 GeV electron beam,  no target , purpose:Calibration Run for CAL 13**
    - beamfile: **<001>**
    - beam momentum: **2** GeV
    - Trigger Condition: **S0S1**
    
    - XCET44: pressure **2.0** bar, events **5345**, gas **CO2**
    - XCET48: pressure **4.0** bar, events **5388**, gas **CO2**
    - Run started: **22-Aug-2026   18:35:22**
    - Run finished: **22-Aug-2026  18:40:43**
    - Number of events: **20209**
    - DESY Table position: *H: 51.348, V:15.831 ###center of the calorimeter 13.*
    - Observation: cal13 is centered at 1700. 
:::info
    we will leave with graphite 5 cm at 3 gev pos hadron beam. 
change of plans, 5 cm graphite doesn't fit in between timepix 
:::
- Run **1787417290** : **3 GeV pos hadron beam,  1 cm alu target , purpose:missing half of the 1 cm alu with timepix**
    - beamfile: **<008>**
    - beam momentum: **3** GeV
    - Trigger Condition: **S0S1FS0FS1**
    
    - XCET44: pressure **2.0** bar, events **x**, gas **CO2**
    - XCET48: pressure **4.0** bar, events **x**, gas **CO2**
    - Run started: **22-Aug-2026   18:48:10**
    - Run finished: **22-Aug-2026  22:10:18**
    - Number of events: **500k**
    - DESY Table position: *H: 35.164, V:1.278 ###center of the calorimeters.*
    - Observation: no no tworking cal or not working timepix.  
:::info
we will continue with the calib runs.
:::
    
- Run **1787430082** : **2 GeV electron beam,  no target , purpose:Calibration Run for CAL 9**
    - beamfile: **<001>**
    - beam momentum: **2** GeV
    - Trigger Condition: **S0S1**
    - Trigger Rate TDAQ: **1700**
    - Trigger Rate CESAR: **5171**
    - XCET44: pressure **2.0** bar, events **5018**, gas **CO2**
    - XCET48: pressure **4.0** bar, events **5036**, gas **CO2**
    - Run started: **22-Aug-2026   22:21:22**
    - Run finished: **22-Aug-2026  22:27:44**
    - Number of events: **20209**
    - DESY Table position: *H: 41.410, V:15.995 ###center of the calorimeter 9.*
    - Observation: cal9 is centered at 2400. it is too much, we might take super short run with the 3 GeV. 
    
- Run **1787430653** : **3 GeV electron beam,  no target , purpose:Calibration Run for CAL 9**
    - beamfile: **<002>**
    - beam momentum: **3** GeV
    - Trigger Condition: **S0S1**
    - Trigger Rate TDAQ: **1700**
    - Trigger Rate CESAR: **5837**
    - XCET44: pressure **2.0** bar, events **5521**, gas **CO2**
    - XCET48: pressure **4.0** bar, events **5797**, gas **CO2**
    - Run started: **22-Aug-2026   22:30:53**
    - Run finished: **22-Aug-2026  22:36:24*
    - Number of events: **20229**
    - DESY Table position: *H: 41.410, V:15.995 ###center of the calorimeter 9.*
    - Observation: cal9 is centered at 3500 count. it is at the limit. 

- Run **1787431119** : **2 GeV electron beam,  no target , purpose:Calibration Run for CAL 19**
    - beamfile: **<001>**
    - beam momentum: **2** GeV
    - Trigger Condition: **S0S1**
    - Trigger Rate TDAQ: **1700**
    - Trigger Rate CESAR: **5236**
    - XCET44: pressure **2.0** bar, events **5095**, gas **CO2**
    - XCET48: pressure **4.0** bar, events **5120**, gas **CO2**
    - Run started: **22-Aug-2026   22:38:39**
    - Run finished: **22-Aug-2026  22:44:35**
    - Number of events: **21415**
    - DESY Table position: *H: 29.327, V:16.035 ###center of the calorimeter 19.*
    - Observation: cal19 is centered at 1200 ADC count, mais not much to do, HV is at 1474V. 


- Run **1787431583** : **2 GeV electron beam,  no target , purpose:Calibration Run for CAL 8**
    - beamfile: **<001>**
    - beam momentum: **2** GeV
    - Trigger Condition: **S0S1**
    - Trigger Rate TDAQ: **1700**
    - Trigger Rate CESAR: **5236**
    - XCET44: pressure **2.0** bar, events **5095**, gas **CO2**
    - XCET48: pressure **4.0** bar, events **5120**, gas **CO2**
    - Run started: **22-Aug-2026   22:46:23**
    - Run finished: **22-Aug-2026   22:52:20**
    - Number of events: **21278**
    - DESY Table position: *H: 19.214, V:16.068 ###center of the calorimeter 8.*
    - Observation: cal8 is centered at 2200 QDC count.
    
- Run **1787432044** : **2 GeV electron beam,  no target , purpose:Calibration Run for CAL 0**
    - beamfile: **<001>**
    - beam momentum: **2** GeV
    - Trigger Condition: **S0S1**
    - Trigger Rate TDAQ: **1700**
    - Trigger Rate CESAR: **5236**
    - XCET44: pressure **2.0** bar, events **5095**, gas **CO2**
    - XCET48: pressure **4.0** bar, events **5120**, gas **CO2**
    - Run started: **22-Aug-2026   22:54:04**
    - Run finished: **22-Aug-2026  22:59:57**
    - Number of events: **21178**
    - DESY Table position: *H:19.050, V:6.187 ###center of the calorimeter 0.*
    - Observation: cal0 is centered at 1900 QDC count.

- Run **1787432452** : **2 GeV electron beam,  no target , purpose:Calibration Run for CAL 2**
    - beamfile: **<001>**
    - beam momentum: **2** GeV
    - Trigger Condition: **S0S1**
    - Trigger Rate TDAQ: **1700**
    - Trigger Rate CESAR: **5236**
    - XCET44: pressure **2.0** bar, events **5095**, gas **CO2**
    - XCET48: pressure **4.0** bar, events **5120**, gas **CO2**
    - Run started: **22-Aug-2026  23:00:52**
    - Run finished: **22-Aug-2026   23:07:08**
    - Number of events: **21186**
    - DESY Table position: *H:29.070, V:6.101 ###center of the calorimeter 2.*
    - Observation: cal2 is centered at 2200 QDC count.

    
- Run **1787432906** : **2 GeV electron beam,  no target , purpose:Calibration Run for CAL 11**
    - beamfile: **<001>**
    - beam momentum: **2** GeV
    - Trigger Condition: **S0S1**
    - Trigger Rate TDAQ: **1700**
    - Trigger Rate CESAR: **5236**
    - XCET44: pressure **2.0** bar, events **5095**, gas **CO2**
    - XCET48: pressure **4.0** bar, events **5120**, gas **CO2**
    - Run started: **22-Aug-2026  23:08:26**
    - Run finished: **22-Aug-2026  23:14:24**
    - Number of events: **21225**
    - DESY Table position: *H:50.990, V:6.108 ###center of the calorimeter 11.*
    - Observation: cal11 is centered at 1800 QDC count.

- Run **1787433329** : **2 GeV electron beam,  no target , purpose:Calibration Run for CAL 14**
    - beamfile: **<001>**
    - beam momentum: **2** GeV
    - Trigger Condition: **S0S1**
    - Trigger Rate TDAQ: **1700**
    - Trigger Rate CESAR: **5236**
    - XCET44: pressure **2.0** bar, events **5095**, gas **CO2**
    - XCET48: pressure **4.0** bar, events **5120**, gas **CO2**
    - Run started: **22-Aug-2026  23:15:29**
    - Run finished: **22-Aug-2026  23:21:55**
    - Number of events: **x**
    - DESY Table position: *H:41.398, V:6.108 ###center of the calorimeter 14.*
    - Observation: cal14 is centered at 2200 QDC count.


- Run **1787433886** : **3 GeV electron beam,  no target , purpose:Calibration Run for CAL 14**
    - beamfile: **<002>**
    - beam momentum: **3** GeV
    - Trigger Condition: **S0S1**
    - Trigger Rate TDAQ: **120**
    - Trigger Rate CESAR: **5236**
    - XCET44: pressure **2.0** bar, events **5095**, gas **CO2**
    - XCET48: pressure **4.0** bar, events **5120**, gas **CO2**
    - Run started: **22-Aug-2026 23:24:46**
    - Run finished: **22-Aug-2026  23:2**
    - Number of events: **52k**
    - DESY Table position: *H:41.398, V:6.108 ###center of the calorimeter 14.*
    - Observation: cal14 is centered at 3200 QDC count.
 
## 2026.08.21

:::info
we've arrived to the control room at 9:32. Calorimeters look fine (SHOCKING) but TimePix stopped at 344 reps,we have restarted again. We stopped the beam at 9:59, because of the social media team. 
:::
:::info
 data recording is finished, however we have noticed that timepix is misaligned. Laser cross was still visible on TimePix chip but the vertical line was in a bit left side I did not think to take the picture :(( 

I believe while we are trying to take out the QDC we have moved the timepix :( so this run is also rubbish then... we will realign it again.
:::
    
:::info
We have made the alignment, ready for background run. Here is the distances after our alignment. 
:::    
    
    
    

| from     | to      | distance (cm) |
| -------- | ------- | ------------- |
| left BP  | CAL8    | 46.7          |
| right BP | CAL9    | 46.7          |
| left BP  | CAL10   | 44            |
| right BP | CAL1    | 44.7          |
| right BP | CAL 18` | 45.2          |
| left BP  | BoDESY  | 41.7          |
| right BP | BoDESY  | 41.5          | 

    
 - Run **1787269191** : **3 GeV beam, collimators at beam_ref, 1cm graphite , purpose: get data**
    - beamfile: **<008>**
    - beam momentum: **+3** GeV
    - Trigger Condition: **S0S1FS0FS1**
    
    - XCET44: pressure **2.0** bar,gas **CO2**
    - XCET48: pressure **4.0** bar,gas **CO2**
    - Run started: **01:39:51, 21-Aug-2026**
    - Run finished: **11:17:2829,21-Aug-2026**
    - Number of events: **2010193**
    - Target position: **45cm from the bosch profiles**
    - Target material thickness: **<C, / 10 mm>**
    - DESY Table position: *H: 35.167, V:1.278 ###center of the calorimeters.*
    - **Observation**: graphite 1 cm data. when we arrived in the morning the calorimeters looked fine, but after we made an entrance ch6 cal8 looked a bit with overflow. 
    
:::info
we will take another background run. cal8 ch6 looks bad.
:::

      
 - Run **1787306041** : **3 GeV beam, collimators at beam_ref, no target , purpose: get background**
    - beamfile: **<008>**
    - beam momentum: **+3** GeV
    - Trigger Condition: **S0S1FS0FS1**
    
    - XCET44: pressure **2.0** bar,gas **CO2**
    - XCET48: pressure **4.0** bar,gas **CO2**
    - Run started: **11:56:00, 21-Aug-2026**
    - Run finished: **12:24,21-Aug-2026**
    - Number of events: **~30k**
    - Target position: **45cm from the bosch profiles**
    - Target material thickness: **no**
    - DESY Table position: *H: 35.167, V:1.278 ###center of the calorimeters.*
    - **Observation**: CAL8, channel 6 behaves wiggly woogly wuby.
    
:::info
Markus has changed V792 at 12:25 with a new one, the serial number of current QDC V792 is: 97 (0x00000061). And now we will get a new short background run     
::: 
    
    
  - Run **1787310616** : **3 GeV beam, collimators at beam_ref, no target , purpose: get background with new QDC board**
    - beamfile: **<008>**
    - beam momentum: **+3** GeV
    - Trigger Condition: **S0S1FS0FS1**
    
    - XCET44: pressure **2.0** bar,gas **CO2**
    - XCET48: pressure **4.0** bar,gas **CO2**
    - Run started: **13:10:00, 21-Aug-2026**
    - Run finished: **14:07:35, 21-Aug-2026**
    - Number of events: **106424**
    - Target position: **45cm from the bosch profiles**
    - Target material thickness: **no**
    - DESY Table position: *H: 35.167, V:1.278 ###center of the calorimeters.*
    - **Observation**:looks okay for now. TimePix is also taking the data.
    
:::info
TIME TO ADD TARGEEET--> 3.054 cm Aluminium @3GeV
:::
   
![](https://codimd.web.cern.ch/uploads/upload_21b60cc80d529664251f1f6362184eaa.png)

  -------------------  
    ![](https://codimd.web.cern.ch/uploads/upload_7316badfcf093cce667ba3b3d23eb545.png)

    -------------------
    
![](https://codimd.web.cern.ch/uploads/upload_464f7c3eb9129e4757813d54ba360cec.jpeg)
    
    
    
  - Run **1787316998** : **3 GeV beam, collimators at beam_ref, Alu target , purpose:PHYSICS RUNS**
    - beamfile: **<008>**
    - beam momentum: **+3** GeV
    - Trigger Condition: **S0S1FS0FS1**
    
    - XCET44: pressure **2.0** bar,gas **CO2**
    - XCET48: pressure **4.0** bar,gas **CO2**
    - Run started: **14:56:38, 21-Aug-2026**
    - Run finished: **17:00:25, 21-Aug-2026**
    - Number of events: **231602**
    - Target position: **45cm from the bosch profiles**
    - Target material thickness: **3 cm Aluminium**
    - DESY Table position: *H: 35.167, V:1.278 ###center of the calorimeters.*
    - **Observation**:
    at 15:55 we have noticed the TimePix was not working, now we will have started again and it is working again. 
    
:::warning
Because of the DG visit we stoped the beam at 16:00. Ignore any data after that time. (People might have changed the aligment)
:::
    
:::info
We checked the alignments. Everything looks good.
:::
    
  - Run **1787325562** : **3 GeV beam, 3 cm Alu target , purpose:PHYSICS RUNS**
    - beamfile: **<008>**
    - beam momentum: **+3** GeV
    - Trigger Condition: **S0S1FS0FS1**
    
    - XCET44: pressure **2.0** bar, events **5110**, gas **CO2**
    - XCET48: pressure **4.0** bar, events **88488**, gas **CO2**
    - Run started: **17:19:22, 21-Aug-2026**
    - Run finished: **22:15:20, 21-Aug-2026**
    - Number of events: **1014948**
    - Target position: **45cm from the bosch profiles**
    - Target material thickness: **3 cm Aluminium**
    - DESY Table position: *H: 35.167, V:1.278 ###center of the calorimeters.*
    - **Observation**:All looks FINE!


:::info
we've decided to get the data for the pedastal, this is with the beam on, HV OFF. Run number is 1787345503. Pedastal run start time  21-Aug-2026 22:51:43, run stop time: 21-Aug-2026 23:08:55, event size:53236. 
:::
    
- Run **1787346586** : **3 GeV beam,  1 cm Alu target , purpose:PHYSICS RUNS**
    - beamfile: **<008>**
    - beam momentum: **+3** GeV
    - Trigger Condition: **S0S1FS0FS1**
    
    - XCET44: pressure **2.0** bar, events **5110**, gas **CO2**
    - XCET48: pressure **4.0** bar, events **88488**, gas **CO2**
    - Run started: **21-Aug-2026 23:09:46**
    - Run finished: **04:52:59, 22-Aug-2026**
    - Number of events: **1079724**
    - Target position: **45cm from the bosch profiles**
    - Target material thickness: **1 cm Aluminium**
    - DESY Table position: *H: 35.167, V:1.278 ###center of the calorimeters.*
    - **Observation**: All looks okay. TimePix seems stopped at  02:55.
    
    
 :::info
 We are switching to copper target!
 :::   
    


    
:::danger
Now time is : 18:00, so until Monday 08:00 we have 62 beam hours left. Let's think that we could not use 5 hours of this beamtime because of various reasons, we might have 58 hours. To collect 1m event we need to wait for 5,5 hours. We can have 10-11 long run before end of testbeam.
    
### The RUNs COMPLETED

| AttoPion | PionIST   | Column 3 |
| -------- | --------- | -------- |
| 1 cm Alu | 1 cm Alu  | Text     |
| 3 cm Alu | 3 cm  Alu |          |
|          |           |          |

    
    

### TO RUN's:

| For AttoPion | For PionIST | Energy (GeV) |
| ------------ | ----------- | ------------ |
| 3 cm Alu     |             | 3            |
| 1 cm Alu     |             | 3            |
| ---          | 3 cm Cu     | 3            |
|              | 1 cm Cu     | 3            |
| 1 cm W       |             | 1.5          |
| 3 cm W       |             | 1.5          |
|              | 3 cm W      | 5            |
|              | 1-2 cm C    | 5            |
|              |             |              |

    
:::    
    
    
## 2026.08.20
    
    
:::danger
We are still trying to find out the source of our  problem with QDC channels/calorimeters.
    
    Problematic channels from last night run:CHANNEL 01, CHANNEL 09, CHANNEL 13, CHANNEL 14, CHANNEL16. So we have switched 01-->16 
:::    
    
    
   - Run **1787243607** : **3 GeV beam, collimators at beam_ref, 1cm graphite , purpose: TEST QDC Channel**
    - beamfile: **<008>**
    - beam momentum: **+3** GeV
    - Trigger Condition: **S0S1FS0FS1**
    - Event rate from CESAR: approx **120421** events/spill
    - Trigger rate from TDAQ: approx **1400** events/spill
    - XCET44: pressure **2.007** bar, events **5824**, gas **CO2**
    - XCET48: pressure **3.993** bar, events **85826**, gas **CO2**
    - Run started: **18:33, 20-Aug-2026**
    - Run finished: **23:09,20-Aug-2026**
    - Number of events: **884719**
    - Target position: **45cm from the bosch profiles**
    - Target material thickness: **<C, / 10 mm>**
    - DESY Table position: *H: 35.167, V:1.278 ###center of the calorimeters.*
    - **Observation**: channel 1  was sus it was showing woogly boogly graph 
    :(
    

![](https://codimd.web.cern.ch/uploads/upload_8b439be407db932d10c8c03448a91e68.png)


- Run **1787261776** : **3 GeV beam, collimators at beam_ref, 1cm graphite , purpose: we unpluged the cable of ch1 to understand the reason for the sus graph **
    - beamfile: **<008>**
    - beam momentum: **+3** GeV
    - Trigger Condition: **S0S1FS0FS1**
    
    - XCET44: pressure **2.007** bar, gas **CO2**
    - XCET48: pressure **3.993** bar, gas **CO2**
    - Run started: **23:36, 20-Aug-2026**
    - Run finished: **23:57,20-Aug-2026**
    - Number of events: **89929**
    - Target position: **45cm from the bosch profiles**
    - Target material thickness: **<C, / 10 mm>**
    - DESY Table position: *H: 35.167, V:1.278 ###center of the calorimeters.*
    - **Observation**: we ran this to find out what was the reason for the sus and unusual graph 

:::info
 this was a run to understand the problem of the Sus QDC graph we pluged out the ch1 cable and ran the beam again 
:::
    
(add graph)
   
 - Run **1787264255** : **3 GeV beam, collimators at beam_ref, 1cm graphite , purpose: TEST QDC Channel again**
    - beamfile: **<008>**
    - beam momentum: **+3** GeV
    - Trigger Condition: **S0S1FS0FS1**
    
    - XCET44: pressure **2.0** bar,gas **CO2**
    - XCET48: pressure **4.0** bar,gas **CO2**
    - Run started: **00:17, 21-Aug-2026**
    - Run finished: **00:29,21-Aug-2026**
    - Number of events: **47991**
    - Target position: **45cm from the bosch profiles**
    - Target material thickness: **<C, / 10 mm>**
    - DESY Table position: *H: 35.167, V:1.278 ###center of the calorimeters.*
    - **Observation**: re-run to know the reason for the sus graph 
    
    
    
## 2026.08.19   
    

   - Run **1787088655** :  **3 GeV beam, TARGET: 1 cm of Tungsten!
 - beamfile: **<008>**
    - beam momentum: **<+3>** GeV
    - Trigger Condition: **S0S1FS0FS1**
    - Event rate from CESAR: approx **106972** vents/spill
    - Trigger rate from TDAQ: approx **<1200>** events/spill
- XCET44: pressure **4.001** bar, events **78639**, gas **CO2**
    - XCET48: pressure **2.002** bar, events **5600**, gas **CO2**
    - Run started: **18-Aug-2026 23:30:55**
    - Run finished: **19-Aug-2026 10:08:28**
    - Number of events: **1482805**
    - DESY Table position: ** H: 35.167, V:1.278 ###center of the calorimeters.
    - **Observation**: TimePix is recorded for 600 minutes, 10 hours, so it doesn't cover the entire run because we thought we would arrive earlier :D 

:::info 
CAL12 needs to be calibrated! (because we have change the qdc channel of it to qdc ch17.)
:::

    



    

- Run **1787131925** : **3 GeV beam, collimators at beam_ref, TARGET; YES, <GOAL: To investigate low Z material - Graphite(3cm) with TimePix.**
 - beamfile: **<008>**
    - beam momentum: **<+3>** GeV
    - Trigger Condition: **S0S1FS0FS1**
    - Event rate from CESAR: approx **107897** vents/spill
    - Trigger rate from TDAQ: approx **<1200>** events/spill
- XCET44: pressure **4.001** bar, events **78658**, gas **CO2**
    - XCET48: pressure **2.002** bar, events **5658**, gas **CO2**
    - Run started: **18-Aug-2026 11:32**
    - Run finished: ** 18-Aug-2026 14:00:45**
    - Number of events: **480878**
 
    - DESY Table position: ** H: 35.167, V:1.278 ###center of the calorimeters.
    - CAL Gap Distance: ~3 cm
    - **Observation**: over here we are having problem with RCDApp! We've decided to stop the run and restart the system to see if they will disappear. TimePix is continuing to have the data, it has GPI01 and GPIO2 connected, GPIO1 is connected to EVTTRG 
    
    
- Run **1787143237** : **3 GeV beam, collimators at beam_ref, TARGET; YES, <GOAL: To investigate low Z material - Graphite(3cm) with TimePix.**
 - beamfile: **<008>**
    - beam momentum: **<+3>** GeV
    - Trigger Condition: **S0S1FS0FS1**
    - Event rate from CESAR: approx **107897** vents/spill
    - Trigger rate from TDAQ: approx **<1200>** events/spill
- XCET44: pressure **4.001** bar, events **78658**, gas **CO2**
    - XCET48: pressure **2.002** bar, events **5658**, gas **CO2**
    - Run started: **19-Aug-2026 14:40:37**
    - Run finished: ** 19-Aug-2026 21:16:04**
    - Number of events: **1334353**
 
    - DESY Table position: ** H: 35.167, V:1.278 ###center of the calorimeters.
    - CAL Gap Distance: ~3 cm
    - **Observation**: everything seems to be working out great (knock on wood) The TimePix data that covers this information is 757 to 1152.  We will put tungsten at 3 cm just to see that probably we cannot build the pi0s :/. 
    
- Run **1787168532** : **3 GeV beam, collimators at beam_ref, TARGET; YES, <GOAL: To investigate low Z material - tungsten(3cm) with TimePix.**
 - beamfile: **<008>**
    - beam momentum: **<+3>** GeV
    - Trigger Condition: **S0S1FS0FS1**
    - Event rate from CESAR: approx **107897** vents/spill
    - Trigger rate from TDAQ: approx **<1200>** events/spill
- XCET44: pressure **4.001** bar, events **78658**, gas **CO2**
    - XCET48: pressure **2.002** bar, events **5658**, gas **CO2**
    - Run started: **19-Aug-2026 21:42**
    - Run finished: ** 19-Aug-2026 22:38**
    - Number of events: **210780**
 
    - DESY Table position: ** H: 35.167, V:1.278 ###center of the calorimeters.
    - CAL Gap Distance: ~3 cm
    - **Observation**: everything looks okay! the TimePix data that covers this data is from 1174 to 1219. It is shorter than the data. The Timepix monitor become so busy after the 3 cm tungsten.

:::info
we will goo see theee moooon
:::
    
  
:::info
we saw it, it was so beautifullll    
:::
  
- Run **1787172822** : **3 GeV beam, collimators at beam_ref, TARGET; YES, <GOAL: To investigate low Z material - GRaphite(1cm) with TimePix.**
 - beamfile: **<008>**
    - beam momentum: **<+3>** GeV
    - Trigger Condition: **S0S1FS0FS1**
    - Event rate from CESAR: approx **107897** vents/spill
    - Trigger rate from TDAQ: approx **<1200>** events/spill
- XCET44: pressure **4.001** bar, events **78658**, gas **CO2**
    - XCET48: pressure **2.002** bar, events **5658**, gas **CO2**
    - Run started: **19-Aug-2026 22:53:42  **
    - Run finished: ** 20-Aug-2026  09:55:54  **
    - Number of events: ** 09:55:54**
 
    - DESY Table position: ** H: 35.167, V:1.278 ###center of the calorimeters.
    - CAL Gap Distance: ~3 cm
    - **Observation**: The TimePix data that covers this run starts with the 1220. Unfortunately it  seems TimePix stopped recording separate txt files 1313 at  00:34. But that files seems huge, we are not sure if it is corrupted or not. Also bad news on the calorimeters. 
![](https://codimd.web.cern.ch/uploads/upload_0e2552db5546ad99d69d4b30b51b5eac.png)

ch1 and ch16 is definitely problematic. Interesting part is that it is the same calorimeter, even at the new channel. We've went to talk to mustafa, he has suggested it looks like a memory issue, he asked if we reset in between. We will share the code with him, and we've got new qdc to test. Sad! We'll copy this event to next day too. 
    
    
:::info
we are aiming to start a long run with 1 cm C and go home to sleeeep
:::
    
## 2026.08.18
    
-->Continuation from last night:
    
:::success
 - We have corrected alignment of FS0, FS1 and center of CALs and their distance between each other. In previous positioning of CALs, laser were passing through the CAL14 and CAL18 but not the center of the gap. So, we have changed the CAL positions and then DESY table position as well.
 - We have marked positions of FS PMT base on the bosch profiles.
 - We have marked the wall vertically and wrote BL4S 2026.
:::    
    
![](https://codimd.web.cern.ch/uploads/upload_f6cdd55ee7a7d7e758635c7e7dfcfda4.jpeg)
   ---------------------------------- 
![](https://codimd.web.cern.ch/uploads/upload_46fa6bfffeaaeb1faee6db8c54561601.jpeg)
    
    
:::info    
- We have placed the TimePix in front of the beam and got 3 spills. There is no event on TimePix, so we will try again tomorrow. We (Aniket, Abhay, Berare and Seyma) are so tired to debug this thing now and also not 100% sure if the Katherine box and TimePix radiation hard or not. Needs to be check with TimePix people.
:::    
    
 ![](https://codimd.web.cern.ch/uploads/upload_c2aa09f9720391937122c3a332b60fac.jpeg)
   
    
:::info
We have placed to 3 cm C target and we have ~3 cm gap between CALs.    
:::    
   - Run **1787004129** : **3 GeV beam, collimators at beam_ref, TARGET; YES, <GOAL: 3 cm C target with ~2.8 - 3 cm gap between CALs.**
 - beamfile: **<008>**
    - beam momentum: **<+3>** GeV
    - Trigger Condition: **S0S1FS0FS1**
    - Event rate from CESAR: approx **107907** vents/spill
    - Trigger rate from TDAQ: approx **<1200>** events/spill
- XCET44: pressure **3.994** bar, events **79054**, gas **CO2**
    - XCET48: pressure **1.999** bar, events **5822**, gas **CO2**
    - Run started: **00:02, 18.08.2026**
    - Run finished: **10:02, 18.08.2026**
    - Number of events: **1539159**
    - Target position: **44 & 45 cm bosh profile**
    - Target material thickness: **C / 30 mm**
    - DESY Table position: ** H: 35.167, V:1.278 ###center of the calorimeters.
    - CAL Gap Distance: 3 cm
    - **Observation**:

    
:::info
We removed the target to measure the background.
:::
- Run **1787045879** : **3 GeV beam, collimators at beam_ref, TARGET; NO, <GOAL: BACKGROUND RUN - NO TARGET, No TimePix**
 - beamfile: **<008>**
    - beam momentum: **<+3>** GeV
    - Trigger Condition: **S0S1FS0FS1**
    - Event rate from CESAR: approx **102651** vents/spill
    - Trigger rate from TDAQ: approx **<1200>** events/spill
- XCET44: pressure **3.994** bar, events **74531**, gas **CO2**
    - XCET48: pressure **1.999** bar, events **5149**, gas **CO2**
    - Run started: **11:37, 18.08.2026**
    - Run finished: **11:57,18.08.2026**
    - Number of events: **50507**
 
    - DESY Table position: ** H: 35.167, V:1.278 ###center of the calorimeters.
    - CAL Gap Distance: 3 cm
    - **Observation**:LOOKS NORMAL. CAL2 AND CAL12 HAS HIGHER BACKGROUND ~4K COUNTS, AS EXPECTED. 

- Run **1787049075** : **3 GeV beam, collimators at beam_ref, TARGET; YES, <GOAL: To investigate higher Z material - Tungsten(2cm) **
 - beamfile: **<008>**
    - beam momentum: **<+3>** GeV
    - Trigger Condition: **S0S1FS0FS1**
    - Event rate from CESAR: approx **108025** vents/spill
    - Trigger rate from TDAQ: approx **<1200>** events/spill
- XCET44: pressure **3.994** bar, events **78279**, gas **CO2**
    - XCET48: pressure **1.999** bar, events **5471**, gas **CO2**
    - Run started: **12:31, 18.08.2026**
    - Run finished: **13:47,18.08.2026 **
    - Number of events: **274068**
 
    - DESY Table position: ** H: 35.167, V:1.278 ###center of the calorimeters.
    - CAL Gap Distance: 3 cm
    - **Observation**:stopped the run because CH10 QDC graph is suspicious
:::info
It is doing the same behavour as seen earlier in the QDC log graph 
:::
:::info
We changed the channel 10 for calorimeter 12 to channel 16 and it seems to work.
:::
    
| From           | To              | Distance |
| -------------- | --------------- | -------- |
| Bottom of CAL9 | Bottom of CAL19 | 21.3 mm  |
| Top of CAL9    | Top of CAL19    | 22.0 mm  |
| CAL2           | CAL14           | 23.5 mm  |
| CAL4           | CAL18           | 24.4 mm  |
| CAL5           | CAL1            | 24.9 mm  |
| Top of CAL5    | Top of CAL1     | 25.8 mm  |
------------------------------------------------------------------------    
- Run **1787058277** : **3 GeV beam, collimators at beam_ref, TARGET; YES, <GOAL: To investigate higher Z material - Tungsten(2cm) **
 - beamfile: **<008>**
    - beam momentum: **<+3>** GeV
    - Trigger Condition: **S0S1FS0FS1**
    - Event rate from CESAR: approx **106972** vents/spill
    - Trigger rate from TDAQ: approx **<1200>** events/spill
- XCET44: pressure **4.001** bar, events **77952**, gas **CO2**
    - XCET48: pressure **2.002** bar, events **5600**, gas **CO2**
    - Run started: **18-Aug-2026 15:04:37**
    - Run finished: **15:04:37 20:50**
    - Number of events: **744709**
 
    - DESY Table position: ** H: 35.167, V:1.278 ###center of the calorimeters.
    - CAL Gap Distance: 3 cm
    - **Observation**: no not working cal. 

:::info 
we have decided to take the target off and record a data in TDAQ and TimePix with the repeater method. We decided for 15 minutes of data taking, we will first start the TimePix and then TDAQ, and then we will give it to our poor students to correlate, good luck. first spill without tdaq. and we will also get the second SMA to BNC our goal is to also timestsamp the EVTTRG not just the CORBO we hope it will be helpful with the timeline analysis. Later update, we couldn't find SMA. 
:::


- Run **1787081424** : **3 GeV beam, collimators at beam_ref, TARGET; NO, <GOAL: to get background run with also TimePix to see if we can correlate the and to see how does the 3 GeV pos hadron beam looks with the TimePix.**
 - beamfile: **<008>**
    - beam momentum: **<+3>** GeV
    - Trigger Condition: **S0S1FS0FS1**
    - Event rate from CESAR: approx **106972** vents/spill
    - Trigger rate from TDAQ: approx **<1200>** events/spill
- XCET44: pressure **4.001** bar, events **78639**, gas **CO2**
    - XCET48: pressure **2.002** bar, events **5600**, gas **CO2**
    - Run started: **18-Aug-2026 21:30:24**
    - Run finished: **18-Aug-2026 21:53:30**
    - Number of events: **69157**
 
    - DESY Table position: ** H: 35.167, V:1.278 ###center of the calorimeters.
    - CAL Gap Distance: 3 cm
    - **Observation**: no not working cal. 
    - **TimePix** from measurement_9 file to measurement_23 file there it belongs to this data without any target and with 3 GeV pos hadron beam. Total timestamps on the TimePix is 40095, less than the TDAQ of course, because TimePix was set to record for 15 minutes. **Important note** over here we only had GPIO2, and it was recording the CORBO on the falling edge.

:::info
we are trying to move the TimePix close to the target as much as possible. And we would like to start 1 cm tungsten target, however we are a bit scared in terms of temperature of the TimePix, it can be monitored on the TrackLab but we don't know if it has protection system. That is why we are also looking for some fan in the lab, hope to find out some solution.
:::

:::info
we've findout a 12V fan, it looks good enough for leaving over night now.
:::

    
    
 


## 2026.08.17    
 Continuation from last night:
    

   - Run **1786914869** : **3 GeV beam, collimators at beam_ref, TARGET; YES, <GOAL: repeating run from June BUT with 3 cm target**
 - beamfile: **<008>**
    - beam momentum: **<+3>** GeV
    - Trigger Condition: **S0S1FS0FS1**
    - Event rate from CESAR: approx **111035** vents/spill
    - Trigger rate from TDAQ: approx **<1200>** events/spill
- XCET44: pressure **3.994** bar, events **78639**, gas **CO2**
    - XCET48: pressure **1.999** bar, events **5887**, gas **CO2**
    - Run started: **23:14:29, 16.08.2026**
    - Run finished: **10:07:39,17.08.2026 **
    - Number of events: **2011309**
    - Target position: **50 cm**
    - Target material thickness: **C / 30 mm**
    - DESY Table position: ** H: 36.151, V:1.180 ###center of the calorimeters.
    - **Observation**: During this long run, Channel10, CAL12, created same weird shape like before with CAL8, CAL0 and CAL1. We will do the calibration for the cal12 again at a lower voltage, this was too high we think.
    
    We are taking the measurement
    
    

| From      | To        | Distance |
| --------- | --------- | -------- |
| DWC0 DS   | DWC1 US   | 98.2 cm  |
| DWC1 US   | FS0 US    | 217.9 cm |
| FS0 US    | FS1 US    | 3.24 cm  |
| FS0 US    | FS0 DS    | 0.7 cm   |
| FS1 US    | FS1 DS    | 0.6 cm   |
| FS1 US    | Target US | 7.67 cm  |
| Target US | Target DS | 3 cm     |
| Target DS | CAL2 US   | 46.3 cm  | 


:::info
Changed the DESY tables position to (52.218, -13.079), and removed the target. Changed the beam to an electron beam. Changed the HV of Cal12 to 1500V and 445uA.
:::
    
    - Run **1786960293** : **-3 GeV electron beam, collimators at beam_ref, TARGET; NO, <GOAL: Repeating our calibiration runs for Cal12**
 - beamfile: **<002>**
    - beam momentum: **<-3>** GeV
    - Trigger Condition: **S0S1**
    - Event rate from CESAR: approx **5221** vents/spill
    - Trigger rate from TDAQ: approx **1600** events/spill
    - XCET44: pressure **3.994** bar, events **5214**, gas **CO2**
    - XCET48: pressure **1.999** bar, events **4987**, gas **CO2**
    - Run started: **17.08.2026, 11:51:33**
    - Run finished: **17.08.2026, 12:06:20**
    - Number of events: **47k**
    - DESY Table position: ** H: 52.218, V:-13.079
   
     - Run **1786961253** : **-2 GeV electron beam, collimators at beam_ref, TARGET; NO, <GOAL: Repeating our calibiration runs for Cal12**
 - beamfile: **<001>**
    - beam momentum: **<-2>** GeV
    - Trigger Condition: **S0S1**
    - Event rate from CESAR: approx **** vents/spill
    - Trigger rate from TDAQ: approx **1600** events/spill
    - XCET44: pressure **3.994** bar, events **5214**, gas **CO2**
    - XCET48: pressure **1.999** bar, events **4987**, gas **CO2**
    - Run started: **17.08.2026, 12:06:20**
    - Run finished: **17.08.2026, 12:57:30**
    - Number of events: **204k**
    - DESY Table position: ** H: 52.218, V:-13.079
    
     - Run **1786964403** : **-1 GeV electron beam, collimators at beam_ref, TARGET; NO, <GOAL: Repeating our calibiration runs for Cal12**
 - beamfile: **<000>**
    - beam momentum: **<-1>** GeV
    - Trigger Condition: **S0S1**
    - Event rate from CESAR: approx **2166** vents/spill
    - Trigger rate from TDAQ: approx **1600** events/spill
    - XCET44: pressure **3.994** bar, events **2157**, gas **CO2**
    - XCET48: pressure **1.999** bar, events **2155**, gas **CO2**
    - Run started: **17.08.2026, 13:00:03**
    - Run finished: **17.08.2026, 13:38:12 :**
    - Number of events: **111836**
    - DESY Table position: ** H: 52.218, V:-13.079
**NOTE: We had issues with loading the beamfile although we tried it more than 4 times. And then, we called the PS control room, now we are waiting for our beamline physicist. It was because we have stayed inside so long that they took us out of the cycle :D** 
    
- Run **1786984559** : **+3 GeV positive hadron beam NO TARGET, background run **
 - beamfile: **<008>**
    - beam momentum: **<+3>** GeV
    - Trigger Condition: **S0S1FS0FS1**
    - Event rate from CESAR: approx **5221** vents/spill
    - Trigger rate from TDAQ: approx **1200** events/spill
:::danger
it seems a bit low than our previous value, the fingers should be alligned again :D
:::
    - XCET44: pressure **3.994** bar, events **x**, gas **CO2**
    - Run started: **17-Aug-2026 18:35:59**
    - Run finished: **17-Aug-2026 20:22:00**
    - Number of events: **311189**
    - DESY Table position: **H: 35.344, V:1.340**
:::info
from here it doesn't seem like the beam is aligned with center.it seems to be more hitting to the cal14. either cal14 is not parallel to the beam and the beam hits later on, or if it is parallel it is just too close. we will repeat the alignment, which is also ncessary since the FS0 and FS1 is not as high as yesterday. 
![](https://codimd.web.cern.ch/uploads/upload_ea53536ec41df76f56398454fa3b3960.png)
:::

:::info
    
we were able to connect to the TimePix in the zone. we will try to put it into the beam just for couple of spills while trying to as much as possible not hitting to the katherine box.
:::
    
:::warning


We have aligned the DWC, XBPF and markers again and again!! After making more precise alignment we figured out that beam is not going through from the gap between CALs but passing through CAL14 and CAL18. So, our plan to make sure we have equal gap between both towers. Difference between distance of upstream of desy table to right tower and left tower >7 mm, needs to be corrected as well.
    

    
:::    
    
    
## 2026.08.16
    
- Run **1786864539** : **-1 GeV BEAM, TRYING TO CALIBRATE CAL18**

    - beamfile: **000**
    - beam momentum: **-1** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **50107**


    - **Initial look**:
        - Event rate from CESAR: approx **2832** events/spill
        - Trigger rate from TDAQ: approx **1400** events/spill
        - XCET44: pressure **0.308** bar, events **132**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **2759**, gas **CO2**
        - Run started: **2026-08-16 09:15 **
        - Run finished: **2026-08-16 09:28 **

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **H:41.755**
        - DESY table vertical position: **V:-3.388**

    - **Observation**: CAL18 IS CENTERED AROUND  ~1000 QDC COUNT.
   
:::success
CAL18 IS DONE YAYY :)
:::
   
:::info
we are doing CAL5 calibration again because the neighbour ECAL's
    are showing high counts in QDC 
    
:::
    
- Run **1786865850** : **-1 GeV BEAM, TRYING TO CALIBRATE CAL5**

    - beamfile: **000**
    - beam momentum: **-1** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **59330**


    - **Initial look**:
        - Event rate from CESAR: approx **2691** events/spill
        - Trigger rate from TDAQ: approx **1400** events/spill
        - XCET44: pressure **0.308** bar, events **150**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **2638**, gas **CO2**
        - Run started: **2026-08-16 09:37 **
        - Run finished: **2026-08-16 09:52 **

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **H:41.755**
        - DESY table vertical position: **V:-3.388**

    - **Observation**: CAL5 IS CENTERED AROUND  ~697 QDC COUNT.
    the left right mean is -1.37+/-25.43mm
    the up down mean is -0.81 +/-23.82mm
    
- Run **1786866862** : **-2 GeV BEAM, TRYING TO CALIBRATE CAL5**

    - beamfile: **001**
    - beam momentum: **-2** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **55630**the version on disk (revert)?



    - **Initial look**:
        - Event rate from CESAR: approx **4886** events/spill
        - Trigger rate from TDAQ: approx **1800** events/spill
        - XCET44: pressure **0.308** bar, events **255**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **4717**, gas **CO2**
        - Run started: **2026-08-16 09:54 **
        - Run finished: **2026-08-16 10:05 **

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **H:41.755**
        - DESY table vertical position: **V:-3.388**

    - **Observation**: CAL5 IS CENTERED AROUND  ~1600 QDC COUNT.
    the left right mean is -0.86 +/-21.94mm
    the up down mean is -2.07 +/-20.26mm
    
- Run **1786867665** : **-3 GeV BEAM, TRYING TO CALIBRATE CAL5**

    - beamfile: **002**
    - beam momentum: **-3** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **52678**


    - **Initial look**:
        - Event rate from CESAR: approx **5229** events/spill
        - Trigger rate from TDAQ: approx **1800** events/spill
        - XCET44: pressure **0.308** bar, events **262**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **4876**, gas **CO2**
        - Run started: **2026-08-16 10:07 **
        - Run finished: **2026-08-16 10:18 **

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **H:41.755**
        - DESY table vertical position: **V:-3.388**

    - **Observation**: CAL5 IS CENTERED AROUND  ~3015 QDC COUNT.
    the left right mean is -0.36 +/-20.49mm
    the up down mean is -1.81 +/-19.14mm

:::success
   CAL5 is done!!! :)
:::
    
:::info
we are callibrating CAL4 because there was no FS0 and FS1 off earlier 
we are going to repeat the CAL4 with FS0 and FS1 included to the DAQ
:::  

- Run **1786868952** : **-3 GeV BEAM, TRYING TO CALIBRATE CAL4**

    - beamfile: **002**
    - beam momentum: **-3** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **51297**


    - **Initial look**:
        - Event rate from CESAR: approx **5502** events/spill
        - Trigger rate from TDAQ: approx **1800** events/spill
        - XCET44: pressure **0.308** bar, events **232**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **5111**, gas **CO2**
        - Run started: **2026-08-16 10:29 **
        - Run finished: **2026-08-16 10:39 **

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **H:31.470**
        - DESY table vertical position: **V:-3.696**

    - **Observation**: CAL4 IS CENTERED AROUND  ~3119 QDC COUNT.
    the left right mean is -0.35 +/-20.46mm
    the up down mean is -1.84 +/-18.81mm  
    
- Run **1786868952** : **-2 GeV BEAM, TRYING TO CALIBRATE CAL4**

    - beamfile: **001**
    - beam momentum: **-2** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **53113**


    - **Initial look**:
        - Event rate from CESAR: approx **4897** events/spill
        - Trigger rate from TDAQ: approx **1800** events/spill
        - XCET44: pressure **0.308** bar, events **258**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **4715**, gas **CO2**
        - Run started: **2026-08-16 10:40 **
        - Run finished: **2026-08-16 10:51 **

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **H:31.470**
        - DESY table vertical position: **V:-3.696**

    - **Observation**: CAL4 IS CENTERED AROUND  ~2107 QDC COUNT.
    the left right mean is -0.92 +/-22.10mm
    the up down mean is -1.49 +/-20.17mm     
    
    
- Run **1786870373** : **-1 GeV BEAM, TRYING TO CALIBRATE CAL4**

    - beamfile: **000**
    - beam momentum: **-1** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **50544**


    - **Initial look**:
        - Event rate from CESAR: approx **5028** events/spill
        - Trigger rate from TDAQ: approx **1400** events/spill
        - XCET44: pressure **0.308** bar, events **261**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **4859**, gas **CO2**
        - Run started: **2026-08-16 10:52 **
        - Run finished: **2026-08-16 11:13 **

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **H:31.470**
        - DESY table vertical position: **V:-3.696**

    - **Observation**: CAL4 IS CENTERED AROUND  ~1112 QDC COUNT.
    the left right mean is -1.65 +/-25.39mm
    the up down mean is -0.22 +/-24.02mm
    
:::success
CAL4 is done yayyyyyy!!   :) with the finger scintillators.
:::
    
:::info
Changed DESY table position from horizontal 31.470 and vertical -3.696 to horizontal 30.468 and vertical -3.696 to test the cluster algorithm by making a controlled change.
:::

    
    - Run **1786872460** : **-3 GeV BEAM, TRYING TO TEST THE CLUSTERING CODE**

    - beamfile: **002**
    - beam momentum: **-3** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **34870**


    - **Initial look**:
        - Event rate from CESAR: approx **5414** events/spill
        - Trigger rate from TDAQ: approx **1800** events/spill
        - XCET44: pressure **0.308** bar, events **239**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **5004**, gas **CO2**
        - Run started: **2026-08-16 11:27 **
        - Run finished: **2026-08-16 11:38 **

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **H:30.468**
        - DESY table vertical position: **V:-3.696**

    - **Observation**: CAL4 IS CENTERED AROUND  ~3.1K QDC COUNT.
    the left right mean is -0.44 +/-20.43mm
    the up down mean is -1.33 +/-19.31mm     
 
:::info
Changed DESY table position from horizontal 30.468 and vertical -3.696 to horizontal 29.467 and vertical -3.696 to test the cluster algorithm by making one more controlled change.
:::

    
- Run **1786873403** : **-3 GeV BEAM, TRYING TO TEST THE CLUSTERING CODE**
   
    - beamfile: **002**
    - beam momentum: **-3** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **35083**


    - **Initial look**:
        - Event rate from CESAR: approx **5450** events/spill
        - Trigger rate from TDAQ: approx **1800** events/spill
        - XCET44: pressure **0.308** bar, events **246**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **5060**, gas **CO2**
        - Run started: **2026-08-16 11:43 **
        - Run finished: **2026-08-16 11:54 **

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **H:29.467**
        - DESY table vertical position: **V:-3.696**

    - **Observation**: CAL4 IS CENTERED AROUND  ~3150 QDC COUNT.
    the left right mean is -0.73 +/-20.20mm
    the up down mean is -2.01 +/-19.10mm    
    

:::info
Changed DESY table position from horizontal 29.467 and vertical -3.696 to horizontal 28.465 and vertical -3.696 to test the cluster algorithm by making the third controlled change.
:::

 - Run **1786874231** : **-3 GeV BEAM, TRYING TO TEST THE CLUSTERING CODE**
    
    - beamfile: **002**
    - beam momentum: **-3** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **143574**


    - **Initial look**:
        - Event rate from CESAR: approx **5450** events/spill
        - Trigger rate from TDAQ: approx **1800** events/spill
        - XCET44: pressure **0.308** bar, events **246**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **5060**, gas **CO2**
        - Run started: **2026-08-16 11:57:11 **
        - Run finished: **2026-08-16 12:29:08 **

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **H:28.465**
        - DESY table vertical position: **V:-3.696**

    - **Observation**: CAL4 IS CENTERED AROUND  ~3100 QDC COUNT.
    the left right mean is -0.73 +/-20.20mm
    the up down mean is -2.01 +/-19.10mm   
    
:::info
Changed DESY table position from horizontal 28.465 and vertical -3.696 to horizontal 27.463 and vertical -3.696 to test the cluster algorithm by making the fourth controlled change.
:::

 - Run **1786876505** : **-3 GeV BEAM, TRYING TO TEST THE CLUSTERING CODE**
    
    - beamfile: **002**
    - beam momentum: **-3** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **35288**


    - **Initial look**:
        - Event rate from CESAR: approx **5450** events/spill
        - Trigger rate from TDAQ: approx **1800** events/spill
        - XCET44: pressure **0.308** bar, events **246**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **5060**, gas **CO2**
        - Run started: **2026-08-16  12:35:05 **
        - Run finished: **2026-08-16 12:42:37 **

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **H:27.463**
        - DESY table vertical position: **V:-3.696**

    - **Observation**: CAL4 IS CENTERED AROUND  ~3100 QDC COUNT.
    the left right mean is -0.73 +/-20.20mm
    the up down mean is -2.01 +/-19.10mm. 
    
:::danger 
CAL1 IS AGAIN MAKING THAT AWKWARD SIGNAL AGAIN.
![](https://codimd.web.cern.ch/uploads/upload_b4f207f21a02557b93da0d18c258943b.jpeg)
WE NEED TO CHANGE THE CAL1 TO CH17.
WE WENT INSIDE AND CHANGED CAL1 FROM CH1 TO CH17. LET'S REPEAT THE RUN.
:::
    
 - Run **1786877233** : **-3 GeV BEAM, TRYING TO TEST THE CLUSTERING CODE, TRYING TO UNDERSTAND**
    
    - beamfile: **002**
    - beam momentum: **-3** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **X**


    - **Initial look**:
        - Event rate from CESAR: approx **5450** events/spill
        - Trigger rate from TDAQ: approx **1800** events/spill
        - XCET44: pressure **0.308** bar, events **246**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **5060**, gas **CO2**
        - Run started: **2026-08-16  12:47:13**
        - Run finished: **2026-08-16 X **

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **H:27.463**
        - DESY table vertical position: **V:-3.696**
:::danger
during this run we've entered the zone to terminate ch0 and ch1 to understand what is going on with those channels.
:::
    - **Observation**: CAL4 IS CENTERED AROUND  ~3000 QDC COUNT.
    the left right mean is -0.73 +/-20.20mm
    the up down mean is -2.01 +/-19.10mm. Now the cal1-ch17 looks okay. but that means we need to repeat the cal1 calibration :(. 
  
run number: 1786878223 total: 110754 finish 16-Aug-2026 13:27:56.
    
:::danger
    The ch0 and ch1 of QDC were reading unreasonably high values. So we discussed the possiblties such as high temperature and technical issues. We first tried to change the ch0 to ch16 and ch1 to ch17. As it didn't work we check the QDCs in the beam area. We removed the panel which is tought to be for holding dust and checked the temperatures of the inside of it which were normal. After leaving it open and leaving the beam area, we restarted the beam and the issue was fixed. Later we changed the ch17 back to ch1. 
:::
    
- Run **1786882172** : **-3 GeV BEAM, TRYING TO TEST THE CLUSTERING CODE, TRYING TO UNDERSTAND HOW THE COUNTS OF NEIGBORING CALORIMETERS CHANGE WHEN THE BEAM HITS 1cm LOWER FROM THE CENTER OF CAL4**
    
    - beamfile: **002**
    - beam momentum: **-3** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **36781**


    - **Initial look**:
        - Event rate from CESAR: approx **4755** events/spill
        - Trigger rate from TDAQ: approx **1800** events/spill
        - XCET44: pressure **0.308** bar, events **219**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **4433**, gas **CO2**
        - Run started: **2026-08-16  14:09:32**
        - Run finished: **2026-08-16 14:17:39**

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **H:31.476**
        - DESY table vertical position: **V:-2.690**

- Run **1786883073** : **-3 GeV BEAM, TRYING TO TEST THE CLUSTERING CODE, TRYING TO UNDERSTAND HOW THE COUNTS OF NEIGBORING CALORIMETERS CHANGE WHEN THE BEAM HITS 2cm LOWER FROM THE CENTER OF CAL4**
    
    - beamfile: **002**
    - beam momentum: **-3** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **35327**


    - **Initial look**:
        - Event rate from CESAR: approx **5383** events/spill
        - Trigger rate from TDAQ: approx **1800** events/spill
        - XCET44: pressure **0.308** bar, events **225**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **4564**, gas **CO2**
        - Run started: **2026-08-16  14:24:33**
        - Run finished: **2026-08-16 14:32:11**

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **H:31.476**
        - DESY table vertical position: **V:-1.694**

- Run **1786883648** : **-3 GeV BEAM, TRYING TO TEST THE CLUSTERING CODE, TRYING TO UNDERSTAND HOW THE COUNTS OF NEIGBORING CALORIMETERS CHANGE WHEN THE BEAM HITS 3cm LOWER FROM THE CENTER OF CAL4**
    
    - beamfile: **002**
    - beam momentum: **-3** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **38658**


    - **Initial look**:
        - Event rate from CESAR: approx **5421** events/spill
        - Trigger rate from TDAQ: approx **1800** events/spill
        - XCET44: pressure **0.308** bar, events **241**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **5005**, gas **CO2**
        - Run started: **2026-08-16  14:34:08**
        - Run finished: **2026-08-16 14:42:41**

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **H:31.476**
        - DESY table vertical position: **V:-0.696**
    
- Run **1786884479** : **-3 GeV BEAM, TRYING TO TEST THE CLUSTERING CODE, TRYING TO UNDERSTAND HOW THE COUNTS OF NEIGBORING CALORIMETERS CHANGE WHEN THE BEAM HITS 4cm LOWER FROM THE CENTER OF CAL4**
    
    - beamfile: **002**
    - beam momentum: **-3** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **31766**


    - **Initial look**:
        - Event rate from CESAR: approx **5177** events/spill
        - Trigger rate from TDAQ: approx **1800** events/spill
        - XCET44: pressure **0.308** bar, events **238**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **4795**, gas **CO2**
        - Run started: **2026-08-16  14:47:59**
        - Run finished: **2026-08-16 14:54:48**

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **H:31.476**
        - DESY table vertical position: **V:0.310**
    
- Run **1786885113** : **-3 GeV BEAM, TRYING TO TEST THE CLUSTERING CODE, TRYING TO UNDERSTAND HOW THE COUNTS OF NEIGBORING CALORIMETERS CHANGE WHEN THE BEAM HITS 5cm LOWER FROM THE CENTER OF CAL4**
    
    - beamfile: **002**
    - beam momentum: **-3** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **31766**


    - **Initial look**:
        - Event rate from CESAR: approx **5389** events/spill
        - Trigger rate from TDAQ: approx **1800** events/spill
        - XCET44: pressure **0.308** bar, events **258**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **4981**, gas **CO2**
        - Run started: **2026-08-16 14:58:33**
        - Run finished: **2026-08-16 15:04**

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **H:31.476**
        - DESY table vertical position: **V:1.310**
:::danger
After we started the high voltage, cal12 exceeded the set limit of current and tripped then we lowered it to 1500V but it tripped again. So we turned it off for a moment. Later due to the high current we changed the limit to 1475V and now it stopped tripping. We also changed the blanket with a black plastic.
:::
    
- Run **1786887458** : **-3 GeV BEAM, TRYING TO TEST THE CLUSTERING CODE, TRYING TO UNDERSTAND HOW THE COUNTS OF NEIGBORING CALORIMETERS CHANGE WHEN THE BEAM HITS 5cm LOWER FROM THE CENTER OF CAL4. WE'RE REDOING THE RUN BECAUSE PREVIOUS DATA WAS A BIT FAULTY.**
    
    - beamfile: **002**
    - beam momentum: **-3** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **35072**


    - **Initial look**:
        - Event rate from CESAR: approx **5320** events/spill
        - Trigger rate from TDAQ: approx **1800** events/spill
        - XCET44: pressure **0.308** bar, events **232**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **4931**, gas **CO2**
        - Run started: **2026-08-16 15:37:38**
        - Run finished: **2026-08-16 15:45:51**

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **H:31.476**
        - DESY table vertical position: **V:1.310**
    
    
- Run **1786890116** : **-1 GeV BEAM, testing the clustering code at low energy.**
    
    - beamfile: **000**
    - beam momentum: **-1** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **32212**


    - **Initial look**:
        - Event rate from CESAR: approx **2826** events/spill
        - Trigger rate from TDAQ: approx **1400** events/spill
        - XCET44: pressure **0.308** bar, events **147**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **2490**, gas **CO2**
        - Run started: **2026-08-16 16:21:56**
        - Run finished: **2026-08-16 16:31:14**

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **H:31.476**
        - DESY table vertical position: **V:1.310**
    
    
- Run **1786890116** : **-1 GeV BEAM,testing the clustering code at low energy**
    
    - beamfile: **000**
    - beam momentum: **-1** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **33970**


    - **Initial look**:
        - Event rate from CESAR: approx **2277** events/spill
        - Trigger rate from TDAQ: approx **1400** events/spill
        - XCET44: pressure **0.308** bar, events **147**, gas **CO2**
        - XCET48: pressure **1.003** bar, events **2490**, gas **CO2**
        - Run started: **2026-08-16 16:36:50**
        - Run finished: **2026-08-16 16:46:51**

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **H:31.476**
        - DESY table vertical position: **V:0.310**
    
    
- Run **1786891837** : **-1 GeV BEAM,testing the clustering code at low energy**
    
    - beamfile: **000**
    - beam momentum: **-1** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **45998**


    - **Initial look**:
        - Event rate from CESAR: approx **2277** events/spill
        - Trigger rate from TDAQ: approx **1400** events/spill
        - XCET44: pressure **0.308** bar, events **120**, gas **CO2**
        - XCET48: pressure **1.003** bar, events **2733**, gas **CO2**
        - Run started: **16-08-2026 16:50:37**
        - Run finished: **16-08-2026 17:03:33**

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **H:31.476**
        - DESY table vertical position: **V:-0.689**
    
    
- Run **1786892766** : **-1 GeV BEAM, testing the clustering code at low energy**
    
    - beamfile: **000**
    - beam momentum: **-1** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **33117**


    - **Initial look**:
        - Event rate from CESAR: approx **2736** events/spill
        - Trigger rate from TDAQ: approx **1400** events/spill
        - XCET44: pressure **0.308** bar, events **140**, gas **CO2**
        - XCET48: pressure **1.003** bar, events **2673**, gas **CO2**
        - Run started: **16-08-2026 17:06:06**
        - Run finished: **16-08-2026 17:14:01**

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **H:31.476**
        - DESY table vertical position: **V:-1.689**
    
    
    
    
    
    - Run **1786893316** : **-1 GeV BEAM, testing the clustering code at low energy**
    
    - beamfile: **000**
    - beam momentum: **-1** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **30446**


    - **Initial look**:
        - Event rate from CESAR: approx **2736** events/spill
        - Trigger rate from TDAQ: approx **1400** events/spill
        - XCET44: pressure **0.308** bar, events **150**, gas **CO2**
        - XCET48: pressure **1.003** bar, events **2746**, gas **CO2**
        - Run started: **16-Aug-2026 17:15:16**
        - Run finished: **16-Aug-2026 17:22:36**

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **H:31.476**
        - DESY table vertical position: **V:-2.689**
    
       
    - Run **1786894793** : **-1 GeV BEAM, testing the clustering code at low energy**
    
    - beamfile: **000**
    - beam momentum: **-1** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **49257**


    - **Initial look**:
        - Event rate from CESAR: approx **2655** events/spill
        - Trigger rate from TDAQ: approx **1400** events/spill
        - XCET44: pressure **0.308** bar, events **300**, gas **CO2**
        - XCET48: pressure **1.003** bar, events **5000**, gas **CO2**
        - Run started: **16-Aug-2026 17:39:53**
        - Run finished: **16-Aug-2026  17:51:50**

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **H:30.473**
        - DESY table vertical position: **V:-3.696**
    
- Run **1786895892** : **-1 GeV BEAM, testing the clustering code at low energy**
    
    - beamfile: **000**
    - beam momentum: **-1** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **367090**


    - **Initial look**:
        - Event rate from CESAR: approx **2655** events/spill
        - Trigger rate from TDAQ: approx **1400** events/spill
        - XCET44: pressure **0.308** bar, events **300**, gas **CO2**
        - XCET48: pressure **1.003** bar, events **5000**, gas **CO2**
        - Run started: **16-Aug-2026 17:58**
        - Run finished: **16-Aug-2026 19:43**

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **H:29.475**
        - DESY table vertical position: **V:-3.696**
        
- Run **1786903064** : **-1 GeV BEAM,**
    
    - beamfile: **000**
    - beam momentum: **-1** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **36740**


    - **Initial look**:
        - Event rate from CESAR: approx **2655** events/spill
        - Trigger rate from TDAQ: approx **1400** events/spill
        - XCET44: pressure **0.308** bar, events **300**, gas **CO2**
        - XCET48: pressure **1.003** bar, events **5000**, gas **CO2**
        - Run started: **16-Aug-2026 19:57**
        - Run finished: **16-Aug-2026 20:09**

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **H:28.479**
        - DESY table vertical position: **V:-3.696**    
        
 - Run **1786903854** : **-1 GeV BEAM, testing the clustering code at low energy**
    
    - beamfile: **000**
    - beam momentum: **-1** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **x**
    - **Initial look**:
        - Event rate from CESAR: approx **2655** events/spill
        - Trigger rate from TDAQ: approx **1400** events/spill
        - XCET44: pressure **0.308** bar, events **300**, gas **CO2**
        - XCET48: pressure **1.003** bar, events **5000**, gas **CO2**
        - Run started: **16-Aug-2026 20:10**
        - Run finished: **16-Aug-2026 20:27**

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **H:27.476**
        - DESY table vertical position: **V:-3.696**    
:::info
when this run is finished, it means we are done with all cluster calibration runs. 
:::

:::info
we've got curious about the beam spot movements and beam spot center at high and low energies. we have pos hadron +15 GeV, +10 GeV, + 5 GeV +1 GeV Beam files. With each one of them we will check how much the beam spot moves.
| Beam Energy | Plane | Mean Position [mm] | RMS Width [mm] | Cut-off |
|-------------|-------|-------------------:|---------------:|--------:|
| +15 GeV | SJ | -0.3 | 3.9 | - |
| +15 GeV | UD | -0.7 | 5.2 | - |
| +10 GeV | SJ | -5.7 | 5.4 | 57% |
| +10 GeV | UD | +6.2 | 5.4 | 60% |
| +5 GeV | SJ | +3.8 | 5.3 | 77% |
| +5 GeV | UD | +3.5 | 5.7 | 73% |
| +3 GeV | SJ | -4.2 | 10.2 | 58% |
| +3 GeV | UD | +0.6 | 10.6 | 53% |
| +3 GeV (second measurement) | SJ | -4.1 | 5.1 | 85% |
| +3 GeV (second measurement) | UD | +2.1 | 4.9 | 85% |
| +1 GeV | SJ | - | - | No clear beam center |
| +1 GeV | UD | - | - | No clear beam center |
:::spoiler
    +15 GeV pos hadrons, beam file number 3. SJ:  -0.3
    mm, RMS 3.9 mm, SJ:-0.7 mm, RMS 5.2 mm. We are now moving to beam file 4, +10 GeV pos hadrons. SJ: -5.7 RMS: 5.4, cut off 57%, UP:6.2 RMS:5.4, cut off 60%. +5 GeV pos hadrons beam file 7. SJ:3.8, RMS:5.3, cut off 77% UD: mean: 3.5, rms:5.7, cut off 73%. for 1 GeV pos hadron beam file 10, no beam center, terrible. +3 GeV pos hadrons, beam file 8. SJ: mean: -4.2, rms:10.2, cut off 58%. UD: mean: 0.6 RMS:10.6 cut off 53%. SJ: mean -4.1, rms 5.1 cut off 85%. UD: mean 2.1 rms:4.9 cut off 85%.
:::
:::
    
 

    
    - Run **1786905364** : **15 GeV BEAM, TO SEE HOW THE WIDTH OF BEAM CHANGES WITH ENERGY **

    - beamfile: **003**
    - beam momentum: **15** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **14699**

    
      - Run **1786906157** : **10 GeV BEAM, TO SEE HOW THE WIDTH OF BEAM CHANGES WITH ENERGY **

    - beamfile: **004**
    - beam momentum: **10** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **52821** 
    
     - Run **1786906692** : **5 GeV BEAM, TO SEE HOW THE WIDTH OF BEAM CHANGES WITH ENERGY **

    - beamfile: **007**
    - beam momentum: **5** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **37615** 
    
    
    
     - Run **1786907349** : **1 GeV BEAM, TO SEE HOW THE WIDTH OF BEAM CHANGES WITH ENERGY **

    - beamfile: **010**
    - beam momentum: **1** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **592** 

    
     - Run **1786907647** : **3 GeV BEAM, TO SEE HOW THE WIDTH OF BEAM CHANGES WITH ENERGY **

    - beamfile: **008**
    - beam momentum: **3** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **70k** 

:::success
we will take our first physics run yihhuu. now setting our cherenkov threshold values. one of them will be set XCET48 to 2 bar to tag e,mu. and XCET48 to 4 bar to tag e mu pi. we have also increased the voltage on the cal12 to 1525 also not to repeat the calibration. But we have changed the cover with something lighter, some thing black, and something smells terrible. but it is designed for dark room experiments, so we believe it is still very helpful.  
:::    
    
    
- Run **1786914869** : **+3 GeV BEAM**

    - beamfile: **008**
    - beam momentum: **+3** GeV
    - Trigger Condition: **S0S1FS0FS1**
    - Number of events: **2011309**


    - **Initial look**:
        - Event rate from CESAR: approx *x** events/spill
        - Trigger rate from TDAQ: approx **1.8K** events/spill
        - XCET44: pressure **0.308** bar, events **x**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **x**, gas **CO2**
        - Run started: **2026-08-16 23:14**
        - Run finished: **2026-08-17 10:07**

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
     
        - DESY table horizontal position: **36.151**
        - DESY table vertical position: **1.180**

    - **Observation**:we put 3 cm Graphite target. Distance between US of Target to US of CALs=50 cm!
:::info    
we go home! we must sleeppppppppppppp 
:::
## 2026.08.15

- Run **1786744833** : **-3 GeV BEAM, TRYING TO CALIBRATE CAL13**

    - beamfile: **002**
    - beam momentum: **-3** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **57401**


    - **Initial look**:
        - Event rate from CESAR: approx *5K** events/spill
        - Trigger rate from TDAQ: approx **1.8K** events/spill
        - XCET44: pressure **0.308** bar, events **311**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **5034**, gas **CO2**
        - Run started: **2026-08-14 00:00:33**
        - Run finished: **2026-08-14 00:12:50**

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **51.414**
        - DESY table vertical position: **15.768**

    - **Observation**:  CAL13 IS CENTERED AROUND  **2400** QDC COUNT.

:::success
CAL13 is finished    
:::

- Run **1786745756** : **-3 GeV BEAM, TRYING TO CALIBRATE CAL11**

    - beamfile: **002**
    - beam momentum: **-3** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **52605**


    - **Initial look**:
        - Event rate from CESAR: approx *5K** events/spill
        - Trigger rate from TDAQ: approx **1.8K** events/spill
        - XCET44: pressure **0.308** bar, events **311**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **5034**, gas **CO2**
        - Run started: **2026-08-15 00:15:56**
        - Run finished: **2026-08-15  00:27:00**

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **51.394**
        - DESY table vertical position: **6.271**

    - **Observation**:  CAL11 IS CENTERED AROUND  **2600** QDC COUNT.

  - Run **1786746501** : **-2 GeV BEAM, TRYING TO CALIBRATE CAL11**

    - beamfile: **001**
    - beam momentum: **-2** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **50280**


    - **Initial look**:
        - Event rate from CESAR: approx *5K** events/spill
        - Trigger rate from TDAQ: approx **1.8K** events/spill
        - XCET44: pressure **0.308** bar, events **311**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **5034**, gas **CO2**
        - Run started: **2026-08-15 00:28:21**
        - Run finished: **2026-08-15  00:39:45**

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **51.394**
        - DESY table vertical position: **6.271**

    - **Observation**:  CAL11 IS CENTERED AROUND  **1800** QDC COUNT.

 - Run **1786747305** : **-1 GeV BEAM, TRYING TO CALIBRATE CAL11**

    - beamfile: **000**
    - beam momentum: **-1** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **54196**


    - **Initial look**:
        - Event rate from CESAR: approx *3K** events/spill
        - Trigger rate from TDAQ: approx **1.3K** events/spill
        - XCET44: pressure **0.308** bar, events **197**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **3.9k**, gas **CO2**
        - Run started: **2026-08-15 00:41:45**
        - Run finished: **2026-08-15  00:57:00**

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **51.394**
        - DESY table vertical position: **6.271**

    - **Observation**:  CAL11 IS CENTERED AROUND  **900** QDC COUNT.

:::success
CAL11 is finished    
:::

 - Run **1786748346** : **-1 GeV BEAM, TRYING TO CALIBRATE CAL14**

    - beamfile: **000**
    - beam momentum: **-1** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **49937**


    - **Initial look**:
        - Event rate from CESAR: approx *3K** events/spill
        - Trigger rate from TDAQ: approx **1.3K** events/spill
        - XCET44: pressure **0.308** bar, events **197**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **3.9k**, gas **CO2**
        - Run started: **2026-08-15 00:59:06**
        - Run finished: **2026-08-15  **01:13:18**

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **41.418**
        - DESY table vertical position: **6.398**

    - **Observation**:  CAL14 IS CENTERED AROUND  **1200** QDC COUNT.

 - Run **1786750147** : **-2 GeV BEAM, TRYING TO CALIBRATE CAL14**

    - beamfile: **001**
    - beam momentum: **-2** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **50381**


    - **Initial look**:
        - Event rate from CESAR: approx *5.3K** events/spill
        - Trigger rate from TDAQ: approx **1.8K** events/spill
        - XCET44: pressure **0.308** bar, events **197**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **5.1k**, gas **CO2**
        - Run started: **2026-08-15 01:29:07**
        - Run finished: **2026-08-15  01:40:14**

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **41.418**
        - DESY table vertical position: **6.398**

    - **Observation**:  CAL14 IS CENTERED AROUND  **2300** QDC COUNT.

 - Run **1786750887** : **-3 GeV BEAM, TRYING TO CALIBRATE CAL14**

    - beamfile: **002**
    - beam momentum: **-3** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **2.6m**


    - **Initial look**:
        - Event rate from CESAR: approx *4.9K** events/spill
        - Trigger rate from TDAQ: approx **1.8K** events/spill
        - XCET44: pressure **0.308** bar, events **197**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **4.6k**, gas **CO2**
        - Run started: **2026-08-15 01:41:27**
        - Run finished: **2026-08-15  09:35**

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **41.418**
        - DESY table vertical position: **6.398**

    - **Observation**:  CAL14 IS CENTERED AROUND  **3300** QDC COUNT.
:::warning
unfort no beam:(    
:::
    
:::success
CAL14 finished
:::
    


 - Run **1786779710** : **-3 GeV BEAM, TRYING TO CALIBRATE CAL2**

    - beamfile: **002**
    - beam momentum: **-3** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **57950**


    - **Initial look**:
        - Event rate from CESAR: approx *5517** events/spill
        - Trigger rate from TDAQ: approx **1.8K** events/spill
        - XCET44: pressure **0.308** bar, events **238**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **4973**, gas **CO2**
        - Run started: **2026-08-15 09:41**
        - Run finished: **2026-08-15  09:54**

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **31.197**
        - DESY table vertical position: **6.333**

    - **Observation**:  CAL2 IS CENTERED AROUND  **3200** QDC COUNT.
    
    
    
     - Run **1786780617** : **-2 GeV BEAM, TRYING TO CALIBRATE CAL2**

    - beamfile: **001**
    - beam momentum: **-2** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **x54909**


    - **Initial look**:
        - Event rate from CESAR: approx *5218** events/spill
        - Trigger rate from TDAQ: approx **1.8k** events/spill
        - XCET44: pressure **0.308** bar, events **266**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **5042**, gas **CO2**
        - Run started: **2026-08-15 09:42**
        - Run finished: **2026-08-15  10:09**

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **31.197**
        - DESY table vertical position: **6.333**

    - **Observation**:  CAL2 IS CENTERED AROUND  **2200** QDC COUNT.
    
  
    
     - Run **1786781408** : **-1 GeV BEAM, TRYING TO CALIBRATE CAL2**

    - beamfile: **000**
    - beam momentum: **-1** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **55253**


    - **Initial look**:
        - Event rate from CESAR: approx **5200** events/spill
        - Trigger rate from TDAQ: approx **1.8k** events/spill
        - XCET44: pressure **0.308** bar, events **162**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **3005**, gas **CO2**
        - Run started: **2026-08-15 10:10**
        - Run finished: **2026-08-15  10:25**

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **31.197**
        - DESY table vertical position: **6.333**

    - **Observation**:  CAL2 IS CENTERED AROUND  **1200** QDC COUNT.  
    
    
:::success
CAL2 has finished 
:::
    
- Run **1786782465** : **-1 GeV BEAM, TRYING TO CALIBRATE CAL0**

    - beamfile: **000**
    - beam momentum: **-1** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **50390**


    - **Initial look**:
        - Event rate from CESAR: approx **5200** events/spill
        - Trigger rate from TDAQ: approx **1.8k** events/spill
        - XCET44: pressure **0.308** bar, events **162**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **3005**, gas **CO2**
        - Run started: **2026-08-15 10:27**
        - Run finished: **2026-08-15  10:42**

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **21.059**
        - DESY table vertical position: **6.421**

    - **Observation**:  CAL0 IS CENTERED AROUND  **1200** QDC COUNT.    
    

- Run **1786787514** : **-2 GeV BEAM, TRYING TO CALIBRATE CAL0**

    - beamfile: **001**
    - beam momentum: **-2** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **52627**


    - **Initial look**:
        - Event rate from CESAR: approx **5000** events/spill
        - Trigger rate from TDAQ: approx **1.8k** events/spill
        - XCET44: pressure **0.308** bar, events **162**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **4.8k**, gas **CO2**
        - Run started: **2026-08-15 11:51:54**
        - Run finished: **2026-08-15  12:06:20**

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **21.059**
        - DESY table vertical position: **6.421**

    - **Observation**:  CAL0 IS CENTERED AROUND  **2000** QDC COUNT.    
    
    
- Run **1786788903** : **-3 GeV BEAM, TRYING TO CALIBRATE CAL0**

    - beamfile: **002**
    - beam momentum: **-3** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **75301**


    - **Initial look**:
        - Event rate from CESAR: approx **5,1k** events/spill
        - Trigger rate from TDAQ: approx **1.8k** events/spill
        - XCET44: pressure **0.308** bar, events **246**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **4.7k**, gas **CO2**
        - Run started: **2026-08-15 12:15**
        - Run finished: **2026-08-15 12:35 **

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **21.059**
        - DESY table vertical position: **6.421**

    - **Observation**:  CAL0 IS CENTERED AROUND  **3000** QDC COUNT.    
    
:::success
CAL0 has finished
:::
    
 - Run **1786790499** : **-3 GeV BEAM, TRYING TO CALIBRATE CAL10**

    - beamfile: **002**
    - beam momentum: **-3** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **68453**


    - **Initial look**:
        - Event rate from CESAR: approx **5,1k** events/spill
        - Trigger rate from TDAQ: approx **1.8k** events/spill
        - XCET44: pressure **0.308** bar, events **246**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **4.7k**, gas **CO2**
        - Run started: **2026-08-15 12:41**
        - Run finished: **2026-08-15  13:03:34 **

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **21.683**
        - DESY table vertical position: **-13.166**

    - **Observation**:  CAL10 IS CENTERED AROUND  **2400** QDC COUNT.      
    
- Run **1786791937** : **-2 GeV BEAM, TRYING TO CALIBRATE CAL10**

    - beamfile: **001**
    - beam momentum: **-2** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **56256**


    - **Initial look**:
        - Event rate from CESAR: approx **5211k** events/spill
        - Trigger rate from TDAQ: approx **1.8k** events/spill
        - XCET44: pressure **0.308** bar, events **230**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **5019**, gas **CO2**
        - Run started: **2026-08-15 13:05**
        - Run finished: **2026-08-15  13:26 **

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **21.683**
        - DESY table vertical position: **-13.166**

    - **Observation**:  CAL10 IS CENTERED AROUND  **1700** QDC COUNT.     
    
     - Run **1786793439** : **-1 GeV BEAM, TRYING TO CALIBRATE CAL10**

    - beamfile: **000**
    - beam momentum: **-1** GeV
    - Trigger Condition: **S0S1**
    - Number of events: ****


    - **Initial look**:
        - Event rate from CESAR: approx **2.7k** events/spill
        - Trigger rate from TDAQ: approx **1.8k** events/spill
        - XCET44: pressure **0.308** bar, events **134**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **2708**, gas **CO2**
        - Run started: **2026-08-15 13:30**
        - Run finished: **2026-08-15  13:49 **

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **21.683**
        - DESY table vertical position: **-13.166**

    - **Observation**:  CAL10 IS CENTERED AROUND  **900** QDC COUNT.     
    
:::success
CAL10 has finishedd!!    
:::    

- Run **1786794828** : **-1 GeV BEAM, TRYING TO CALIBRATE CAL5**

    - beamfile: **000**
    - beam momentum: **-1** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **53044**


    - **Initial look**:
        - Event rate from CESAR: approx **2.9k** events/spill
        - Trigger rate from TDAQ: approx **1.2k** events/spill
        - XCET44: pressure **0.308** bar, events **139**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **2867**, gas **CO2**
        - Run started: **2026-08-15 13:53**
        - Run finished: **2026-08-15 14:12 **

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **31.856**
        - DESY table vertical position: **-12.986**

    - **Observation**:  CAL5 IS CENTERED AROUND  **1090** QDC COUNT. 
    
- Run **1786796090** : **-2 GeV BEAM, TRYING TO CALIBRATE CAL5**

    - beamfile: **001**
    - beam momentum: **-2** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **51109**


    - **Initial look**:
        - Event rate from CESAR: approx **5k** events/spill
        - Trigger rate from TDAQ: approx **1.6k** events/spill
        - XCET44: pressure **0.308** bar, events **219**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **4837**, gas **CO2**
        - Run started: **2026-08-15 14:14 **
        - Run finished: **2026-08-15 14:28 **

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **31.856**
        - DESY table vertical position: **-12.986**

    - **Observation**:  CAL5 IS CENTERED AROUND  **2070** QDC COUNT. 

      - Run **1786797061** : **-3 GeV BEAM, TRYING TO CALIBRATE CAL5**

    - beamfile: **002**
    - beam momentum: **-3** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **52630**


    - **Initial look**:
        - Event rate from CESAR: approx **5.4k** events/spill
        - Trigger rate from TDAQ: approx **1.8k** events/spill
        - XCET44: pressure **0.308** bar, events **233**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **5018**, gas **CO2**
        - Run started: **2026-08-15 14:31**
        - Run finished: **2026-08-15 14:44**

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **31.856**
        - DESY table vertical position: **-12.986**

    - **Observation**:  CAL5 IS CENTERED AROUND  **3089** QDC COUNT. 
    
:::success
CAL5 has finished YAY!!    
:::  

    
- Run **1786798201** : **-3 GeV BEAM, TRYING TO CALIBRATE CAL1**

    - beamfile: **002**
    - beam momentum: **-3** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **51149**


    - **Initial look**:
        - Event rate from CESAR: approx **5.5K** events/spill
        - Trigger rate from TDAQ: approx **1.8K** events/spill
        - XCET44: pressure **0.308** bar, events **288**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **5197**, gas **CO2**
        - Run started: **2026-08-15 14:50**
        - Run finished: **2026-08-15 15:03**

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **42.114**
        - DESY table vertical position: **-12.986**

    - **Observation**:  CAL1 IS CENTERED AROUND  **2308** QDC COUNT. 
    
- Run **1786799056** : **-2 GeV BEAM, TRYING TO CALIBRATE CAL1**

    - beamfile: **001**
    - beam momentum: **-2** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **50791**


    - **Initial look**:
        - Event rate from CESAR: approx **5.2K** events/spill
        - Trigger rate from TDAQ: approx **1.8K** events/spill
        - XCET44: pressure **0.308** bar, events **227**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **5120**, gas **CO2**
        - Run started: **2026-08-15 15:04**
        - Run finished: **2026-08-15 15:18**

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **42.114**
        - DESY table vertical position: **-12.986**

    - **Observation**:  CAL1 IS CENTERED AROUND  **1516** QDC COUNT. 
  
- Run **1786800039** : **-1 GeV BEAM, TRYING TO CALIBRATE CAL1**

    - beamfile: **000**
    - beam momentum: **-1** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **50235**


    - **Initial look**:
        - Event rate from CESAR: approx **2.8K** events/spill
        - Trigger rate from TDAQ: approx **1.4K** events/spill
        - XCET44: pressure **0.308** bar, events **125**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **2703**, gas **CO2**
        - Run started: **2026-08-15 15:20**
        - Run finished: **2026-08-15 15:38**

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **42.114**
        - DESY table vertical position: **-12.986**

    - **Observation**:  CAL1 IS CENTERED AROUND  **820** QDC COUNT. 
    
:::success
CAL1 FINISHED
:::
    
- Run **1786801341** : **-1 GeV BEAM, TRYING TO CALIBRATE CAL12**

    - beamfile: **000**
    - beam momentum: **-1** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **54129**


    - **Initial look**:
        - Event rate from CESAR: approx **2748** events/spill
        - Trigger rate from TDAQ: approx **1.4K** events/spill
        - XCET44: pressure **0.308** bar, events **131**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **2789**, gas **CO2**
        - Run started: **2026-08-15 15:42**
        - Run finished: **2026-08-15 16:01:43**

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **42.114**
        - DESY table vertical position: **-12.986**

    - **Observation**:  CAL12 IS CENTERED AROUND  **750** QDC COUNT. 

- Run **1786802590** : **-2 GeV BEAM, TRYING TO CALIBRATE CAL12**

    - beamfile: **001**
    - beam momentum: **-2** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **50889**


    - **Initial look**:
        - Event rate from CESAR: approx **4783** events/spill
        - Trigger rate from TDAQ: approx **1.7K** events/spill
        - XCET44: pressure **0.308** bar, events **201**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **4627**, gas **CO2**
        - Run started: **2026-08-15 16:03:10**
        - Run finished: **2026-08-15 16:17:43**

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **42.114**
        - DESY table vertical position: **-12.986**

    - **Observation**:  CAL12 IS CENTERED AROUND  **1400** QDC COUNT. 
    
:::warning
We had ~2k counts with CAL12 in June Testbeam. Now it is less. This CAL12 also get tripped once today. It looks fine now, but let's follow it up.
:::
    
- Run **1786803907** : **-3 GeV BEAM, TRYING TO CALIBRATE CAL12**

    - beamfile: **002**
    - beam momentum: **-3** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **50661**


    - **Initial look**:
        - Event rate from CESAR: approx **4989** events/spill
        - Trigger rate from TDAQ: approx **1.8K** events/spill
        - XCET44: pressure **0.308** bar, events **200**, gas **CO2**
        - XCET48: pressure **1.004** bar, events **4642**, gas **CO2**
        - Run started: **2026-08-15 16:25:07**
        - Run finished: **2026-08-15 16:38:51**

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **42.114**
        - DESY table vertical position: **-12.986**

    - **Observation**:  CAL12 IS CENTERED AROUND  **2000** QDC COUNT.
                        The QDC count is lower than the June test beam.

:::success
Cal12 has finished
:::
- Run **1786805198** : **-3 GeV BEAM, TRYING TO CALIBRATE CAL17**

    - beamfile: **002**
    - beam momentum: **-3** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **52349**


    - **Initial look**:
        - Event rate from CESAR: approx **5042** events/spill
        - Trigger rate from TDAQ: approx **1.8K** events/spill
        - XCET44: pressure **0.308** bar, events **239**, gas **CO2**
        - XCET48: pressure **1.004** bar, events **4666**, gas **CO2**
        - Run started: **2026-08-15 16:46:38**
        - Run finished: **2026-08-15 17:00:25**

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **21.695**
        - DESY table vertical position: **-3.697**

    - **Observation**:  CAL17 IS CENTERED AROUND  **2700** QDC COUNT.
                        The QDC count is lower than the June test beam.

- Run **1786806354** : **-2 GeV BEAM, TRYING TO CALIBRATE CAL17**

    - beamfile: **001**
    - beam momentum: **-2** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **51081**


    - **Initial look**:
        - Event rate from CESAR: approx **5015** events/spill
        - Trigger rate from TDAQ: approx **1.8k** events/spill
        - XCET44: pressure **0.308** bar, events **236**, gas **CO2**
        - XCET48: pressure **1.004** bar, events **4866**, gas **CO2**
        - Run started: **2026-08-15 17:05:54**
        - Run finished: **2026-08-15 17:23:05**

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **21.695**
        - DESY table vertical position: **-3.697**

    - **Observation**:  CAL17 IS CENTERED AROUND  **1900** QDC COUNT.
                        The QDC count is lower than the June test beam.
 
   - Run **1786807867** : **-1 GeV BEAM, TRYING TO CALIBRATE CAL17**

    - beamfile: **000**
    - beam momentum: **-1** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **58556**


    - **Initial look**:
        - Event rate from CESAR: approx **2775** events/spill
        - Trigger rate from TDAQ: approx **1.4k** events/spill
        - XCET44: pressure **0.308** bar, events **128**, gas **CO2**
        - XCET48: pressure **1.004** bar, events **2742**, gas **CO2**
        - Run started: **2026-08-15 17:31:07**
        - Run finished: **2026-08-15 17:52**

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **21.695**
        - DESY table vertical position: **-3.697**

    - **Observation**:  CAL17 IS CENTERED AROUND  **1000** QDC COUNT.
                        The QDC count is slightly lower than the June test beam.

18:33 we have brought these signals (CAL12 & CAL17) into the control through the patch panel to see if there is something wrong with the timing of the signal. It seems they are both in the gate perfectly well. Now there is one remaining possiblity with it which is that they are not aligned well. We And also very interestingly when we are aiming for cal12, cal0 is reading a lot of values. We've decided its time for us to give a break, because this is not making an!y sense to us. 
    
We need the entire monitors to begin with.

And we have checked the cal1 an cal7 and cal18, with the 3 GeV beam, cal7 seems to read quite high value. we will do the alignment of the cal12 again. It didn't seem way too amazing, and we decided to center the circle. The new H: 52.084, V:-13.246. After this the cal7 that is under the cal12 was still reading a lot of values. We will just lower the DESY 1 cm to see the effect. And cal0 is completely crazy at this point. You ca
n see the data at: **1786820108**.
    we are at H: 52.084, V:-14.245 we take it! We've recorded about 30k particles, and it seems a bit higher, however cal7 is still counting a considerable amount. We will lower the desy table another cm, you can check this data at **1786820649**.
    now we are at H:52.084, V:-15.247. Let's start another run. You can see the run at **1786821153**. It seems the lower and the left detectors are still counting. OK the left cal1 is counting, but why the cal7 is still counting!!! I'll go 1 more cm lower. cal0 is still completely crazy.
    one at H:52.084. V:-16.248. Starting another run to see the monitors. It didn't matter much, it can be seen at **1786821668**. We will increase the HV. 
    We've made the HV 1525 V, don't tell it to anybody. It can be seen **1786822004**. It got a bit higher but 

We wanted to check the neighbor values on the previous calibration (june) procedure. 
it seems the cal12 which is the problematic lower counting cal at that point had well centered beam. what we will do now is that we will convert all of our files (august) in to ROOT format (with old DWC calibration values, this should be checked again later on), so that we make sure on our calibration beam is centered enough.
    
meanwhile we will do the calibration of the DWCs. 

This signal is our fake signal for the calibration of the DWCs. 
1 kHz
Pulse 100 mVpp, 0 mV offset
120 ns width, ramp up 10 ns, ramp down 60 ns. 


We've noticed that DWC0 is incredibly noisy. Firstly it is better to do the calibration without HV! secondly 2700 is either to high or the threshold of the discriminator is too low. At 2600 the detector calms down.
Trigger is BUSY & AH0&AV0.
**DWC0 LU**: 1786828413 
**DWC0 C**: 1786828126
**DWC0 RD**: 1786828280
Trigger is BUSY & AH1&AV1. 
**DWC1 LU**: 1786828856
**DWC1 C**: 1786828723
**DWC1 RD**: 1786828590

**Pedastal runs**:
HV ON, Trigger BUSY & AH1&AV1, Fake signal on DWC1 : 1786828994
HV OFF, Trigger BUSY & AH1&AV1, Fake signal on DWC1 : 1786829188

switching to our normal trigger configuration, S0S1. 
Okay Cal0 is measuring this without the HV! 
![](https://codimd.web.cern.ch/uploads/upload_3db4263c59913ff8d6cf61191176aa4d.jpeg)
this is soo unacceptable. I'll try to check some cables.

I've noticed that the cable that goes into the delay unit is a bit loose. but I'd be shocked if it is because of that one. let's turn the beam on, and HV will stay OFF to see if it is still crayay. The run can be seen at **1786829938** cal0 is still completely crazy. On the oscilloscope the the signal that goes into the delay unit didn't seem to cause a problem. let's turn off the beam and see the signal that comes out of the delay unit, otherwise it is the QDC cable that is the problematic one! The run number for this trial is 1786829938. Now we've pushed the QDC adaptor, it didn't feel like it was loose, however let's see the cal0. as disgusting as before. :( run number can be seen at 1786830571. We need to get diabolical and get the other adaptor and measure on channel17. 
:::info  
**\overline{Pedastal runs with the new Ch16 which is where the cal0 is at from now on! this is actually not important that cal0 is at ch16. because ch16 is already also taken, on the previous runs, so they should be taken into care, not these. **:
HV ON, Trigger BUSY & AH1&AV1, Fake signal on DWC1 : x
HV OFF, Trigger BUSY & AH1&AV1, Fake signal on DWC1 : 1786832059}
:::   
    
:::info
now cal0 ch16 seems okay. but we need to repeat the calibration runs for it, we need to move the desy table in that direction. now the H:21.061, V:6.423. 
:::
    
- Run **1786833136** : **-3 GeV BEAM, TRYING TO CALIBRATE CAL0**

    - beamfile: **002**
    - beam momentum: **-3** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **55074**


    - **Initial look**:
        - Event rate from CESAR: approx **5373** events/spill
        - Trigger rate from TDAQ: approx **1800** events/spill
        - XCET44: pressure **0.308** bar, events **313**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **4972**, gas **CO2**
        - Run started: **2026-08-16 00:32:16 **
        - Run finished: **2026-08-16 00:49:02**

    - **Calorimeters and DESY table**: H:21.094 V:16.233
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **H:21.061**
        - DESY table vertical position: **6.423**

    - **Observation**: CAL0 IS CENTERED AROUND  ~2800 QDC COUNT. Seems a bit less but nothing todo.

- Run **1786834513** : **-2 GeV BEAM, TRYING TO CALIBRATE CAL0**

    - beamfile: **001**
    - beam momentum: **-2** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **30588**


    - **Initial look**:
        - Event rate from CESAR: approx **5021** events/spill
        - Trigger rate from TDAQ: approx **1800** events/spill
        - XCET44: pressure **0.308** bar, events **342**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **4850**, gas **CO2**
        - Run started: **2026-08-16 00:55:13 **
        - Run finished: **2026-08-16 01:03:30**

    - **Calorimeters and DESY table**:
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **H:21.061**
        - DESY table vertical position: **6.423**

    - **Observation**: CAL0 IS CENTERED AROUND  ~1900 QDC COUNT. Seems a bit less but nothing todo.
    

- Run **1786835122** : **-1 GeV BEAM, TRYING TO CALIBRATE CAL0**

    - beamfile: **000**
    - beam momentum: **-1** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **48433**


    - **Initial look**:
        - Event rate from CESAR: approx **2921** events/spill
        - Trigger rate from TDAQ: approx **1400** events/spill
        - XCET44: pressure **0.308** bar, events **207**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **2872**, gas **CO2**
        - Run started: **2026-08-16 01:05:22 **
        - Run finished: **2026-08-16 01:22:36**

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **H:21.061**
        - DESY table vertical position: **6.423**

    - **Observation**: CAL0 IS CENTERED AROUND  ~1000 QDC COUNT. 
:::success
cal0 is finished again. moving on the cal7, changing the desy table position.
:::


- Run **1786836376** : **-1 GeV BEAM, TRYING TO CALIBRATE CAL7**

    - beamfile: **000**
    - beam momentum: **-1** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **41229**


    - **Initial look**:
        - Event rate from CESAR: approx **2921** events/spill
        - Trigger rate from TDAQ: approx **1400** events/spill
        - XCET44: pressure **0.308** bar, events **207**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **2872**, gas **CO2**
        - Run started: **2026-08-16 01:05:22 **
        - Run finished: **2026-08-16  01:41:22**

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **H:51.773**
        - DESY table vertical position: **-3.436**

    - **Observation**: CAL7 IS CENTERED AROUND  ~1100 QDC COUNT. 

- Run **1786837396** : **-2 GeV BEAM, TRYING TO CALIBRATE CAL7**

    - beamfile: **001**
    - beam momentum: **-2** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **50k**


    - **Initial look**:
        - Event rate from CESAR: approx **5021** events/spill
        - Trigger rate from TDAQ: approx **1800** events/spill
        - XCET44: pressure **0.308** bar, events **342**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **4850**, gas **CO2**
        - Run started: **2026-08-16 00:55:13 **
        - Run finished: **2026-08-16 01:57:08**

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **H:51.773**
        - DESY table vertical position: **-3.436**

    - **Observation**: CAL7 IS CENTERED AROUND  ~2100 QDC COUNT. 

- Run **1786838309** : **-3 GeV BEAM, TRYING TO CALIBRATE CAL7**

    - beamfile: **002**
    - beam momentum: **-3** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **56611**


    - **Initial look**:
        - Event rate from CESAR: approx **5373** events/spill
        - Trigger rate from TDAQ: approx **1800** events/spill
        - XCET44: pressure **0.308** bar, events **313**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **4972**, gas **CO2**
        - Run started: **2026-08-16 01:58:29 **
        - Run finished: **2026-08-16 02:13:47**

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **H:51.773**
        - DESY table vertical position: **-3.436**

    - **Observation**: CAL7 IS CENTERED AROUND  ~3000 QDC COUNT. 

:::success
cal7 is also finished, moving onto cal18. moved the desy table to H:41.755, V:-3.388.
:::

- Run **1786839384** : **-3 GeV BEAM, TRYING TO CALIBRATE CAL18**

    - beamfile: **002**
    - beam momentum: **-3** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **50965**


    - **Initial look**:
        - Event rate from CESAR: approx **5373** events/spill
        - Trigger rate from TDAQ: approx **1800** events/spill
        - XCET44: pressure **0.308** bar, events **313**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **4972**, gas **CO2**
        - Run started: **2026-08-16 02:16:24 **
        - Run finished: **2026-08-16 02:30:01**

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **H:41.755**
        - DESY table vertical position: **V:-3.388**

    - **Observation**: CAL18 IS CENTERED AROUND  ~2800 QDC COUNT. 

- Run **1786840283** : **-2 GeV BEAM, TRYING TO CALIBRATE CAL18**

    - beamfile: **001**
    - beam momentum: **-2** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **1.8m**


    - **Initial look**:
        - Event rate from CESAR: approx **5073** events/spill
        - Trigger rate from TDAQ: approx **1800** events/spill
        - XCET44: pressure **0.308** bar, events **377**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **4902**, gas **CO2**
        - Run started: **2026-08-16 02:31:23 **
        - Run finished: **2026-08-16 09:12**

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **H:41.755**
        - DESY table vertical position: **V:-3.388**

    - **Observation**: CAL18 IS CENTERED AROUND  ~2000 QDC COUNT. 
    
    

## 2026.08.14

Continuation from last night...

- Run **1786662364** : **-2 GeV BEAM, TRYING TO CALIBRATE CAL4**

    - beamfile: **001**
    - beam momentum: **-2** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **1.86m**


    - **Initial look**:
        - Event rate from CESAR: approx **** events/spill
        - Trigger rate from TDAQ: approx **1700** events/spill
        - XCET44: pressure **??** bar, events **?**, gas **CO2**
        - XCET48: pressure **1** bar, events **5159**, gas **CO2**
        - Run started: **2026-08-14 01:06:04**
        - Run finished: **2026-08-14 09:29:13**

    - **Calorimeters and DESY table**:
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **31.472**
        - DESY table vertical position: **-3.696**

    - **Observation**: XCET44 IS MISSING!!! CAL4 IS CENTERED AROUND 1734 QDC COUNT.Here is the SS below to see QDC counts from CAL4:
    
    ![](https://codimd.web.cern.ch/uploads/upload_9a7d77d4554c44e914a692340e4e7cdc.png)
    

    
    ### CALIBRATION RUNS:
    
- Run **1786708920** : **-3 GeV BEAM, TRYING TO CALIBRATE CAL8**

    - beamfile: **002**
    - beam momentum: **-3** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **55074**


    - **Initial look**:
        - Event rate from CESAR: approx **5167** events/spill
        - Trigger rate from TDAQ: approx **1800** events/spill
        - XCET44: pressure **0.308** bar, events **372**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **7235**, gas **CO2**
        - Run started: **2026-08-14 14:02 **
        - Run finished: **2026-08-14 14:33**

    - **Calorimeters and DESY table**: H:21.094 V:16.233
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **21.094**
        - DESY table vertical position: **16.233**

    - **Observation**: XCET44 came back! CAL8 IS CENTERED AROUND  ~2000 QDC COUNT. 
    
:::danger
 Warning: This run is a bit suspicious, we are not fully sure if CESAR has upload the - 3 GeV beam file correctly or if it stuck in 2 GeV run.
:::
    
    
    
    
- Run **1786711761**: **-3 GeV BEAM, TRYING TO CALIBRATE CAL8**

    - beamfile: **002**
    - beam momentum: **-3** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **51008**


    - **Initial look**:
        - Event rate from CESAR: approx **5355** events/spill
        - Trigger rate from TDAQ: approx **1800** events/spill
        - XCET44: pressure **0.308** bar, events **376**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **7566**, gas **CO2**
        - Run started: **2026-08-14 14:49**
        - Run finished: **2026-08-14 15:08**

    - **Calorimeters and DESY table**: H:21.094 V:16.233
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **21.094**
        - DESY table vertical position: **16.233**

    - **Observation**: CAL8 IS CENTERED AROUND  ~2600 QDC COUNT.
    
    
- Run **1786713224** : **-2 GeV** BEAM, TRYING TO CALIBRATE CAL8**

    - beamfile: **001**
    - beam momentum: **-2** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **51913**


    - **Initial look**:
        - Event rate from CESAR: approx **~5k** events/spill
        - Trigger rate from TDAQ: approx **1600** events/spill
        - XCET44: pressure **0.308** bar, events **349**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **7210**, gas **CO2**
        - Run started: **2026-08-14 15:13**
        - Run finished: **2026-08-14 15:32**

    - **Calorimeters and DESY table**: H:21.094 V:16.233
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **21.094**
        - DESY table vertical position: **16.233**

    - **Observation**:  CAL8 IS CENTERED AROUND  1681 QDC COUNT.
    
        
- Run **1786714515** : **-1 GeV BEAM, TRYING TO CALIBRATE CAL8**

    - beamfile: **000**
    - beam momentum: **-1** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **54535**


    - **Initial look**:
        - Event rate from CESAR: approx **2835** events/spill
        - Trigger rate from TDAQ: approx **1200** events/spill
        - XCET44: pressure **0.308** bar, events **128**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **2786**, gas **CO2**
        - Run started: **2026-08-14 15:35**
        - Run finished: **2026-08-14 15:57**

    - **Calorimeters and DESY table**: H:21.094 V:16.233
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **21.094**
        - DESY table vertical position: **16.233**

    - **Observation**:  CAL8 IS CENTERED AROUND  **** QDC COUNT.
    
    
:::success
CAL8 is finished    
:::
    
- Run **1786723178** : **-1 GeV BEAM, TRYING TO CALIBRATE CAL19**

    - beamfile: **000**
    - beam momentum: **-1** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **46714**


    - **Initial look**:
        - Event rate from CESAR: approx **2846** events/spill
        - Trigger rate from TDAQ: approx **1400** events/spill
        - XCET44: pressure **0.308** bar, events **289**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **5507**, gas **CO2**
        - Run started: **2026-08-14 17:59**
        - Run finished: **2026-08-14 18:23:09**

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **31.501**
        - DESY table vertical position: **15.943**

    - **Observation**:  CAL19 IS CENTERED AROUND  **800** QDC COUNT.
    
    
- Run **1786724681** : **-2 GeV BEAM, TRYING TO CALIBRATE CAL19**

    - beamfile: **001**
    - beam momentum: **-2** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **49674**


    - **Initial look**:
        - Event rate from CESAR: approx *5011** events/spill
        - Trigger rate from TDAQ: approx **1.8K** events/spill
        - XCET44: pressure **0.308** bar, events **450**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **5243**, gas **CO2**
        - Run started: **2026-08-14 18:24**
        - Run finished: **2026-08-14  18:36:15*

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **31.501**
        - DESY table vertical position: **15.943**

    - **Observation**:  CAL19 IS CENTERED AROUND  **1200** QDC COUNT.
 
- Run **1786725412** : **-3 GeV BEAM, TRYING TO CALIBRATE CAL19**

    - beamfile: **002**
    - beam momentum: **-3** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **47546**


    - **Initial look**:
        - Event rate from CESAR: approx *5841** events/spill
        - Trigger rate from TDAQ: approx **1.8K** events/spill
        - XCET44: pressure **0.308** bar, events **327**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **5409**, gas **CO2**
        - Run started: **2026-08-14 18:36**
        - Run finished: **2026-08-14  18:47*

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **31.501**
        - DESY table vertical position: **15.943**

    - **Observation**:  CAL19 IS CENTERED AROUND  **1700** QDC COUNT.


:::success
CAL19 is finished    
:::
    
     
- Run **1786726168** : **-3 GeV BEAM, TRYING TO CALIBRATE CAL9**

    - beamfile: **002**
    - beam momentum: **-3** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **~600000**


    - **Initial look**:
        - Event rate from CESAR: approx *5841** events/spill
        - Trigger rate from TDAQ: approx **1.8K** events/spill
        - XCET44: pressure **0.308** bar, events **327**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **5409**, gas **CO2**
        - Run started: **2026-08-14 18:49**
        - Run finished: **2026-08-14  22:34:57*

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **41.551**
        - DESY table vertical position: **15.943**

    - **Observation**:  CAL9 IS CENTERED AROUND  **3500** QDC COUNT.

- Run **1786739830** : **-2 GeV BEAM, TRYING TO CALIBRATE CAL9**

    - beamfile: **001**
    - beam momentum: **-2** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **92689**


    - **Initial look**:
        - Event rate from CESAR: approx *5211** events/spill
        - Trigger rate from TDAQ: approx **1.8K** events/spill
        - XCET44: pressure **0.308** bar, events **311**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **5034**, gas **CO2**
        - Run started: **2026-08-14 22:37:10**
        - Run finished: **2026-08-14 23:10:49**

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **41.551**
        - DESY table vertical position: **15.943**

    - **Observation**:  CAL9 IS CENTERED AROUND  **2300** QDC COUNT.
    
- Run **1786741940** : **-1 GeV BEAM, TRYING TO CALIBRATE CAL9**

    - beamfile: **000**
    - beam momentum: **-1** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **51918**


    - **Initial look**:
        - Event rate from CESAR: approx **~3k** events/spill
        - Trigger rate from TDAQ: approx **1.3k** events/spill
        - XCET44: pressure **0.308** bar, events **~280**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **~2890**, gas **CO2**
        - Run started: **2026-08-14 23:12:20**
        - Run finished: **2026-08-14 23:28:49**

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **41.551**
        - DESY table vertical position: **15.943**

    - **Observation**:  CAL9 IS CENTERED AROUND  **1200** QDC COUNT.
:::success
CAL9 is finished    
:::

- Run **1786743090** : **-1 GeV BEAM, TRYING TO CALIBRATE CAL13**

    - beamfile: **000**
    - beam momentum: **-1** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **50587**


    - **Initial look**:
        - Event rate from CESAR: approx **~3k** events/spill
        - Trigger rate from TDAQ: approx **1.3k** events/spill
        - XCET44: pressure **0.308** bar, events **~300**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **~3k**, gas **CO2**
        - Run started: **2026-08-14 23:31:30**
        - Run finished: **2026-08-14 23:45:25**

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **51.414**
        - DESY table vertical position: **15.768**

    - **Observation**:  CAL13 IS CENTERED AROUND  **900** QDC COUNT.
    
- Run **1786744038** : **-2 GeV BEAM, TRYING TO CALIBRATE CAL13**

    - beamfile: **001**
    - beam momentum: **-2** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **50373**


    - **Initial look**:
        - Event rate from CESAR: approx *5K** events/spill
        - Trigger rate from TDAQ: approx **1.8K** events/spill
        - XCET44: pressure **0.308** bar, events **~300**, gas **CO2**
        - XCET48: pressure **1.005** bar, events **~5000**, gas **CO2**
        - Run started: **2026-08-14 23:47:18**
        - Run finished: **2026-08-14 23:58:23**

    - **Calorimeters and DESY table**: 
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **51.414**
        - DESY table vertical position: **15.768**

    - **Observation**:  CAL13 IS CENTERED AROUND  **1600** QDC COUNT.



## 2026.08.13
    
As discussed we will first bring the evttrg and central 4 calorimeters to the zone. Central 4 calorimeters are 2 4 14 18. EVTTRG is at B01, CAL2 is at B02, cal4 is at b03 cal14 is at b04 and cal18 is at b05. to all the distances that they go into their modules, we have added 8 ns for everything and 13 ns for the cal18 because its unit is far away. 
    
Okay, to here we are showing how much each of them is away from the trigger (EVTTRG is yellow, cal signal is blue).
CAL2<img src="https://codimd.web.cern.ch/uploads/upload_5edc0b5b0109158e177864cf7385f1e9.jpeg" width="300">
CAL4<img src="https://codimd.web.cern.ch/uploads/upload_8b3ef39601a453280cf9012b7b011388.jpeg" width="300">

CAL14<img src="https://codimd.web.cern.ch/uploads/upload_40f267583d2412530782245787c32969.jpeg" width="300">
CAL18<img src="https://codimd.web.cern.ch/uploads/upload_01d3e702caa3a5a76b938f45d5e90151.jpeg" width="300">

As it can be seen in here, some of them are 80ns away after the brown and aditional 16 ns cables, some of them are more like 40 ns away. What we have decided on is that we are going to add 10 ns or 16 ns cables (we have 8 left of each) and apply 66 ns of delay unit's delay on top of this. but, as we are scared group of people, we will also make EVTTRG width to 120ns.

Here is how much ns is added to each of the calorimeters.
| Cal | Delay (ns) |
|---|---:|
| Cal0 | 10 |
| Cal1 | 16 |
| Cal2 | 16 |
| Cal4 | 16 |
| Cal5 | 16 |
| Cal7 | 10 |
| Cal8 | 16 |
| Cal9 | 16 |
| Cal10 | 10 |
| Cal11 | 16 |
| Cal12 | 10 |
| Cal13 | 10 |
| Cal14 | 16 |
| Cal17 | 10 |
| Cal18 | 10 |
| Cal19 | 10 |

    
And then we have worked on the alignment of the laser lines to the Cal4. The DESY table values at this point is: H:31.472, V:-3.696. 
<img src="https://codimd.web.cern.ch/uploads/upload_f412b86299ba34597dcea117adae8fce.jpeg" width="300">
<img src="https://codimd.web.cern.ch/uploads/upload_9be22a276d49b56ad7ad301d1b97b080.jpeg" width="300">
<img src="https://codimd.web.cern.ch/uploads/upload_210dd350b7e41664a7cf4cc22933f8a2.jpeg" width="300">
<img src="https://codimd.web.cern.ch/uploads/upload_c9886bf94608316ab9913480f614a7f8.jpeg" width="300">
<img src="https://codimd.web.cern.ch/uploads/upload_ecd11692c60c7ae268f6d62b751d2e22.jpeg" width="300">

We have also tried to align the DWCs and the DWC1 is aligned well, DWC0 is not so much, pictures are attached. 
<img src="https://codimd.web.cern.ch/uploads/upload_53fa23ce762946736cfa06231291e974.jpeg" width="300">
<img src="https://codimd.web.cern.ch/uploads/upload_75a6fbdb31bbed63a24a344f17711701.jpeg" width="300">
<img src="https://codimd.web.cern.ch/uploads/upload_d4bd2e3149143b32c5dddc880a6dcd4f.jpeg" width="300">
and the XSCA table values at this points are V:3.96, H:0.80.

In principle, we are ready to turn on the detectors and start data taking. We leave the DWC calibration to tomorrow (we are tired, shocking we know), but we want to do the Cal4 calibration, and for this we will do with our previous HV values, because it seems the values that has been tested in the lab are too small.

    
:::info

  ### HV STATUS UPDATE:
![](https://codimd.web.cern.ch/uploads/upload_138e969bc1beedadf3f1e73f2f3d61a8.png)

 :::   
    
:::success
our first run is here
:::
 - Run **1786657998** : **-1 GeV BEAM, TRYING TO CALIBRATE CAL4**

    - beamfile: **000**
    - beam momentum: **-1** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **63343**


    - **Initial look**:
        - Event rate from CESAR: approx **3006** events/spill
        - Trigger rate from TDAQ: approx **1400** events/spill
        - XCET44: pressure **<value>** bar, events **<value>**, gas **<gas>**
        - XCET48: pressure **0.3** bar, events **1180**, gas **CO2**
        - Run started: **2026-08-13 23:53:18**
        - Run finished: **2026-08-14 00:18:21**

    - **Calorimeters and DESY table**:
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **31.472**
        - DESY table vertical position: **-3.696**

    - **Observation**: XCET44 IS MISSING!!! CAL4 IS CENTERED AROUND 1100 QDC COUNT. It is interesting but on our scaler we can read out C0. We have increased the pressure on C1 to see how much of the beam is electron to 1 bar, it seems super high purity. we have recorded another file with all the same conditions but with 1 bar C0, beam file number 1786660465. 
    
 - Run **1786660965** : **-3 GeV BEAM, TRYING TO CALIBRATE CAL4**

    - beamfile: **002**
    - beam momentum: **-3** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **74323**


    - **Initial look**:
        - Event rate from CESAR: approx **5556** events/spill
        - Trigger rate from TDAQ: approx **1800** events/spill
        - XCET44: pressure **<value>** bar, events **<value>**, gas **<gas>**
        - XCET48: pressure **1** bar, events **5159**, gas **CO2**
        - Run started: **2026-08-14 00:42:45**
        - Run finished: **2026-08-14 01:02:52**

    - **Calorimeters and DESY table**:
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **31.472**
        - DESY table vertical position: **-3.696**

    - **Observation**: XCET44 IS MISSING!!! CAL4 IS CENTERED AROUND 3300 QDC COUNT. 

     - Run **1786662364** : **-2 GeV BEAM, TRYING TO CALIBRATE CAL4**

    - beamfile: **001**
    - beam momentum: **-2** GeV
    - Trigger Condition: **S0S1**
    - Number of events: **1.86m**


    - **Initial look**:
        - Event rate from CESAR: approx **** events/spill
        - Trigger rate from TDAQ: approx **1700** events/spill
        - XCET44: pressure **??** bar, events **?**, gas **CO2**
        - XCET48: pressure **1** bar, events **5159**, gas **CO2**
        - Run started: **2026-08-14 01:06:04**
        - Run finished: **2026-08-14 09:29:13**

    - **Calorimeters and DESY table**:
        - calorimeter gap: **NO GAP**
        - DESY table horizontal position: **31.472**
        - DESY table vertical position: **-3.696**

    - **Observation**: XCET44 IS MISSING!!! CAL4 IS CENTERED AROUND 1734 QDC COUNT.Here is the SS below to see QDC counts from CAL4:
    
    ![](https://codimd.web.cern.ch/uploads/upload_9a7d77d4554c44e914a692340e4e7cdc.png)

    
## 2026.08.12
18:38, we have finished installing all the detectors, cabling is not completely finished, safety check is done, and our dear beamline physicist Dipanwita will soon create our beam files, and we will start turning on our detectors on by one. 
18:58 she has started.

19:25 Dipanwita is finished.
    
Afterwards we have done so much cabling, we did the calorimeters, DWCs, NIMs VMEs, and our NIM wiring cable and the VME layout is finalized, it can be seen from above.
    
AND THEN WE'VE HAD OUR FIRST TRIGGER WITH S0S1 with e-beam!!! We didn't save the file because there is no HV. We cannot see the IP of HV source. 

    
:warning:To get information of Main Frame IP ping the name of the device, for example ping POOL04310028. 

We have made planning for tomorrow: firstly we will join our students' meetings, and then we will come back to the zone, first Berare will bring the signals to the zone (four central calorimeters) and the event trigger, and we will measure how far apart, and Seyma will do her presentation. And then Berare will do her presentation, Seyma will find out the central points of the calorimeters. 
    
## 2026.08.11
    
Madeleine has measured the delay of each unit for us

![](https://codimd.web.cern.ch/uploads/upload_d7ab5811e4beb2ed8ae2cdfb7e57a0b2.jpeg)
    


We have setup CAENGECO to bl4sdaq7, it automatically starts working when you should say caengeco2020 (it is part of the path). We are making the connection between bl4sdaq7, and sbc-isotdaq-5. 

We are setting up the system on the opt mode.
