# Buildpad

This is my first time working on any hardware-ish stuff. This took me way longer than it should have because there are many versions that I scrapped (I didn't even push) and because I had to learn how to use KiCad and Fusion360. I initially planned on having two rotary encoders but I decided that IO expansion was a little too difficult to deal with especially to be within the size constraint and without SMD parts (since I am not comfortable soldering them). I also wanted to have Neopixels for the underglow but that never ended up happening because I designed a solution and later realized the need for resistors and decoupling capacitors which I tried adding, but I also later decided that I did not want to solder SMD components. My best solution to still get the RGB effect I wanted was to use these color changing LEDs in my BOM below.

# BOM:

- 16x Gateron Milky Yellow Switches (or any other switch)
- 16x Through-hole 1N4148 Diodes
- 16x Slow Fading RGB LEDs (234-RGB-Slow at https://www.aliexpress.com/item/1005005310058942.html) (3.0-3.4V, 20mA)
- 16x 15 Ohm Resistors (for the LEDs)
- 1x Bottom of the Case 3D Printed in Yellow Filament (if available or just the closest available color)
- 1x Top of the Case 3D Printed in Yellow Filament (if available or just the closest available color)
- 4x 3D Printed Screws in Black Filament (if available or just the closest available color)
- 16x Blank Red Keycaps (1u size)
- 1x 0.91 inch OLED Display (128x32) SSD1306
- 1x Xiao Seed RP2040
- 1x PCB
