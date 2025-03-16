import board

from kmk.keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.macros import Macros, Press, Release, Tap
from kmk.modules.layers import Layers
from kmk.module.mouse_keys import MouseKeys
from kmk.modules.encoder import EncoderHandler
from kmk.keys import Key

encoder = EncoderHandler()
keyboard.modules = [Macros(), Layers(), encoder, MouseKeys()]
keyboard = KMKKeyboard()
keyboard.col_pins(board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP15, board.GP16, board.GP17, board.GP18, board.GP19, board.GP20, board.GP21)
keyboard.row_pins(board.GP6, board.GP7, board.GP8, board.GP9)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

X = KC.NO
_ = KC.TRNS
flip = False

class flippingScroll(Key):
    def __init__(self, dir):
        self.dir = dir
    def on_press(self, keyboard, coord_int=None):
        if self.dir == "u":
            if flip:
                self.key = KC.MW_UP
            else:
                self.key = KC.MW_RT
        elif self.dir == "d":
            if flip:
                self.key = KC.MW_DOWN
            else:
                self.key = KC.MW_LT
        keyboard.add_key(self.key)
    def on_release(self, keyboard, coord_int=None):
        keyboard.remove_key(self.key)

ZOOMI = KC.LCTL(KC.EQUAL)
ZOOMO = KC.LCTL(KC.MINUS)

flipScrollU = flippingScroll('u')
flipScrollD = flippingScroll('d')
def flips():
    flip = !flip

encoder.pins = (
    (board.D2, board.D3, board.D28),
    (board.D0, board.D1)
)
encoder.map = [
    ((KC.VOLU, KC.VOLD, KC.MUTE), (KC.TO(2), KC.TO(1))),
    ((flipScrollU, flipScrollD, flips), (KC.TO(0), KC.TO(2))),
    ((_,_,_), (KC.TO(1), KC.TO(0)))
]

copy = KC.MACRO(
    Press(KC.LCTL),
    Tap(KC.C),
    Release(KC.LCTL)
)
paste = KC.MACRO(
    Press(KC.LCTL),
    Tap(KC.v),
    Release(KC.LCTL)
)

keyboard.keymap = [
    [
        KC.TAB  , KC.Q    , KC.W   ,   KC.E    , KC.R , KC.T   , KC.Y   , KC.U  , KC.I    , KC.O    , KC.P    , KC.BSPC,
        KC.CAPS , KC.A    , KC.S   ,   KC.D    , KC.F , KC.G   , KC.H   , KC.J  , KC.K    , KC.L    , KC.SCLN , KC.ENT,
        KC.LSFT , KC.Z    , KC.X   ,   KC.C    , KC.V , KC.B   , KC.N   , KC.M  , KC.COMM , KC.DOT  , KC.QUOT , KC.RSFT,
        KC.LCTL , KC.LGUI , X,   KC.LALT , copy , KC.SPC , KC.SPC , paste , X , KC.LBRC , KC.RBRC , KC.SLSH
    ],
    [
        _,KC.N1,KC.N2,KC.N3,KC.N4,KC.N5,KC.N6,KC.N7,KC.N8,KC.N9,KC.N0,_,
        _,KC.Q,KC.W,KC.E,_,_,_,_,_,_,_,_,
        _,KC.A,KC.S,KC.D,_,_,_,_,_,_,_,_,
        _,_,_,_,_,_,_,_,_,_,_,_
    ],
    [
        X, X       , KC.UP   , X       , X , X , X , X , KC.N7 , KC.N8   , KC.N9   , KC.KP_MINUS,
        X, KC.LEFT , KC.DOWN , KC.LEFT , X , X , X , X , KC.N4 , KC.N5   , KC.N6   , KC.KP_PLUS,
        _, X       , X       , X       , X , X , X , X , KC.N1 , KC.N2   , KC.N3   , KC.KP_ENTER,
        X, X       , X       , X       , X , X , X , X , KC.N0 , KC.PDOT , KC.PSLS , KC.PPLS
    ],
]

if __name__ == '__main__':
    keyboard.go()