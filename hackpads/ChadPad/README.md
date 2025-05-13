## ChadPad Macropad
This is my submission for the HackPad YSWS event. I have to admit, the design is lacking and could be way more polished, but I learned about HackPad 3 days before the submission date and therefore had a limited amount of time. 

The ChadPad includes 9x Choc V2 switches, each with its own SK6812 MINI LED for backlighting. There are also 4 additional RGB LEDs which can be programmed as indicators (Show if user is muted, deafened, etc.). The case includes channels which guide the light from the indicator LEDs to the top panel, with the idea that 3D printed icons can be inserted into the slots, and lit up by the LEDs. The current firmware has limited support for the LEDs, which will be rectified when I am able to debug it with the physical device. 

Im quite happy with how the design turned out, despite its shortcomings. If I had more time to work on it, I would definitely improve the case (I´ll probably print an improved version) and the firmware (Honestly I have no clue whether it will work or not, its quite hard to write firmware that you cant test). In hindsight, changing the switch layout to a matrix type would also be an improvement.

## PCB Screenshots

![Schematic Screenshot](https://cdn.hack.pet/slackcdn/3ce64c73d192c096a010f3dfe9e93135.png)
![PCB Screenshot](https://cdn.hackclubber.dev/slackcdn/d8379c542c32ca6b37fe968bdc94ba31.png)
![PCB-3D Screnshot](https://cdn.hackclubber.dev/slackcdn/8480b65bd1dd608ebc7b952a1d726b12.png)

## Case and instructions

![Case Screenshot](https://cdn.hackclubber.dev/slackcdn/9a77b300d45a2d4c367fcc823e627208.png)
![Case Bottom Screenshot](https://cdn.hack.pet/slackcdn/cce73c40b190106827b52dcfc2e812e7.png)

## BILL OF MATERIALS
9x Choc V2 switches (ideally blue but does not really matter)  
9x White 1U DSA keycaps    
13x SK6812 MINI-E LEDs  
1x SEEED XIAO RP2040  
1x 3D printed case (ideally white, black also works)  
1x PCB (ideally purple or black)  


## DISCLAIMER
Even though the submission requirements ask that DRC runs without issues, for some reason it complains about clearance on the XIAO pins, this is not an issue that would affect the function of the PCB, it is most likely an issue with me modifying the footprint and messing something up. If you do run DRC on the PCB, please ignore the XIAO pad errors. I attempted to fix it, but unfortunately I was unsuccessful.