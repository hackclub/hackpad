# Sammie's Chonkpad
A macropad I think might be somewhat chonky

Note: I did not include the OPL submodule + other stuff, you can see https://github.com/sz6084/hackpad-self for the full repository.

![Hackpad-case v12](https://github.com/user-attachments/assets/5aa71cc5-84b1-45f7-84d2-9d4e23bbaadc)

### Inspiration

I wanted to create a macropad for the keys I lost when i moved from daily-driving a laptop to a PC. Specifically, keys like Rewind, Play/Pause, and Next. These keys were not part of my laptop's function key alternates-they were dedicated buttons which I missed since my current keyboard, a (surprisingly decent and fully-sized) membrane keyboard, only had function keys with no dedicated media buttons. This is definitely not something everyone agrees with (and I find binding my function keys would be too tedious, especially since my old laptop did not have these bound to function keys anyways). It has 16 switches (numpad functions too!), 1 rp2040, and no LEDs (I don't want the hassle and my membrane keyboard doesn't have it anyways, thought RGB in a future macropad would be cool). Something else I might consider is using Choc v2 switches but since the guide used Cherry MX switches I decided to do the same.


### Challenge

I had never designed a macropad before, let alone use Fusion360 or KiCAD at all. I followed the online guide (thanks @Cyao but please update it!) and consulted my trusty friend who had more experience than I did. I also asked questions in the Hack Club Slack.


### Specifications

BOM:
 - 16x Cherry MX switches
 - 16x 1N4148 diodes
 - 1x XIAO RP2040
 - 16x Blank DSA keycaps
 - 4x M3x16 Bolt
 - 4x M3 Heatset

Others:
 - KMK firmware
 - Top_Plate.stl
 - Bottom_Case.stl

Schematic            |  PCB         |   Case
:-------------------------:|:-------------------------:|:-------------------------:|
![image](https://github.com/user-attachments/assets/377f4dae-6c65-4e2d-9600-ef55ea8351d8)  |  ![image](https://github.com/user-attachments/assets/f171720a-bc69-4301-b0b4-cf3f069113da)  |  ![Hackpad-case v13](https://github.com/user-attachments/assets/f433e493-c04b-4526-92c6-a2f8bdb94357)
