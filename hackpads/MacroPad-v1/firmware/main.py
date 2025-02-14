from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.handlers.sequences import simple_key_sequence
from kmk.modules.encoder import EncoderHandler
import board

keyboard = KMKKeyboard()

encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

keyboard.keymap = [
    [KC.W, KC.A, KC.S, KC.D]
]

keyboard.gpio_pins = [board.GP3, board.GP4, board.GP2, board.GP1]

def encoder_handler_fn(index, clockwise):
    if clockwise:
        keyboard.tap_key(KC.VOLU)
    else:
        keyboard.tap_key(KC.VOLD)

encoder_handler.pins = ((board.GP28, board.GP29),)
encoder_handler.callback = encoder_handler_fn

keyboard.tap_key(KC.MUTE)

if __name__ == '__main__':
    keyboard.go()
