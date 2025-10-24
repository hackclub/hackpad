# representative implementation i plan to manually figure out and map keys to custom asus functions which im not able to get once it comes for my laptop 
import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC

from kmk.modules.layers import Layers
from kmk.modules.macros import Macros, Press, Release, Tap
from kmk.extensions.encoder import EncoderHandler
keyboard = KMKKeyboard()
layers = Layers()
macros = Macros()
keyboard.modules.append(layers)
keyboard.modules.append(macros)

encoder_handler = EncoderHandler()
keyboard.extensions.append(encoder_handler)


PINS = [
    board.D1,  
    board.D2,  
    board.D3,  
    board.D4,  
    board.D5,  # side button
    board.D6,  
]


encoder_handler.pins = (
    (board.D7, board.D8, None, False),  
)


keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,  
    pull=True,
)



keyboard.keymap = [

    [
        KC.MACRO("Hello from Profile 1!"),
        KC.MACRO("Macro 2, Profile 1"),
        KC.MACRO("Macro 3, Profile 1"),
        KC.MACRO("Macro 4, Profile 1"),

        KC.TO(1),

        KC.NO,
    ],
    [
        KC.MACRO("Hello from Profile 2!"),
        KC.MACRO("Macro 2, Profile 2"),
        KC.MACRO("Macro 3, Profile 2"),
        KC.MACRO("Macro 4, Profile 2"),
        KC.TO(0),

        KC.NO,
    ],
]

encoder_handler.map = [

    ((KC.VOLD, KC.VOLU),),
    ((KC.PGDN, KC.PGUP),),
]
if __name__ == '__main__':
    keyboard.go()
