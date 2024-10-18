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
    num_pixels=12,
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
keyboard.col_pins = (board.D7, board.D8, board.D9)
keyboard.row_pins = (board.D0, board.D1, board.D2, board.D3)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# 3x4 Matrix Keymap
keyboard.keymap = [
    [KC.RGB_TOG],
    [KC.MUTE],
    [KC.MPRV],
    [KC.MPLY],
    [KC.MNXT],
    [KC.F13],
    [KC.F14],
    [KC.F15],
    [KC.F16],
    [KC.F18],
    [KC.F19],
    [KC.F20],
]

if __name__ == '__main__':
    keyboard.go()