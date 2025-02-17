# Yet Another Hackpad

Yet Another Hackpad is a 4 key macropad with a rotary encoder and LEDs.

## Features

- 4 Keys
- 4 SK6812 Mini Addressable RGB LEDs
- EC11 Rotary Encoder

## CAD Model

<img src=assets/cad.png alt="CAD" width="500"/>

<img src=assets/cad2.png alt="CAD" width="500"/>

## PCB

Schematic

<img src=assets/schematic.png alt="Schematic" width="500"/>

PCB

<img src=assets/pcb.png alt="PCB" width="500"/>

<img src=assets/rendered_pcb.png alt="Rendered PCB" width="500" />

Silkscreen Credit: [Go Gopher](https://go.googlesource.com/website/+/refs/heads/master/_content/doc/gopher/frontpage.png) by Renee French, used under [CC BY 4.0](http://creativecommons.org/licenses/by/4.0/)

## Firmware

The firmware is written using kmk

## Inspiration

I usually have my laptop docked to an external keyboard when working, but the keyboard doesn't have the function keys that the laptop keyboard does. I also often find myself forgetting shortcuts, so I made this so I could work more efficiently.

## Challenges

I haven't done any PCB design before, so it took a while to get accustomed to KiCAD, and figure out to import all the necessary libraries and export the board to my CAD program.

## BOM

- 1 Seeed XIAO RP2040
- 1 EC11 Rotary Encoder
- 4 MX-Style switches
- 4 White Keycaps
- 4 Reverse Mount SK6812 MINI-E LEDs
- 4 M3 hex nuts
- 4 M3x16mm screws
- 1 3D Printed Case (2 parts)
