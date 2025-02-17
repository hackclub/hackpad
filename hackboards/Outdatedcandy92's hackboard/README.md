## Hackpad V2

Don't have a name for it yet :c

It's a 75% compact keyboard with an oled display and 2 rotary encoders

### Inspiration
I wanted to create a keyboard that was approximatly the same size as my current keychron k2 but with additional components on top, like the 2 rotary encoders (which im gonna use for audio and playback), and an oled screen (to display cool stuff 😎)

### Challenges
uhhh, routing this was a nightmare. my original plan was to have per key lighting but I quickly decided that it was not worth it after routing up all the switches, instead of per key I opted for a light bar at the top (which I would make reactive to music maybe?). 

### BOM

- 1 x Raspberry Pi Pico or Orpheus Pico (With headers preferably) (I'm assuming they have the same pinout)
- 1 x PCB
- 1 x 3D Case (3 parts- top, bottom and plate)
- 1 x Acrylic part 
- 2 x EC11 15mm Rotary Encoder
- 1 x MCP23017_SO
- 84 x [Cherry MX2A Blue 60g Clicky Switch (PCB Mount) ](https://mechanicalkeyboards.com/products/cherry-mx2a-blue-60g-clicky?variant=48020492058924)
- 84 x 1N4148 diodes
- 84 x White Keycaps (75% compact)
    - 1 x 6.25u (space)
    - 2 x 2.25u (enter,shift)
    - 1 x 2.00u (backspace)
    - 2 x 1.75u (caps lock, shift)
    - 2 x 1.5u (tab, backslash)
    - 3 x 1.25u (win,ctrl,alt)
    - 73 x 1.00u
- 3 x MX 2.00u Stabilizer
- 1 x MX 6.25u Stabilizer
- 1 x SSD1306 128x32 OLED (sda,scl,vcc,gnd)
- 8 x SK6812-MINI-E LED

### CAD Model:

![Image](https://github.com/user-attachments/assets/7b87e407-d79c-497e-8629-5d52ffbd069a)

![Image](https://github.com/user-attachments/assets/b7d5115e-8d71-42ef-a7a1-eefe91df1a06)
-- 
Bottom Part
![Image](https://github.com/user-attachments/assets/9d59f530-49e7-46e2-8a70-9a6b51ce71f0)
Top Part
![Image](https://github.com/user-attachments/assets/19641d7b-f417-4e17-a85a-54d3cf9efcf0)


### PCB & Schematic

![Image](https://github.com/user-attachments/assets/5e753087-a1a0-417e-b721-aec991e8f0ec)

![Image](https://github.com/user-attachments/assets/0207cbf5-97eb-4c43-ad57-8f1611828219)

### Firmware

Firmware was written using kmk. (no idea if it work rn tho)
