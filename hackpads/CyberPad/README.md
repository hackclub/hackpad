# Orpheuspad

Cyberneel Hackpad is a 3x3 key macropad with a rotary encoder, an OLED Display. Uses QMK firmware

## Features:
- 128x64 OLED Display
- EC11 Rotary encoder for whatever you want
- 9 Keys

## CAD Model:
Everything fits together using 4 M3 Bolt. 4 for the case.

It has 2 separate printed pieces. The base where the PCB sits, and the top cover.

<img src=assets/cad.png alt="Schematic" width="500"/>

Made in Blender 3D.

## PCB
Here's my PCB! It was made in KiCad.

Schematic
<img src=assets/schematic.png alt="Schematic" width="300"/>

PCB
<img src=assets/pcb.png alt="Schematic" width="300"/>

I used MX_V2 for the keyswitch footprints.

## Firmware Overview
This hackpad uses [QMK](https://qmk.fm/) firmware for everything. 

- the rotary encoder changes volume. press to mute
- The 9 keys currently act as function keys.
- The OLED can show various information

I plan on getting more familiar with QMK and VIA to add more features

## BOM:
Here should be everything you need to make this hackpad

- 9x Cherry MX Switches
- 9x DSA Keycaps
- 4x M3x16mm SHCS Bolts
- 9x 1N4148 DO-35 Diodes.
- 1x 0.96" 128x64 OLED Display
- 1x EC11 Rotary Encoder with switch
- 1x XIAO RP2040
- 1x Case (2 printed parts)