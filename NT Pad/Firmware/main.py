# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.modules.macros import Press, Release, Tap, Macros

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Add the encoder extension
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

# Define your pins here!
PINS = [board.D3, board.D4, board.D2, board.D1, board.D0]

# Define rotary encoder pins
ENCODER_PINS = (board.D6, board.D7)  # Modify these based on your wiring

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Encoder mapping
encoder_handler.pins = ENCODER_PINS
encoder_handler.map = [  # Had to get help from gpt for the encoder :(
    ((KC.VOLU,), (KC.VOLD,)),  
]

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [
        KC.LCTL(KC.C),  # Copy
        KC.LCTL(KC.V),  # Paste
        KC.LGUI(KC.LSFT(KC.FOUR)),  # SS
        KC.LGUI(KC.LSFT(KC.H)),  # Find Replace
        KC.ESC,  # Escape
    ]
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()
