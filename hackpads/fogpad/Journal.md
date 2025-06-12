# 26 May 2025
I finally decided to start highway by building a starter project. I researched on the web the potential designs I could use and the functionality that I could implement. I came across the qmk software and tinkered with it to learn the basics and flashed my spare keyboard in the hopes to reuse it (ended up breaking it and and luckily restoring it to the default firmware). Then I researched the layouts I could use that would be optimum and decided on a Numpad format with 2 knobs for volume, brightness and other controls. I also decided to add an OLED display to inform the user of messages, control music from spotify etc.
I finalised on these functionalities:
- Numpad Like Design
- Spotify Music Fetching and Playing
- Custom GIF and Image display on the screen
- Volume knob and Scrubber knob
- Macro functionality
- Bluetooth support
- Calculator
**Time Spent** : ~5.5 Hours

# 27 May 2025
I decided to get rid of Bluetooth as that would deviate too much from the Hackpad and I didn't wanna take on a custom project because I'm new to hardware. I also decided to scrap the numpad design and instead turn it into a WASD format to save space. I also planned on adding diodes in a matrix form to prevent ghosting. I decided to follow a guide from youtube to use a matrix wiring style and then made this schematic which would look more like a soup if not for tags

![schematic](https://github.com/user-attachments/assets/0249f4af-8c91-44dc-910f-cdf94b1ee42a)

Then I began wiring up the pcb which was a mess because I couldn't figure out how to compact the design. Then I began routing the wires which I did enjoy but took me some time to figure out the shortest path because my stupid a** BELIEVED THAT IT WOULD REDUCE LATENCY. Anyway, after figuring out a good enough layout, I finished the PCB

![pcb](https://github.com/user-attachments/assets/7e0d0e7b-ff2e-4fed-bc5a-e11675cd77c9)

After a feeling of pride that could even compete with drugs, I began working on the case. That was my biggest mistake. ＞﹏＜ 
- I couldn't get Fusion 360 to DOWNLOAD
- When I finally did, it took a million years to compile stuff and finally open
- When it did open, I couldn't find tools right in front of my eyes X﹏X
- After following the guide and generating a STEP file for my case, I closed the project without saving it.
- After figuring out how to open a STEP file with the help of ChatGPT, Gemini, and even Grok, I couldn't add the name.

TL;DR : I am not cut out for 3D Modelling.
![plate1](https://github.com/user-attachments/assets/4415e65e-a336-4f76-a677-980cc952df85)
![base1](https://github.com/user-attachments/assets/4b795606-9884-4f62-a183-5b32ef61a4a8)


Finally getting that done was the firmware time. I made a starter firmware that I could use for the keyboard by the time it was arriving while I worked on a better one that could do a lot more stuff. I will also release a desktop software with that so that it can communicate with the computer and perform everything properly. I hope that was everything

**Time Spent** : ~6.5-7 Hours
