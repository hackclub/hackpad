print("STARTING")

import board;

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.tapdance import TapDance
from kmk.modules.macros import Macros

print(dir(board))

keyboard = KMKKeyboard()

keyboard.modules.append(Layers())
tapdance = TapDance()
tapdance.tap_time = 750
keyboard.modules.append(tapdance)
keyboard.modules.append(Macros())

keyboard.col_pins = (board.GP1, board.GP0, board.GP28, board.GP29, board.GP3)
keyboard.row_pins = (board.GP26, board.GP27, board.GP4, board.GP5)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

QWERTY_LAYER = KC.TO(0)
NUM_LAYER = KC.TO(1)
FUNC_LAYER = KC.TO(2)
MOUSE_LAYER = KC.TO(3)

tapdance.tap_dance_keys = {
    KC.SPACE: [KC.SPACE, QWERTY_LAYER, NUM_LAYER, FUNC_LAYER, MOUSE_LAYER],
    KC.LGUI: [KC.LGUI, KC.LGUI(KC.C), KC.LGUI(KC.V)],
    KC.Q: [KC.Q, KC.TAB, KC.ESC]
}

keyboard.keymap = [
    [ #QWERTY LEFT
        KC.Q,   KC.W,   KC.E,    KC.R,    KC.T,
        KC.A,   KC.S,   KC.D,    KC.F,    KC.G,
        KC.Z,   KC.X,   KC.C,    KC.V,    KC.SPACE,
        KC.LSHIFT,  KC.LCTRL,    KC.LALT, KC.LGUI
    ], 
    [#NUM LAYER
        KC.N1,  KC.N2, KC.N3, KC.N4, KC.N5,
        KC.TAB, KC.MS_UP, KC.NO, KC.NO, KC.MS_LEFT,
        KC.MS_LEFT,  KC.MS_DOWN, KC.MS_RIGHT, KC.NO, KC.SPACE,
        KC.LSHIFT,  KC.LCTRL,    KC.LALT, KC.LGUI
    ],
    [#FUNC LAYER
        KC.F1, KC.F2, KC.F3, KC.F4, KC.F5,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.LSHIFT,  KC.LCTRL,    KC.LALT, KC.LGUI
    ], 
    [#MOUSE LAYER
        KC.NO, KC.NO, KC.MS_UP, KC.NO, KC.NO,
        KC.NO, KC.MS_LEFT, KC.MS_BTN1, KC.MS_RIGHT, KC.NO,
        KC.NO, KC.NO, KC.MS_DOWN, KC.NO, KC.NO,
        KC.LSHIFT, KC.LCTRL, KC.LALT, KC.LGUI
    ]   
]

if __name__ == '__main__':
    keyboard.go()