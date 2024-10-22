#maybe incomplete btw
print("Starting")

#import stuff

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

#innit stuff

from kmk.modules.macros import Macros

from kmk.modules.encoder import EncoderHandler
encoder_handler = EncoderHandler()
keyboard.modules = [layers, holdtap, encoder_handler]

macros = Macros()
keyboard.modules.append(macros)

keyboard = KMKKeyboard()

keyboard.col_pins = (board.A0, board.A1,board.A3,board.A2)
keyboard.row_pins = (board.A7,board.A8)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

encoder_handler.pins = ((board.A9, board.A10, board.A3, True),)

keyboard.keymap = [
    [
    KC.Macro(macro), KC.A, KC.B, KC.C,
    KC.D, KC.E, KC.F, KC.G
    ]
]
 
encoder_handler.map = [ 
    ((KC.UP, KC.DOWN, KC.MUTE),), # Standard
    ]

if __name__ == '__main__':
    keyboard.go()

#temp
