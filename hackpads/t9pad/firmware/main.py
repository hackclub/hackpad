from kb import T9Keyboard

from kmk.keycodes import KC
from kmk.modules.tapdance import TapDance
# init keyboard
keyboard = T9Keyboard()

# modules
tapdance = TapDance()
keyboard.modules.append(tapdance)


tapdance.taptime = 300

# tapdances - default mode
TD1 = KC.TD(KC.SPACE, KC.DOT, KC.COMMA, KC.QUESTION, KC.DOUBLE_QUOTE, KC.COLON, KC.SCOLON)
TD2 = KC.TD(KC.A, KC.B, KC.C)
TD3 = KC.TD(KC.D, KC.E, KC.F)

TD4 = KC.TD(KC.G, KC.H, KC.I)
TD5 = KC.TD(KC.J, KC.K, KC.L)
TD6 = KC.TD(KC.M, KC.N, KC.O)

TD7 = KC.TD(KC.P, KC.Q, KC.R, KC.S)
TD8 = KC.TD(KC.T, KC.U, KC.V)
TD9 = KC.TD(KC.W, KC.X, KC.Y, KC.Z)

# numpad layer - unimplemented rn, kinda hard to work on this without actually having anything to test it on
NUM1 = KC.TD(KC.N1, KC.N0)
NUM2 = KC.N2
NUM3 = KC.N3

NUM4 = KC.N4
NUM5 = KC.N5
NUM6 = KC.N6

NUM7 = KC.TD(KC.N7, KC.PLUS, KC.ASTERISK)
NUM8 = KC.TD(KC.N8, KC.ENTER)
NUM9 = KC.TD(KC.N9, KC.MINUS, KC.HASH)

# set keymap
keyboard.keymap = [
[ # Letter tapdances
    TD1, TD2, TD3,
    TD4, TD5, TD6,
    TD7, TD8, TD9
],
[ # Numpad mode
    NUM1, NUM2, NUM3,
    NUM4, NUM5, NUM6,
    NUM7, NUM8, NUM9
]

]

if __name__ == '__main__':
    keyboard.go()