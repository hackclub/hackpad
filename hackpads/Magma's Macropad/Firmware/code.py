import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler

# layout
COL0 = board.D11
COL1 = board.D10
COL2 = board.D9
ROW0 = board.D3
ROW1 = board.D4
ROTA = board.D2
ROTB = board.D1

keyboard = KMKKeyboard()

#matrix settings
keyboard.col_pins = (COL0, COL1, COL2)
keyboard.row_pins = (ROW0, ROW1)
keyboard.diode_orientation = DiodeOrientation.COL2ROW


# rotary encoder settings
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
encoder_handler.pins = ((ROTA, ROTB, False),)
encoder_handler.map = (((KC.VOLD, KC.VOLU),),)

# Keymap
keyboard.keymap = [
    [KC.NO, KC.W, KC.NO,
     KC.A, KC.S, KC.D
    ]
]

if __name__ == '__main__':
    keyboard.go()