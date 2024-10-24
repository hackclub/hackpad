import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.lock_status import LockStatus
from kmk.extensions.oled import Oled, OledDisplayMode, OledReactionType, OledData

class NumpadKeyboard(KMKKeyboard):
    col_pins = (board.PA11, board.PA8, board.PA9)
    row_pins = (board.PA02, board.PA04, board.PA10)
    diode_orientation = DiodeOrientation.COL2ROW

    encoder_pin_0 = board.PA5
    encoder_pin_1 = board.PA7
    encoder_pin_2 = board.PA6

    SCL = board.PA9
    SDA = board.PA8
    i2c = board.I2C

    def __init__(self):
        super().__init__()
        self.modules.append(Layers())
        self.modules.append(EncoderHandler())
        self.extensions.append(MediaKeys())
        self.extensions.append(LockStatus())

        oled_ext = Oled(
            OledData(
                corner_one={0: OledReactionType.STATIC, 1: ["Layer"]},
                corner_two={0: OledReactionType.LAYER, 1: ["1", "2"]},
                corner_three={0: OledReactionType.STATIC, 1: ["Enc"]},
                corner_four={0: OledReactionType.STATIC, 1: [""], 2: OledReactionType.LAYER, 3: ["Vol", "Nav"]},
            ),
            toDisplay=OledDisplayMode.TXT,
            flip=False
        )
        self.extensions.append(oled_ext)

KC_FN = KC.MO(1)

keyboard = NumpadKeyboard()
keyboard.keymap = [
    [
        KC.N7,    KC.N8,   KC.N9,
        KC.N4,    KC.N5,   KC.N6,
        KC.N1,    KC.N2,   KC.N3,
    ],
    [
        KC.F7,    KC.F8,   KC.F9,
        KC.F4,    KC.F5,   KC.F6,
        KC.F1,    KC.F2,   KC.F3,
    ],
]

keyboard.encoders = [
    ((keyboard.encoder_pin_0, keyboard.encoder_pin_1, keyboard.encoder_pin_2), 
     (KC.VOLU, KC.VOLD, KC_FN),
     (KC.RIGHT, KC.LEFT, KC.ENTER)),
]

if __name__ == '__main__':
    keyboard.go()