# RGBar
RGBoard is an 8 key macropad with a rotary encoder. Each key is backlit with a SK6812 reverse mounted neopixel.
![KW-01 Assembled](https://github.com/user-attachments/assets/8986adfd-3117-437b-9bf0-5ade84aad97a)

### Inspiration
I wanted to make something sleek and minimalist - kinda like a streamdeck, but with keys. I couldn't resist the RGB temptation though... oh well. More is better than less, right?

### Challenges
Since this was my first ever PCB, routing and learning the process took a looong time... Also, writing firmware without testing was a bit unorthodox, it it's *probably* fine...

## Features
- 3D printed case
- EC11 rotary encoder
- 8 keys w/ rgb backlighting

## CAD
The top and bottom are assembled using 4 M3 bolts and heated inserts. 
![KW-01 Deconstructed](https://github.com/user-attachments/assets/96ae4558-9c86-4993-9616-8be3fa3641ab)

Here's a top view:
![image](https://github.com/user-attachments/assets/d3515b09-fb1e-4789-a6e7-f877bb367d06)

## PCB
The PCB was made in KiCad - the board is powered by a Seeed Studio XIAO RP2040.

Here's the schematic:
![image](https://github.com/user-attachments/assets/5e89411a-cf8a-455e-a475-4935679ddaf7)

...and the PCB:
![image](https://github.com/user-attachments/assets/af50de53-bd76-4e84-acf5-79fd17acc93d)

## Firmware
This hackpad uses KMK firmware. Currently, RGBar just acts like a numpad (with backlighting on press) and the rotary encoder adjusts screen brightness, but it can be reprogrammed to do much more...

## BOM
### Custom Components
- 1x Custom PCB
- 1x 3D printed case (top, bottom, and knob)
- 8x 3D printed keycaps (...or any other keycap for Cherry MX switches)
  
### COTS Components
- 8x Cherry MX switches (4 clicky and 4 linear as a personal preference~)
- 8x 1N4148 Diodes (through hole)
- 8x SK6812 MINI-E LEDs
- 1x EC11 Rotary encoder
- 1x Seeed XIAO RP2040 (through hole)
- 14x Male headers
- 4x M3 x 6mm Screws
- 4x M3x5mx4mm heatset inserts

## Extra stuff
I built this as a part of Hack Club's Hackpad program. I haven't tested any of it yet, since I don't currently have the parts~
