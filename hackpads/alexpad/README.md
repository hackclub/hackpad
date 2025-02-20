# alexpad

A 16 key macropad with individual per-key rgb lighting, a rotary encoder and oled screen powered by QMK firmware.

## Features:
- 128x32 OLED Display
- EC11 Rotary encoder
- 16 Keys
- 16 SK6812 LEDs (one per key)
- Loud buzzer
- **__Vibration motor__**

## CAD Model:

![image](https://github.com/user-attachments/assets/c79dbcdb-139f-4f5c-b48d-ee0aaa23672b)

## PCB
![image](https://github.com/user-attachments/assets/fb6c07d1-f93b-4b67-ad24-6584d2ab9534)

![image](https://github.com/user-attachments/assets/b417ad52-5d23-4165-8abe-f90606c79a1d)

![image](https://github.com/user-attachments/assets/cde31cd6-9f0c-4040-8952-7c44e5a3a4d6)

![image](https://github.com/user-attachments/assets/178d8d32-a372-4632-a61c-2588a8657eaf)


Made using KiCad!

Uses an RP2040

I used the normal Cherry MX footprint. 

Also has a vibration motor. Don't ask why

## Firmware Overview
Built using [KMK](https://github.com/KMKfw/kmk_firmware) firmware. 

## BOM:
- 16x Cherry MX Blues Switches
- 16x keycaps
- 16x SK6812 (reverse mounted)
- 4x M3x5x4 Heatset inserts
- 4x M3x16mm SHCS Bolts
- 4X M3x12mm SHCS Bolts (not sure which one I'm supposed to use, so send both?)
- 1x EC11 Rotary Encoder (I know that I have 1 too many inputs, but just send me 15 switches instead of 16 since I have some at home)
- 1x Case (2 printed parts)

That's everything I'm getting from hack club, the full bom can be found in the bom.csv file which I will send to LCSC.
