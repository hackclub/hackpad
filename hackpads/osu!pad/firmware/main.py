import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()
encoder_handler = EncoderHandler()
layers = Layers()

keyboard.modules = [layers, encoder_handler]

keyboard.direct_pins = [
    board.GPIO6,
    board.GPIO7,
    board.GPIO0,
    board.GPIO1
]

encoder_handler.pins = ((board.GPIO2, board.GPIO3, board.GPIO1, False),)

_______ = KC.TRNS
XXXXXXX = KC.NO

MEDIA_MUTE = KC.MUTE
MEDIA_VOLUP = KC.AUDIO_VOL_UP
MEDIA_VOLDN = KC.AUDIO_VOL_DOWN

keyboard.keymap = [
    [
        KC.S,
        KC.D,
        KC.E,
        MEDIA_MUTE
    ]
]

encoder_handler.map = [
    ((MEDIA_VOLUP, MEDIA_VOLDN, MEDIA_MUTE),)
]

if __name__ == '__main__':
    keyboard.go()