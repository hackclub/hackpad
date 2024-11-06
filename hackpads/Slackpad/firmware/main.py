print("Booting....")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

from kmk.modules.encoder import EncoderHandler
from kmk.extensions.RGB import RGB
from kmk.extensions.RGB import AnimationModes

keyboard = KMKKeyboard()

# Xiao RP2040 RGB LED
rgbOnBoard= RGB(
    pixel_pin=board.NEOPIXEL,
    num_pixels=1,
    animation_mode=AnimationModes.RAINBOW,
)
keyboard.extensions.append(rgbOnBoard)

# Switch Matrix Pins
keyboard.col_pins = (board.D1, board.D0, board.D2)
keyboard.row_pins = (board.D3, board.D9, board.D8)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Matrix Keymap
keyboard.keymap = [
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
