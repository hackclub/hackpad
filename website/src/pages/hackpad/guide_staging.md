# Make your own Hackpad!

Hey there! Welcome to the guide

In this guide, we're going to be making a super simple 4x4 macropad - it'll look something like this!

Copying this guide won't get you automatically approved.

If you ever need help, make sure to join the Hack Club Slack!

**Anything unclear? Head on over to the [FAQ](/faq)!**

## A bit of theory

All keyboards, macropads, and related consist of roughly 3 parts:

(table with 3 columns)

The case, which provides a shell and physically holds all the pieces together

The PCB and its components, which electrically connects everything (and also helps hold things together)

The firmware, which processes all the electrical signals and sends them as keystrokes to the computer!

We'll go over how create each part, each with its own sub-parts:

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
    - Other firmware

One thing that you'll find useful to reference will be [this](/hackpad/resources) giant wall of resources to reference!

## Initial Setup!

Before we start designing, we need to do some basic setup! This will set up the libraries etc needed for

### Software installation

Inital setup is super simple! First, install the necessary pre-requesite software:

- [KiCAD](https://www.kicad.org/), an open source PCB designer tool
- [Fusion360](https://www.autodesk.com/products/fusion-360/overview), a parametric 3D modeling software.
- [VSCode](https://code.visualstudio.com/) is an open-source code editor. Not strictly necessary, but highly recommended! We'll be using it to edit our firmware.
- (Optional)[Hack Club Lapse!](https://lapse.hackclub.com) - it's our open source timelapsing software

### Library download & installation

You'll also need to download a couple libraries! For your PCB, you'll need to install our KiCAD care package!

To do that, head over to the releases

_for those of you curious: this is just a cherry-picked XIAO footprint from Seeed Studio, and a fixed SK6812MINI-E footprint for the reverse mount version_

After that, come back here! You're officially done with all the setup, so now we can move onto...

## Designing your Circuit Board:

Your PCB (**P**rinted **C**ircut **B**oard) is the part of your design that connects everything together electrically!

A PCB design consists of two parts. The first is a schematic, which visualizes how all of your components are linked together!

We're going to be using KiCAD for this part of the guide! Make sure you have it open

To start, create a new project!

(gif of creating a new project)

### Drawing the Schematic

Next, we're going to create our schematic! Hit the "Schematic Editor" button on the homepage:

(screenshot w/ arrow)

<img src="https://hc-cdn.hel1.your-objectstorage.com/s/v3/70f2f1950d3af13329ddc7f8ece3524070d409bc_schematicbutton.png" class="max-w-96" />

This should open up a new window with your schematic editor!

This is where we're going to add our different symbols

This is where we're going to add our different symbols

Schematics consists of symbols & wires. Symbols represent your components

Once you're in, press the A key on your keyboard. This should open up a menu where you can add **symbols** for your different components! Search for the following to add them:

Start by placing these symbols down. They don't have to be in any particular order, but place them somewhat close together.

To rotate the symbols, click R. And to mirror them, click X.

### Placing parts & routing

## Designing your case!

## Coding your firmware!

Now that you have your macropad Down

## Next steps

Nice work on finishing your macropad! Your next steps would be to create a macropad of your own design

-
