import board
import digitalio
import rotaryio
import time
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import MatrixScanner
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.OLED_Display import Oled,OledDisplayMode

keyboard = KMKKeyboard()

keyboard.matrix = MatrixScanner(
    cols=[board.GP1, board.GP2, board.GP3],
    rows=[board.GP26, board.GP27, board.GP28, board.GP29],
    diodes=True
)

keyboard.keymap = [
    [KC.N7, KC.N8, KC.N9,
     KC.N4, KC.N5, KC.N6,
     KC.N1, KC.N2, KC.N3,
     KC.N0, KC.DOT, KC.ENT]
]

encoder = EncoderHandler()
encoder.pins = (board.GP0, board.GP4)
encoder.on_clockwise = KC.VOLU
encoder.on_counterclockwise = KC.VOLD
keyboard.modules.append(encoder)

oled = Oled(oled_type=OledDisplayMode.IMAGE, flip=False)
keyboard.extensions.append(oled)

def render_animation(oled):
    animation = [
        0b00011000, 0b00111100, 0b01111110, 0b11111111,
        0b01111110, 0b00111100, 0b00011000, 0b00000000,
    ]
    oled.image(animation)

oled.display_function = render_animation

if __name__ == '__main__':
    keyboard.go()