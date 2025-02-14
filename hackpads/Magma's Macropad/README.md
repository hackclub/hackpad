# Magma's Macropad

![](https://cdn.hackclubber.dev/slackcdn/069b79df7569e9e1600e752b3b9bc1d4.png)


**Inspiration**

I wanted to create a macropad that helped me move around in video games easier. I used an rp2040, 4 switches and a rotary encoder for the volume.

**Challenges**

This was my first time using fusion 360 and kicad, so it was quite tough. however, after learning how to use these softwares, i feel more comfortable with PCBs and 3D design.

**Specifications**

BOM:
 - 4x Cherry MX switches
 - 1x SK6812 MINI Led
 - 1x XIAO RP2040
 - 4x blank DSA keycaps
 - 1x RotaryEncoder Alps EC11E Vertical H20mm
 - 4x M3x16mm screws
 - 4x M3x5mmx4mm heatset inserts
 - 4x Through-hole 1N4148 Diodes

Others:
 - KMK Firmware
 - Macropad Case.STEP
 - Macropadtop.STEP


| **Schematic** | **PCB** | **Case** |
|---------------|---------|----------|
|![](https://cdn.hack.pet/slackcdn/2a1ae648924a0e662cd118a8f83509fe.png)|![](https://cdn.hack.pet/slackcdn/48e177c8b59bb30721047313a89f933d.png)|![](https://cdn.hack.pet/slackcdn/a95901f19c3e030a88db1f98165ba00d.png)|

**Firmware**

The firmware uses kmk. the keys are laid out in a COL2ROW manner, like arrow or WASD keys. The rotary encoder helps increase and decrease volume of the system.
