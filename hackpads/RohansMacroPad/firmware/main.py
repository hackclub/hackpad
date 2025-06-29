# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.rgb import RGB

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Rotary Encoder implementation
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

encoder_handler.pins = ((board.A0, board.A1),)  # A0 = GPIO26, A1 = GPIO27
encoder_handler.map = [((KC.VOLD, KC.VOLU),)]   # Rotate left/right

# LED implementation
rgb_ext = RGB(pixel_pin=board.D4, num_pixels=1)
keyboard.extensions.append(rgb_ext)

# Define your pins here!
PINS = [board.D1, board.D2, board.D4, board.D3]
# Encoder button
PINS.append(board.A2)

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [
        KC.A,
        KC.DELETE,
        KC.MACRO("Hello world!"),
        KC.Macro(Press(KC.LCMD), Tap(KC.S), Release(KC.LCMD)),
        KC.ENTER,
    ]
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()