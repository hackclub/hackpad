import board
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.RGB import RGB, AnimationModes
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.oled import OLED, OLED_DisplaySize
from adafruit_pcf8574 import PCF8574

i2c = busio.I2C(board.SCL, board.SDA) # init i2c
pcf = PCF8574(i2c, address=0x20)  # default PCF8574A address

keyboard = KMKKeyboard()

keyboard.col_pins = (board.D0, board.D1, board.D2, board.D3)
keyboard.row_pins = (board.D10, board.D9, board.D8)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

rgb = RGB(
    pixel_pin=board.D7,
    num_pixels=10,
    animation_mode=AnimationModes.STATIC,
    val_limit=100,
    hue_default=0,
    sat_default=100,
    val_default=20,
)
keyboard.extensions.append(rgb)

oled = OLED(
    width=128,
    height=32,
    size=OLED_DisplaySize.OLED_128x32,
    flip=False
)
keyboard.extensions.append(oled)

def update_oled():
    oled.clear()
    oled.text("Makropad", 0, 0)
    oled.show()

# encoders
encoder_handler = EncoderHandler()
encoder_handler.pins = (
    # encoder 1
    ((pcf.get_pin(0), pcf.get_pin(1)), None, False),
    # encoder 2
    ((pcf.get_pin(2), pcf.get_pin(3)), None, False),
)

# encoder actions
def encoder_1_handler(keyboard, state):
    if state:
        keyboard.tap_key(KC.VOLU)
    else:
        keyboard.tap_key(KC.VOLD)

def encoder_2_handler(keyboard, state):
    if state:
        keyboard.tap_key(KC.MNXT)
    else:
        keyboard.tap_key(KC.MPRV)

encoder_handler.map = (
    ((encoder_1_handler, encoder_1_handler),),  # layer 0
    ((encoder_2_handler, encoder_2_handler),),  # layer 0
)

keyboard.modules.append(encoder_handler)
keyboard.modules.append(Layers())
keyboard.extensions.append(MediaKeys())

keyboard.keymap = [
    [   # base layer
        KC.A,    KC.B,    KC.C,    KC.D,
        KC.E,    KC.F,    KC.G,    KC.H,
        KC.NO,   KC.J,    KC.K,    KC.NO,  # NO = encoder buttons
    ]
]

if __name__ == '__main__':
    update_oled() # start oled
    keyboard.go()

