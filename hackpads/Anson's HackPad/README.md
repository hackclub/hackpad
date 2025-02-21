# Anson's HackPad

Just a generic 12 keys macropad I made in 16 hours. It features 12 addressable RGB leds (reverse mounted) for lighting effects, and an oled display to show some graphics.

## Features

- 12x Keys
- 0.91" OLED screen
- 12x SK6812 (Addressable RGB leds)

## PCB

Schematic:  
<img src=assets/schematic.png alt="schematic"/>

PCB:  
<img src=assets/pcbfront.png alt="PCB"/>
<img src=assets/pcbrear.png alt="PCB"/>

Silkscreen:
<img src=assets/FrontSilkScreen.png alt="Silkscreen"/>


## Analysis

Render:
<img src=assets/1.png alt="render"/>
<img src=assets/2.png alt="render"/>
<img src=assets/3.png alt="render"/>

Cross Section:
<img src=assets/4.png alt="crosssection"/>
<img src=assets/5.png alt="crosssection"/>
<img src=assets/6.png alt="crosssection"/>



## Firmware

Firmware was written with KMK micropython

## Challenges

The biggest challenge I faced was getting used to KiCad, as my transition from easyEDA was pretty rough

## BOM

- 1x XIAO RP2040 (Wihout header pins)
- 12x Red Linear MX-Style Switches (The ones that allow leds to shine through)
- 12x Generic White DSA Keycaps
- 1x SSD1306 128x32 0.91" OLED
- 12x 1N4148 Diodes
- 12x SK6812 MINI-E LED
- 2x 4.7k resistor
- 4x M3x16mm SHCS Bolts
- 4x M3x5x4 Heatset inserts
- 1x Black Case
- Black PCB Solder Mask (1.6mm board thickness)
