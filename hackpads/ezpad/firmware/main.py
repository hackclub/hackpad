# You import all the IOs of your board
import board
import busio

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.rgb import RGB, AnimationModes
from kmk.extensions.display import Display, TextEntry, ImageEntry
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.extensions.media_keys import MediaKeys
from kmk.keys import KC

keyboard = KMKKeyboard()

# define matrix
keyboard.col_pins = (board.GP29, board.GP1, board.GP2)
keyboard.row_pins = (board.GP26, board.GP27, board.GP28)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# mediakeys
keyboard.extensions.append(MediaKeys())

# rgb
rgb = RGB(
    pixel_pin=board.GP0,       
    num_pixels=9,              
    val_limit=100,             # Maximum brightness (0-255)
    val_default=80,            # Default brightness
    animation_speed=2,         
    animation_mode=AnimationModes.RAINBOW, 
    refresh_rate=30,           
)
keyboard.extensions.append(rgb)

# ─── OLED Display (128x64 I²C) ───────────────────────────────
i2c_bus = busio.I2C(board.GP21, board.GP20)
display_driver = SSD1306(
    i2c=i2c_bus,
    # device_address=0x3C,
)

display = Display(
    display=display_driver,
    entries=[
        TextEntry(text='Layer: ', x=0, y=32, y_anchor='B'),
        TextEntry(text='BASE', x=40, y=32, y_anchor='B', layer=0),
        TextEntry(text='NUM', x=40, y=32, y_anchor='B', layer=1),
        TextEntry(text='NAV', x=40, y=32, y_anchor='B', layer=2),
        TextEntry(text='0 1 2', x=0, y=4),
        TextEntry(text='0', x=0, y=4, inverted=True, layer=0),
        TextEntry(text='1', x=12, y=4, inverted=True, layer=1),
        TextEntry(text='2', x=24, y=4, inverted=True, layer=2),
    ],
    # Optional width argument. Default is 128.
    # width=128,
    height=64,
    dim_time=10,
    dim_target=0.2,
    off_time=1200,
    brightness=1,
)

keyboard.extensions.append(display)

# encoder
encoder = EncoderHandler()
keyboard.modules.append(encoder)
encoder.pins = (
    (board.GP3, board.GP4, None),  # a/b/none
)
encoder.map = [
    ((KC.VOLD, KC.VOLU),)  # ccw down, cw up
]

# Keymap 3x3
keyboard.keymap = [
    [
        KC.N7, KC.N8, KC.N9,
        KC.N4, KC.N5, KC.N6,
        KC.N1, KC.N2, KC.N3,
    ]
]
# Run firmware
if __name__ == '__main__':
    keyboard.go()
