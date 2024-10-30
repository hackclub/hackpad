# jokapad

![jokapad](https://cloud-nkwkfzasl-hack-club-bot.vercel.app/0jokapad_v18.png)

*A 4x4 MacroPad made with love for HackPad YSWS created by Hack Club*

* Keyboard Maintainer: [Bartosz Budnik](https://github.com/BudzioT)
* Hardware Supported: *JokaPad keyboard with Xiao RP2040 as MCU*
* Hardware Availability: *[JokaPad github](https://github.com/BudzioT/JokaPad)*

Make example for this keyboard (after setting up your build environment):

    make jokapad:default

Flashing example for this keyboard:

    make jokapad:default:flash

See the [build environment setup](https://docs.qmk.fm/#/getting_started_build_tools) and the [make instructions](https://docs.qmk.fm/#/getting_started_make_guide) for more information. Brand new to QMK? Start with our [Complete Newbs Guide](https://docs.qmk.fm/#/newbs).

## Bootloader

Enter the bootloader in 2 ways:

* **Bootmagic reset**: Hold down the key at (0,0) in the matrix (usually the top left key or Escape) and plug in the keyboard
* **Keycode in layout**: Press the key mapped to `QK_BOOT` if it is available
