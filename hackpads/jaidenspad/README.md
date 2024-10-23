# Jaiden's Hackpad

This is a hackpad featuring 3 rotary encoders, 12 keys, and 2 OLED screens. The design itself is inspired in part by Dieter Rams' "Prototype for a TV set" (1974).

The firmware allows for pretty easy customiztion, featuring a "switching" feature, allowing a user to switch between different keyboard layouts/settings.

The hardest challenge was fitting everything into the 100mmx100mm space. Originally, I had planned to use a few more switches, but I couldn't fit it into the space I had. Additionally, the CAD required me to think carefully about how I would assemble the piece easily.


A video of the assembly is located in the CAD folder, entitled, "assembly_video_example.mp4". Additionally, a render can also be found in the CAD folder, entitled "screenshot".


# Bill of Materials

Also the `BOM.md` file exists.

- 1x Seeed Studio XIAO RP2040
- 15x Through-hole 1N4148 Diodes
- 3x 10k Through-hole Resistors
- 12x Cherry MX Switches
- 12x Keycaps (I don't know much about keycaps... the standard ones?)
- 3x EC11 Encoders
- 1x PCF8574A
- 2x SSD1306 0.91 inch OLED 4 pin (128x32) boards (hopefully with a place to solder a jumper to change the i2c address on the back)
- 2x Header female 4x1 pitch 2.54mm

Additionally,

- 1x M3 Screw (preferably a 15mm long screw)
- White filament (if possible!) for the case pieces.
