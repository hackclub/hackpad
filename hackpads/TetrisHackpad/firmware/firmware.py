import board

from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation


keyboard = KMKKeyboard()

keyboard.col_pins = (board.D1, board.D2, board.D3, board.D4, board.D5,)
keyboard.row_pins = (board.D6, board.D0)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.LEFT, KC.DOWN, KC.RIGHT, KC.UP, KC.R],
    [KC.SPACE, KC.C, KC.D, KC.S, KC.A]
]


if __name__ == '__main__':
    keyboard.go()
