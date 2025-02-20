# LakyPad

Welcome to LakyPad, my ultimate keypad! I plan to use it for shortcuts and for extra function keys I can use for... more shortcuts :)


## Features:
- 128x64 OLED Display to display any keyboard-related information... or to create the weirdest ArduBoy ever :P
- 4x3 keyboard for ultimate keyboardness - 12 extra keys at your disposal!
- EC11 Rotary encoder - did I say 12 keys? I meant 12 * 30 keys since this can be used to cycle between layers!
- No RGB! - Although that isn't a feature, I just didn't have enough pins and multiplexers are still a bit too scary for me :)

This board was made 100% in Fusion360 and KiCad! Guess that is one good use for the free education license... :)

## CAD Model:

It has 2 printed pieces: A baseplate and a cover. It needs 4 M3 Screws.

<img src=assets/cad.png alt="CAD Model" width="500"/>


## PCB

Schematic
<img src=assets/schematic.png alt="Schematic" width="300"/>

PCB
<img src=assets/pcb.png alt="Schematic" width="300"/>


## Firmware Overview
This hackpad uses KMK for its firmware. Currently only the OLED display and the keys are used since I couldn't figure out layers yet!
I will definitely upgrade the firmware though as soon as I get the real thing!

## BOM:
Here should be everything needed for this hackpad:

- 12x Cherry MX Switches
- 12x DSA Keycaps
- 4x M3x16mm screws
- 12x 1N4148 DO-35 Diodes
- 1x 0.96" 128x64 OLED Display
- 1x EC11 Rotary Encoder
- 1x XIAO RP2040
- 1x Case (2 printed parts)

A nice render
<img src=assets/render.png alt="Render" width="300"/>
