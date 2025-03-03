import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import MatrixScanner
from kmk.keys import KC

keyboard = KMKKeyboard() # main instance of keeb

keyboard.matrix = MatrixScanner(
    column_pins=[board.AO, board.A1, board.A2, board.A3, board.MISO],  # column
    row_pins=[board.SCK, board.RX],  # row
    value_when_pressed=False,
)

# keymap
keyboard.keymap = [
    [
        KC.D, KC.A, KC.B, KC.T, KC.Y,
        KC.SPACE, KC.KP_1, KC.KP_2, KC.KP_3, KC.KP_4
    ]
]

if __name__ == '__main__':
    keyboard.go()
