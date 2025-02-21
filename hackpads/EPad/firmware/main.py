import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()

encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

keyboard.col_pins = (board.GP6, board.GP7, board.GP0, board.GP3)  # 5, 6, 7, 11
keyboard.row_pins = (board.GP4, board.GP2, board.GP1)             # 10, 9, 8
keyboard.diode_orientation = DiodeOrientation.COL2ROW

encoder_handler.pins = ((board.GP4, board.GP2, board.GP3))

keyboard.keymap = [
    [
        KC.A, KC.B, KC.C, KC.D,
        KC.E, KC.F, KC.G, KC.H,
        KC.I, KC.J, KC.K, KC.L
    ]
]

encoder_handler.map = [
    [
        KC.VOLU, KC.VOLD
    ]
]

if __name__ == '__main__':
    keyboard.go()