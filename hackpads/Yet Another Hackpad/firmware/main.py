import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.RGB import RGB
from kmk.extensions.media_keys import MediaKeys

keyboard.extensions.append(MediaKeys())

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

rgb = RGB(pixel_pin=board.D4, num_pixels=4, hue_default=100, sat_default=255, val_default=15)
keyboard.extensions.append(rgb)

PINS = [board.D10, board.D9, board.D8, board.D7]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

encoder_handler.pins = (
    (board.D2, board.D1, board.D0,)
)

encoder_handler.map = [
    ((KC.VOLD, KC.VOLU, KC.MUTE),),
]

keyboard.keymap = [
    [
        KC.MEDIA_PLAY_PAUSE,
        KC.MEDIA_NEXT_TRACK,
        KC.MACRO(Press(KC.LGUI), Tap(KC.ENTER), Release(KC.LGUI)),  # Open Terminal
        KC.MACRO(Press(KC.LALT), Tap(KC.E), Release(KC.LALT)),  # Open Nautilus
    ]
]

if __name__ == '__main__':
    keyboard.go()
