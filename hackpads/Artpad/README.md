# Artpad  
This is the Artpad, a macro pad created created to be compatible with the [artsey.io](https://artsey.io/) keyboard layout. It currently has firmware that uses it as a macro pad, but in the future, I intend to convert it to use the artsey layout.  
The features of this macro pad include an expansion port with easy access to the gpio of the Seeed Xiao RP2040 so that with only a small change to the firmware, add a new module can be added to the board to extend its functionality. This can include things like extra keys, rotary encoders, or even oled screens or leds.  
The Artpad was designed with asthetics in mind. It has a window in the plate to give a view of the pcb, where there is a neatly lined up row of diodes and the microcontroller. This also allows easy access to the reset and bootloader buttons for a much easier time updating firmware. It may also be possible to add rgb funcionality to this board because the Seeed Xiao RP2040 has a built-in neopixel led.  

![Artpad_front](https://github.com/user-attachments/assets/416c0d17-56d7-4888-9174-a453d4cc3bfa)

![Artpad_angle2](https://github.com/user-attachments/assets/8bc669ec-5949-454f-bbb4-294408ddb023)

![Artpad_angle1](https://github.com/user-attachments/assets/fcd46eb0-6238-4ed0-b085-4991f6ccf03c)

![image](https://github.com/user-attachments/assets/405760e8-94c6-4f2a-b917-42f50aeee882)

![image](https://github.com/user-attachments/assets/79c5e09d-6c15-4b7b-80c9-bdec61c5d68c)

![image](https://github.com/user-attachments/assets/14e39728-8bc9-4831-9eb2-ba2cb5048c71)

![Artpad_expanded](https://github.com/user-attachments/assets/ce4f4f78-586a-4981-b197-84be23a3a03d)

# BOM  
### PCB
- 8 MX switches (preferably something with a very light spring, under 40 grams)
- 8 Kalih MX hotswap sockets
- 1 2x7 horizontal female 2.54mm header (digikey part number S5560-ND)
- 1 Seeed Xiao RP2040 microcontroler
- 2 1x7 2.54mm pitch header pins
- 8 1n4148 through hole diodes
- 1 PCB
### Case  
- 4 m3 heat set inserts
- 4 m3x16mm hex socket cap head screws
- 1 plate
- 1 case
- 1 plate rim

Because this uses surface mount hotswap sockets I am perfectly fine with soldering everything myself.
