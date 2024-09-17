# Hackpad

## Overview // your task!
This is a limited-time introductory YSWS (you ship, we ship) where *you* design your own macropad, and we'll ship it to you for free! With this YSWS, *you* can get stuff like this:

![Work louderxfigma](/assets/examples/worklouder.png)
![Lelepad](/assets/examples/lelepad.png)

This is something you definitely don't want to miss out, so make sure to join #hackpad in the slack!


<details>
<summary> <h3> Submission info & Details (click me)</summary>


#### You ship:
- A PCB Design and schematic
- Files for a case, either in STL or DXF format.
- Firmware for the keyboard. You are allowed to use QMK or other pre-existing firmware!

#### We'll send you:
- 3 PCBs! Keep one for yourself, or share some with your friends. Or you can keep them all, I won't judge.
- a Seeed XIAO RP2040 microcontroller. They're pretty nifty microcontrollers, so you can use them for something else too
- Switches! Choices TBD, but you'll have a great selection
- Other components you may need, such as LEDs, diodes, knobs, OLED screens, and more!
- Your case! You can either have it 3D printed, laser cut in acrylic, or both.
- A grab bag of DSA keycaps, and a custom Hack Club keycap too


You can get the macropads soldered if you don't have a soldering iron, or we can send you the parts directly if you're up for a soldering task. The only catch is that if you want it to be soldered, you *must* use through-hole components only!

#### Requirements:
- You design a macropad that integrates a [Seeed XIAO RP2040](https://wiki.seeedstudio.com/XIAO-RP2040/) as the main MCU. Nothing else allowed, sorry!
- It has 20 or less switches
- It is meaningfully unique to you. This could be as simple as making a custom layout and adding some decor, or as elaborate as writing an entire firmware in Rust
- The PCB only uses 2 layers
- Don't make a macropad with 40 screens. Or out of pure gold. Please!!

Once that's done, you can go on and make a PR. The instructions will be in the template.

</details>

## I have no clue how to make one!

Not to fret! There are a *ton* of guides out there that teach you every step of the way. For each task:

PCB Design:
- [ai03's PCB guide](https://wiki.ai03.com/books/pcb-design) (note: you can skip the part about wiring up the MCU)
- [How a matrix works (qmk)](https://docs.qmk.fm/how_a_matrix_works)
- Feel free to make a PR to add stuff here

CAD:
- Feel free to make a PR to add stuff here


Firmware:
- [QMK Documentation](https://docs.qmk.fm/newbs)
- [KMK Documentation](https://github.com/KMKfw/kmk_firmware)
- Feel free to make a PR to add stuff here

Misc great info:
- [Rollover, blocking and ghosting](https://deskthority.net/wiki/Rollover,_blocking_and_ghosting)
- Feel free to make a PR to add stuff here

## Anything else?

This YSWS is only guaranteed to run through September 30th, so make sure to get yours submitted before then. Depending on skill level, this should take roughly 6-12 hours to finish.

List of questions from the slack that you may want answered too:

### FAQ

Can I use SMD parts?
- You can! Only catch is that PCBAlex will not assemble them for you

How do I write the firmware without having hackpad available?
- Pre-existing firmwares like QMK and KMK are pretty reliable - we'll do a final check once we get your hackpad at HQ to make sure it actually works



Can I use... (for any of these you MUST write the firmware for it)
- IO expanders? YES!
- OLED displays? YES! Just make sure they're the small i2c ones
- Joysticks? YES!
- Rotary encoders? YES!
- a 70 inch TV? NO!!!!

How expensive can the components be?
- Please run by me what you want to get @alexren on the slack

When are we getting more guides???
- soonTM






