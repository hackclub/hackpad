# williams_hackpad

![williams_hackpad]

*HELLO!!!! This is my first hackclub project and I have been super exicted about it (just ask my mom I've bearly slept and am flunking out of school!!!! Ok but this micro-pad is a 2x2 ORTHO with 2 rotary encoders and 2 LEDs, this is my first time working with qmk so please don't judge my terrible code! Thanks!)*

* Keyboard Maintainer: [William](https://github.com/BOTwillplayz)
* Hardware Supported: *6 Cherry MX brown switches, 2 rotary encoders, 2 leds, 1 XIAO RP2040*

Make example for this keyboard (after setting up your build environment):

    make williams_hackpad:default

Flashing example for this keyboard:

    make williams_hackpad:default:flash

See the [build environment setup](https://docs.qmk.fm/#/getting_started_build_tools) and the [make instructions](https://docs.qmk.fm/#/getting_started_make_guide) for more information. Brand new to QMK? Start with our [Complete Newbs Guide](https://docs.qmk.fm/#/newbs).

## Bootloader

Enter the bootloader in 3 ways:

* **Bootmagic reset**: Hold down the key at (0,0) in the matrix (usually the top left key or Escape) and plug in the keyboard
* **Physical reset button**: Briefly press the button on the back of the PCB - some may have pads you must short instead
* **Keycode in layout**: Press the key mapped to `QK_BOOT` if it is available
