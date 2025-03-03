# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.rotary_encoder import RotaryEncoderHandler
from kmk.extensions.peg_rgb_matrix import Rgb_matrix

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Tell kmk we are gonna have a brain poop! (key matrix)
keyboard.matrix = MatrixScanner(
    column_pins=[board.GP27, board.GP28, board.GP29],  # Columns
    row_pins=[board.GP4, board.GP2, board.GP1],  # Rows
    value_when_pressed=False,
)

# ROTARY!
encoder = RotaryEncoderHandler(pin_a=board.GP7, pin_b=board.GP6)
encoder.rotation_cw = KC.VOLU  # ears go boom!
encoder.rotation_ccw = KC.VOLD  # ears go deaf!
keyboard.modules.append(encoder)

rgb = Rgb_matrix(pin=[board.GP26,board.GP3], led_count=4)
keyboard.extensions.append(rgb)

rainbow_index = 0
last_press_time = 0

def update_leds():
    global rainbow_index, last_press_time
    current_time = time.monotonic()
    
    if keyboard.keys_pressed:
        rgb.set_rgb_fill((255, 0, 0))
        last_press_time = current_time
    elif encoder.encoder_moved:
        rgb.set_rgb_fill((0, 255, 0)) 
    else:
        rainbow_colors = [
            (255, 0, 0), (255, 127, 0), (255, 255, 0), 
            (0, 255, 0), (0, 0, 255), (75, 0, 130), (148, 0, 211)
        ]
        rgb.set_rgb_fill(rainbow_colors[rainbow_index % len(rainbow_colors)])
        rainbow_index += 1

    time.sleep(0.1) 

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [KC.A, KC.DELETE, KC.MACRO("Hello world!"), KC.Macro(Press(KC.LCMD), Tap(KC.S), Release(KC.LCMD)),]
]

# "i am planting zhe bomb"
if __name__ == '__main__':
    keyboard.go()