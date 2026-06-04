"""KMK firmware for the hexpad macropad (Seeed XIAO RP2040).

6 keys (3x2) direct-wired to GPIO + 1 EC11 rotary encoder. No matrix, no diodes
-- each switch ties its pin to GND and uses the RP2040's internal pull-up.

Install: drop this file plus the `kmk/` library folder onto the CIRCUITPY drive
(see firmware/README.md for the full flashing steps).
"""
import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()

# --- Switches -------------------------------------------------------------
# Each switch connects its pin to GND; pressed = LOW (internal pull-up).
# Pin order here == key order in the keymap below:
#   0 = SW1 front-left    D0      3 = SW4 rear-left    D3
#   1 = SW2 front-center  D1      4 = SW5 rear-center  D6
#   2 = SW3 front-right   D2      5 = SW6 rear-right   D7
keyboard.matrix = KeysScanner(
    pins=[board.D0, board.D1, board.D2, board.D3, board.D6, board.D7],
    value_when_pressed=False,   # pull-up wiring: a press pulls the pin LOW
)

# --- Rotary encoder (EC11) ------------------------------------------------
encoder = EncoderHandler()
keyboard.modules.append(encoder)
# (pin_a, pin_b, pin_button)  ->  A=D8, B=D9, push-switch=D10
encoder.pins = ((board.D8, board.D9, board.D10),)

# --- Keymap ---------------------------------------------------------------
# Edit any KC.* below to taste. Quick reference:
#   plain keys : KC.A, KC.F13, KC.ENTER, KC.SPACE, KC.ESC
#   combos     : KC.LCTL(KC.C) -> Ctrl+C   |  KC.LGUI(KC.L) -> Win/Cmd+L
#   media      : KC.VOLU, KC.VOLD, KC.MUTE, KC.MPLY, KC.MNXT, KC.MPRV
keyboard.keymap = [
    [
        KC.LCTL(KC.C), KC.LCTL(KC.V), KC.LCTL(KC.X),   # SW1 Copy   SW2 Paste  SW3 Cut
        KC.LCTL(KC.Z), KC.LCTL(KC.Y), KC.LCTL(KC.S),   # SW4 Undo   SW5 Redo   SW6 Save
    ],
]

# Encoder: (turn left, turn right, press)
encoder.map = [
    ((KC.VOLD, KC.VOLU, KC.MUTE),),
]

if __name__ == "__main__":
    keyboard.go()
