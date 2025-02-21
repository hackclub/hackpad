from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

# Define keymap for 9 switches
keyboard.keymap = [
    [KC.A, KC.B, KC.C,
     KC.D, KC.E, KC.F,
     KC.G, KC.H, KC.I]
]

# Encoder setup (single encoder on the macropad)
encoder_handler.pins = ((1, 2),)  # Update with correct GPIO pins
encoder_handler.map = ((KC.VOLU, KC.VOLD),)  # Volume up/down example

if __name__ == '__main__':
    keyboard.go()