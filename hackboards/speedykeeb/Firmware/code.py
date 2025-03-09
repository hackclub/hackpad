print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()
keyboard.modules.append(Layers())
keyboard.extensions.append(MediaKeys())

keyboard.col_pins = (board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP15, board.GP16, board.GP17, board.GP18,)
keyboard.row_pins = (board.GP19, board.GP20, board.GP21, board.GP22, board.GP26, board.GP27,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

xxx = KC.NO
___ = KC.TRNS

keyboard.keymap = [ # 19x6 keymap; ISO-CH layout
    [KC.ESC, xxx, KC.F1, KC.F2, KC.F3, KC.F4, xxx, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, KC.INS, KC.PAUSE, KC.PGUP, KC.PGDN,
    KC.GRV, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINS, KC.EQL, KC.BSPC, KC.NUHS, KC.NLCK, KC.PSLS, KC.PAST, KC.PMNS,
    KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC, KC.ENTER, xxx, KC.P7, KC.P8, KC.P9, KC.PPLS,
    KC.CAPS, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT, KC.SLSH, xxx, xxx, KC.P4, KC.P5, KC.P6, xxx,
    KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.RSFT, xxx, KC.UP, KC.P1, KC.P2, KC.P3, KC.PENT,
    KC.LCTL, KC.LGUI, KC.LALT, xxx, xxx, xxx, KC.SPC, xxx, xxx, xxx, KC.RALT, KC.MO(1), KC.RCTL, KC.LEFT, KC.DOWN, KC.RIGHT, KC.P0, KC.PDOT],
    [___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, KC.MPRV, KC.MPLY, KC.MNXT, ___, ___, ___, ___,
    ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___,
    ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___,
    ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___,
    ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___,
    ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___],
]

if __name__ == '__main__':
    keyboard.go()