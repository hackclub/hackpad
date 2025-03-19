**Just Another Hackboard**

It's what the title says, just another hackboard.
But seriously, this is a 75% keyboard which I designed over the course of a couple of days (and the case the night before :l) for fun and to see just how hard designing a keyboard could be!

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

![Screenshot 2025-03-19 131045](https://github.com/user-attachments/assets/6b96a7e5-b404-4ddf-ba90-d164c1382b23)

![Screenshot 2025-03-19 132216](https://github.com/user-attachments/assets/2ced3a89-f7ac-4f6c-bd33-fe66bea3cc22)

Top Case:

![image](https://github.com/user-attachments/assets/d4b6cd0a-bf35-4c06-92d8-75ab300db509)

Middle Case:

![image](https://github.com/user-attachments/assets/7d688780-1679-46d3-81bc-67f8b491f849)

Bottom Case (Top):

![image](https://github.com/user-attachments/assets/b8876218-29e2-4c5d-81bf-4acff671e48e)

Bottom Case (Underside):

![image](https://github.com/user-attachments/assets/61f3a54f-e2ba-4bb9-9c73-c83517b58732)

This is the part I changed after my initial PR since there was an issue with the switch holes not aligning properly with the switches themselves along with there not being holes for the stabilsers and 2 screws. This in itself took a while seeing as I initially eyeballed the measurements for the stabilisers before being told to just go to ai03's plate generator (which I should've done from the start). That turned out to be much quicker than scouring the internet for the dimensions thankfully).
After fixing those issues, I saw a nice design from aryatajne28's reaperboard (the middle plate which allowed for depth in the design) and decided to make one of my own - making the original topPlate the middle plate and creating a completely new top plate with pretty much a massive hole in it (but it works!).
I also changed how the art for my board is done - I liked the idea of seeing the MRC through the case but thought that a grate would look weird on the board. The top of my case also looked barren at the top due to it having a "massive forehead" (thanks ben) so I also had to find a solution for that. Luckily, I thought of the idea of using the top of the PCB (also barren) as the art, putting a lot of silkscreen art there to make it look nicer! This not only solved the art problem, but also lets me see the MRC (yay!).
The art includes boywithuke, chiikawa, orpheus and some handpicked quotes from my friends. I've put a gap in the top plate so I can put an acrylic plate there when I order my parts.
The feet of the case were ***heavily inspired*** (carbon copied) from my current keyboard (Logitech G513) since imo they're pretty perfect and I like them. Plus my hands are already used to the angle of my current keyboard so copying the feet in theory should make this keyboard also feel nice!
I've modelled the parts for the feet and stabilising holes separately and can ask a friend to print them for me instead of asking for them from HQ - if I need to add the files anyway just lmk!

Firmware:

There's not much to put here since I've learned a lot from the hackpad firmware incident, meaning this part only took like 30 minutes to do :D.
It's basic firmware (led controls, matrix and rotary encoder controls) which I plan on expanding and developing when I have the board to experiment with since it'll be easier to do then.
