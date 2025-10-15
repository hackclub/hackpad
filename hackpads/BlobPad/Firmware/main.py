# This isn't complete because I couldn't yet find out how to use the IO expander with kmk and I'm running out of time now. (And also I think I need the ToF distance sensor to test before being able to write any working code for it).
# Basically, the keyboard will have 4 sets of 8 macros, and the left rotary encoder will switch between those.
# The other rotary encoder will switch between what the ToF distance sensor controls (screen brightness, audio volume, keyboard brightness, off) (you raise/lower your hand over the sensor to control the currently selected setting). I think this will probably need something running on the computer as well.
# The OLED will simply display both of these states controlled by the rotary encoders.


import board
from kmk.modules.encoder import EncoderHandler

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

keyboard = KMKKeyboard()

encoder_handler = EncoderHandler()

io_expander = ... # TODO figure this out

macros = Macros()
keyboard.modules.append(macros)

PINS = [board.D8, board.D9, board.D10, board.D11]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [KC.A, KC.DELETE, KC.MACRO("Hello world!"), KC.Macro(Press(KC.LCMD), Tap(KC.S), Release(KC.LCMD)),]
]

if __name__ == '__main__':
    keyboard.go()
