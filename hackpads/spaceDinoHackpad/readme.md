# Space Dino Hackpad
The Space Dino Hackpad is a 12 key macropad. It also contains a rotary encoder, and 12 leds, one under each key.
It uses KMK firmware, designed to make programming easier.


## Features List
- 2 part 3d printed case
- EC11 Rotary Encoder
- 12 keys
- 12 rgb leds


## Case
The case is fully 3d printed, and contains two parts. The two parts are attached with 4 M3 bolts and heatset inserts. It was designed in FreeCad.
![20250217_14h36m06s_grim](https://github.com/user-attachments/assets/1d0431aa-5ae7-4c66-aa22-69fda548ad19)


## PCB
The PCB was designed in KiCad. It uses a switch matrix to attach all the keys. The LED's are reverse mounted, and simply wired in a line.


Schematic
![20250220_13h25m19s_grim](https://github.com/user-attachments/assets/e606b22d-887a-4b61-bd81-80d79b3cb136)


The PCB is 2 layers, and contains a ground plane. The silkscreen art was drawn by me.
PCB
![20250220_13h31m59s_grim](https://github.com/user-attachments/assets/95e4db66-8a4e-430e-8b67-852bf64f5dd9)


## Firmware
The firmware was written in python using KMK.


### Rotary Encoder
The rotary encoder simply controls volume. Pressing the switch mutes volume.


### LEDs
The LEDs are set to run a "rainbow" animation


### Keys
The keys are all linked to various functions useful when programming.


#### Copy Paste


The first two keys on the top row are routed to Ctrl+Shift+C and Ctrl+Shift+V. This allows for copying and pasting in the terminal on most Linux systems.
The two keys below these are routed to Ctrl+C and Ctrl+V for copy pasting in most IDEs and text editors


#### Run
On the first row the rightmost key is routed to F5. This is the shortcut in VS Code to start debugging.
The key below this is routed to Ctrl+F5, which runs without debugging in VS Code.


#### Macros
The third row is dedicated to useful macros for programming. The first key inserts a TODO comment.
The second inserts a formatedd docstring with spots to insert a function description, info on parameters, and info on returns.
The last key copies the current line, pastes it on a new line below, and comments the original. This is useful for testing alternative parameters, without deleting the original.
These are all setup to use python formatting, and the last one uses VS Code shortcuts.


#### Terminal shortcut
The first key on the fourth row is routed to Ctrl+ `. In VS Code, this switches between the code editor and the terminal.


#### Blank Keys
The last two keys currently have no function. Functions will likely be added in the future. For now, they serve as keys to fidget with while thinking.

## Challenges
This was my first time using both KiCad and 3d design software, meaning I had to learn the ins and outs of the software. I also attempted to use FreeCad on a pi 4, which in hindsight wasn't the best of ideas. It led to long loading times, slow software, and many crashes. It wasn't too bad, as these problems were minimized for most of the design process, and mostly caused problems when the PCB was loaded into the software. 

## BOM
- 12x Cherry MX Switches
- 12x DSA Keycaps(assorment of colors prefered)
- 12x SK6812 MINI-E LEDs
- 12x Through hole 1N4148 Diodes
- 1x EC11 Roatary Encoder
- 1x Seeed XIAO RP2040
- 4x M3 screws
- 4x M3 heatset inserets
- 1x 3d printed case(2 parts)

