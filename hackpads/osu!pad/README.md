# Osu!Pad

Osu!Pad is a 3 key macropad optimised for Osu! gameplay to make sure your click the circles better.

## Inspiration
I'm an avid Osu! player, as one is, and I've wanted to buy a 3-key macropad for a long time but didn't think it was a "good" purchase. So I delayed it. Thats when I discovered Hackpad where I was able to make my dream of a 3-key macropad come true

## Challenges
I am a complete beginner at everything Electrical so that includes the PCB and the Schematic. I learnt some of these skills through my parents. The CAD was a completely new thing, so a friend of mine helped me build it in blender such as teaching what the buttons do etc.

## Features:
- Designed in blender
- Optimised for osu gameplay with just 4 buttons (including the rotary encoder!!)
- Uses the EC11 Rotary Encoder (and its inbuilt switch) to control volume (and mute mic)

## CAD Model:
My Osu!Pad uses no screws to attach the top and bottom since the fit together. I made both the top and bottom in 1 file while still being under the 200x200 dimensions.

Final Case CAD
<img src="/hackpads/osu!pad/assets/case.png" alt="CAD" width="800"/>

## Schematic:
I built my schematic using KiCad

Final Schematic
<img src="/hackpads/osu!pad/assets/schematic.png" alt="schematic" width="800"/>

## PCB:
I built my PCB using KiCad

Final PCB
<img src="/hackpads/osu!pad/assets/pcb.png" alt="pcb" width="800"/>

## Firmware Overview
The osu!pad uses KMK with python for the firmware

The code seems to work as I've checked with other peers

## BOM:
This is everything needed to make HackPanel:

- 3x Cherry MX Switches
- 3x DSA Keycaps
- 1x EC11 Rotary Encoder
- 1x XIAO RP2040
- 1x Case (2 parts, 1 file)