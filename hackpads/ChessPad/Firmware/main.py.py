# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.rotary_encoder import RotaryEncoderHandler


# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Define your pins here!
PINS = [board.D7, board.D8, board.D9, board.D10, board.D6, board.D5, board.D2, board.D3]

# Define rotary encoder module
encoder_handler = RotaryEncoderHandler()
keyboard.modules.append(encoder_handler)

# Assign rotary encoder actions
encoder_handler.pins = (board.GP26, board.GP27)
encoder_handler.divisor = 4
encoder_handler.map = [KC.VOLD, KC.VOLU]  # Rotate Left = Volume Down, Rotate Right = Volume Up

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [KC.W, KC.A, KC.S, KC.D, KC.DEL, KC.SPC]
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()