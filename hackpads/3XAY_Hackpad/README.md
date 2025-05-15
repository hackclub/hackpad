# HackPad

![image](renderSideView.png)
A 3 knob, 6 switch macropad with a 128x32 OLED.
All powered by a Seeed XIAO RP2040 along with a PCF8574A. 

## Why
The three knobs make this great for content creation. You can adjust the volume / scrub through your timeline in Davinci Resolve or use each knob for each dimension in Blender. You can make it into whatever you want (as long as you only want 6 buttons, 3 knobs, and 1 small screen)

## BOM:
- 3x Cherry MX Switches
- 3x EC11 Encoder WITH button
- 1x 0.91in 128x32px OLED (SSD1306)
- 1x PCF8574A
- 1x PCB
- 4x M3x20mm screws
- 1x Bottom case (3D Printed)
- 1x Top plate (3D Printed)
- 1x Switch plate (Laser-cut acrylic)
- 1x Through-hole 10k resistor
- 1x Seeed XIAO RP2040

## What was the hardest challenge?
I think the hardest challenge was the firmware for me. Although this was my first time designing a PCB, it felt fairly easy and I was able to breeze through it. I'm not new to Blender, so the case was also fairly simple. And even though I'm decent at programming, especially in Python, the firmware took a while. This was because I couldn't easily get QMK to work with my hardware. Then, with very little time left, I had to make something quickly in Circuitpython, which was new to me.

## Other fun facts to know
I was actually making a YouTube short for every day I was working on this project. You can go ahead and check it out [here!](https://youtube.com/playlist?list=PL8pZ9v0F1Ks2gfHrP7J-pUTj4NAnL8gHc&si=MliIfDuidp5TVAae) I also had my own [GitHub repository](https://github.com/3XAY/3XAY_HackPad) where I was uploading the project files / images daily, so you can go through the version history and see every single change!
