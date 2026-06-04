# Firmware

KMK (CircuitPython) firmware for the hexpad macropad — 6 keys + 1 rotary encoder
on a **Seeed XIAO RP2040**. KMK is used because it needs no build toolchain:
you drag files onto the board's USB drive and edit `code.py` to remap keys.

## Files

| File | Purpose |
|------|---------|
| `code.py` | The keymap + wiring. This is the firmware you edit. |

## Flash it (one-time setup)

1. **Put CircuitPython on the XIAO RP2040.**
   - Download the XIAO RP2040 build: <https://circuitpython.org/board/seeeduino_xiao_rp2040/>
   - Plug the XIAO in. Enter the bootloader: hold **BOOT**, tap **RESET**, release BOOT
     (or double-tap RESET). A drive named **RPI-RP2** appears.
   - Drag the downloaded `.uf2` onto **RPI-RP2**. It reboots as a drive named **CIRCUITPY**.
2. **Add the KMK library.**
   - Download KMK: <https://github.com/KMKfw/kmk_firmware> (green *Code → Download ZIP*).
   - Copy the **`kmk/`** folder from that zip to the root of the **CIRCUITPY** drive.
3. **Add this firmware.**
   - Copy **`firmware/code.py`** to the root of **CIRCUITPY** (replace the default `code.py`).
   - It runs immediately. Press a key / turn the knob to test.

To change keys later: just edit `code.py` on the CIRCUITPY drive and save — it
reloads automatically.

## Default keymap

```
   ( encoder: turn = volume,  press = mute )

   [ Copy ] [ Paste ] [ Cut  ]      <- front row  (SW1 SW2 SW3)
   [ Undo ] [ Redo  ] [ Save ]      <- rear row   (SW4 SW5 SW6)
```

Edit the `KC.*` entries in `code.py` to remap. Examples are in the comments
there (plain keys, Ctrl/Cmd combos, media keys).

## Pin map (matches the PCB)

Each switch: pin → GND, internal pull-up (press = LOW). No diodes.

| Key | XIAO pin | RP2040 GPIO |
|-----|----------|-------------|
| SW1 | D0 | GPIO26 |
| SW2 | D1 | GPIO27 |
| SW3 | D2 | GPIO28 |
| SW4 | D3 | GPIO29 |
| SW5 | D6 | GPIO0 |
| SW6 | D7 | GPIO1 |
| Encoder A | D8 | GPIO2 |
| Encoder B | D9 | GPIO4 |
| Encoder push | D10 | GPIO3 |
| Encoder common / switch GND | GND | — |

`code.py` uses the `board.D#` names, so it stays correct regardless of the
underlying GPIO numbers.

## Prefer QMK?

QMK also runs on the RP2040 but needs a compile toolchain (`qmk` CLI, a
`info.json` declaring `direct` pins for the 6 keys + an `encoders` block, and a
`keymap.c`). KMK is recommended here for the no-build workflow; ask if you want
the QMK variant instead.
