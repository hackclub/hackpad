from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import MatrixScanner
from kmk.keys import KC
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()
keyboard.modules.append(Layers())

keyboard.col_pins = (15, 14, 13, 3, 4, 5, 28, 27, 26, 22, 21, 20) 
keyboard.row_pins = (6, 7, 8, 9, 19, 18, 17, 16) 
keyboard.diode_orientation = MatrixScanner.DIODE_COL2ROW


LAYER_BASE = 0
LAYER_SHIFT = 1
LAYER_ALTGR = 2

keymap = [
    [KC.TAB,   KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.ESC],
    [KC.CAPS,  KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.H,    KC.J,    KC.K,    KC.L,    KC.ENT,  KC.DEL],
    [KC.LSFT,  KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH, KC.RSFT],
    [KC.LCTL,  KC.LGUI, KC.LALT, KC.SPC,  KC.DEL,  KC.RGUI, KC.RCTL, KC.LEFT, KC.DOWN, KC.UP,   KC.RGHT],
]

shift_layer = [
    [KC.TRNS, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.TRNS],
    [KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS],
    [KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.SCLN, KC.COLN, KC.QUES, KC.ASTR],
    [KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS],
]

altgr_layer = [
    [KC.TRNS, KC.AT, KC.EXLM, KC.DQUO, KC.HASH, KC.DLR, KC.PERC, KC.AMPR, KC.SLSH, KC.LPRN, KC.RPRN, KC.EQL],
    [KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS],
    [KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.UNDS, KC.MINS, KC.IEXL, KC.BSLS],
    [KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS],
]

keyboard.keymap = [keymap, shift_layer, altgr_layer]

if __name__ == '__main__':
    keyboard.go()
