**Just Another Hackboard**

It's what the title says, just another hackboard.
But seriously, this is a 75% keyboard which I designed over the course of a couple of days (and the case the night before :l) for fun and to see just how hard designing a keyboard could be!

Spoilers: It was difficult.

Schematic:
![image](https://github.com/user-attachments/assets/995d8fcf-d1aa-4701-a841-ec692e2b851e)
![image](https://github.com/user-attachments/assets/6f2aa29f-deaf-46ef-ac56-3ba0a11f4d1b)
![image](https://github.com/user-attachments/assets/6607ca3a-f9d2-424d-bef2-c37913acca1f)

Arguably the easiest part of the project, the schematic was more just tedious in the sense that wiring the LED matrix along with the switches got pretty tiring after the first 5 or so minutes.
However, it didn't take me too long to make the whole schematic, people on slack helped me with choosing the correct MRC to wire it all to.

PCB:
![image](https://github.com/user-attachments/assets/803a2887-6a9a-4668-bb07-e77ac93b76c2)

Ever felt like wiring 700 wires on a pcb? Well now you can!
The pcb design was probably my favourite part and took me more than a few hours over a few days to get all the wiring done to a point where I was happy with it.
The initial positioning also took a while because I was pulling my hair out trying to calculate the sizes of different keycaps (e.g. Tab and caps lock) so the keycaps didn't overlap.
That *was* until I was helping someone on slack and saw they had different sized outlines for the keycaps and decided to take a second look at the footprint library... and lo and behold, people aren't masochists and made different sized footprints for the different keys...
Good news - I got all the measurements right on my own :D.
Bad news - I wasted about an hour doing that :(.

I didn't add all the 3D models for the switches since I'm *very* out of time for this (currently 11:30pm on a Sunday :c) but lmk if I need to and I'll update all the images and this readme!

Case:
Top Plate:
![image](https://github.com/user-attachments/assets/88872136-6cb2-4fa4-95ba-4c3f6e1b1ae6)

Cutout Under Art:
![image](https://github.com/user-attachments/assets/7847d267-b314-471c-9009-b9db5ed48c5a)

Back Plate:
![image](https://github.com/user-attachments/assets/2b08dbfc-efa7-4d10-93f1-09cf3876aa3b)

Underside Of Back Plate:
![image](https://github.com/user-attachments/assets/20276ce0-2502-481e-8fe0-9f99cd33e8ac)

This is the part I underestimated this time around.
I thought this might take a couple of hours (like maybe 4 or 5??). But no, this took me 8-9 hours to make and made me realise how slow of a worker I am.
That doesn't matter now though, because I'm done! (or at least I hope I am).
The case is just a normal rectangular case with some touches from me, them being:
- My *spectacular* art at the top of the top plate. These are cutouts of orpheus and chiikawa (whom I DID NOT do justice to in my drawing) which I will put another coloured 3D printed plate behind in order to add colour. You can see this in image 2, where under the cutouts the thickness of the top plate is 1mm instead of 2mm.
- Some stabilising holes inside the bottom plate to help align the pcb when I build the keyboard.
- Holes for the keyboard feet to fit inside of along with the hinge for them.
I've modelled the parts for the feet and stabilising holes separately and can most likely ask a friend to print them for me instead of asking for them from HQ - if I need to add the files anyway just lmk!

Firmware:

There's not much to put here since I've learned a lot from the hackpad firmware incident, meaning this part only took like 30 minutes to do :D.
It's basic firmware (led controls, matrix and rotary encoder controls) which I plan on expanding and developing when I have the board to experiment with since it'll be easier to do then.

Note:
The things in this PR will be modified to improve upon them, I just didn't have time to improve upon them tonight (sorry) but any needed fixes and changes will be made tomorrow (or today even).
