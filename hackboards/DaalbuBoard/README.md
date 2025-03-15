# DaalbuBoard

This is my hackboard. I've wanted to try an orthographic keyboard so I designed one. It's close to a TKL and I've added a big esc key. I had to redo the PCB design multiple times because I chose a wrong spacing and I had to edit the footprint to account for this spacing.

## Features
 - 82 keys
 - ortholinear layout
 - big esc key
 - display
 - KMK software

## CAD model
You need 4 screws in the corners to mount the pcb. I've tried to create some interesting triangle design on the sides. There is no plate to widen the compatibility with keycaps since im using low profile switches.
<img src=assets/case.png alt="Case" width="500"/>
<img src=assets/completed.png alt="Completed Hackboard" width="500"/>

## PCB
Here is my PCB. I've done it in Kicad and the silkscreen is an png imported from [Haikei](https://haikei.app/)
<img src=assets/pcb.png alt="pcb" width="500"/>
<img src=assets/schematic.png alt="Schematic" width="500"/>

## Firmware
The firmware is KMK written in python and it currently acts as a normal layout.

## BOM
 - 1x Orpheus pico
 - 81x choc v2 linear (preferably silent) switches
 - 1x EC11 rotary encoder
 - 6x 2u cherry pcb stabilizer
 - 1x 6.25u cherry pcb stabilizer
 - 82x DO-35 diodes
 - 2x 4.7kohm resistors
 - 1x SSD1306 128x32 OLED display
 - 1x 3d printed case
 - 4x M2 screws

## Fun facts
This README is being written on a phone since I went to a physics competition and I need to finish this before my birthday.
