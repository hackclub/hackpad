# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.modules.macros import Press, Release, Tap, Macros
encoder_handler = EncoderHandler()
from kmk.extensions.media_keys import MediaKeys
keyboard.extensions.append(MediaKeys())


# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Define your pins here!
PINS = [board.P1, board.P0, board.P27 , board.P28]

encoder_handler.pins = (
    # regular direction encoder and a button
    (board.P26, board.P28, board.P7,), # encoder #1
    (board.P3, board.P4, board.P2,),# encoder #2
    )

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [KC.LEFT, KC.DOWN, KC.RIGHT, KC.UP]
]

encoder_handler.map = [ ((KC.VOLU, KC.VOLD, KC.MUTE), (KC.MNXT, KC.MPRV, KC.MPLY),),
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()