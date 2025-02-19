import board
import time
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import MatrixScanner
from kmk.keys import KC
from kmk.modules.rotary_encoder import RotaryEncoderHandler
from kmk.extensions.peg_rgb_matrix import Rgb_matrix

keyboard = KMKKeyboard()

rgb = Rgb_matrix()
keyboard.extensions.append(rgb)


keyboard.matrix = MatrixScanner(
    column_pins=[board.GP3, board.GP4, board.GP2, board.GP1], 
    row_pins=[board.GP27, board.GP28, board.G29],  
    value_when_pressed=False,
    )

keyboard.keymap = [
   #layer0
   [
        [KC.F13, KC.F14, KC.F15, KC.F16,],
        [KC.F17, KC.F18, KC.F19, KC.F20,],
        [KC.F21, KC.F22, KC.F23, KC.F24,],
    ],
    #layer1
    [
        [KC.F25, KC.F26, KC.F27, KC.F28,],
        [KC.F29, KC.F30, KC.F31, KC.F32,],
        [KC.F33, KC.F34, KC.F35, KC.F36,],
    ],
    #layer2
    [
        [KC.F37, KC.F38, KC.F39, KC.F40,],
        [KC.F41, KC.F42, KC.F43, KC.F44,],
        [KC.F45, KC.F46, KC.F47, KC.F48,],
    ],
]




def switch_layer(layer):
    keyboard.active_layers = [layer]
    if layer == 0:
        keyboard.set_pixel(0, 255, 0, 0)
        keyboard.set_pixel(1, 255, 1, 1)
        keyboard.set_pixel(2, 255, 2, 2)
        keyboard.set_pixel(3, 255, 3, 3)
    elif layer == 1:
        keyboard.set_pixel(0, 0, 255, 0)
        keyboard.set_pixel(1, 1, 255, 1)
        keyboard.set_pixel(2, 2, 255, 2)
        keyboard.set_pixel(3, 3, 255, 3)
    elif layer == 2:
        keyboard.set_pixel(0, 0, 0, 255)
        keyboard.set_pixel(1, 1, 1, 255)
        keyboard.set_pixel(2, 2, 2, 255)
        keyboard.set_pixel(3, 3, 3, 255)
    rgb.write()

current_layer = 0
switch_layer(current_layer)

encoder = RotaryEncoderHandler(pin_a=board.GP7, pin_b=board.GP6,pin_S1=board.GP1)
encoder.rotation_cw = KC.VOLU  
encoder.rotation_ccw = KC.VOLD  
keyboard.modules.append(encoder)

while True:
    keyboard.update()
    if keyboard.matrix.is_pressed(0, 0):
        current_layer = (current_layer + 1) % 3
        switch_layer(current_layer)
        time.sleep(0.3)


if __name__ == '__main__':
    keyboard.go()