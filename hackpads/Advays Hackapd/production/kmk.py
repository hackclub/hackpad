import board

#done

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.digital import DirectPinScanner
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.scanners.keypad import KeysScanner
from kmk.modules.macros import Press, Release, Tap, Macros

keyboard = KMKKeyboard()
PINS = [board.GP1, board.GP2, board.GP4, board.GP29]



macros = Macros()
keyboard.modules.append(macros)

keyboard.keymap = [
    [KC.A, KC.DELETE, KC.MACRO("hello"), KC.ENTER], 
]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

#encoder 
encoder_handler = EncoderHandler()
encoder_handler.pins = [(board.GP28, board.GP0)]  
encoder_handler.map = [
    ((KC.VOLU, KC.VOLD)),  
]
keyboard.modules.append(encoder_handler)

if __name__ == "__main__":
    keyboard.go()
