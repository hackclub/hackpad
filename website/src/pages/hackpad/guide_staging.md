# Make your own Hackpad!

(sketch & collage of random hackpad layouts)

Hey there! Welcome to the guide!

In this guide, we're going to be making a super simple 3x1 macropad - it'll look something like this!

(image of macropad, pre-polish)

If you ever need help, make sure to join the [Hack Club Slack!](https://hackclub.com/slack)

**Anything unclear? Head on over to the [FAQ](/faq)!**

Copying this guide won't get you a project approval, but it'll get you started and ready to make your own!

_ignore my sketching skills.. its a work in progress_

---

## A bit of theory first

All keyboards, macropads, and related consist of roughly 3 parts:

| PCB   | Case      | Firmware          |
| ----- | --------- | ----------------- |
| Image | Image IRL | Screenshot ? idfk |

**The PCB** (**P**rinted **C**ircut **B**oard) and its components, which electrically connects everything & also holds many of the electronics together

**The case**, which provides a shell and physically holds all the pieces together

**The firmware**, which processes all the electrical signals and sends them as keystrokes to the computer!

All of these come together to then create your fully working macropad!

We'll go over how to create each part, each with its own sub-parts:

- [Initial Setup!](#initial-setup)
    - Software install
    - Library install
- [Designing your PCB](#designing-your-pcb)
    - [Drawing the Schematic](#drawing-the-schematic)
    - [Routing the PCB](#routing-the-pcb)
- [3D modeling your case](#creating-your-case)
    - Setting up the base
    - Adding in a plate
    - Carving in details!
- [Setting up your firmware!](#firmware)
    - KMK Setup
    - Other firmware instructions

One thing that you'll find useful to reference will be [this](/hackpad/resources) giant wall of resources to reference!

---

## Initial Setup!

Before we start designing, we need to do some basic setup! This will set up the software & libraries we need to make our macropad!

### Software installation

Inital setup is super simple! First, install the necessary pre-requesite software:

- [KiCAD](https://www.kicad.org/), an open source PCB design tool
- [Fusion360](https://www.autodesk.com/products/fusion-360/overview), a parametric 3D modeling software.
- [VSCode](https://code.visualstudio.com/) is an open-source code editor. Not strictly necessary, but highly recommended! We'll be using it to edit our firmware.
- (Optional) [Hack Club Lapse!](https://lapse.hackclub.com) - it's our open source timelapsing software! It's not mandatory, but at the end you'll get some super cool footage of you making your macropad!

### Library download & installation

You'll also need to download a couple libraries!

Download `kicad_care_package.zip` from the [releases](https://github.com/hackclub/hackpad/releases) tab!

You'll have ot unzip it, and then add it to your project library - there's a ton of tutorials on youtube on how to do that!

_for those of you curious: this is just a cherry-picked XIAO footprint from Seeed Studio, and a fixed SK6812MINI-E footprint for the reverse mount version_

After that, come back here! You're officially done all the setup, so now we can move onto...

## Designing your Circuit Board:

Your PCB is the part of your design that connects everything together electrically!

A PCB design consists of two parts: a schematic, which visualizes how all of your components are linked together

![image](https://cdn.hackclub.com/01a05933-3362-7626-a2b6-e40992d566a2/paste-1788202922466.png)

![image](https://cdn.hackclub.com/01a05933-b187-70f6-8a5c-b8d977f0ba56/paste-1788202954720.png)

We're going to be using KiCAD for this part of the guide! Make sure you have it open

To start, create a new project!

(gif of creating a new project)

### Drawing the Schematic

Next, we're going to create our schematic! Hit the "Schematic Editor" button on the homepage:

![image](https://cdn.hackclub.com/01a0592c-d047-7574-ad9e-5fe3e8492b39/paste-1788202504022.png)

_This should open up a new window with your schematic editor!_

![image](https://cdn.hackclub.com/01a0592f-42c2-7326-baba-a3cdce918906/paste-1788202664340.png)

Welcome to the schematic editor!

Schematics consists of symbols & wires. Symbols represent your components

Once you're in, press the A key on your keyboard. This should open up a menu where you can add **symbols** for your different components! Search for the following to add them:

Start by placing these symbols down. They don't have to be in any particular order, but place them somewhat close together.

To rotate the symbols, click R. And to mirror them, click X.

### Placing parts & routing

Once you're done your schematic, you can actually

## Designing your case!

### Sketching the base

### Adding in the plate

### Putting it all together

## Coding your firmware!

Sans sabotage

## Next steps

Nice work on finishing your macropad! Your next steps would be to create a macropad of your own design
