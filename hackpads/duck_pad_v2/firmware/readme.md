# duck_pad

![duck_pad](https://i.ibb.co/D948Sg4/Screenshot-2024-10-10-214637.png)

*My first macro pad, made with inspiration and motivation by Hack Club*

* Keyboard Maintainer: [Sayhan Rahman](https://github.com/sayhan1610)
* Hardware Supported: *Seeed Studio XIAO RP2040*
* Hardware Availability: *https://www.seeedstudio.com/XIAO-RP2040-v1-0-p-5026.html?srsltid=AfmBOoqIYNKOO90sk7d1Sr9WwA4RFpI1v81WrclKAUQE2BLNjRs2U4hl*

Make example for this keyboard (after setting up your build environment):

    make duck_pad:default

Flashing example for this keyboard:

    make duck_pad:default:flash

See the [build environment setup](https://docs.qmk.fm/#/getting_started_build_tools) and the [make instructions](https://docs.qmk.fm/#/getting_started_make_guide) for more information. Brand new to QMK? Start with our [Complete Newbs Guide](https://docs.qmk.fm/#/newbs).

## Bootloader

Enter the bootloader in 3 ways:

* **Bootmagic reset**: Hold down the key at (0,0) in the matrix (usually the top left key or Escape) and plug in the keyboard
* **Physical reset button**: Briefly press the button on the back of the PCB - some may have pads you must short instead
* **Keycode in layout**: Press the key mapped to `QK_BOOT` if it is available
