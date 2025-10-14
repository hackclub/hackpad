# Hex Numpad

Hex Numpad is a hexadecimal numpad. Pretty self-explanatory. Uses KMK firmware.

## Features:
- Dual layer acrylic case. looks looks awesome doesn't it??
- 128x32 OLED Display
- EC11 Rotary encoder for whatever you want
- 2 WS2812B RGB LEDs. One for underglow, and one that diffuses throughout the case
- 4 Keys
- [VIA](https://www.caniusevia.com/) support!

## CAD Model:
Fits together using 4 M3 Bolts and heatset inserts. 4 for the case, none for the PCB... (it'll say in... right?).

It 2 printed pieces. The base where the PCB sits, and the top cover.

<img src=assets/cad.png alt="CAD" width="500"/>

Made in FreeCAD (took 5+ hours because I'm dumb).


## PCB
Here's my PCB! It was made in KiCad. The silkscreen was imported from images I ~~stole from the internet~~ found.

Schematic
<img src=assets/schematic.png alt="Schematic" width="300"/>

PCB
<img src=assets/pcb.png alt="PCB" width="300"/>

I used MX_V2 for the keyswitch footprints. I intended to use hyprid Cherry MX/Alps footprints, but it's too late now. ~~I can just drill extra holes if I want to build one with Alps switches.~~

## Firmware Overview
This hackpad uses [KMK firmware](https://github.com/KMKfw/kmk_firmware/) for everything. 

I might add more in the future (layers?). That's it for now

## BOM:
Here should be everything you need to make this hackpad

- 16x Cherry MX Switches
- 16x DSA Keycaps
- 4x M3 heatset
- 4x M3x16mm screws
- 16x 1N4148 DO-35 Diodes.
- 1x XIAO RP2040
- 1x Case (2 printed parts)
- 1x PCB
