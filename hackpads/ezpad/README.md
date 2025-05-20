# ezpad

by Eddy Zhao (@eddyzow)

* Note: the full CAD file was greater than 25 MB and thus I had to zip it for github to allow it onto the servers. otherwise all other files should follow the correct structure

![image](https://github.com/user-attachments/assets/6eca65f7-fa06-414b-b9ac-68b172981000)

A macropad (mini-keyboard) with 9 mechanical keys, 0.91" OLED screen, and rotary encoder. Custom-built and wired PCB. Powered by a Seeed XIAO RP2040.

This project was really fun to work on! I learned a lot about how key matrices work and expanded my knowledge of electronics along the way. I had to rewire the PCB three times because I had accidentally flipped the switch sockets to the front, then I used the wrong socket, etc... it was a painful process. However, after many failed attempts, I finally created my very first PCB! I then put it in a case that I created on Onshape. The rotary encoder turns the volume up and down, but unfortunately due to pin constraints the button press does not work.

This is my submission for Hackpad V3 and my second submission for Highway! I'm a mechanical keyboard person who owns five mechanical keyboards, but only one of them is custom (not the PCB) -- this is thus also hopefully a precursor project to a larger custom mechanical keyboard I'll be making soon!

# Images

| Schematic    | PCB | Case |
| -------- | ------- | ------- |
| ![image](https://github.com/user-attachments/assets/228fc7bc-6125-4b40-b424-ff02428df9f7) | ![image](https://github.com/user-attachments/assets/03804ac7-8eb5-410c-ad74-194b3dca9ba3) | ![image](https://github.com/user-attachments/assets/b8abe84e-1a56-4fd6-9fd6-c8c6e83b9a3c) |


# BOM

- 1x 0.91" 128x32 OLED (SSD1306)
- 9x Cherry MX Switch
- 9x DSA Keycaps
- 9x 1N4148 Diodes
- 9x NeoPixels (SK6812 MINI-E LEDs)
- 1x Seeed XIAO RP2040
- 1x EC11 Rotary Encoder Switch
- 1x 3D Printed Case

parts I already have:
- 4x 20mm M4 screws and nuts
