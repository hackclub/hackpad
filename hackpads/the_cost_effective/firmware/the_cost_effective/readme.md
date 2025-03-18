# the_cost_effective

![the_cost_effective](https://github.com/snaeker58/Karls-Hackpad/blob/main/images/layout.jpg)

*A 4x5 ortholinear macro keyboard made by Karl.*

* Keyboard Maintainer: [Karl](https://github.com/snaeker58)
* Hardware Supported: *[Custom PCB and case](https://github.com/snaeker58/Karls-Hackpad)*
* Hardware Availability: *DIY build, not sold or distributed*

Make example for this keyboard (after setting up your build environment):

    make the_cost_effective:default

Flashing example for this keyboard:

    make the_cost_effective:default:flash

See the [build environment setup](https://docs.qmk.fm/#/getting_started_build_tools) and the [make instructions](https://docs.qmk.fm/#/getting_started_make_guide) for more information. Brand new to QMK? Start with our [Complete Newbs Guide](https://docs.qmk.fm/#/newbs).

## Bootloader

Enter the bootloader in 3 ways:

* **Bootmagic reset**: Hold down the key at (0,0) in the matrix (usually the top left key or Escape) and plug in the keyboard
* **Physical reset button**: Briefly press the button on the back of the PCB - some may have pads you must short instead
* **Keycode in layout**: Press the key mapped to `QK_BOOT` if it is available
