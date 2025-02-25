import board
import kmk.modules.macros

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
macros = Macros(unicode_mode=UnicodeModeWinC)
keyboard.modules.append(macros)
keyboard = KMKKeyboard()
encoder_handler = EncoderHandler()  
encoder_handler.pins = ((board.GPIO0, board.GPIO1, None))

keyboard.col_pins = (board.GPIO26, board.GPIO27, board.GPIO28, board.GPIO29)
keyboard.row_pins = (board.GPIO2,board.GPIO4,board.GPIO3)
keyboard.diode_orientation = DiodeOrientation.COL2ROW
knuckle = KC.MACRO(KC.G, on_hold=KC.F, on_release=KC.G, blocking=False)
#uses G to switch to knuckleblaster, holds F to punch/blast, switches back
keyboard.keymap = [
    [KC.R, KC.F, knuckle, KC.SPACE]
    [KC.E, KC.D, KC.S, KC.W]
    [KC.A, KC.BSLASH, KC.LSHIFT, KC.LCTRL]
]
encoder_handler.map = [((KC.VOLD, KC.VOLU, KC.NO))]

if __name__ == '__main__':
    keyboard.go()