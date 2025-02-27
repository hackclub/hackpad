import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)


PINS = [board.D7, board.D8, board.D9, board.D10]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [KC.F13,KC.F14,KC.F15,KC.F16,]
]

encoder_handler = EncoderHandler()
keyboard.extensions.append(encoder_handler)

encoder_handler.pins = [(board.D4, board.D5)]  
encoder_handler.map = [(
    (KC.VOLU, KC.VOLD),  
)]

if __name__ == '__main__':
    keyboard.go()
