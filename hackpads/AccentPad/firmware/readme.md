# accent_macro_pad

![accent_macro_pad](imgur.com image replace me!)

*A 4x4 keypad that lets you type most accents.*

* Keyboard Maintainer: [Hazel Viswanath](https://github.com/transdryad)
* Hardware Supported: *Accent Pad Board with Seeed Studio Xiao RP2040 Controller*
* Hardware Availability: *Links to where you can find this hardware*

**You must set your os keyboard lay to us international or this won't work. AltGr should be right alt.**

The main accents will work on any OS, but ā, å, ą, ă, and ǎ (substituting a) support may be spotty on other OSes than linux.

Layout:

       ┌───┬───┬───┬───┐
       │ á │ à │ â │ ä │
       ├───┼───┼───┼───┤
       │ ã │ ç │ ā │ ø │
       ├───┼───┼───┼───┤
       │ å │ ą │ ă │ ǎ │
       ├───┼───┼───┼───┤
       │ æ │ œ │ ð │ þ │
       └───┴───┴───┴───┘

Make example for this keyboard (after setting up your build environment):

    qmk build

Flashing example for this keyboard:

    qmk flash

See the [build environment setup](https://docs.qmk.fm/#/getting_started_build_tools) and the [make instructions](https://docs.qmk.fm/#/getting_started_make_guide) for more information. Brand new to QMK? Start with our [Complete Newbs Guide](https://docs.qmk.fm/#/newbs).

## Bootloader

Enter the bootloader in one ways:

* **Bootmagic reset**: Hold down the key at (0,0) in the matrix (usually the top left key or Escape) and plug in the keyboard
