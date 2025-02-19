import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.extensions.media_keys import MediaKeys
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner
from kmk.modules.macros import Press, Release, Tap, Macros 
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.RGB import RGB

encoder_handler = EncoderHandler()
keyboard = KMKKeyboard()
macros = Macros()
media_keys = MediaKeys()
rgb = RGB(pixel_pin=D0, num_pixels=4)

keyboard.modules.append(macros)
keyboard.modules.append(encoder_handler)
keyboard.modules.append(media_keys)
keyboard.modules.append(encoder_handler)
keyboard.modules.append(rgb)

PINS = [board.D7, board.D8, board.D9, board.D10]

#figure out what to do with the display later?

encoder_handler.pins = (
    (board.D2, board.D3, board.D1)
)
encoder_handler.map = [
    ((KC.VOLU, KC.VOLD, KC.MUTE))
]

keyboard.matrix = KeysScanner(
    pins=PINS, 
    value_when_pressed=False
)

encoder_handler.map = [
    ((VolumeUp, VolumeDown, VolumeMute))
]

keyboard.keymap = [
    [KC.F, KC.G, KC.H, KC.J]
]

if __name__ == '__main__':
    keyboard.go()