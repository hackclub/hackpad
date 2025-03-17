This is a keyboard that tries to mimic the feel of the Apple Magic Keyboard but with more customizability and a little more travel distance. Also no keycaps because target practice (read BOM)

# Features
- Is a keyboard
- Has some encoders
- Has an OLED that you'll never look at

# BOM
- PCB (two parts, JLCPCB black?)
- 2x Orpheus Picos (Hackclub HQ)
- 90x key switches (Gateron Low Profile KS-33, https://www.gateron.co/products/gateron-low-profile-mechanical-switch-set?variant=41935580823641)
- 90x 1N4148 diodes (https://www.digikey.com/en/products/detail/onsemi/1n4148/458603)
- 0x key caps because target practice (I'll 3D print them because of the way they're laid out on the PCB but I haven't done that yet)
- 1x 0.96" SSD1306 OLED (https://www.digikey.com/en/products/detail/universal-solder-electronics-ltd/26095/16822116)
- 2x EC11 rotary encoders (https://www.digikey.com/en/products/detail/bourns-inc/PEC11R-4220K-S0024/6164059)
- 2x 4.7k pull up resistors (I used 1/4 watt ones but any work, self-supplied)

DO NOT PRINT THE CASE! I am currently making one with wood (no CNC) so stay updated. If I give up still don't make the case because I'll have a better one eventually. 

# CAD
![Schematic](https://github.com/Omegon0/hackpad/blob/8d51c22a4dad73814eff892e6db910a267227f93/hackboards/targetpractice/schematic.png)
![PCB](https://github.com/Omegon0/hackpad/blob/8d51c22a4dad73814eff892e6db910a267227f93/hackboards/targetpractice/pcb.png)
![CAD](https://github.com/Omegon0/hackpad/blob/8d51c22a4dad73814eff892e6db910a267227f93/hackboards/targetpractice/cad.png)

# Firmware
Uses QMK because I don't know how to use KMK
