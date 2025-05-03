---
modified: 2025-02-20T21:09:22-07:00
---
# JoyKey
This is a small macropad that simultaneously acts as game controller and an entertainment device. 

The name is inspired by the Nintendo JoyCon portmanteau (Joystick Controller) except I have replaced the 2nd word with "Keypad" (Joystick Keypad). See [name ideas](name%20ideas.md) for other things I came up with.

My main repo were development will continue: https://github.com/techy-robot/JoyKey

# Features
- Customizable macro pad using QMK firmware
- Game controller mimicking a joy-con
- Offline games that can be played on the display with no connections
- Small handheld size
- Linear keys

# Approoved Parts BOM
- 8 Cherry mx Red keys with clear shell variant
- 8 Black keycaps
- 128x64 px SSD1306-based monochrome display near the top
- SEEED Xiao RP2040 (can be replaced later w/ SEEED xiao MG24 or nRF52840 Sense for BLE and other goodies)
- 12 Sk6812 Mini-E reverse mount RGB leds
- 3 M3x16 screws and M3 heatsets
- 12 1N4148 diodes. (I may get the 1N4148 W varient for SMD)

# Extra Parts BOM
- 1 Analog PS2 Joystick (I already have)
- 1 **EC12** encoder 8.5mm tall (flat volume dial on the side)
- AP2112K-3.3 Linear Regulator
- MCP73831-2-OT Lipo Battery Charger
- 4 10uf 0805 capacitors
- DMG3415 Sot23-3 PMOS
- 3 10k 0805 resistors
- 1 2k 0805 resistor
- 1 0603 LED

# Pictures

## Case
![](media/Case%20Bottom.png)

![](media/Case%20Front.png)

![](media/Case%20Inside.png)

![](media/Case%20Top.png)

![](media/Final%20View.png)

## PCB
Bottom
![](media/Board%20Bottom.png)
Top
![](media/Board%20Top.png)

## Schematic
![](media/Schem%201.png)

![](media/Schem%202.png)

![](media/Schem%203.png)

![](media/Schem%204.png)

![](media/Schem%205.png)