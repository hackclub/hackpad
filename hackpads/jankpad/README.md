# Janky Macropad #

This is my hackpad submission!

![image](assets/V3_full_front.png)

![image](assets/v3_full_back.png)

It features a 128x32 OLED display, 16 MX switches, and a rotary switche, the case is seperated into two three parts connected by screws

![image](assets/v3_case.png)

# Pretty PCB Pictures 

A 4x4 keyboard matrix is used to support 16 keys. An IO extender is used to give the XIAO enough pins to connect to the matrix and other components

![image](assets/v3_schematic.png)

![image](assets/v3_pcb_back.png)

![image](assets/v3_pcb_front.png)

# Design Process #

I wanted to challenge myself by trying to route as many components as possible on my pcb.
Because of this the, first Jankpad had almost every item in the approved list. 
I was able to fit 16 switches, 16 leds, an OLED, and 2 diodes on the V1 using an IO expander.

![assets/full.png]

Jankpad V3 managed to slim down the design at the cost of a rotary encoder, as I learned that I could place components on the back side of the board.

# Reflection #

I'm pretty proud of Jankpad V3, and it baffles me that I was able to go from never having touched kicad to having designed my own macropad from scratch in a span of two days

My goal with making this hackpad was to familiarize PCB design, which I think I definitely accomplished here today. 

# BOM #

- 3D printed case parts
- PCB
- 1 Seeed XIAO RP2040 SMD
- 16 MX-Style Switches
- 16 1N4148 Diodes
- 16 SK6812 LEDs
- 16 Keycaps
- 1 EC11 Rotary encoder
- 1 MCP23017
- 0.96 inch OLED
- 5 M3x16mm screws
- 10 M3x5mx4mm heatset inserts

