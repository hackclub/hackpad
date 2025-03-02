print ("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.extensions.oled import Oled, OledDisplayMode, OledReactionType, OledData

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

PINS = [board.D1, board.D2, board.D3, board.D4]

oled = Oled(
    OledData(
        image_path="/path_to_image" #Too tired to get one, think this is how it works...
    ),
    toDisplay=OledDisplayMode.IMG,
    flip=false
)

keyboard.extensions.append()

KEYMAP_1 = [
    owo = KC.MACRO(
        "OwO"
    )
    uwu = KC.MACRO(
        "UwU"
    )
    colon = KC.MACRO(
        ":3"
    )
    angy = KC.MACRO(
        "3:<"
    )
]

keyboard.keymap = [

if __name__ == '__main__':
    keyboard.go()
