print("Waking Up ~w~")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

from kmk.modules.encoder import EncoderHandler
from kmk.extensions.RGB import RGB
from kmk.extensions.RGB import AnimationModes

keyboard = KMKKeyboard()

# Backlight
rgb = RGB(
    pixel_pin=board.D10,
    num_pixels=8,
    animation_mode=AnimationModes.RAINBOW,
)
keyboard.extensions.append(rgb)

# Xiao RP2040 RGB LED
rgbOnBoard= RGB(
    pixel_pin=board.NEOPIXEL,
    num_pixels=1,
    animation_mode=AnimationModes.RAINBOW,
)
keyboard.extensions.append(rgbOnBoard)

# Switch Matrix Pins
keyboard.col_pins = (board.D0, board.D1, board.D2, board.D3)
keyboard.row_pins = (board.D9, board.D8, board.D7)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# 4x3 Matrix Keymap
keyboard.keymap = [
    [KC.RGB_TOG],
    [KC.MUTE],
    [KC.P1],
    [KC.P2],
    [KC.P3],
    [KC.P4],
    [KC.P5],
    [KC.P6],
    [KC.P7],
    [KC.P8],
    [KC.P9],
    [KC.P0],
]

# Rotary Encoder
encoder_handler = EncoderHandler()
encoder_handler.divisor = 2
encoder_handler.pins = (board.D5, board.D6, board.D4)
encoder_handler.map = (KC.VOLD, KC.VOLU, KC.MUTE)
keyboard.modules.append(encoder_handler)

if __name__ == '__main__':
    keyboard.go()