from kmk.modules.split import Split, SplitSide
from storage import getmount

SIDE = SplitSide.RIGHT if str(getmount('/').label)[-1] == 'R' else SplitSide.LEFT



import board as b, busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC, Key
from kmk.scanners import DiodeOrientation

from kmk.extensions.RGB import RGB
from kmk.modules.holdtap import HoldTap
from kmk.modules.encoder import EncoderHandler

from kmk.extensions.display import Display, TextEntry, ImageEntry

# For SSD1306
from kmk.extensions.display.ssd1306 import SSD1306



keyboard = KMKKeyboard()

holdtap = HoldTap()
keyboard.modules.append(holdtap)

rgb = None # type: RGB

if SIDE == SplitSide.LEFT:
    keyboard.col_pins = (b.GP8, b.GP9, b.GP10, b.GP11, b.GP12, b.GP13, b.GP14, b.GP15, b.GP16, b.GP17, b.GP18, b.GP19, b.GP20, b.GP21, b.GP22)
    keyboard.row_pins = (b.GP2, b.GP3, b.GP4, b.GP5, b.GP6, b.GP7)

    rgb = RGB(pixel_pin=b.GP26, num_pixels=80, sat_default=0, val_default=0)
    keyboard.modules.append(rgb)
elif SIDE == SplitSide.RIGHT:
    keyboard.col_pins = (b.GP7, b.GP8,  b.GP9, b.GP10, b.GP11, b.GP12, b.GP13,   None,   None,   None,   None,   None,   None,   None,   None)
    keyboard.row_pins = (b.GP6, b.GP5, b.GP4, b.GP3, b.GP2,  None)

    rgb = RGB(pixel_pin=b.GP18, num_pixels=32, sat_default=0, val_default=0)
    keyboard.modules.append(rgb)

    encoder_handler = EncoderHandler()
    encoder_handler.pins = (
        (b.GP14, b.GP15, None),
    )
    encoder_handler.map = (
        (KC.VOLD, KC.VOLU, KC.MUTE),
    )
    keyboard.modules.append(encoder_handler)

    i2c_bus = busio.I2C(b.GP_SCL, b.GP_SDA)
    driver = SSD1306(
        i2c=i2c_bus,
    )
    display = Display(
        display=driver,
        width=128,
        height=64,
    )
    display.entries = [
        TextEntry("GamerPad", x = 5, y = 5),
    ]
    keyboard.extensions.append(display)

keyboard.diode_orientation = DiodeOrientation.COL2ROW


class MacroKey(Key):
    def __init__(self):
        self.macro = []

    def on_press(self, keyboard, coord_int=None):
        pass

    def on_release(self, keyboard, coord_int=None):
        pass

### may be reintroduced later, to make some kind of rgb disabling animation
# class LightSwitch(Key):
#     def __init__(self):
#         pass

#     def on_press(self, keyboard, coord_int=None):
#         fn_activated = not fn_activated

#     def on_release(self, keyboard, coord_int=None):
#         pass

# ls_sw = LightSwitch()

media_pp_k = KC.HT(KC.MEDIA_NEXT_TRACK, KC.MEDIA_PREV_TRACK)

kcno_8 = (KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO)

keyboard.keymap = [
    [
        KC.NO,      KC.ESC,      KC.F1,   KC.F2,   KC.F3, KC.F4, KC.NO,    KC.F5, KC.F6, KC.F7,   KC.F8,    KC.F9,      KC.F10,      KC.F11,        KC.F12,        KC.PSCREEN, KC.SLCK, KC.PAUSE,  KC.KP_EQUAL, KC.KP_SLASH, KC.KP_ASTERISK, KC.KP_MINUS, *kcno_8,
        KC.NO,      KC.GRAVE,    KC.N1,   KC.N2,   KC.N3, KC.N4, KC.N5,    KC.N6, KC.N7, KC.N8,   KC.N9,    KC.N0,      KC.MINUS,    KC.EQUAL,      KC.BSPACE,     KC.INSERT,  KC.HOME, KC.PGUP,   KC.KP_7,     KC.KP_8,     KC.KP_9,        KC.KP_PLUS,  *kcno_8,
        KC.NO,      KC.TAB,      KC.Q,    KC.W,    KC.E,  KC.R,  KC.T,     KC.Y,  KC.U,  KC.I,    KC.O,     KC.P,       KC.LBRACKET, KC.RBRACKET,   KC.ENTER,      KC.DELETE,  KC.END,  KC.PGDOWN, KC.KP_4,     KC.KP_5,     KC.KP_6,        KC.NO,       *kcno_8,
        MacroKey(), KC.CAPSLOCK, KC.A,    KC.S,    KC.D,  KC.F,  KC.G,     KC.H,  KC.J,  KC.K,    KC.L,     KC.SCOLON,  KC.QUOTE,    KC.NONUS_HASH, KC.NO,         KC.MB_LMB,  KC.UP,   KC.MB_RMB, KC.KP_1,     KC.KP_2,     KC.KP_3,        KC.KP_ENTER, *kcno_8,
        MacroKey(), KC.LSHIFT,   KC.NUBS, KC.Z,    KC.X,  KC.C,  KC.V,     KC.B,  KC.N,  KC.M,    KC.COMMA, KC.DOT,     KC.SLASH,    KC.RSHIFT,     KC.NO,         KC.LEFT,    KC.DOWN, KC.RIGHT,  KC.KP_0,     KC.NO,       KC.KP_DOT,      KC.NO,       *kcno_8,
        media_pp_k, KC.LCTRL,    KC.LGUI, KC.LALT, KC.NO, KC.NO, KC.SPACE, KC.NO, KC.NO, KC.NO,   KC.RALT,  KC.RGUI,    KC.RGB_TOG,  KC.RCTRL,      KC.NO,         KC.NO,      KC.NO,   KC.NO,     KC.NO,       KC.NO,       KC.NO,          KC.NO,       *kcno_8,
    ],
]

split = Split(
    split_flip=True,
    data_pin=b.GP0,
    data_pin2=b.GP1,
)
keyboard.modules.append(split)

if __name__ == '__main__':
    keyboard.go()
