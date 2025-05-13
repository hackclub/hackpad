# DawPad

![PCB Render](https://github.com/user-attachments/assets/7b59db36-3e2d-4628-bedd-b27dfa3b1bc2)

This is a small MIDI controller designed to make it a bit easier to control a DAW. It won't really do anything on its own, but with a good input map it will be a nice extenison of the DAW interface (I can see it being used as a controller for a few audio channels - the knobs could be used for gains, and the buttons could be channel parameters like mute, as well as a couple other things like playback controls).

## PCB

I'm pretty happy with how the PCB turned out for this. This is the first PCB that I'm actually getting made, and it's also the most complicated one that I've designed by far. I tried to keep things pretty neat, and I managed to keep everything reasonably compact while still keeping pretty much everything I could through-hole, which I'm much more comfortable with soldering.

![PCB Schematic](https://github.com/user-attachments/assets/5df3af07-ee74-4963-803d-1f5e063a1c76)

![PCB Layout](https://github.com/user-attachments/assets/08c3af90-4070-4fa1-94d4-e2376163b0e2)

## Firmware

The firmware for the DawPad is built in Arduino, using the [Control-Surface](https://tttapa.github.io/Control-Surface/Doxygen/index.html) library for MIDI functionality. At the moment, it likely doesn't really work at all, but a lot of the (likely) broken stuff is related to the I/O expander, which I can't really debug without the actual hardware. Some more detailed information about building this can be found in the firmware README.

## Case

The case for the DawPad is designed in Onshape (you can find a link to the document in the CAD README). I don't really know what I'm doing when it comes to CAD, so it's definitely a bit messy, but it should work. The case is designed to be 3D printed, and is bolted together with a couple M3 screws.

![image](https://github.com/user-attachments/assets/a7793793-4ef6-4b50-baef-528941c3cd3b)

## BOM

Here's the components needed to make this.

* 1x XIAO RP2040
* 1x MCP23017
* 12x 1N4148 DO-35 Diodes
* 2x 4.7k THT Resistor
* 12x Cherry MX switches
* 4x EC11 Rotary Encoder (preferably one without detents and with a reasonably high resolution)
* 4x SK6812 MINI (regular mount)
* 12x SK6812 MINI-E (reverse mount)
