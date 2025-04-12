print("Starting")

# Import all the IOs of the board
import board
print(dir(board)) #check that the pin names are the same as the pins defined below

# Imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.extensions.rgb import RGB
from kmk.modules.layers import Layers
# from kmk.modules.macros import Press, Release, Tap, Macros

# Main instance of  keyboard
keyboard = KMKKeyboard()

keyboard.modules.append(Layers())

# Add the macro extension
# macros = Macros()
# keyboard.modules.append(macros)

#Define the RGB pin
rgb = RGB(rgb_pixel_pin = board.SDA, num_pixels = 3)
keyboard.extensions.append(rgb)

# Define the pins
PINS = [board.SCK, board.MISO, board.MOSI, board.RX]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

RAISE = KC.LT(1, KC.ESCAPE)
LOWER = KC.LT(0, KC.RGB_TOG)

# Define the buttons corresponding to the pins
# Keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# Macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [#layer 0
        KC.PAUSE, KC.DELETE, KC.SPACE, RAISE,
    ],
    [#layer 1
        KC.RGB_MODE_BREATHE_RAINBOW, KC.RGB_HUI, KC.RGB_MODE_SWIRL, LOWER,
    ],

]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()