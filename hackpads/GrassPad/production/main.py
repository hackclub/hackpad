import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.display import Display
from kmk.extensions.RGB import RGB, AnimationModes
from kmk.extensions.display.ssd1306 import SSD1306
import time

keyboard = KMKKeyboard()
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
keyboard.extensions.append(MediaKeys())

display = Display(
    SSD1306(
        width=128,
        height=32,
        i2c=board.I2C(),
        addr=0x3C,
        rotation=180,
    )
)
keyboard.extensions.append(display)

keyboard.col_pins = (board.D6, board.D3, board.D2)
keyboard.row_pins = (board.D0, board.D1)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

rgb = RGB(
    pixel_pin=board.D10,
    num_pixels=5,
    animation_mode=AnimationModes.STATIC,
    val_limit=100,
    hue_default=0,
    sat_default=100,
    val_default=20,
)
keyboard.extensions.append(rgb)

encoder_handler.pins = (
    (board.D8, board.D7, board.D9),
)

encoder_handler.map = [
	[
		KC.VOLU, KC.VOLD
	]
]

keyboard.keymap = [
    [
        KC.A, KC.B, KC.C
        KC.D, KC.E, KC.F
    ]
]

if __name__ == '__main__':
    keyboard.go()