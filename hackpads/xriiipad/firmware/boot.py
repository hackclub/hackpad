print("Starting")

import board
import busio

from kmk.extensions.display import Display, TextEntry, ImageEntry

from kmk.extensions.display.ssd1306 import SSD1306

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

i2c_bus = busio.I2C(board.SCL, board.SDA)

driver = SSD1306(
    i2c=i2c_bus
)

display = Display(
    display=driver,
    width=128,
    height=64
)

display.entries = [
    ImageEntry(image="Untitled.bmp", x=0, y=0),
]

keyboard.col_pins = (board.GP0, board,GP1, board.GP2, board.GP3)
keyboard.row_pins = (board.RX, board.SCK, board.MISO)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.Q, KC.W, KC.O, KC.P],
    [KC.S, KC.D, KC.K, KC.L],
    [KC.NO, KC.C, KC.M, KC.NO]
]

if __name__ == '__main__':
    keyboard.go()