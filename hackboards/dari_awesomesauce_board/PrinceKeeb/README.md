# PrinceKeeb

## Overview
The PrinceKeeb is an ortholinear, 84-key split keyboard. It is designed for ergonomic typing, and the use of RJ11(6p4c) jacks makes it hotpluggable. I designed it to help improve my touch typing and limit the strain of using a keyboard.

### PCB
I designed the pcb in KICAD. This keyboard is hotswappable, so I used a [MX hotswap switch footprint](https://github.com/daprice/keyswitches.pretty) I found on Github. Since this keyboard is split, the two halves are connected with RJ11 jacks via the UART protocol. I chose this connection method because it is hotpluggable, whTich means that you can plug and unplug the power cable without damaging the microcontroller(in this case the orpheus pico). There are mounting holes in the pcb to allow the screws to pass throgh it.

### Cases
I designed the the cases in Fusion 360. Each one consists of a bottom case and a plate to hold the keyswitches. The bottom case has standoffs to place heatset inserts, as I am using the tray mounting method. The plate has holes to accomodate the screws. On the underside of my plate, I made a rectangle around where the stabilizers would be, and decreased the thickness from the original 3mm to 1.5mm. In addition, I created a 1mm offset around each switch hole, and decreased the thickness of that area from 3mm to 1.5mm. This is so the keyswitches clip in to the plate properly.

### Firmware
I used KMK for the firmware, as it fully supports wired UART. [Link to the page in the KMK repository I used](https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/split_keyboards.md)

## Schematic
Left
![Screenshot 2025-03-16 224342](https://github.com/user-attachments/assets/083331bc-ae72-48b8-bd2c-ed01829d94de)

Right
![Screenshot 2025-03-16 225523](https://github.com/user-attachments/assets/f9ec0f50-a422-4d07-9d7f-33eb1d59c286)

## PCB
![image](https://github.com/user-attachments/assets/64459d5f-a114-4b20-a5d9-314ac80f526a)


## Case
Left
![Screenshot 2025-03-16 205816](https://github.com/user-attachments/assets/9240f575-ec98-4d1e-a5e5-d9f515af5d0f)

Right(Ignore the pcb in the background)
![image](https://github.com/user-attachments/assets/cabb4bdd-c175-4046-b5f7-a2a91bf4d5d7)


