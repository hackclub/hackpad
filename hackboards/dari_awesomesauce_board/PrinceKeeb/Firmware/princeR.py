# main.py
print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitType, SplitSide


keyboard = KMKKeyboard()


split = Split(split_type=SplitType.UART, split_side=SplitSide.RIGHT, data_pin=board.GP0, data_pin2=board.GP1 )

keyboard.modules.append(split)

keyboard.row_pins = (board.GP9, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14)
keyboard.col_pins = (board.GP16, board.GP17, board.GP18, board.GP19, board.GP20, board.GP21, board.GP22, board.GP26, board.GP27)
keyboard.diode_orientation = DiodeOrientation.COL2ROW


keyboard.keymap = [
    # Base Layer
    [
        # COL GP16		COL GP17	COL GP18	COL GP19    COL GP20	COL GP21    COL GP22    COL GP26    COL GP27	

        KC.F6,		    KC.F7,		KC.F8,	    KC.F9,	    KC.F10,	    KC.F11,     KC.F12,     KC.DEL,
        KC.N6,		    KC.N7,		KC.N8,		KC.N9,		KC.N0,		KC.MINS,    KC.EQL,     KC.BSPC,    KC.PSCR,
        KC.Y,		    KC.U,		KC.I,		KC.O,		KC.P,       KC.LBRC,    KC.RBRC,    KC.BSLS,    KC.HOME
        KC.H,		    KC.J,		KC.K,		KC.L,		KC.SCLN,	KC.QUOT,    KC.ENTER,   KC.END		
        KC.N,		    KC.M,		KC.COMM,	KC.DOT,		KC.SLSH,	KC.RSHIFT,  KC.UP		

        KC.SPACE,       KC.RALT,    KC.FN,      KC.FN,      KC.RCTRL,   KC.LEFT,    KC.DOWN,    KC.RIGHT,
     ],

