# Perihelion ⌨️

Perihelion is a 4 key macropad with a OLED display and RGB underglow,
made for Hackclub's HackPad YSWS.

This is my first time using KiCad, so I had a lot of trouble with designing the PCB and wiring it correctly.
That's also the reason as to why the Macropad is extremely simple. If there will (ever) be a Perihelion v2,
I really want to add more to it!

## Renders

![Perihelion Macropad with top part opened](https://raw.githubusercontent.com/roschreiber/perihelion-hackpad/refs/heads/main/hackpads/perihelion/CAD/Renders/Assembled%20open.png)

![Perihelion Macropad with top part closed](https://raw.githubusercontent.com/roschreiber/perihelion-hackpad/refs/heads/main/hackpads/perihelion/CAD/Renders/Assembled.png)

![Perihelion Bottom Case](https://raw.githubusercontent.com/roschreiber/perihelion-hackpad/refs/heads/main/hackpads/perihelion/CAD/Renders/Case%20Bottom%20Render.png)

![Perihelion Top Case](https://raw.githubusercontent.com/roschreiber/perihelion-hackpad/refs/heads/main/hackpads/perihelion/CAD/Renders/Case%20Top%20Render.png)

![Perihelion PCB](https://raw.githubusercontent.com/roschreiber/perihelion-hackpad/refs/heads/main/hackpads/perihelion/CAD/Renders/PCB.png)

![KiCad PCB Front Render](https://raw.githubusercontent.com/roschreiber/perihelion-hackpad/refs/heads/main/hackpads/perihelion/PCB/Images/Front%20PCB.png)

![KiCad PCB Back Render](https://raw.githubusercontent.com/roschreiber/perihelion-hackpad/refs/heads/main/hackpads/perihelion/PCB/Images/Back%20PCB.png)

## BOM (Bill of Materials)

Everything you need to build your own Perihelion Macropad can be found in [BOM.md](./BOM.md).

## Features

- 4 key macropad
- OLED display
- RGB underglow
  - 7 SK6812MINI LEDs
- Multiple Button Modes!
  
## Software

This macropad is powered by **[KMK](https://github.com/KMKfw/kmk_firmware)**, a fork of QMK.
KMK allows you to get the following with the macropad:

- Multiple button modes! (layers)
- LED Control!
- Custom keymaps for macros!

