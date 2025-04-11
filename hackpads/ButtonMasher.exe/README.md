# ButtonMasher.exe

ButtonMasher.exe is a 5 key macropad (arranged in a D-pad shape!) with 3 leds and a rotational encoder!

## Features and Inspiration:
- EC11 Rotational encoder for screen brightness control (finally I can stop irking about setting brightness on my monitor! (tbh I was too lazy to look up how to set macros before this))
- 5 whopping keys for epic macros: one should be set up to control the leds too!
- 3 WS2812B RGB LEDs

I wanted a macropad for various bindings I don't have: everything from screen brightness to song fast-forward/rewind are in here. Lots of variety!

## CAD Model:
It's made of two pieces: a bottom case and top cover. I might rework this in the future to better show off the leds.
I learned Fusion 360 basics to do it!

<img src=assets/cad.png alt="Schematic" width="500"/>
(PS I know these pics don't show the case in full. I've got the pcb model fitted though)

## PCB
My PCB has some special sauce cooked up by a friend experienced in wojaks. 
I cannot confirm or deny who might be in those drawings...

Schematic<br>
<img src=assets/pcb_schematic.png alt="Schematic" width="300"/>

PCB<br>
<img src=assets/pcb.png width="300"/>

## Firmware Overview
This hackpad uses [QMK](https://qmk.fm/) firmware for everything. 

I hope to add VIA/further RGB options in the future. (hackboard idea hmmmmmmm (:

## Challenges:
I've never touched CAD or PCB design before, so almost everything I did had a learning curve. Especially fusion...

## BOM:
- 5x Cherry MX Switches
- 4x DSA Keycaps
- 3x SK6812 MINI LEDs
- 1x EC11 Rotary Encoder (can I ask for a knob matching the case color?)
- 1x XIAO RP2040
- 1x Case (2 printed parts, in black preferably)
- 4x M3x16 Bolts (and nuts)

Feel free to look at the firmware or other files for inspiration! This was a fun project
