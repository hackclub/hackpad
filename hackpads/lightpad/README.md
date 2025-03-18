# Lightpad

## Info
Featuring 16 (on device) bindable buttons, 3 rotary encoders, as well as an OLED display, the *Lightpad* functions as an extremely versatile midi controller, with easy options for expandability of firmware. <br><br>I made this hackpad mainly to assist with running lights for my bands live shows, and hopefully some other bands in the near future. It took me quite a while to settle on the design of this hackpad, going through three versions with various designs and combinations of buttons and encoders, but I eventually settled on the current design. <br><br>During the latest design, there were a couple problems I ran into, the most prevalent clearly being the firmware. Due to my key matrix being on an IO expander, I was unable to use qmk or kmk without manually modifying the matrix scanning script, so instead I have created my own firmware from scratch, which also adds the benefit of being able to create very in depth controls on board the pcb, enabling much more customization and potentially in the future, menus and additional settings to control the various features of the board.

## Features
- 16 bindable keyswitches
- 3 rotary encoders (with buttons)
- 16 programmable Neopixel leds
- Ultra High Definition OLED Display (128 x 32)
- (Soon to be) onboard menus and led controls

## Assembly Notes
Please leave rotary encoders, keyswitches, and the OLED display unsoldered, as I will need to solder the neopixels first.
### Materials
The plate is made out of 3mm clear acrylic, and top and bottom cases 3d printed, ideally black.
# BOM
- 1x Seeed Studio Xiao RP2040
- 1x 0.91" OLED Display
- 1x Microchip Technology MCP23017 IO Expander
- 3x 4.7k THT Resistor
- 16x WS2812B Neopixel SMD
- 16x Cherry MX Switch (Gateron Milky Yellows)
- 19x 1N4148 Diode (through hole)
- 3x EC11 Rotary Encoder (With Switch)
- 4x Heatset Inserts (M2xD4.0xL4.0), mounted in bottom case
- 4x M2 screws


![image](https://github.com/user-attachments/assets/965d2bb6-6c83-4d3c-b4d6-a86ae7c5cdc4)
![image](https://github.com/user-attachments/assets/46baf860-0ce0-4bbb-b514-fc6029504718)

