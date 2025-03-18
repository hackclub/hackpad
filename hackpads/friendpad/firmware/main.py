print("Hello world!")

import board
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.adafruit.pcf8574 import PCF8574

# encoder imports
from kmk.modules.encoder import EncoderHandler

# display imports
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.extensions.display import Display, TextEntry, ImageEntry

keyboard = KMKKeyboard()

i2c_bus = busio.I2C(board.GP_SCL, board.GP_SDA)
driver = SSD1306(
    i2c=i2c_bus,
    device_address=0x3C,
)

expander = PCF8574(board.I2C(), address=0x38)

# matrix pins
keyboard.col_pins = (board.D10, board.D9, board.D8, board.D7)
keyboard.row_pins = (board.D0, board.D1, board.D2, board.D3)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

# rotary encoders
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
SDA = board.D4
SCL = board.D5
i2c = busio.I2C(SCL, SDA)
encoder_handler.pins = (
    (expander.get_pin(0), expander.get_pin(1), None, False,),
    (expander.get_pin(2), expander.get_pin(3), None, False,),
)
encoder_handler.map = (
    ((KC.VOLD, KC.VOLU, None),
     (KC.LCTRL(KC.MINUS), KC.LCTRL(KC.EQUAL), None),),
)

# OLED
display = Display(
    display = driver,
    entries = [
        TextEntry(text=":)", x=0, y=0, x_anchor="M", y_anchor="M")
    ]
    width=128,
    height=32,
    dim_time=30,
    dim_target=0.2,
    off_time=300,
    brightness=1
)
keyboard.extensions.append(display)

# keymap
keyboard.keymap = [
    [KC.LCTRL(KC.C), KC.LCTRL(KC.V), KC.ENTER, KC.BSPC],
    [KC.B, KC.E, KC.LCTRL(KC.Z), KC.LCTRL(KC.LSHIFT(KC.Y))],
    [KC.D, KC.F, KC.J, KC.K],
    [KC.MUTE, KC.N1, KC.NO, KC.NO]
]