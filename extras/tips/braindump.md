# Braindump

Here lies a braindump of everything useful I've picked up over the years. Will add more as I think of stuff

## The REALLY good stuff:
- Most DIY Keyboards are at least partially open source. You can go to their repositories on github

- Use [The Keyboard Atelier's discord](https://kbatelier.org/). Insanely useful resource to work with.

- You can export your KiCad PCB designs as a PDF and print them on paper to get a sense of scale.

## The good stuff
- Most keyboards are wired in a matrix instead of directly to the microcontroller to be more efficient with pins. [This QMK page](https://docs.qmk.fm/how_a_matrix_works) has a really good explanation.
    - If you have < 5 switches, avoid the matrix and just wire directly to the microcontroller

- Heatset inserts are a great way to fasten your print. Use 4.7mm diameter holes for the cavity, and then 3.4mm holes for the screws. I use [these](https://www.aliexpress.us/item/2255800046543591.html) ones made for 3D printed parts, picked it up from the VORONDesign sourcing guide.

- For designing your case, read this page on [keyboard mount styles](https://www.keyboard.university/200-courses/keyboard-mounting-styles-4lpp7)
- Generate your plates with [KLE (Keyboard layout editor)](https://www.keyboard-layout-editor.com/) and [ai03's plate generator](https://kbplate.ai03.com/)


## Cool tips
- Software I use // recommend:
    - CAD: Fusion360, Onshape
    - PCB Design: KiCad. Hands down.
    - Firmware: VSCode, but really doesn't matter
- Sketch out your design before making it. Helps a ton with being clear on what to do

### Adding parts

**Rotary Encoders**:
- Use the Rotary_Encoder:RotaryEncoder_Alps_EC11E-Switch_Vertical_H20mm footprint in KiCad. These are clickable EC11's, which is what you'll find 90% of the time.

**Screens**:
- Use generic i2c OLEDs
- For footprints, just use a 4-pin header

**Other**: \
Ask me on slack @alexren!

## Misc stuff
- Instead of using Kailh hotswap sockets, you can use millmax ones instead. They fit directly into regular Cherry MX switch footprints, and they actually work pretty well! I can do them for you. Example https://mech.land/products/mill-max-sockets
