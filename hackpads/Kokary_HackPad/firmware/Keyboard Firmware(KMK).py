print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.D1)
keyboard.row_pins = (board.D10,board.D9,board.D8,board.D6,board.D5)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.N6, KC.N7, KC.N8, KC.N9, KC.N0]
]

if __name__ == '__main__':
    keyboard.go()
