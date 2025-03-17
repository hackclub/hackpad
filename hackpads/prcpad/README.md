# PRC
![image](https://github.com/user-attachments/assets/b3626148-774a-4b7b-97bc-15d7907cd9ba)

intended as a button box for sim racing

features 6 buttons, 2 toggle switches, rotary encoder + click, 128x64 oled, 16 neopixels, and a single-piece case

The odd shape on the PCB is intended to be removed and mounted as a replacment for the circuitry in a samsung 40.5mm rotary encoder knob, which has a LED as stock but is now replaced with a neopixel.

Both the oled, rotary, and daughterboard are connected on pcb by 2.54mm pin headers

Mounted with the two holes on the case on 8020 profile

I do not need this printed, I own a 3d printer.

This is my first use of kicad and i enjoyed routing

BOM:
- 1x Seeed XIAO RP2040 Through-hole
- 6x MX-Style switches (the more tactile and heavier, the better)
- 7x Through-hole 1N4148 Diodes
- 2x MTS-101 (grant)
- 1x EC11 Rotary encoder
- 1x 0.96 inch SSD1306 OLED display
- 6x DSA keycaps (white to allow some neopixel light)
- 16x SK6812 MINI-E LEDs
- 6x M3x16mm screws
- 6x M3 hex nuts
- 1x 3 pin 2.54mm Header (owned)
- 1x 4 pin 2.54mm Header (owned)
- 1x 5 pin 2.54mm Header (owned)

## Challenge
Kicad footprint/3dmodel/symbol libraries are a mess; someone needs to unify them. That being said it does work and not bad at all. Swapping is very easy and doesn't break.

I am terrible at soldering so it will be painful but luckily I have 5 of them to break from JLCPCB

## Photography
<img width="529" alt="image" src="https://github.com/user-attachments/assets/5464bbe7-f831-4d43-a581-23b816131320" />
<img width="860" alt="image" src="https://github.com/user-attachments/assets/c1a1f78e-7c71-4dac-b845-56ee2bbb93ec" />
<img width="250" alt="image" src="https://github.com/user-attachments/assets/edb45a97-317f-4f59-a401-db37024c5d41" />
