print("Nano Deck")

import board
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.scanners.keypad import I2CExpander
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.extensions.RGB import RGB
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.rapidfire import RapidFire
from kmk.modules.holdtap import HoldTap
from kmk.modules.tapdance import TapDance


holdtap = HoldTap()

tapdance = TapDance()
tapdance.tap_time = 750

keyboard = KMKKeyboard()

# Initialize I2C bus on the XIAO RP2040
i2c = busio.I2C(board.GP7, board.GP6)  # SCL=GP7, SDA=GP6, adjust as necessary

driver = SSD1306(
    # Mandatory:
    i2c=i2c,
    # Optional:
    device_address=0x3C,
)

display = Display(display=driver, width=128, height=64)

display.entries = [
    TextEntry(text="Booting up...", x=128, y=0, x_anchor="R", y_anchor="T"), # text in Top Right corner
    TextEntry(text="ON", x=128, y=64, x_anchor="R", y_anchor="B"), # text in Bottom Right corner
    TextEntry(text="Nano Deck!", x=64, y=32, x_anchor="M", y_anchor="M"), # text in the Middle of screen
]
keyboard.extensions.append(display)

keyboard.extensions.append(MediaKeys())

keyboard.modules.append(RapidFire())

keyboard.modules.append(holdtap)
keyboard.modules.append(tapdance)



# Set up the PCF8574A I/O expander (adjust address as per your setup, default is 0x38)
expander = I2CExpander(i2c, address=0x38)

encoder_handler = EncoderHandler()
layers = Layers()
keyboard.modules = [encoder_handler, layers]

rgb = RGB(pixel_pin=expander.pin(4), num_pixels=16, rgb_order=(1, 0, 2),)
keyboard.extensions.append(rgb)

encoder_handler.pins = ((board.GP1, board.GP2, None, False), (board.GP3, board.GP4, None, False))

# Define your column and row pins
keyboard.col_pins = (board.GP26, board.GP27, board.GP28, board.GP29)  # Direct GPIO pins for columns
keyboard.row_pins = (board.GP0, expander.get_pin(0), expander.get_pin(1), expander.get_pin(2), expander.get_pin(3))  # Row pins from PCF8574A

# Set the diode orientation
keyboard.diode_orientation = DiodeOrientation.COL2ROW

xxx = KC.NO
___ = KC.TRNS

TO_FN = KC.TO(0)
TO_GI = KC.TO(1)
TO_RGB = KC.TO(2)
TO_RGB_ANI = KC.MO(3)

TO_GI_SWITCH = KC.HT(TO_GI, TO_RGB, prefer_hold=True, tap_interrupted=False, tap_time=None, repeat=HoldTapRepeat.NONE)
TO_FN_SWITCH = KC.HT(TO_FN, TO_RGB, prefer_hold=True, tap_interrupted=False, tap_time=None, repeat=HoldTapRepeat.NONE)

LAYER_SWITCH = KC.TD(TO_FN, TO_GI, TO_RGB)

SPAM_SHIFT = KC.RF(KC.LSFT, timeout=200, interval=100, enable_interval_randomization=True, randomization_magnitude=25)

# Define the keymap
keyboard.keymap = [
        # Function Layer
        [
            KC.MUTE, KC.MPLY,
            KC.ESCAPE,  LAYER_SWITCH,
            KC.F1, KC.F2, KC.F3, KC.F4,
            KC.F5, KC.F6, KC.F7, KC.F8,
            KC.F9, KC.F10, KC.F11, KC.F12,
        ], 
        # Genshin Impact Layer
        [
            ___, ___,
            ___, ___,
            KC.1, KC.2, KC.3, KC.4,
            KC.Z, KC.Q, KC.UP, KC.E,
            SPAM_SHIFT, KC.LEFT, KC.DOWN, KC.RIGHT,
        ],
        # RGB Layer
        [
            KC.VOLD, KC.VOLU,
            KC.BRID, ___,
            KC.RGB_TOG, KC.RGB_MOD, KC.RGB_HUI, KC.RGB_HUD,
            KC.RGB_SAI, KC.RGB_SAD, KC.RGB_VAI, KC.RGB_VAD,
            KC.RGB_ANI, KC.RGB_AND, xxx, xxx,
        ],
        # RGB Animation Layer
        [
            xxx, xxx,
            xxx, xxx,
            KC.RGB_M_P, KC.RGB_M_B, KC.RGB_M_R, KC.RGB_M_BR,
            KC.RGB_M_K, KC.RGB_M_S, xxx, xxx,
            ___, ___, xxx, xxx,
        ],
    ]

encoder_handler.map = [ 
    
    # Function Layer
    (( KC.VOLD, KC.VOLU), ( KC.BRID, KC.BRIU), ), 
    
    # Genshin Impact Layer
    (( KC.VOLD, KC.VOLU), ( KC.BRID, KC.BRIU), ),
    
    # RGB Layer
    (( KC.VOLD, KC.VOLU), ( KC.BRID, KC.BRIU), ),
    ] 

if __name__ == '__main__':
    keyboard.go()
