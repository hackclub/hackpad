This is a workout tracker that can give you a list of exercises to do based on which day it is, remember which workouts you've done, how many sets, and how much weight. Optionally, a micro SD card can be added to store workouts and view workout progression. It's mostly made to motivate me to work out more because I waste enough time. 

## Features
- workout timer
- set tracker
- tells you exercises based on which day it is (push/pull/legs/core)

## BOM
2x Cherry MX switches and keycaps
1x EC11 Encoder 
1x PCB - black with white drawings if possible 
3x Through-hole resistors (5k) 
1x 0.96" OLED 
3D printed case

Self-provided SD card reader (supported but optional)

## CAD
![Schematic](https://github.com/Omegon0/hackpad/blob/padimo/hackpads/workout_tracker/schematic.png)
Schematic
![Schematic](https://github.com/Omegon0/hackpad/blob/padimo/hackpads/workout_tracker/pcb.png)
PCB
![Schematic](https://github.com/Omegon0/hackpad/blob/padimo/hackpads/workout_tracker/hackpad.png)
Case is fit together using magnets (3mm diameter by 2mm) and has an open top because I like seeing my PCBs. 

## Firmware
Uses Arduino IDE because it's easier to make a big if tree in Arduino than in QMK. 
