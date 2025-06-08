# DBC Documentation

## Index

| Message Name | ID (Dec) | ID (Hex) | Notes |
|--------------|---------|----------|-------|
| [ResGO](#resgo) | 32 | 0x20 |  |
| [EbsStatus](#ebsstatus) | 60 | 0x3C |  |
| [CarMission](#carmission) | 71 | 0x47 |  |
| [PcuFault](#pcufault) | 81 | 0x51 |  |
| [Paddle](#paddle) | 82 | 0x52 |  |
| [Driver](#driver) | 83 | 0x53 |  |
| [BmsLv1](#bmslv1) | 84 | 0x54 |  |
| [BmsLv2](#bmslv2) | 85 | 0x55 |  |
| [BmsHv1](#bmshv1) | 87 | 0x57 |  |
| [BmsHv2](#bmshv2) | 88 | 0x58 |  |
| [Imu1](#imu1) | 96 | 0x60 |  |
| [Imu2](#imu2) | 97 | 0x61 |  |
| [Imu3](#imu3) | 98 | 0x62 |  |
| [IMUCalib](#imucalib) | 99 | 0x63 | RESERVER FOR IMU mask - DO NOT USE |
| [Map](#map) | 100 | 0x64 |  |
| [CarStatus](#carstatus) | 101 | 0x65 |  |
| [CarSettings](#carsettings) | 102 | 0x66 |  |
| [CheckASBReq](#checkasbreq) | 104 | 0x68 |  |
| [EbsBrakeReq](#ebsbrakereq) | 105 | 0x69 |  |
| [ResStatus](#resstatus) | 106 | 0x6A |  |
| [LapStart](#lapstart) | 112 | 0x70 |  |
| [CarMissionStatus](#carmissionstatus) | 113 | 0x71 |  |
| [Temp1](#temp1) | 256 | 0x100 |  |
| [Temp2](#temp2) | 257 | 0x101 |  |
| [SuspRear](#susprear) | 258 | 0x102 |  |
| [RESERVED2](#reserved2) | 259 | 0x103 | RESERVER FOR SMU mask - DO NOT USE |
| [SuspFront](#suspfront) | 260 | 0x104 |  |
| [TempFrontR](#tempfrontr) | 261 | 0x105 |  |
| [PressBrake](#pressbrake) | 264 | 0x108 | Hydraulic Brakes Pressures |
| [InvVolt](#invvolt) | 288 | 0x120 |  |
| [Pcu](#pcu) | 304 | 0x130 |  |
| [Calib](#calib) | 305 | 0x131 |  |
| [CalibAck](#caliback) | 306 | 0x132 |  |
| [PcuSwControl](#pcuswcontrol) | 307 | 0x133 |  |
| [PcuRfAck](#pcurfack) | 308 | 0x134 |  |
| [EmbeddedAliveCheck](#embeddedalivecheck) | 310 | 0x136 |  |
| [Lem](#lem) | 962 | 0x3C2 |  |


#### ResGO

| ID (Dec) | ID (Hex) | DLC |
|----------|----------|-----|
| 32 | 0x20 | 1 |

| Signal Name | Start Bit | Length | Byte Order | Value Type | Factor | Offset | Min | Max | Unit | Receiver |
|-------------|-----------|--------|------------|------------|--------|--------|-----|-----|------|----------|
| go_signal | 0 | 1 | little_endian | False | 1 | 0 | 0 | 1 | None |  |


#### EbsStatus

| ID (Dec) | ID (Hex) | DLC |
|----------|----------|-----|
| 60 | 0x3C | 2 |

| Signal Name | Start Bit | Length | Byte Order | Value Type | Factor | Offset | Min | Max | Unit | Receiver |
|-------------|-----------|--------|------------|------------|--------|--------|-----|-----|------|----------|
| system_check | 0 | 1 | little_endian | False | 1 | 0 | 0 | 1 | None |  |
| press_left_tank | 1 | 5 | little_endian | False | 0.25 | 6 | 6 | 10 | Bar |  |
| press_right_tank | 6 | 5 | little_endian | False | 0.25 | 6 | 6 | 10 | Bar |  |
| sanity_left_sensor | 11 | 1 | little_endian | False | 1 | 0 | 0 | 1 | None |  |
| sanity_right_sensor | 12 | 1 | little_endian | False | 1 | 0 | 0 | 1 | None |  |
| ASB_check | 13 | 1 | little_endian | False | 1 | 0 | 0 | 1 | None |  |
| brakes_engaged | 14 | 1 | little_endian | False | 1 | 0 | 0 | 1 | None |  |


#### CarMission

| ID (Dec) | ID (Hex) | DLC |
|----------|----------|-----|
| 71 | 0x47 | 1 |

| Signal Name | Start Bit | Length | Byte Order | Value Type | Factor | Offset | Min | Max | Unit | Receiver |
|-------------|-----------|--------|------------|------------|--------|--------|-----|-----|------|----------|
| Mission | 0 | 3 | little_endian | False | 1 | 0 | 0 | 7 | None | VCU |

**Enumerations:**

- **Mission**:
  - 7: dv_inspection
  - 6: dv_ebs_test
  - 5: dv_trackdrive
  - 4: dv_autocross
  - 3: dv_skidpad
  - 2: dv_acceleration
  - 1: manualy
  - 0: none


#### PcuFault

| ID (Dec) | ID (Hex) | DLC |
|----------|----------|-----|
| 81 | 0x51 | 1 |

| Signal Name | Start Bit | Length | Byte Order | Value Type | Factor | Offset | Min | Max | Unit | Receiver |
|-------------|-----------|--------|------------|------------|--------|--------|-----|-----|------|----------|
| fault_12v | 0 | 1 | little_endian | False | 1 | 0 | 0 | 1 | on |  |
| fault_dv | 1 | 1 | little_endian | False | 1 | 0 | 0 | 1 | on |  |
| fault_24v | 2 | 1 | little_endian | False | 1 | 0 | 0 | 1 | on |  |
| fault_pumpl | 3 | 1 | little_endian | False | 1 | 0 | 0 | 1 | on |  |
| fault_pumpr | 4 | 1 | little_endian | False | 1 | 0 | 0 | 1 | on |  |
| fault_fanbattr | 5 | 1 | little_endian | False | 1 | 0 | 0 | 1 | on |  |
| fault_fanbattl | 6 | 1 | little_endian | False | 1 | 0 | 0 | 1 | on |  |


#### Paddle

| ID (Dec) | ID (Hex) | DLC |
|----------|----------|-----|
| 82 | 0x52 | 1 |

| Signal Name | Start Bit | Length | Byte Order | Value Type | Factor | Offset | Min | Max | Unit | Receiver |
|-------------|-----------|--------|------------|------------|--------|--------|-----|-----|------|----------|
| regen | 0 | 8 | little_endian | False | 1 | 0 | 0 | 100 | % | VCU |


#### Driver

| ID (Dec) | ID (Hex) | DLC |
|----------|----------|-----|
| 83 | 0x53 | 4 |

| Signal Name | Start Bit | Length | Byte Order | Value Type | Factor | Offset | Min | Max | Unit | Receiver |
|-------------|-----------|--------|------------|------------|--------|--------|-----|-----|------|----------|
| throttle | 0 | 8 | little_endian | False | 1 | 0 | 0 | 100 | % | VCU, SW |
| brake | 8 | 8 | little_endian | False | 1 | 0 | 0 | 100 | % | VCU, SW |
| steering | 16 | 12 | little_endian | True | 1 | 0 | -120 | 120 | deg | VCU, SW |
| no_implausibility | 28 | 1 | little_endian | False | 1 | 0 | None | None | None |  |
| bre_implausibility | 29 | 1 | little_endian | False | 1 | 0 | None | None | None |  |
| pad_implausibility | 30 | 1 | little_endian | False | 1 | 0 | None | None | None |  |
| pot_implausibility | 31 | 1 | little_endian | False | 1 | 0 | None | None | None |  |


#### BmsLv1

| ID (Dec) | ID (Hex) | DLC |
|----------|----------|-----|
| 84 | 0x54 | 7 |

| Signal Name | Start Bit | Length | Byte Order | Value Type | Factor | Offset | Min | Max | Unit | Receiver |
|-------------|-----------|--------|------------|------------|--------|--------|-----|-----|------|----------|
| max_volt | 0 | 16 | little_endian | False | 0.1 | 0 | None | None | mV | VCU, SW |
| min_volt | 16 | 16 | little_endian | False | 0.1 | 0 | None | None | mV | VCU, SW |
| avg_volt | 32 | 16 | little_endian | False | 0.1 | 0 | None | None | mV | VCU, SW |
| soc | 48 | 8 | little_endian | False | 1 | 0 | 0 | 100 | % | VCU, SW |


#### BmsLv2

| ID (Dec) | ID (Hex) | DLC |
|----------|----------|-----|
| 85 | 0x55 | 7 |

| Signal Name | Start Bit | Length | Byte Order | Value Type | Factor | Offset | Min | Max | Unit | Receiver |
|-------------|-----------|--------|------------|------------|--------|--------|-----|-----|------|----------|
| max_temp | 0 | 16 | little_endian | False | 1 | 0 | None | None | C | VCU, SW |
| min_temp | 16 | 16 | little_endian | False | 1 | 0 | None | None | C | VCU, SW |
| avg_temp | 32 | 16 | little_endian | False | 1 | 0 | None | None | C | VCU, SW |
| fan_speed | 48 | 8 | little_endian | False | 1 | 0 | 0 | 100 | % | VCU, SW |


#### BmsHv1

| ID (Dec) | ID (Hex) | DLC |
|----------|----------|-----|
| 87 | 0x57 | 7 |

| Signal Name | Start Bit | Length | Byte Order | Value Type | Factor | Offset | Min | Max | Unit | Receiver |
|-------------|-----------|--------|------------|------------|--------|--------|-----|-----|------|----------|
| max_volt | 0 | 16 | little_endian | False | 0.1 | 0 | None | None | mV | VCU, SW |
| min_volt | 16 | 16 | little_endian | False | 0.1 | 0 | None | None | mV | VCU, SW |
| avg_volt | 32 | 16 | little_endian | False | 0.1 | 0 | None | None | mV | VCU, SW |
| soc | 48 | 8 | little_endian | False | 1 | 0 | 0 | 100 | % | VCU, SW |


#### BmsHv2

| ID (Dec) | ID (Hex) | DLC |
|----------|----------|-----|
| 88 | 0x58 | 7 |

| Signal Name | Start Bit | Length | Byte Order | Value Type | Factor | Offset | Min | Max | Unit | Receiver |
|-------------|-----------|--------|------------|------------|--------|--------|-----|-----|------|----------|
| max_temp | 0 | 16 | little_endian | False | 1 | 0 | None | None | C | VCU, SW |
| min_temp | 16 | 16 | little_endian | False | 1 | 0 | None | None | C | VCU, SW |
| avg_temp | 32 | 16 | little_endian | False | 1 | 0 | None | None | C | VCU, SW |
| fan_speed | 48 | 8 | little_endian | False | 1 | 0 | 0 | 100 | % | VCU, SW |


#### Imu1

| ID (Dec) | ID (Hex) | DLC |
|----------|----------|-----|
| 96 | 0x60 | 8 |

| Signal Name | Start Bit | Length | Byte Order | Value Type | Factor | Offset | Min | Max | Unit | Receiver |
|-------------|-----------|--------|------------|------------|--------|--------|-----|-----|------|----------|
| acc_x | 0 | 32 | little_endian | True | 1 | 0 | None | None | m/s^2 | VCU |
| acc_y | 32 | 32 | little_endian | True | 1 | 0 | None | None | m/s^2 | VCU |


#### Imu2

| ID (Dec) | ID (Hex) | DLC |
|----------|----------|-----|
| 97 | 0x61 | 8 |

| Signal Name | Start Bit | Length | Byte Order | Value Type | Factor | Offset | Min | Max | Unit | Receiver |
|-------------|-----------|--------|------------|------------|--------|--------|-----|-----|------|----------|
| acc_z | 0 | 32 | little_endian | True | 1 | 0 | None | None | m/s^2 | VCU |
| omega_x | 32 | 32 | little_endian | True | 1 | 0 | None | None | rad/s | VCU |


#### Imu3

| ID (Dec) | ID (Hex) | DLC |
|----------|----------|-----|
| 98 | 0x62 | 8 |

| Signal Name | Start Bit | Length | Byte Order | Value Type | Factor | Offset | Min | Max | Unit | Receiver |
|-------------|-----------|--------|------------|------------|--------|--------|-----|-----|------|----------|
| omega_y | 0 | 32 | little_endian | True | 1 | 0 | None | None | rad/s | VCU |
| omega_z | 32 | 32 | little_endian | True | 1 | 0 | None | None | rad/s | VCU |


#### IMUCalib

| ID (Dec) | ID (Hex) | DLC |
|----------|----------|-----|
| 99 | 0x63 | 1 |

**Comment:** RESERVER FOR IMU mask - DO NOT USE

| Signal Name | Start Bit | Length | Byte Order | Value Type | Factor | Offset | Min | Max | Unit | Receiver |
|-------------|-----------|--------|------------|------------|--------|--------|-----|-----|------|----------|
| start_imu_calibration | 0 | 1 | little_endian | False | 1 | 0 | None | None | None |  |


#### Map

| ID (Dec) | ID (Hex) | DLC |
|----------|----------|-----|
| 100 | 0x64 | 2 |

| Signal Name | Start Bit | Length | Byte Order | Value Type | Factor | Offset | Min | Max | Unit | Receiver |
|-------------|-----------|--------|------------|------------|--------|--------|-----|-----|------|----------|
| power | 0 | 4 | little_endian | False | 1 | 0 | 1 | 12 | map | VCU |
| regen | 4 | 4 | little_endian | False | 1 | 0 | 1 | 12 | map | VCU |
| torque_rep | 8 | 4 | little_endian | False | 1 | 0 | 0 | 12 | map |  |


#### CarStatus

| ID (Dec) | ID (Hex) | DLC |
|----------|----------|-----|
| 101 | 0x65 | 4 |

| Signal Name | Start Bit | Length | Byte Order | Value Type | Factor | Offset | Min | Max | Unit | Receiver |
|-------------|-----------|--------|------------|------------|--------|--------|-----|-----|------|----------|
| HV | 0 | 1 | little_endian | False | 1 | 0 | None | None |  Off/On |  |
| AIR1 | 1 | 1 | little_endian | False | 1 | 0 | None | None |  Closed/Open |  |
| AIR2 | 2 | 1 | little_endian | False | 1 | 0 | None | None |  Closed/Open |  |
| AS_NODE | 3 | 1 | little_endian | False | 1 | 0 | None | None |  Open/Closed |  |
| rtd_req | 4 | 1 | little_endian | False | 1 | 0 | None | None |  Open/Closed |  |
| RunningStatus | 5 | 2 | little_endian | False | 1 | 0 | 0 | 3 |  Phase |  |
| speed | 7 | 8 | little_endian | False | 1 | 0 | None | None |  km/h |  |
| brake_front_press | 15 | 8 | little_endian | False | 0.25 | 0 | 0 | 60 | Bar |  |
| brake_rear_press | 23 | 8 | little_endian | False | 0.25 | 0 | 0 | 60 | Bar |  |

**Enumerations:**

- **RunningStatus**:
  - 3: Running
  - 2: Ts Ready
  - 1: Precharge started
  - 0: System off


#### CarSettings

| ID (Dec) | ID (Hex) | DLC |
|----------|----------|-----|
| 102 | 0x66 | 8 |

| Signal Name | Start Bit | Length | Byte Order | Value Type | Factor | Offset | Min | Max | Unit | Receiver |
|-------------|-----------|--------|------------|------------|--------|--------|-----|-----|------|----------|
| max_regen_current | 0 | 8 | little_endian | False | 1 | 0 | 0 | 150 | A |  |
| pwr_limit | 8 | 8 | little_endian | False | 1 | 0 | 0 | 80 | kW |  |
| speed_lim | 16 | 8 | little_endian | False | 1 | 0 | None | None | krpm |  |
| max_pos_trq | 24 | 8 | little_endian | False | 1 | 0 | None | None | Nm |  |
| max_neg_trq | 32 | 8 | little_endian | True | 1 | 0 | None | None | Nm |  |
| front_motor_repartition | 40 | 8 | little_endian | False | 1 | 0 | None | None | % |  |
| rear_motor_repartition | 48 | 8 | little_endian | False | 1 | 0 | None | None | % |  |
| torque_vectoring | 56 | 1 | little_endian | False | 1 | 0 | 0 | 1 | on |  |


#### CheckASBReq

| ID (Dec) | ID (Hex) | DLC |
|----------|----------|-----|
| 104 | 0x68 | 1 |

| Signal Name | Start Bit | Length | Byte Order | Value Type | Factor | Offset | Min | Max | Unit | Receiver |
|-------------|-----------|--------|------------|------------|--------|--------|-----|-----|------|----------|
| req | 0 | 1 | little_endian | False | 1 | 0 | 0 | 1 | None |  |
| reqAck | 1 | 1 | little_endian | False | 1 | 0 | 0 | 1 | None |  |


#### EbsBrakeReq

| ID (Dec) | ID (Hex) | DLC |
|----------|----------|-----|
| 105 | 0x69 | 1 |

| Signal Name | Start Bit | Length | Byte Order | Value Type | Factor | Offset | Min | Max | Unit | Receiver |
|-------------|-----------|--------|------------|------------|--------|--------|-----|-----|------|----------|
| req | 0 | 1 | little_endian | False | 1 | 0 | 0 | 2 | None |  |


#### ResStatus

| ID (Dec) | ID (Hex) | DLC |
|----------|----------|-----|
| 106 | 0x6A | 1 |

| Signal Name | Start Bit | Length | Byte Order | Value Type | Factor | Offset | Min | Max | Unit | Receiver |
|-------------|-----------|--------|------------|------------|--------|--------|-----|-----|------|----------|
| data | 0 | 1 | little_endian | False | 1 | 0 | 0 | 2 | None |  |


#### LapStart

| ID (Dec) | ID (Hex) | DLC |
|----------|----------|-----|
| 112 | 0x70 | 1 |

| Signal Name | Start Bit | Length | Byte Order | Value Type | Factor | Offset | Min | Max | Unit | Receiver |
|-------------|-----------|--------|------------|------------|--------|--------|-----|-----|------|----------|
| start | 0 | 8 | little_endian | False | 1 | 0 | 0 | 1 | start |  |


#### CarMissionStatus

| ID (Dec) | ID (Hex) | DLC |
|----------|----------|-----|
| 113 | 0x71 | 1 |

| Signal Name | Start Bit | Length | Byte Order | Value Type | Factor | Offset | Min | Max | Unit | Receiver |
|-------------|-----------|--------|------------|------------|--------|--------|-----|-----|------|----------|
| Mission | 0 | 3 | little_endian | False | 1 | 0 | 0 | 7 | None | SW |
| MissionStatus | 3 | 2 | little_endian | False | 1 | 0 | 0 | 2 | None | SW |
| AsStatus | 5 | 3 | little_endian | False | 1 | 0 | 0 | 7 | None | SW |

**Enumerations:**

- **Mission**:
  - 7: dv_inspection
  - 6: dv_ebs_test
  - 5: dv_trackdrive
  - 4: dv_autocross
  - 3: dv_skidpad
  - 2: dv_acceleration
  - 1: manualy
  - 0: none
- **MissionStatus**:
  - 2: Mission_finished
  - 1: Mission_running
  - 0: Mission_not_running
- **AsStatus**:
  - 5: finish
  - 4: emergency_brake
  - 3: driving
  - 2: ready
  - 1: off


#### Temp1

| ID (Dec) | ID (Hex) | DLC |
|----------|----------|-----|
| 256 | 0x100 | 8 |

| Signal Name | Start Bit | Length | Byte Order | Value Type | Factor | Offset | Min | Max | Unit | Receiver |
|-------------|-----------|--------|------------|------------|--------|--------|-----|-----|------|----------|
| temp_motor_post_L | 0 | 16 | little_endian | False | 1 | 0 | None | None | C | VCU |
| temp_motor_pre_L | 16 | 16 | little_endian | False | 1 | 0 | None | None | C | VCU |
| temp_motor_pre_R | 32 | 16 | little_endian | False | 1 | 0 | None | None | C | VCU |
| temp_coldplate_pre_R | 48 | 16 | little_endian | False | 1 | 0 | None | None | C | VCU |


#### Temp2

| ID (Dec) | ID (Hex) | DLC |
|----------|----------|-----|
| 257 | 0x101 | 8 |

| Signal Name | Start Bit | Length | Byte Order | Value Type | Factor | Offset | Min | Max | Unit | Receiver |
|-------------|-----------|--------|------------|------------|--------|--------|-----|-----|------|----------|
| temp_cold_pre_L | 0 | 16 | little_endian | False | 1 | 0 | None | None | C | VCU |
| temp_cold_post_R | 16 | 16 | little_endian | False | 1 | 0 | None | None | C | VCU |
| temp_cold_post_L | 32 | 16 | little_endian | False | 1 | 0 | None | None | C | VCU |
| temp_mot_post_R | 48 | 16 | little_endian | False | 1 | 0 | None | None | C | VCU |


#### SuspRear

| ID (Dec) | ID (Hex) | DLC |
|----------|----------|-----|
| 258 | 0x102 | 3 |

| Signal Name | Start Bit | Length | Byte Order | Value Type | Factor | Offset | Min | Max | Unit | Receiver |
|-------------|-----------|--------|------------|------------|--------|--------|-----|-----|------|----------|
| susp_rr | 0 | 12 | little_endian | False | 0.1 | 0 | None | None | mm | VCU |
| susp_rl | 12 | 12 | little_endian | False | 0.1 | 0 | None | None | mm | VCU |


#### RESERVED2

| ID (Dec) | ID (Hex) | DLC |
|----------|----------|-----|
| 259 | 0x103 | 0 |

**Comment:** RESERVER FOR SMU mask - DO NOT USE



#### SuspFront

| ID (Dec) | ID (Hex) | DLC |
|----------|----------|-----|
| 260 | 0x104 | 3 |

| Signal Name | Start Bit | Length | Byte Order | Value Type | Factor | Offset | Min | Max | Unit | Receiver |
|-------------|-----------|--------|------------|------------|--------|--------|-----|-----|------|----------|
| susp_fr | 0 | 12 | little_endian | False | 0.1 | 0 | None | None | mm | VCU |
| susp_fl | 12 | 12 | little_endian | False | 0.1 | 0 | None | None | mm | VCU |


#### TempFrontR

| ID (Dec) | ID (Hex) | DLC |
|----------|----------|-----|
| 261 | 0x105 | 3 |

| Signal Name | Start Bit | Length | Byte Order | Value Type | Factor | Offset | Min | Max | Unit | Receiver |
|-------------|-----------|--------|------------|------------|--------|--------|-----|-----|------|----------|
| temp_mot_pot_FR | 0 | 10 | little_endian | False | 1 | 0 | None | None | C |  |
| temp_mot_pre_FR | 10 | 10 | little_endian | False | 1 | 0 | None | None | C |  |


#### PressBrake

| ID (Dec) | ID (Hex) | DLC |
|----------|----------|-----|
| 264 | 0x108 | 2 |

**Comment:** Hydraulic Brakes Pressures

| Signal Name | Start Bit | Length | Byte Order | Value Type | Factor | Offset | Min | Max | Unit | Receiver |
|-------------|-----------|--------|------------|------------|--------|--------|-----|-----|------|----------|
| press_front | 0 | 8 | little_endian | False | 0.25 | 0 | 0 | 64 | Bar | EBS, VCU |
| press_rear | 8 | 8 | little_endian | False | 0.25 | 0 | 0 | 64 | Bar | EBS, VCU |


#### InvVolt

| ID (Dec) | ID (Hex) | DLC |
|----------|----------|-----|
| 288 | 0x120 | 2 |

| Signal Name | Start Bit | Length | Byte Order | Value Type | Factor | Offset | Min | Max | Unit | Receiver |
|-------------|-----------|--------|------------|------------|--------|--------|-----|-----|------|----------|
| car_voltage | 0 | 16 | little_endian | False | 1 | 0 | 0 | 600 | V | VCU, SW, BMSHV |


#### Pcu

| ID (Dec) | ID (Hex) | DLC |
|----------|----------|-----|
| 304 | 0x130 | 7 |

| Signal Name | Start Bit | Length | Byte Order | Value Type | Factor | Offset | Min | Max | Unit | Receiver |
|-------------|-----------|--------|------------|------------|--------|--------|-----|-----|------|----------|
| mode | 0 | 2 | little_endian | False | 1 | 0 | 0 | 2 | None |  |
| rf | 2 | 1 | little_endian | False | 1 | 0 | 0 | 1 | on |  |
| enable_dv | 2 | 1 | little_endian | False | 1 | 0 | 0 | 1 | on |  |
| enable_embedded | 3 | 1 | little_endian | False | 1 | 0 | 0 | 1 | on |  |
| pump_enable_left | 8 | 1 | little_endian | False | 1 | 0 | 0 | 1 | on |  |
| pump_speed_left | 9 | 7 | little_endian | False | 1 | 0 | 0 | 100 | % |  |
| pump_enable_right | 16 | 1 | little_endian | False | 1 | 0 | 0 | 1 | on |  |
| pump_speed_right | 17 | 7 | little_endian | False | 1 | 0 | 0 | 100 | % |  |
| fanrad_enable_left | 24 | 1 | little_endian | False | 1 | 0 | 0 | 1 | on |  |
| fanrad_speed_left | 25 | 7 | little_endian | False | 1 | 0 | 0 | 100 | % |  |
| fanrad_enable_right | 32 | 1 | little_endian | False | 1 | 0 | 0 | 1 | on |  |
| fanrad_speed_right | 33 | 7 | little_endian | False | 1 | 0 | 0 | 100 | % |  |
| fanbatt_enable_left | 40 | 1 | little_endian | False | 1 | 0 | 0 | 1 | on |  |
| fanbatt_speed_left | 41 | 7 | little_endian | False | 1 | 0 | 0 | 100 | % |  |
| fanbatt_enable_right | 48 | 1 | little_endian | False | 1 | 0 | 0 | 1 | on |  |
| fanbatt_speed_right | 49 | 7 | little_endian | False | 1 | 0 | 0 | 100 | % |  |


#### Calib

| ID (Dec) | ID (Hex) | DLC |
|----------|----------|-----|
| 305 | 0x131 | 1 |

| Signal Name | Start Bit | Length | Byte Order | Value Type | Factor | Offset | Min | Max | Unit | Receiver |
|-------------|-----------|--------|------------|------------|--------|--------|-----|-----|------|----------|
| position | 0 | 8 | little_endian | False | 1 | 0 | 0 | 1 | high | ATC |


#### CalibAck

| ID (Dec) | ID (Hex) | DLC |
|----------|----------|-----|
| 306 | 0x132 | 1 |

| Signal Name | Start Bit | Length | Byte Order | Value Type | Factor | Offset | Min | Max | Unit | Receiver |
|-------------|-----------|--------|------------|------------|--------|--------|-----|-----|------|----------|
| position | 0 | 8 | little_endian | False | 1 | 0 | 0 | 1 | high | SW |


#### PcuSwControl

| ID (Dec) | ID (Hex) | DLC |
|----------|----------|-----|
| 307 | 0x133 | 1 |

| Signal Name | Start Bit | Length | Byte Order | Value Type | Factor | Offset | Min | Max | Unit | Receiver |
|-------------|-----------|--------|------------|------------|--------|--------|-----|-----|------|----------|
| pump | 0 | 1 | little_endian | False | 1 | 0 | 0 | 1 | None | VCU |
| fan | 1 | 1 | little_endian | False | 1 | 0 | 0 | 1 | None | VCU |

**Enumerations:**

- **pump**:
  - 1: On
  - 0: Off
- **fan**:
  - 1: On
  - 0: Off


#### PcuRfAck

| ID (Dec) | ID (Hex) | DLC |
|----------|----------|-----|
| 308 | 0x134 | 1 |

| Signal Name | Start Bit | Length | Byte Order | Value Type | Factor | Offset | Min | Max | Unit | Receiver |
|-------------|-----------|--------|------------|------------|--------|--------|-----|-----|------|----------|
| rf_signalAck | 0 | 1 | little_endian | False | 1 | 0 | 0 | 1 | on | VCU |


#### EmbeddedAliveCheck

| ID (Dec) | ID (Hex) | DLC |
|----------|----------|-----|
| 310 | 0x136 | 0 |



#### Lem

| ID (Dec) | ID (Hex) | DLC |
|----------|----------|-----|
| 962 | 0x3C2 | 8 |

| Signal Name | Start Bit | Length | Byte Order | Value Type | Factor | Offset | Min | Max | Unit | Receiver |
|-------------|-----------|--------|------------|------------|--------|--------|-----|-----|------|----------|
| current | 7 | 32 | big_endian | False | 1 | -2147483648 | None | None | mA | VCU, SW, BMSHV |


