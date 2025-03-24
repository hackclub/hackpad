## Isaiah's Shortcut Hackpad
My hackpad project to create a macropad for the Hack Club YWSW, and to learn about macropad / keyboard design! My hackpad uses 9 switches in a basic 3x3 configuration, as well as 2 LED lights, and the RP2040 microcontroller. I was starting from scratch for all but the CAD part of this project, so there was a big learning curve, but I've learned a lot about PCB design (schematics/layout) and also firmware through this project! My hackpad primarily functions for keyboard shortcuts for easy convenience, currently set with the volume buttons, control/shift, and the directional arrows.
![Screenshot 2025-02-19 103913](https://github.com/user-attachments/assets/63cddc35-e154-438c-93a1-52afed3ca97f)


# PCB
This took me a while to learn initially, but after I started getting the hang of the software I learned a lot! 
![Screenshot 2025-02-19 104112](https://github.com/user-attachments/assets/90d3ff82-ab86-498a-95ff-d6f31835dd50)
![Screenshot 2025-02-19 104001](https://github.com/user-attachments/assets/93ae264f-7256-40ac-b1fa-140643fddd7d)

# CAD
I already knew how to design in CAD, the only hard part for me on this part was figuring out the dimensions of the switches for the top part of the case.
![Screenshot 2025-02-19 223053](https://github.com/user-attachments/assets/096e9b92-f93e-4c75-b3f0-9b7ba720dd8b)

# Challenges/Inspiration
I had no particular inspiration for my design, I just wanted to learn the process on how to create a macropad! My design evolved along the way as I stumbled through from step to step, and slowly learned and understood more of what I was doing. Eventually, I settled on a simple design with 9 switches in the 3x3 configuration. I was challenged a lot in kicad, as I tried to learn how to use the software and what the different parts of the schematic meant - this was my first foray into anything of this sort! I also had some struggles with QMK, mainly due to me being silly and making syntax errors that took me a while to find.

# BOM
* 1x Seeed XIAO RP2040
* 2x SK6812 MINI-E LEDs
* 4x M3x16mm screws
* 4x M3 Heatset
* 9x Through-hole 1N4148 Diodes
* 9x Blank DSA keycaps (3 red, 4 white, 2 black)
* 9x Cherry MX Brown Switches
