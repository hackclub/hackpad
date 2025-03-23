**Just Another Hackboard**

It's what the title says, just another hackboard.
But seriously, this is a 75% keyboard which I designed over the course of a couple of days for fun and to see just how hard designing a keyboard could be!

Spoilers: It was difficult.

Schematic:
![image](https://github.com/user-attachments/assets/e7a38927-3d77-436f-b328-701bc1124f09)
![image](https://github.com/user-attachments/assets/6f2aa29f-deaf-46ef-ac56-3ba0a11f4d1b)
![image](https://github.com/user-attachments/assets/6607ca3a-f9d2-424d-bef2-c37913acca1f)

Arguably the easiest part of the project, the schematic was more just tedious in the sense that wiring the LED matrix along with the switches got pretty tiring after the first 5 or so minutes.
However, it didn't take me too long to make the whole schematic, people on slack helped me with choosing the correct MRC to wire it all to.

PCB:

![image](https://github.com/user-attachments/assets/79c1f397-91e0-4369-9c15-ad88463334f2)

Ever felt like wiring 700 wires on a pcb? Well now you can!
The pcb design was probably my favourite part and took me more than a few hours over a few days to get all the wiring done to a point where I was happy with it.
The initial positioning also took a while because I was pulling my hair out trying to calculate the sizes of different keycaps (e.g. Tab and caps lock) so the keycaps didn't overlap.
That *was* until I was helping someone on slack and saw they had different sized outlines for the keycaps and decided to take a second look at the footprint library... and lo and behold, people aren't masochists and made different sized footprints for the different keys...
Good news - I got all the measurements right on my own :D.
Bad news - I wasted about an hour doing that :(.

Case:

Fully Assembled:

![image](https://github.com/user-attachments/assets/4ea43f57-9278-49d4-b2c0-d80f60a2ee00)

![image](https://github.com/user-attachments/assets/c912326d-1a4c-4c4a-937b-f37688a0bf6c)

(Note: MRC pins are clipping through the case in the second screenshot, this shouldn't be an issue when building the keyboard to the best of my knowledge)

Top Case:

![image](https://github.com/user-attachments/assets/c15ccecc-b048-4b0d-b3d6-72bb347be2b7)

![image](https://github.com/user-attachments/assets/7147ca92-0de1-4036-9acf-cbc7e33c0398)

Bottom Case:

![image](https://github.com/user-attachments/assets/411e294e-dc8e-4765-ad6c-d305704a2e55)

![image](https://github.com/user-attachments/assets/40052b47-057d-46b4-a31c-3b82b084adfb)

This is the part I changed after my initial PR since there was an issue with the switch holes not aligning properly with the switches themselves along with there not being holes for the stabilsers and 2 screws. This in itself took a while seeing as I initially eyeballed the measurements for the stabilisers before being told to just go to ai03's plate generator (which I should've done from the start). That turned out to be much quicker than scouring the internet for the dimensions thankfully).
After fixing those issues, I saw a nice design from aryatajne28's reaperboard and decided to make one of my own - initially making a separate top and middle plate but merging them in the end in order to fix an issue where screwing the case together wouldn't actually attach the case layers.
I also changed how the art for my board is done - I liked the idea of seeing the MRC through the case but thought that a grate would look weird on the board. The top of my case also looked barren at the top due to it having a "massive forehead" (thanks ben) so I also had to find a solution for that. Luckily, I thought of the idea of using the top of the PCB (also barren) as the art, putting a lot of silkscreen art there to make it look nicer! This not only solved the art problem, but also lets me see the MRC (yay!).
The art includes boywithuke, chiikawa, orpheus and some handpicked quotes from my friends. I've put a gap in the top plate so I can put an acrylic plate there when I order my parts.
The feet of the case were ***heavily inspired*** (carbon copied) from my current keyboard (Logitech G513) since imo they're pretty perfect and I like them. Plus my hands are already used to the angle of my current keyboard so copying the feet in theory should make this keyboard also feel nice!
I've modelled the parts for the feet and stabilising holes separately and can ask a friend to print them for me instead of asking for them from HQ - if I need to add the files anyway just lmk!

Firmware:

There's not much to put here since I've learned a lot from the hackpad firmware incident, meaning this part only took like 30 minutes to do :D.
It's basic firmware (led controls, matrix and rotary encoder controls) which I plan on expanding and developing when I have the board to experiment with since it'll be easier to do then.
