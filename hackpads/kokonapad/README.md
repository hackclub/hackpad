# Kokonapad

Kokonapad is my macropad with four keys, a rotary encoder, an OLED 128x32 display, with 4 SK6812_Mini LEDs, and uses KMK firmware.

<img src=assets/kokonapad.png alt="Parts view" height="450"/>

## Features

- 128x32 OLED Display
- EC11 Rotary encoder for volume control
- 4 SK6812_Mini LEDs, adjacent to each of the 4 keys

## CAD Model

<img src=assets/KokonapadPartView.png alt="Parts view" height="450"/>
Case designed in OnShape

## PCB

Schematic

<img src=assets/KokonapadSchematic.png alt="Schematic" height="450"/>

PCB

<img src=assets/KokonapadPCB.png alt="PCB" height="450"/>

<img src=assets/KokonaPCBv1.png alt="PCB" height="500"/>
I designed the PCB in KiCad. My wife Kokona is on the PCB!!!

## Firmware
Kokonapad uses KMK firmware. 

- The rotary encoder changes volume. Pressing the switch mutes audio
- The 4 keys represent arrow keys
- I still have yet to work on the OLED screen as of 2025.02.20

## BOM
Here is the list of components used in this build!

- 1* Xiao RP2040
- 4* Cherry_MX switches
- 4* of your own (standard size) keycaps!
- 4* SK6812_Mini LEDs
- 1* 0.91_128x32 OLED display
- 1* EC11 rotary encoder
- 1* case (consists of three 3D-printed parts)
