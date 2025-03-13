import boardfrom kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import MatrixScannerkeyboard = KMKKeyboard()keyboard.matrix = MatrixScanner(
    column_pins=[board.GP7, board.GP8, board.GP9, board.GP10],
    row_pins=[board.GP4, board.GP5, board.GP6],
)

keyboard.keymap = [
    [
        KC.N1,  KC.N2,  KC.N3,  KC.A,
        KC.N4,  KC.N5,  KC.N6,  KC.B,
        KC.N7,  KC.N8,  KC.N9,  KC.C,
    ]
]

if __name__ == '__main__':
    keyboard.go()