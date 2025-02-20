import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.display import Display, TextEntry, ImageEntry
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.extensions.RGB import RGB, AnimationModes
import busio

keyboard = KMKKeyboard()

keyboard.col_pins = (board.D10, board.D9, board.D8, board.D7)
keyboard.row_pins = (board.D0, board.D1, board.D2, board.D3)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
     KC.N7,     KC.N8,      KC.N9,      KC.KP_ASTERISK,
     KC.N4,     KC.N5,      KC.N6,      KC.KP_MINUS,
     KC.N1,     KC.N2,      KC.N3,      KC.KP_SLASH,
     KC.BSPC,	KC.N0,      KC.KP_DOT,  KC.KP_ENTER,
    ]
]

i2c_bus = busio.I2C(board.GP_SCL, board.GP_SDA)

driver=SSD1306(
    i2c=i2c_bus,
    device_address=0x3C,
)

display = Display(
    display=display_driver,
    entries=[
        TextEntry(text='Full-Size Hackpad.V1', x=0, y=0, y_anchor='M'),
    ],
    width=128,
    height=32,
    dim_time=10,
    dim_target=0.2,
    off_time=1200,
    brightness=1,
)

keyboard.extensions.append(display)


rgb = RGB(
    pixel_pin=board.D6,
    num_pixels=16,
    animation_mode=AnimationModes.STATIC,
    val=100,
    hue=230,
)
keyboard.extensions.append(rgb)

if __name__ == '__main__':
    keyboard.go()