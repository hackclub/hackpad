print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.scanners.keypad import KeysScanner
from kmk.modules.encoder import EncoderHandler


encoder_handler = EncoderHandler()
keyboard = KMKKeyboard()

# Add the macro extension
keyboard.modules = [layers, holdtap, encoder_handler]

encoder_handler.pins = (
    (board.GP1, board.GP2, board.GP4,)
)
encoder_handler.map = [(KC.VOLD, KC.VOLU, KC.MUTE)]



keyboard.col_pins = (board.GP26, board.GP27, board.GP28)
keyboard.row_pins = (board.GP29, board.GP6, board.GP7, board.GP0)
keyboard.diode_orientation = DiodeOrientation.COL2ROW
keyboard.keymap = [
    [KC.N7, KC.N8, KC.N9],
    [KC.N4, KC.N5, KC.N6],
    [KC.N1, KC.N2, KC.N3],
    [KC.LCTL(KC.LEFT), KC.N0, KC.LCTL(KC.RIGHT)]
]

if __name__ == '__main__':
    keyboard.go()





