import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.scanners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys

keyboard.extensions.append(MediaKeys())
# Initialize the keyboard
keyboard = KMKKeyboard()

# USB configuration
keyboard.usb.device_version = "1.0.0"
keyboard.usb.pid = 0x0000
keyboard.usb.vid = 0xFEED

# Matrix pin configuration
keyboard.matrix_pins = {
    "cols": [board.GP2, board.GP3],  # D2, D3
    "rows": [board.GP0, board.GP1, board.GP5],  # D0, D1, D5
}

# Rotary encoder setup
encoder = EncoderHandler()
encoder.pins = [
    {board.GP7, board.GP6, None}  # D7, D6
]
keyboard.modules.append(encoder)

# Define the keymap
keyboard.keymap = [[[KC.F2, KC.F11], [KC.MNXT, KC.MPLY], [KC.NO, KC.MUTE]]]
keyboard.diode_orientation = DiodeOrientation.COL2ROW


encoder.map = [(KC.AUDIO_VOLUME_UP, KC.AUDIO_VOLUME_DOWN)]

# Register the encoder update callback


if __name__ == "__main__":
    # Go to the main loop
    keyboard.go()
