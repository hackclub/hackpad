from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.oled import OLED, OledReactionType, OledData

keyboard = KMKKeyboard()
keyboard.diode_orientation = DiodeOrientation.COLUMNS

keyboard.col_pins = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
keyboard.row_pins = (14, 15, 16, 17, 18)

encoder = EncoderHandler()
encoder.pins = ((19, 20, None),)  # (pin_a, pin_b, button)
encoder.map = [((KC.VOLD, KC.VOLU, KC.MUTE),)]  # Encoder 1 functions

oled = OLED(
    OledData(
        corner_one={0:OledReactionType.STATIC, 1:["Layer:"]},
        corner_two={0:OledReactionType.LAYER, 1:["0", "1", "2"]},
        corner_three={0:OledReactionType.STATIC, 1:["Volume:"]},
        corner_four={0:OledReactionType.ENCODER, 1:["%"]},
    ),
    toDisplay=OledReactionType.TEXT,
    oWidth=128,
    oHeight=32,
    scl_pin=21,
    sda_pin=22,
)

keyboard.keymap = [
    [
        KC.ESC,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.MINS, KC.EQL,  KC.BSPC,
        KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.LBRC, KC.RBRC, KC.BSLS,
        KC.CAPS, KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOT, KC.ENT,  KC.PGUP,
        KC.LSFT, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH, KC.RSFT, KC.UP,   KC.PGDN,
        KC.LCTL, KC.LGUI, KC.LALT, KC.MO(1),KC.SPC,  KC.SPC,  KC.RALT, KC.MO(2),KC.RCTL, KC.LEFT, KC.DOWN, KC.RGHT, KC.DEL,  KC.INS
    ],
    [
        KC.GRV,  KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,   KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,  KC.F12,  KC.DEL,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.VOLU,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.VOLD,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.MPRV, KC.MPLY, KC.MNXT, KC.MUTE, KC.TRNS
    ]
]

keyboard.modules = [encoder]
keyboard.extensions.append(MediaKeys())
keyboard.extensions.append(oled)

if __name__ == '__main__':
    keyboard.go()
