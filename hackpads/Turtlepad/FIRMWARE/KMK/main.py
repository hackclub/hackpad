import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.encoder import EncoderHandler
import neopixel

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

mode1 = [[KC.N1, KC.N2, KC.N3], [KC.N4, KC.N5, KC.N6], [KC.N7, KC.N8, KC.N9], [KC.N0, KC.ENTER, KC.BSPC]]

# Define your pins here!
keyboard.col_pins = (board.GPIO4, board.GPIO2, board.GPIO1)
keyboard.row_pins = (board.GPIO28, board.GPIO29, board.GPIO6, board.GPIO7)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Tell kmk we are not using a key matrix
keyboard.keymap = mode1

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md

encoder = EncoderHandler()
encoder.pins = (board.GPIO3, board.GPIO26, GPIO0)  # Define the pins for the encoder
encoder.map = [
    (KC.VOLU, KC.VOLD, KC.MUTE),  # Volume up/down
]

keyboard.extensions.append(encoder)

NUM_PIXELS = 2  # Number of RGB LEDs
pixels = neopixel.NeoPixel(board.GPIO9, NUM_PIXELS)

# Set the colors (R, G, B) for the LEDs
pixels[0] = (255, 0, 0)  # Red
pixels[1] = (0, 255, 0)  

# Start kmk!
if __name__ == '__main__':
    keyboard.go()