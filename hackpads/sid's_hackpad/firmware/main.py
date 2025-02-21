import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP6, board.GP28, board.GP27, board.GP26,)
keyboard.row_pins = (board.GP29, board.GP07, board.GP0)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
        KC.PSCREEN, KC.SCROLLOCK, KC.INSERT,
        KC.INSERT, KC.HOME, KC.PGUP, KC.PGDOWN,
        KC.DELETE, KC.NUMLOCK, KC.F, KC.E
    ]
]

if __name__ == '__main__':
    keyboard.go()