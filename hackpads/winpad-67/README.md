# winpad

## About

Macropad to manage Sway/I3 window arrangement
- In the default layer, keys rearrange windows, change splitting behavior, and modify arrangement style (floating, tabbed, stacked, or tiled)
- The OLED shows the config for the current window
- The rotary encoder controls volume

Includes a **monitor customization layer** (through DDC/CI)
- Rotary encoder controls brightness
- Buttons change monitor input (in order to avoid dealing with slow monitor menus)

### Challenges

- Designing the case/figuring out plate alignment
- Figuring out the switch/encoder layout

## BOM

* 8x Cherry MX switches
* 8x Keycaps
* 1x EC11 encoder
* 1x EC11 cap
* 3x WS2812B LEDs
* 9x through-hole 1N4148 diodes
* 1x PCB
* 1x though-hole Seeed XIAO RP2040
* 1x 0.91" OLED + pin headers

_(I will provide/solder the 300 ohm resistor myself)_

## Case

The case has 5 parts:

* Base (3d-printed - white)
* Plate (laser cut acrylic)
* Top (3d-printed - white)
* Left and right stands (laser cut acrylic)

## Firmware

The keyboard needs an additional host-side daemon to run in order to display the current window status and handle DDC/CI requests. I haven't made this yet.

[Onshape Assembly](https://cad.onshape.com/documents/a1757479993afdf8900976a8/w/f04ce65470661a1db78923f0/e/f06774e191f49aedcdf2b5ff)

