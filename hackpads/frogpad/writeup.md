# The PCB
The first step in my design was to create the pcb schematic.
This involved choosing what components to use and how they should be wired to each other. Overall, this was the easiest step in the design process, since
I am only using 15 switches and 1 rotary encoder.

The next step was for me to decide on a layout for my board.
I decided to go for an erginomic key layout. The encoder sits conveniently in a spot that could be considered a "nose." The macropad truly became a frog when
I decided that I wanted a unique outline and couldn't quite achieve what I was initally going for. During the case design, I was forced to relocate the SeeedStudio
XIAO RP2040 several times, to allow it to plug in better. I also modified the through-hole sizes several times for a similar reason: I needed the case to stay together.

I made many mistakes on the way of my project, and several times had to completely rebuild my case design. Although I encountered many setbacks, 
I still continued on. The hardest thing with designing the pcb was when I was forced to completely restart on the wire traces due to a slight layout change.

# The Case
For this step I decided to use Onshape. Since this was my first time using Onshape, this took longer than i had hoped for. Luckily, after learning the basics, it was pretty easy to design my case to fit my board. I'm really happy with how it turned out.

# The Firmware
In the past, i have mainly used python for my hardware projects (the only one to date being for bin.) However, in my mind, this project is more like professional design. Since this was the case, I decided to use a dedicated keyboard firmware tool: QMK. I struggled a lot on this step, since i couldn't immediatly find a good firmware base for the RP2040. In the end, I was able to finish the firmware succesfully, with support for the encoder and all 15 keys.

# In Retrospect
During the time spent designing my macropad, I learned more about how to use Kicad, Onshape and QMK. All of these tools were hard in there own way.

Kicad was difficult for me due to the unique board outline and drill hole sizes.

Onshape was tricky because it was my first time using 3D cad software other than Blender.

OMK was especially difficult due to lack of information on using a RP2040 microcontroller.
