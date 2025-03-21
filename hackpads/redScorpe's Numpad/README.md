# redScorpe's Numpad

This is my custom version of a simple numpad with a Rotary Encoder and a 9.1" OLED-Display. Since I have recently switched to a TKL-Keyboard to easier switch between mouse and keyboard I wondered how cool it would be to have an external numpad which also has a rotary which my new keyboard is missing.

# Challenges
I was genuinely confused about a lot things regarding the whole process of building my first hackpad since all of this was new to me. However making my own symbol in KiCad for the OLED directly at the start of this journey was honestly the most challenging part for me.

## CAD Model
| **Model**                                                                  | **Render**                                                              |
|----------------------------------------------------------------------------|-------------------------------------------------------------------------|
| ![](https://cdn.hackclubber.dev/slackcdn/a9e1c880677854b64dbcdd8c9dc36e76.png) | ![](https://cdn.hack.pet/slackcdn/678d118c57094d6aae49122bccd28d9b.PNG) |

## PCB
| **Schematic** | **PCB** |
|---------------|---------|
|![](https://cdn.hack.pet/slackcdn/a3ad7a5903431038cb79955e694afb3e.png)|![](https://cdn.hack.pet/slackcdn/e540ac6891c7700b64d7c771695121bb.png)|

## Third-Party KiCad Libraries
- https://github.com/kiswitch/kiswitch/tree/main/library/footprints/Switch_Keyboard_Cherry_MX.pretty
- https://github.com/Seeed-Studio/OPL_Kicad_Library


## BOM
- 1 Seeed Studio XIAO RP2040
- 12x MX-Style Switches
- 12x DSA Keycaps
- 12x 1N4148 Diodes
- 1x 0.91" 128x32 OLED Display
- 1x EC11 Rotary Encoder
- 4x M3x16mm Screws
- 4x M3x5mx4mm Heatset Inserts
- 1x 3d-Printed Case (Top, Middle and Bottom Parts)
- 1x [3d-Printed Knob](https:/ /makerworld.com/en/models/628840#profileId-593261)