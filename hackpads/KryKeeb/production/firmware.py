import board
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306

# Define column and row pins based on your schematic
COL1 = board.D0
COL2 = board.D1
COL3 = board.D2
ROW1 = board.D3
ROW2 = board.D4

# Initialize I2C bus for the OLED display
i2c_bus = busio.I2C(board.D5, board.D6)  # SCL, SDA

# Initialize the SSD1306 display
display_driver = SSD1306(
    i2c=i2c_bus,
    device_address=0x3C,  # Common I2C address for SSD1306
)

# Create the keyboard instance
keyboard = KMKKeyboard()

# Define column and row pins
keyboard.col_pins = (COL1, COL2, COL3)
keyboard.row_pins = (ROW1, ROW2)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Set up the display with initial text
display = Display(
    display=display_driver,
    entries=[
        TextEntry(text='KryKeeb', x=64, y=10, x_anchor='M', y_anchor='M'),
        TextEntry(text='by Krishna', x=64, y=22, x_anchor='M', y_anchor='M'),
    ],
    width=128,
    height=32,
    dim_time=10,     # Time in seconds before dimming
    dim_target=0.2,  # Dim brightness level (0.0 to 1.0)
    off_time=1200,   # Time in seconds before turning off
    brightness=1,    # Initial brightness level (0.0 to 1.0)
)

# Add display to keyboard extensions
keyboard.extensions.append(display)

# Define the keymap
keyboard.keymap = [
    [KC.A, KC.B, KC.C],  # Row 1
    [KC.D, KC.E, KC.F],  # Row 2
]

# Start the keyboard
if __name__ == '__main__':
    keyboard.go()
