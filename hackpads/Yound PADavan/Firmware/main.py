import board
import time
import digitalio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import MatrixScanner
from kmk.keys import KC
from kmk.modules.rotary_encoder import RotaryEncoderHandler
from kmk.extensions.peg_rgb_matrix import Rgb_matrix

keyboard = KMKKeyboard()

keyboard.matrix = MatrixScanner(
    column_pins=[board.GP2, board.GP3, board.GP4], 
    row_pins=[board.GP5, board.GP6, board.GP7],
    value_when_pressed=False
)

layer0 = [KC.A, KC.B, KC.C, KC.D, KC.E, KC.F, KC.G, KC.H, KC.I]
layer1 = [KC.J, KC.K, KC.L, KC.M, KC.N, KC.O, KC.P, KC.Q, KC.R]
layer2 = [KC.S, KC.T, KC.U, KC.V, KC.W, KC.X, KC.Y, KC.Z, KC.ENTER]

keyboard.keymap = [layer0, layer1, layer2]
keyboard.active_layers = [0]

encoder = RotaryEncoderHandler(pin_a=board.GP26, pin_b=board.GP27)
encoder.rotation_cw = KC.VOLU
encoder.rotation_ccw = KC.VOLD
keyboard.modules.append(encoder)

enc_btn = digitalio.DigitalInOut(board.GP28)
enc_btn.switch_to_input(pull=digitalio.Pull.UP)

rgb = Rgb_matrix(pin=board.GP1, led_count=3)
keyboard.extensions.append(rgb)

current_mode = 0
last_button_value = True

def update_hook():
    global current_mode, last_button_value

    btn_val = enc_btn.value
    if last_button_value and not btn_val:
        current_mode = (current_mode + 1) % 3
        keyboard.active_layers = [current_mode]
    last_button_value = btn_val

    if current_mode == 0:
        rgb.set_rgb(0, (255, 0, 0))
        rgb.set_rgb(1, (0, 0, 0))
        rgb.set_rgb(2, (0, 0, 0))
    elif current_mode == 1:
        rgb.set_rgb(0, (0, 0, 0))
        rgb.set_rgb(1, (0, 255, 0))
        rgb.set_rgb(2, (0, 0, 0))
    else:
        rgb.set_rgb(0, (0, 0, 0))
        rgb.set_rgb(1, (0, 0, 0))
        rgb.set_rgb(2, (0, 0, 255))

keyboard.update_hook = update_hook

if __name__ == '__main__':
    keyboard.go()