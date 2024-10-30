# Porterpad 🎹
![{37B623EF-546C-4EC2-A377-DDC8D0F68D47}](https://github.com/user-attachments/assets/af89acdd-7f61-490d-8046-f76d2c965eeb)
Porterpad uses 3 encoders and 4 keys to allow control in many things. It also has neopixel leds that shine underneath the key plate and illuminate neat rgb lights. 

## What was your inspiration to make it?
I wanted a separate keyboard for macros and maybe even midi control for DAWs. I also wanted to give it out to some of my friends.

## Hardest challenges faced
The QMK Firmware was definitely the hardest to make. It took some time but I did it instead of circuitpython because i wanted something industry standard.

## Other fun facts to know
I chose onshape instead of fusion360 because i had the most experience in it, which meant i couldn't use the plate gen tool. But it also allows me to share my project [here](https://cad.onshape.com/documents/61d943230a12fcbc1f772cb8/w/d8f3315bbaec89d5a2d0339b/e/b05043413dee042d916ef43c?renderMode=0&uiState=6714361283a7fb0fbd7b6b09)

I also made a [simple guide](https://docs.google.com/document/d/1JV8aVDMf2TwetxhckK0Wdf9FykIQtn7HA-_w5BLeQas) for the QMK Firmware for the people in slack

Porter is also a reference to a music artist lol

# BOM
Below is a BOM for only one Porterpad. It uses smd components which i choose to solder everything

## PCB BOM
* 1x PCB with front and back silkscreen (white would be nice)
* 1x Seeed Xiao RP2040
* 3x EC11 Rotary Encoders (if you have non clicky ones, i would prefer those)
* 4x SKC6812E - SMD Neopixel LED
* 4x RC0402FR-07220RL - 0402 SMD 220Ω Resistor
* 4x SMF6.5CA - SOD-123 SMD Diode for Matrix

## Keyboard BOM
* 4x Gateron Milky Yellows
* 4x DSA Keycaps
* 3x EC11 Encoder Caps
* 5x 2.9mm Screws (10mm)
* 1x Top Chassis 3d Print (mint green preferred)
* 1x Plate 3d Print (transparent, but if not possible use white)
* 1x Bottom Chassis 3d Print (black)
* 1x USB-C to USB-2.0 Cable
