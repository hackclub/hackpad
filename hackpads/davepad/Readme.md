
# Davepad
# Assembly
I'm happy to solder and assemble it myself and do the mounting screws and spacers.

# BOM
| QTY | Part |
| --- | --- |
| 18   | Any Cherry MX style switches, ideally brown but I don't mind|
| 18   | Blank keycaps|
| 2    | Ec11 Rotary Encoder|
| 20   | Through-hole 1N4148 Diodes (Ideally with dimensions L3.6, D1.6 mm or close to)|
| 2    | Through hole resistors, 4.7k (Ideally with dimensions L3.6, D1.6 mm or close to)|
| 4    | Through hole resistors, 1k (Ideally with dimensions L3.6, D1.6 mm or close to)|
| 1    | 0.91" I2C OLED (with SSD1306)|
| 1    | Seeed XIAO through hole RP2040|
| 1    | 1x4 Header|
| 1    | MCP23017, through hole|
| 1    | PCB|
| 1    | Case|

# Case
3d printed, there's just one component, don't mind the colour but purple would be cool.

# Notes
- I want a macropad with easily selectable modes for different applications. In particular, I want to use it as a laptop numpad when I don't have a full keyboard with me.
- It also needs enough keys to be able to move my main keyboard out of the way when using a graphics tablet and still access all the hotkeys I need in creative software.
- The case is pretty barebones because I want to be able to see the pcb.
- My biggest challenge was writing firmware. The QMK docs are pretty good, but don't have specific instructions for running a matrix through an IO expander. This was fun though, as I got to write a lot more code this way :).
