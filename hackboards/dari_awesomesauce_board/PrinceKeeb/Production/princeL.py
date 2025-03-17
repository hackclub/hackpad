# main.py
print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitType, SplitSide


keyboard = KMKKeyboard()


split = Split(split_type=SplitType.UART, split_side=SplitSide.LEFT, data_pin=board.GP16, data_pin2=board.GP17 )

keyboard.modules.append(split)

keyboard.row_pins = (board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11)
keyboard.col_pins = (board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5)
keyboard.diode_orientation = DiodeOrientation.COL2ROW


keyboard.keymap = [
    # Base Layer
    [
        # COL GP0		COL GP1	    COL GP2	    COL GP3	    COL GP4	    COL GP5	

        KC.CAPS,		KC.F1,		KC.F2,	    KC.F3,	    KC.F4,	    KC.F5,
        KC.TILDE,		KC.N1,		KC.N2,		KC.N3,		KC.N4,		KC.N5,		
        KC.TAB,			KC.Q,		KC.W,		KC.E,		KC.R,		KC.T,				
        KC.Escape,		KC.A,		KC.S,		KC.D,		KC.F,		KC.G,		
        KC.LSHIFT,		KC.Z,		KC.X,		KC.C,		KC.V,		KC.B,		

        KC.LCTRL,       KC.FN,      KC.FN,      KC.FN,      KC.LALT,    KC.SPACE
     ],
]
