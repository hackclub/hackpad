import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.modules.macros import Press, Release, Tap, Macros


keyboard = KMKKeyboard()
encoder_handler = EncoderHandler()

macros = Macros()
keyboard.modules.append(macros)

keyboard.col_pins = (board.GP26, board.GP27, board.GP28, board.GP29,)
keyboard.row_pins = (board.GP3, board.GP4, board.GP2)
keyboard.diode_orientation = DiodeOrientation.COLUMNS

encoder_handler.pins = ((board.GP3, board.GP26),)

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
# Leaving the defaults here - would like to configure it when I get the hardware so I can properly play around with it
keyboard.keymap = [
    [KC.A, KC.DELETE, KC.MACRO("Hello world!"), KC.Macro(Press(KC.LCMD), Tap(KC.S), Release(KC.LCMD)),]
]

encoder_handler.map = [((KC.VOLD, KC.VOLU, KC.MUTE),)]

if __name__ == '__main__':
    keyboard.go()