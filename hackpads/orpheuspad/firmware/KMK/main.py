# DEAD CODE, NOT DONE!

print("Hackpad Testing!")

# Basic imports for orpheuspad
import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

# Extra features

from kmk.modules.encoder import EncoderHandler
from kmk.extensions.RGB import RGB


print(dir(board))

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP27, board.GP26)
keyboard.row_pins = (board.GP29, board.GP28)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

# RGB imports
# TODO: ADD PINS
rgb = RGB(pixel_pin=board.GP3, num_pixels=2)
keyboard.extensions.append(rgb)

# TODO: add OLED display

encoder_handler = EncoderHandler()
encoder_handler.pins = ((keyboard.pin_a, keyboard.pin_b, None, False))


keyboard.keymap = [ # TODO: fix this lol
    [
        # Example for rotary encoder
        KC.AUDIO_VOL_DOWN,
        KC.AUDIO_VOL_UP,

        # switches
              KC.F, 
        KC.U, KC.C, KC.K,
    ]
]


if __name__ == '__main__':
    keyboard.go()