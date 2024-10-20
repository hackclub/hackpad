# MuffinPad-9-Key

![muffinpad9](https://i.imgur.com)

A 9-key macropad. Case files available [here](https://github.com/TheDanishMuffin).

*   Keyboard Maintainer: [Dinesh Babu](https://github.com/TheDanishMuffin)
*   Hardware Supported: PCB, OLED, Rotary Encoder, MX Switches
*   Hardware Availability: [Seeed Studio Wiki](https://wiki.seeedstudio.com/XIAO-RP2040/)

Make example for this keyboard (after setting up your build environment):

    make handwired/muffinpad/muffinpad9:default

Flashing example for this keyboard:

    make handwired/muffinpad/muffinpad9:default:flash

## Bootloader

Enter the bootloader in 3 ways:

* **Bootmagic reset**: Hold down the key at (0,0) in the matrix (usually the top left key or Escape) and plug in the keyboard
* **Physical reset button**: Briefly press the button on the back of the PCB - some may have pads you must short instead
* **Keycode in layout**: Press the key mapped to `QK_BOOT` if it is available