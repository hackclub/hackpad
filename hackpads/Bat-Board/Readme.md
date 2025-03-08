# Bat-Board

Bat-Board is a 12 key macropad with an OLED Display. It uses QMK firmware, easy to use and customize macro

I tried to make a multipupose and multi layer macropad. 1 layer for 1 purpose. I tried to make somthing like adafruit or protodesigns macropad. It will work like them but need a better case more like acrylic. I have used all of this first time. It was fun somtimes and sometimes frustrating. If think i need to add a stand like system in the case but building it is a liitle hard for me.

## Features:
- Multilayer Functionality.
- 128x32 OLED Display
- First key for main controller or for whatever you want
- 12 Keys



## PCB
Here's my PCB! It was made in KiCad. I was thing of using a silkscreen but didn't like anything .

<img src=Images/pcb_f.png alt="Pcb" width="300"/>
<img src=Images/pcb_b.png alt="Pcb" width="300"/>
<img src=Images/pcb_3d_f.png alt="Pcb" width="300"/>
<img src=Images/pcb_3d_b.png alt="Pcb" width="300"/>

Schematic
- [Schematics](/PCB/Macropad_Schematics.pdf) 

<img src=Images/schematics.png alt="schematics" width="300"/>


## Firmware Overview
This hackpad uses [QMK](https://qmk.fm/) firmware for everything. 

- The main left button is for contol purpose works as togle and to switch between layers and more. More like ctrl button of keyboard
- Last 4 white keys will be the arrow keys of keyboard. Other keys are custom set macros and links.
- The OLED is Not decided yet but i am thing of something from naruto or demon slayer


I might add more in the future! That's it for now

## CAD:

<img src=Images/cad_3d.png alt="Cad" width="300"/>
<img src=Images/cad_3d_2.png alt="Cad" width="300"/>
<img src=Images/cad_3d_3.png alt="Cad" width="300"/>

## BOM:

Here should be everything you need to make this hackpad

- 13x Cherry MX Switches
- 4x SK6812 MINI Leds
- 1x XIAO RP2040
- 4x Blank DSA Keycaps
- 9x M3x16 Bolt
- 9x M3 Heatset
- 1x 0.91" 128x32 OLED Display
- 13x Through-hole 1N4148 Diodes
- 1x Red Blank DSA keycaps
- 4x White Blank DSA keycaps
- 9x Black Blank DSA keycaps
- 9x M3 hex nuts

Extras:-
- Few Jump Wires
- Breadboard
- A soldering iron and its required materials
For testing before placing
- a sd card

Others:
- KMK Firmware
- Top Case.stl 
- Bottom Case.stl
