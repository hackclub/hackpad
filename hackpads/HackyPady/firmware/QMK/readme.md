# hackypady

![hackypady](imgur.com image replace me!)

Hi! I'm Victoria from Argentina and I enjoyed (and suffer xd) all this process to create my own mini keyboard! It was so amazing and I have improved a lot of skills, so cool!
Best wishes for those who didn't finish, you can do it. 
See ya!

* Keyboard Maintainer: [Victoria](https://github.com/Vichack18)
* Hardware Supported: *The PCBs, controllers supported*
* Hardware Availability: *Links to where you can find this hardware*

Make example for this keyboard (after setting up your build environment):

    make hackypady:default

Flashing example for this keyboard:

    make hackypady:default:flash

See the [build environment setup](https://docs.qmk.fm/#/getting_started_build_tools) and the [make instructions](https://docs.qmk.fm/#/getting_started_make_guide) for more information. Brand new to QMK? Start with our [Complete Newbs Guide](https://docs.qmk.fm/#/newbs).

## Bootloader

Enter the bootloader in 3 ways:

* **Bootmagic reset**: Hold down the key at (0,0) in the matrix (usually the top left key or Escape) and plug in the keyboard
* **Physical reset button**: Briefly press the button on the back of the PCB - some may have pads you must short instead
* **Keycode in layout**: Press the key mapped to `QK_BOOT` if it is available
