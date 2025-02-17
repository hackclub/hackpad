# alexpad

A 16 key macropad with individual per-key rgb lighting, with a rotary encoder and oled screen powered by QMK firmware.

## Features:
- 128x32 OLED Display
- EC11 Rotary encoder
- 16 Keys
- 16 SK6812 LEDs (one per key)

## CAD Model:




## PCB
Made using KiCad!

Uses an RP2040

I used the normal cherry mx footprint. 

## Firmware Overview
Built using [KMK](https://github.com/KMKfw/kmk_firmware) firmware. 

Also has a vibration motor. Don't ask why

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

## Special Requests
My hackpad mildly breaks the rules, so there are a few things I want to specify.

I would like to have the pcb **with a stencil**, and all the parts I listed in the bom. The rest of the stuff I'll buy from LCSC. 

I intend to use my money to add onto the $20 LCSC grant, so expect a donation to the HCB once I get this approved. Please use that to top-up my grant.
