print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC

keyboard = KMKKeyboard()

# Assign each key to its corresponding pin
keyboard.direct_pins = [
    board.D10,  # Key 1
    board.D9,   # Key 2
    board.D8,   # Key 3
    board.D7    # Key 4
]

keyboard.keymap = [
    [KC.A, KC.B, KC.C, KC.D]
]

if __name__ == '__main__':
    keyboard.go()