# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.encoder import EncoderHandler

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Rotary encoder
encoder_handler = EncoderHandler()
# Regular GPIO Encoder
encoder_handler.pins = (
    # regular direction encoder and a button
    (board.GP27, board.GP26, board.GP28,),
)
# Encoder keymap (vol up, vol down, mute button)
encoder_handler.map = [((KC.VOLD, KC.VOLU, KC.MUTE),)]
keyboard.modules.append(encoder_handler)

# Define your pins here!
PINS = [board.D1, board.D2, board.D3, board.D4]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [KC.UP, KC.LEFT, KC.RIGHT, KC.UP]
]

# Start kmk!
if __name__ == "__main__":
    keyboard.go()