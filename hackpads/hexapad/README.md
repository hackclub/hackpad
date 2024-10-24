# Hexapad

A DIY macropad made for the [Hack Club](https://hack.club) [Hackpad](https://hackpad.hackclub.com) program! It's got 16 Cherry MX switches, a "jewel" of 3 THT NeoPixels, a rotary encoder, and an OLED screen. A I/O expander is used to make everything work. This repo holds the PCB design, case design, and KMK firmware.

## Making it

This was my _first time_ doing... most of this. I've dabbled in mechanical keyboards before (I'm typing this on one right now!) but I've never touched PCB design or CAD. Therefore, I made the perfectly rational decision to YOLO it and try not to mess up. Thankfully, it went quite well! I think. I picked up KiCad really quickly, and the community (#hackpad on the Hack Club Slack) was super helpful. OnShape was harder to grasp but I think I kinda get it now? The firmware was super easy thanks to KMK, all I really had to do was paste in a few things from the docs.

For the schematic, I wired up the matrix (easy enough) directly to the microcontroller - a Seeed Studio Xiao RP2040. As I'm writing this I've realized I probably should have skipped the INT pin on the I/O expander and used that for the NeoPixels instead but oh well. To accomodate my rotary encoder and RGB I added a PCF8574A I/O expander, which was a little tricky to wire but I think I got it. Then I added my OLED display, my NeoPixels... and then took a three-week long break from the project.

After my break, I opened up the PCB editor and started cooking! It was actually really easy - all I had to do was arrange my parts nicely and add some graphics. Then I ran the FreeRouting autorouter which GREATLY speeded up my process.
With that done, I exported the 3D model of the PCB and put it into - oh wait. I don't have a CAD program of choice ¯\\\_(ツ)\_/¯

Following some recommendations from Hack Clubbers, I picked OnShape. It was super confusing at first, with all the mounting styles, different measurements, and fasteners. I ended up using a fully 3D printed sandwich mount but dropping the top plate. I sketched out a 102 x 102mm square (the size of my pcb + 2mm) then offset it by 12mm. I then added holes and hexagonal holes in the corners to accomodate M4 screws and nuts. I then made my plate with [Keyboard Layout Editor](https://keyboard-layout-editor.com/) and the [keeb.io plate generator](https://plate.keeb.io/) with a fillet of 0mm so nothing weird happened when I moved it around. Then after some quick sketching and decoration, the Hexapad was done! I made sure to import the PCB model and checked for fit. You can check out my design [here.](https://cad.onshape.com/documents/2133e09e1f245de59bbe7858/w/b4533889f6300572d81eb032/e/b0c575e6e2f32d509dfa7b54) _(note: this design's PCB model is outdated. I moved some things around to give more clearance.)_

Finally, I coded up the firmware. I don't really have much to say for this, it was just importing various modules and setting them up, then choosing things for the keymap.

Overall, I'm pretty happy with this project! It was super fun making everything, and I think I learnt some really useful skills. Of course, I haven't gotten it yet and I have no idea if it'll work... but let's hope it does.


## BOM

The Hexapad uses the following parts:

- **1x** Hexapad PCB
- **1x** SEEED Studio XIAO RP2040 microcontroller with pin headers
- **1x** PCF8574A I/O expander
- **16x** Gateron Milky Yellow Switches
- **16x** 1N4148 Diodes
- **3x** 10kΩ THT resistors
- **1x** 10uF THT capacitor
- **4x** 0.1uF THT capacitors
- **3x** [5mm THT NeoPixels](https://www.adafruit.com/product/1938)
- **1x** 0.91in OLED SSD1306 display
- **1x** EC11 rotary encoder
- **1x** 3D printed Hexapad case (preferably orange)
- **1x** 3D printed Hexapad plate (preferably orange)
- **4x** M4x0.7mm screws (25mm length)
- **4x** M4x0.7mm nuts (2mm to 6mm height, 6mm-7mm width)
- **16x** Cherry MX compatible keycaps
