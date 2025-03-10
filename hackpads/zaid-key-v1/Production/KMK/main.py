# Note : for now I have set the keymap to a basic one, and I intend on changing it later after I receive the pcb and parts, Thanks!

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

hackpad = KMKKeyboard()

macros = Macros()
hackpad.modules.append(macros)

PINS = [board.D7, board.D0, board.D3, board.D4, board.D2, board.D1]

hackpad.matrix = KeysScanner(pins=PINS, value_when_pressed=False)

hackpad.keymap = [
    [KC.A, KC.B, KC.C, KC.D, KC.E, KC.MACRO("Zaid :>")]
]

if __name__ == '__main__':
    hackpad.go()