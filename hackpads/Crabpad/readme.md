# Crabpad

Crabpad is a 7 key macropad, an OLED Display, and uses KMK firmware

## Features:
- Dual layer acrylic case. looks looks awesome doesn't it??
- 128x32 OLED Display
- 7 Keys
- 4 modes for upto 24 macros!!

## CAD Model:
Everything fits together using 4 M3 Bolts and heatset inserts.

It has 2 separate printed pieces.

Made in OpenScad i think.


## PCB
Here's my PCB! It was made in KiCad.

Schematic
<img Crabpad/PCB/schematic.png alt="Schematic" width="300"/>

PCB
<img src=Crabpad/PCB/CrabPAd.png alt="Schematic" width="300"/>

I used MX_V2 for the keyswitch footprints. I think in retrospect, I should've added a ground plane

## Firmware Overview
This hackpad uses KMK firmware for everything. 
- The 6 keys currently act as macros I dynamically change them from the mode button thats the 7th key.
- The OLED is a mode displayer  for now thinking of adding a game
I might add more in the future! That's it for now

## BOM:
Here should be everything you need to make this hackpad

- 7x Cherry MX Switches
- 7x DSA Keycaps
- 4x M3x5x4 Heatset inserts
- 4x M3x16mm SHCS Bolts
- 4X M3x12mm SHCS Bolts
- 1x 0.96" 128x32 OLED Display
- 1x XIAO RP2040
- 1x Case (2 printed parts)

