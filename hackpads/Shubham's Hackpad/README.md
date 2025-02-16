# Shubham's Hackpad

A 11 keys macropad with a rotary encoder, a 128x32 OLED display and firmware using KMK.

## Features

-   Vs Code shortcuts like Format Document
-   Quality of Life shortcuts like Cut, Copy, Paste, Print Screen, Snipping Tool
-   Media Control Keys with Rotary Encoder for Volume Control
-   128x32 OLED Display

## BOM ( Bill of Materials )

-   11x Cherry MX Switches
-   11x DSA Keycaps (Red)
-   1x EC11 Encoder Switch
-   1x SSD1306 128x32 0.91" OLED Display
-   12x Through-hole 1N4148 Diodes
-   1x XIAO RP2040 Microcontroller
-   1x PCB
-   1x Case
    -   Base (Printed, Yellow)
    -   Plate (Printed, White)
-   4x M3x16mm SHCS Bolts

## Firmware Overview

The firmware is based on [KMK](https://github.com/KMKfw/kmk_firmware) and [Adafruit SSD1306](https://docs.circuitpython.org/projects/ssd1306/en/latest) for display.

-   The first row keys are for `Save`, `Format`, `Switch Application` and `Screenshot`
-   The second row keys are `Copy`, `Cut`, `Paste` and `Snipping Tool`
-   The third row keys are `Media Previous`, `Media Play / Pause` and `Media Next`
-   The `Rotary Encoder` is used for `Media Volume`, press to `Media Mute / Unmute`
-   The display is currently set to `Hello World!` which I would be able to configure after getting the hackpad, as I have no way of debugging. 

## Demo Images

### Case

![Case](https://cdn.hackclubber.dev/slackcdn/91513f3fad3484a438e61aafcab39d22.png)

![Case](https://cdn.hack.pet/slackcdn/42f48582fe129df23cc4a94f4d5943dd.png)

![Case](https://cdn.hackclubber.dev/slackcdn/37592ad03e53f0f90dd2bcb34556ff7a.png)

![Case](https://cdn.hackclubber.dev/slackcdn/58c0674f6cd6df7da9a35bdb3baef8c7.png)

![Case](https://cdn.hack.pet/slackcdn/b1ac1ff3825c742e00b0c249fc2b1cb4.png)

![Case](https://cdn.hack.pet/slackcdn/b77a07eed7226095d67b3bf26be6adf0.png)

### Plate

![Plate](https://cdn.hackclubber.dev/slackcdn/a8efd8ab2f7599fca2e47aab2d38d14d.png)

![Plate](https://cdn.hack.pet/slackcdn/f7c48b5cf1b7490f4bd9b660f453d9cb.png)

![Plate](https://cdn.hackclubber.dev/slackcdn/ee7ebd9179a5276da88a737cbe607080.png)

### Base

![Base](https://cdn.hackclubber.dev/slackcdn/96232b9b6ccbe14a50e86289f9fc29b1.png)

![Base](https://cdn.hackclubber.dev/slackcdn/b076d26a434c1e3aa14c0ad56a9482c9.png)

![Base](https://cdn.hackclubber.dev/slackcdn/e4303db6199d327e9a3b653d947ae424.png)

![Base](https://cdn.hackclubber.dev/slackcdn/c022695f1013c5134c224da0dda39daf.png)

![Base](https://cdn.hackclubber.dev/slackcdn/9530b37b0d03ebbc0e4f935f1a5f73bb.png)

![Base](https://cdn.hackclubber.dev/slackcdn/3ec96167cb9d17cc958df5e7381c15b3.png)

## PCB and Schematic

### Schematic

![Schematic](https://cdn.hackclubber.dev/slackcdn/9e92014d58048dfde7ce4f72196f31e1.png)

### PCB

![PCB](https://cdn.hackclubber.dev/slackcdn/f63bfd705631e81dd8a705cbed762f79.png)

### PCB 3D

![PCB 3D](https://cdn.hackclubber.dev/slackcdn/47c90c25393937a8cdc223540b15391b.png)

![PCB 3D](https://cdn.hackclubber.dev/slackcdn/03cd833db40647f23acb614a7ea24bdf.png)

### Extra Footprints and Schematics Library

[OPL Kicad Library](https://github.com/Seeed-Studio/OPL_Kicad_Library/tree/master/Seeed%20Studio%20XIAO%20Series%20Library), [ScottoKicad](https://github.com/joe-scotto/scottokeebs/tree/main/Extras/ScottoKicad)

### Extra 3D Models

[EC11 Rotary Encoder with Switch](https://grabcad.com/library/ec11-rotary-encoder-with-switch-1), [Seeed Studio XIAO RP2040](https://grabcad.com/library/seeed-studio-xiao-rp2040-1)