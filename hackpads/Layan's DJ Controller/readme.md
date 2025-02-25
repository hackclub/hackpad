
# Layan's DJ Controller

This is a macropad that I have designed for the Hackpad YSWS from Hack Club.

It has components that can be mapped to DJ software and uses KMK Python firmware.
## Features

- 3d printed case
- 8 Cherry MX switches
- 6 EC11 Rotary encoders
- 2 Bourns slide potentiometers
- 2 RGB LEDs
## CAD Model

It should all fit together nicely with a few bolts using the holes provided in the case.

There are two separate 3d prints for the case which go together, with the PCB in the middle.

![Screenshot of case](https://github.com/LayanJethwa/dj-controller-hackpad/blob/main/assets/full-model.png)

![Screenshot of case bottom](https://github.com/LayanJethwa/dj-controller-hackpad/blob/main/assets/bottom-model.png)

![Screenshot of case top](https://github.com/LayanJethwa/dj-controller-hackpad/blob/main/assets/top-model.png)

![Screenshot of PCB model](https://github.com/LayanJethwa/dj-controller-hackpad/blob/main/assets/pcb-model.png)

Made in Fusion360.
## PCB

Here is the PCB, made in KiCad. I spent a lot of time on the wiring (I thought it was a topology problem and then realised you can use the back as well)

Schematic
![Schematic](https://github.com/LayanJethwa/dj-controller-hackpad/blob/main/assets/schematic.png)

PCB
![PCB](https://github.com/LayanJethwa/dj-controller-hackpad/blob/main/assets/pcb.png)
## Firmware Overview

The controller uses KMK Firmware, it is not currently interfaced with the DJ software (I use VirtualDJ) as I don't yet have the hardware for testing.
## BOM

This should be all the materials needed to make the controller:

- 1x XIAO SEEED RP2040: XIAO-RP2040-DIP
- 1x MCP23017-SO: Package_SO:SOIC-28W_7.5x17.9mm_P1.27mm
- 2x LEDs: LED_SK6812MINI_PLCC4_3.5x3.5mm_P1.75mm
- 2x Bourns slide potentiometer: TRIM_PTA4543-2015DPA103
- 2x 4.7kΩ resistors: R_Axial_DIN0204_L3.6mm_D1.6mm_P7.62mm_Horizontal
- 8x Cherry MX switches: SW_Cherry_MX_1.00u_PCB
- 2x Alps rotary encoders: RotaryEncoder_Alps_EC11E_Vertical_H20mm