# QOLPad

The QOLPad (Quality Of Life Pad) is a 6 key macropad designed fooorr, about anything which minorly inconveniences me in day-to-day life.
Too hard to press your hotkey for deafening in discord? Well now you can use the QOLPad, an entirely different keyboard for deafening yourself (among other things)!
But seriously, this macropad is used for discord hotkeys, media and volume control, featuring skipping and rewinding songs and a rotary encoder for easier control of volume!

CAD Design:
![image](https://github.com/user-attachments/assets/5ce9eabe-ca9a-4400-839e-e98805dabedd)
![image](https://github.com/user-attachments/assets/b8eb4b18-26bd-403c-b3a4-eb7c26b96b4b)

The top image image shows the pcb and case parts in 1 file fitting together. I sadly didn't have time to import the 3D models for the footprints :c since I had *too* much trouble finding out how to code the firmware, leading me to be writing this readme about 3 hours before the deadline :l. From what I could see, the 3D models weren't required and I made sure that every switch and the MRC each had enough space to fit inside the case (shown in the second topdown image). I planned to use Cherry MX Brown switches so on the pcb I used a cherry MX 1.00u footprint for the switches. As for the rotary encoder, I used the EC11E footprint with circular mounting holes.

PCB:
Schematic:
![image](https://github.com/user-attachments/assets/7e27b659-25d0-4383-8e0a-2b9e0aa7cc1e)

The schematic itself wasn't actually too difficult to do once I found the footprints for each component and got some help from a friend about the ports for the LEDs (SK6812 MINI-Es). Just had to make some global labels and search up how to do a matrix layout and I was set!

Layout (Without back silkscreen art):

![image](https://github.com/user-attachments/assets/17fecf9d-68d9-4603-acc8-514441187dff)

Oh God, the layout. Actually deciding on the layout caused me to add another key to make it look nicer along with the rotary encoder which caused a massive headache since this was after initially wiring it. Furthermore, since I was told that my wiring was ***atrocious*** I rewired the layout *4 times* until I finally managed to get a decent wiring layout. This took ~3 days along with the mandatory procrastination and college work. However, in the end I was really pleased with how it turned out! I don't think I could've done much better given the timeframe.

Firmware:

The bane of my existance (and exhibit A for my lack of common sense). This took ***WAY*** too long because of me jumping around from KMK to QMK and bashing my head against the documentation for 3 hours before I realised that I'd missed the initial pin numbers on the MRC... After that and the pain of figuring out how to install KMK and use the modules, it took me ~1 hour to make the firmware. However, due to my lack of eyes and subpar reading skills, this section took me around 8 hours (yes I know it's bad).

Even with the firmware issues, I really enjoyed making a hackpad (even if it is a bit simple) and it's gotten me interested more in CAD and PCB design as a whole!

Potential Issues:
When running DRC in the pcb layout designer, there are ~30 errors, however these are from the reverse mounted neopixels having too little clearance. From the guide of common DRC errors, I was told to ignore this however please lmk if this is incorrect and if anything needs changing!
