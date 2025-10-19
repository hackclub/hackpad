'''
KW-01 RGBoard V1
Untested code for a 2x4 macropad using the XIAO RP2040. 
Currently supports simple numpad function. Blocked on hardware assembly.
'''

import board
import neopixel
from screen_brightness_control import set_brightness, get_brightness
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.matrix import MatrixScanner, DiodeOrientation
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.encoder import EncoderHandler

# Initialize the NeoPixel chain
NUM_PIXELS = 8
pixels = neopixel.NeoPixel(board.D6, NUM_PIXELS, auto_write=False)
keys_pressed = []

# Define colors for each key
colors = [
    (255, 0, 0),    # Red
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    (255, 255, 0),  # Yellow
    (0, 255, 255),  # Cyan
    (255, 0, 255),  # Magenta
    (255, 255, 255),# White
    (128, 0, 128)   # Purple
]


# Encoder rotation
def encoder_handler(direction):
    SCREEN_BRIGHTNESS = get_brightness()
    if direction == 1:
        # Increase brightness
        print("Increase brightness")
        SCREEN_BRIGHTNESS += 1
        set_brightness(SCREEN_BRIGHTNESS)
    elif direction == -1:
        # Decrease brightness
        print("Decrease brightness")
        SCREEN_BRIGHTNESS -= 1
        set_brightness(SCREEN_BRIGHTNESS)

# Neopixel lighting
def update_keys():
    for i in range(NUM_PIXELS):
        if i in keys_pressed:
            pixels[i] = colors[i]
        else:
            pixels[i] = (0, 0, 0)
    pixels.show()

def press(key):
    keys_pressed.append(key.index)
    update_keys()
    return Press(key)

def release(key):
    keys_pressed.remove(key.index) 
    update_keys()
    return Release(key)

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

# Matrix definitions
ROW_PINS = [board.D1, board.D7]
COL_PINS = [board.D2, board.D3, board.D4, board.D5]

# Matrix scanner
keyboard.matrix = MatrixScanner(
    cols=COL_PINS,
    rows=ROW_PINS,
    diode_orientation=DiodeOrientation.ROW2COL
)

# Encoder definition
ENCODER_PINS = (board.D9, board.D10)

# Encoder handler
encoder = EncoderHandler(ENCODER_PINS, encoder_handler)
keyboard.modules.append(encoder)

# Here you define the buttons corresponding to the matrix
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [KC.N1, KC.N2, KC.N3, KC.N4],
    [KC.N5, KC.N6, KC.N7, KC.N8]
]

macros.press = press
macros.release = release

# Start kmk!
if __name__ == '__main__':
    keyboard.go()