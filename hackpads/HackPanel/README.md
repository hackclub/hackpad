# HackPanel

HackpPanel is a 5 key macropad with a rotary encoder. HackPanel uses KMK for it's firmware.

## Features:
- Special case designed with blender
- EC11 Rotary encoder for volume control
- 5 Customizationable keys
- Utilizes the Xiao RP2040's onboard RGB LED

## CAD Model:
HackPanel focuses on simplicity, meaning no screws. to attach the top and bottom, the pieces perfectly fit together, and the bottom of the PCB has no traces or vias so everything is attachable with simple glue or adhesive, including the case.

It has 2 pieces in 1 print file while still following the printing diameters. The top piece is branded and perfectly fits into the bottom piece.

<img src=assets/case.png alt="Schematic" width="500"/>

Made in Blender. Very Simple.


## PCB
This is my PCB, made in KiCad.

Schematic
<img src=assets/schematic.png alt="Schematic" width="300"/>

PCB
<img src=assets/pcb.png alt="Schematic" width="300"/>


## Firmware Overview
This hackpad uses KMK firmware for the Xiao RP2040. 

- the rotary encoder controls volume. press to mute/unmute
- The 5 keys currently act as customizationable macro keys, but can also be used as arrow and space bar keys


I shouldn't need to change anything, it's perfectly fine to me.

## BOM:
This is everything needed to make HackPanel:

- 5x Cherry MX Switches
- 5x DSA Keycaps
- 1x EC11 Rotary Encoder
- 1x XIAO RP2040
- 1x Case (2 parts, 1 file)


## Extra stuff
There's not much to say, but it was an interesting challenge and I learned a lot.