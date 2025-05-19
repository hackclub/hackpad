import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import MatrixScanner
from kmk.keys import KC

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP0, board.GP1, board.GP2)
keyboard.row_pins = (board.GP3, board.GP4, board.GP5)
keyboard.diode_orientation = MatrixScanner.DIODE_COL2ROW

keyboard.keymap = [
    [
        KC.MPRV, KC.MPLY, KC.MNXT,
        KC.MUTE, KC.VOLU, KC.VOLD,
        KC.HOME, KC.PGUP, KC.PGDN,
    ]
]

if __name__ == '__main__':
    keyboard.go()