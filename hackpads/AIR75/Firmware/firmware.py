import board
import busio
import time
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import MatrixScanner
from kmk.keys import KC
from kmk.modules.rotary_encoder import RotaryEncoderHandler
from kmk.modules.layers import Layers
from kmk.extensions.display import Display, SSD1306, TextEntry, ImageEntry

keyboard = KMKKeyboard()

keyboard.matrix = MatrixScanner(
    column_pins=[board.GP26, board.GP27, board.GP28, board.GP29],  # Columns
    row_pins=[board.GP2, board.GP4, board.GP3],  # Rows
    value_when_pressed=False,
)

# Define Keymap
keyboard.keymap = [
    [
        KC.ENTER, KC.NO, KC.NO, KC.PSSCREEN,
        KC.F1, KC.F2, KC.F3, KC.F4,
        KC.F5, KC.F6, KC.F7, KC.F8,
    ]
]

encoder = RotaryEncoderHandler(pin_a=board.GP0, pin_b=board.GP1)
encoder.rotation_cw = KC.VOLU  # Volume Up
encoder.rotation_ccw = KC.VOLD  # Volume Down
keyboard.modules.append(encoder)

# Display
layers = Layers()
keyboard.modules.append(layers)

i2c_bus = busio.I2C(board.GP6, board.GP7)
display_driver = SSD1306(
    i2c=i2c_bus,
    # Optional device_addres argument. Default is 0x3C.
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

if __name__ == '__main__':
    keyboard.go()