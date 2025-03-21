import board
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306

# Define column and row pins for a 4x5 matrix
COL1 = board.D2
COL2 = board.D3
COL3 = board.D4
COL4 = board.D5
ROW1 = board.D6
ROW2 = board.D7
ROW3 = board.D8
ROW4 = board.D9
ROW5 = board.D10

# Initialize I2C bus for the displays
i2c_bus = busio.I2C(board.D4, board.D5)

# Initialize the SSD1306 displays
display_driver1 = SSD1306(
    i2c=i2c_bus,
    device_address=0x3C,  # First OLED address
)

display_driver2 = SSD1306(
    i2c=i2c_bus,
    device_address=0x3D,  # Second OLED address
)

# Create the keyboard instance
keyboard = KMKKeyboard()

# Define column and row pins
keyboard.col_pins = (COL1, COL2, COL3, COL4)
keyboard.row_pins = (ROW1, ROW2, ROW3, ROW4, ROW5)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Set up the displays with initial text
display1 = Display(
    display=display_driver1,
    entries=[TextEntry(text='Name', x=0, y=0, y_anchor='M')],
    width=128,
    height=32,
    dim_time=10,
    dim_target=0.2,
    off_time=1200,
    brightness=1,
)

display2 = Display(
    display=display_driver2,
    entries=[TextEntry(text='WELCOME', x=0, y=0, y_anchor='M')],
    width=128,
    height=32,
    dim_time=10,
    dim_target=0.2,
    off_time=1200,
    brightness=1,
)

# Add displays to keyboard extensions
keyboard.extensions.append(display1)
keyboard.extensions.append(display2)

# Define the keymap
keyboard.keymap = [
    [KC.MPRV, KC.MNXT, KC.NO, KC.NO],  # Row 1
    [KC.NO,   KC.NO,   KC.NO, KC.NO],  # Row 2
    [KC.NO,   KC.Z,    KC.X,  KC.NO],  # Row 3
    [KC.NO,   KC.NO,   KC.NO, KC.NO],  # Row 4
    [KC.NO,   KC.NO,   KC.NO, KC.NO],  # Row 5
]

# Start the keyboard
if __name__ == '__main__':
    keyboard.go()