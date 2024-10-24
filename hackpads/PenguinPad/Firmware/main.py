print("Starting")

import board
from kmk.kmkkeyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.macros import Macros
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.display.ssd1306 import SSD1306
import busio

#Initialize the keyboard
keyboard = KMKKeyboard()

#Initialize modules
encoderhandler = EncoderHandler()
macros = Macros()

#Initialize the I2C bus for the OLED display
i2c = busio.I2C(scl=board.GP7, sda=board.GP6)

#Initialize the SSD1306 display
display = SSD1306(i2c=i2c, width=128, height=32)

#Add modules and extensions to the keyboard
keyboard.modules = [macros, encoderhandler]
keyboard.extensions.append(display)

#Define the pins
keyboard.colpins = (board.GP26, board.GP27, board.GP28)
keyboard.rowpins = (board.GP29, board.GP0)
keyboard.diodeorientation = DiodeOrientation.COL2ROW

#Define encoder pins and map
encoderhandler.pins = ((board.GP9, board.GP10, board.GP3, True),)
encoderhandler.map = [
    ((KC.UP, KC.DOWN, KC.MUTE),),  # Standard
]

#Define the keymap with multiple layers
keyboard.keymap = [
    # Layer 0
    [
        KC.A, KC.B, KC.C, KC.D,  # 1: A / B / C / D
        KC.MO(1), KC.MO(2),  # 2: Toggle Layer 1 / 2
        KC.MPLY, KC.MPLY,  # 3: Play/Pause
    ],
]

#Function to update the OLED display with the current layer
def updatedisplay():
    display.clear()
    display.text(f"Layer: {keyboard.active_layers[0]}", 0, 0, 1)
    display.show()

if __name == '__main':
    keyboard.go()