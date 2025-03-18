import board
import busio

from kmk.extensions.display import Display, ImageEntry
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.display.ssd1306 import SSD1306

keyboard = KMKKeyboard()

keyboard.col_pins = (board.D7, board.D8, board.D9)
keyboard.row_pins = (board.D1, board.D2, board.D3)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.F13, KC.F14, KC.F15],
    [KC.F16, KC.F17, KC.F18],
    [KC.F19, KC.F20, KC.F21]
]

i2c_bus = busio.I2C(board.D5, board.D4)

driver = SSD1306(
    i2c = i2c_bus
)
display = Display(
    display=driver,
    width=128, 
    height=64, 
    flip = False,
    flip_left = False,
    flip_right = False,
    brightness=1, 
    brightness_step=0.1, 
    dim_time=20,
    dim_target=0.1,
    off_time=60, 
    powersave_dim_time=10,
    powersave_dim_target=0.1, 
    powersave_off_time=30,
)

display.entires = [
    ImageEntry(image="yan.bmp", x=0, x=0)
]

keyboard.extensions.append(display)

if __name__ == '__main__':
    keyboard.go()