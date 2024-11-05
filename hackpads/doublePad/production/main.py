# Write your code here :-)
print("Starting")

import board
from kmk.kmk_keyboard import KMKKeyboard

keyboard.col_pins = (board.D0, board.D1,board.D2, board.D3,board.D4, board.D5,board.D6, board.D7)


keyboard.keymap = [
    [KC.LCTL(c), KC.LCTL(v), KC.W, KC.A, KC.S, KC.D, KC.RELOAD, KC.TILDE]
]


if __name__ == '__main__':
    keyboard.go()
