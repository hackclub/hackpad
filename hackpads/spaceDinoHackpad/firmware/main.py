# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.RGB import RGB

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
encoderHandler = EncoderHandler
macros = Macros()
rgb = RGB(pixel_pin = board.D0, num_pixels = 12)
keyboard.extensions.append(rgb, MediaKeys())
keyboard.modules.append(macros, encoderHandler)

rgb.animation_mode("rainbow")

# Define your pins here!
keyboard.col_pins = (board.D26, board.D27, board.D28)
keyboard.row_pins = (board.D3, board.D4, board.D2, board.D1)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

encoderHandler.pins = ((board.D29, board.D7, board.D6))

DocString = '"""desc\nParameters:\n    var1 (type): desc\n    var2 (type): desc\nReturns:\n    out1 (type): desc\n"""'
commentAndCopy = KC.MACRO(
    Tap(KC.HOME),
    Tap(KC.LSFT(KC.END)),
    Tap(KC.LCTL(KC.C)),
    Tap(KC.LCTL(KC.SLASH)),
    Tap(KC.LCTL(KC.ENT)),
    Tap(KC.LCTL(KC.V))

)

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [[KC.LCTL(KC.LSFT(KC.C)), KC.LCTL(KC.LSFT(KC.V)),KC.LCTL(KC.F5)],
     [KC.LCTL(KC.C), KC.LCTL(KC.V),KC.F5], 
     [KC.MACRO("#TODO: "), KC.MACRO(DocString), commentAndCopy],
     [KC.LCTL(KC.GRV), KC.NO, KC.NO]]
]

encoderHandler.map = [[[KC.VOLU, KC.VOLD, KC.MUTE]]]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()