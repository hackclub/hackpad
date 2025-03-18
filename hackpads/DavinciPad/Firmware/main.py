print("Starting")

import board
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.display import Display, TextEntry, ImageEntry
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.display.ssd1306 import SSD1306

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP26, board.GP27, board.GP28)
keyboard.row_pins = (board.GP29, board.GP0)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Initialize the I2C bus for the OLED display
i2c = busio.I2C(scl=board.GP7, sda=board.GP6)

# Initialize the SSD1306 display
display = SSD1306(i2c=i2c, width=128, height=32)
keyboard.extensions.append(Display(display=display))

# Define the keymap with multiple layers
keyboard.keymap = [
    # Layer 0
    [
        KC.LCTL(KC.LSFT(KC.Z)), KC.LGUI(KC.SPC),  # 1: Ctrl+Shift+Z / Windows+Space
        KC.MO(1), KC.MO(2),  # 2: Toggle Layer 1 / 2
        KC.MPLY, KC.MPLY,  # 3: Play/Pause
    ],
    [
        KC.LCTL(KC.Z), KC.LCTL(KC.C),  # 4: Ctrl+Z / Ctrl+C
        KC.DEL, KC.LCTL(KC.V),  # 5: Delete / Ctrl+V
        KC.LCTL(KC.B), KC.FN(KC.S),  # 6: Ctrl+B / Fn+S
    ]
]

# Function to update the OLED display with the current layer
def update_display():
    display.clear()
    display.text(f"Layer: {keyboard.active_layers[0]}", 0, 0, 1)
    display.show()

# Hook the display update function to the keyboard's layer change event
keyboard.before_matrix_scan.append(update_display)

if __name__ == '__main__':
    keyboard.go()