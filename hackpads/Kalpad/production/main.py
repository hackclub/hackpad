# import all the IOs of your board
import board

# KMK library imports
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import MatrixScanner
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler

# main instance of keyboard
keyboard = KMKKeyboard()

# define encoders
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

encoder_handler.pins = [
    (1, 2), # first encoder (A, B pins)
    (3, 4), # second encoder (A, B pins)
]

# define key matrix
keyboard.matrix = MatrixScanner(
    rows=(5, 6, 7),
    cols=(8, 9, 10, 11)
)

# MARK: - mappings
# keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md

# map encoders
encoder_handler.map = [
    ((KC.LEFT, KC.RIGHT)),  # left encoder - brush size
    ((KC.MINUS, KC.EQUAL)),  # right encoder - zoom
]

# map matrix
keyboard.keymap = [
    [
        KC.BRIGHTNESS_DOWN, KC.BRIGHTNESS_UP, KC.LCMD(KC.Z),    KC.LCMD(KC.LSFT(KC.Z)),     # Row 1: brightness down, brightness up, undo, redo
        KC.LCMD(KC.X),      KC.LCMD(KC.C),    KC.LCMD(KC.V), KC.L, # Row 2: selection (Cmd+X), transform (Cmd+C), HSB (Cmd+V), layer menu
        KC.LCMD,            KC.TAB,           KC.G,    KC.E      # Row 3: Cmd, slide over, eyedropper, color menu
    ]
]


# start KMK!
if __name__ == '__main__':
    keyboard.go()