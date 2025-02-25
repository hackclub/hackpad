# Daalbupad

I've taken up this project because I wanted to help myself with writing code and this seemed like a nice opportunity to solve my problem of programming on a laptop with 60% keyboard. I've also added several different layers for different uses. The default layer has some common shortcuts for browsing. The programming layers has some useful keys for writing code. The gaming layer has mainly discord shortcuts for now but I want to have Microsoft Flight Simulator specific functions and maybe figure out the rotary encoders with autopilot. There is also a numpad layer. The swap layer together with the display ties the layers together by allowing you to easily swap layers by holding swap key and pressing the specific layer.

The biggest hurdle to overcome was definitely PCB design. I've previously never tried such a thing. I had to redo the traces like 5 times throughout the iterations of the desing. But I think it has improved during this. The next thing was QMK. It just wasn't accepting my json keymap. I switched to KMK and I hope that will work on the final design.

# BOM:

- 16x Cherry MX switches
- 4x EC11 Clickable Encoders
- 1x PCB
- 1x MCP23017_SP
- 1x Seeed XIAO RP2040
- 20x 1N4148 THT Diodes
- 1x SSD1306 0.91' OLED 128x32
- 2x 4.7kΩ Vertical THT Resistors
