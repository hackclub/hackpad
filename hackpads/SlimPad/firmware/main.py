from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
#Basic configuration 

# Optional OLED support
from kmk.extensions.oled import OLEDExtension
from kmk.keys import KC

# Initialize the keyboard
keyboard = KMKKeyboard()

# Define GPIO pins for rows and columns
keyboard.col_pins = (3, 4, 2, 1)  # Columns connected to GP3, GP4, GP2, GP1
keyboard.row_pins = (26, 27)      # Rows connected to GP26, GP27

# Set the diode direction
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Add keys (replace these with your actual key mapping)
keyboard.keymap = [
    [KC.A, KC.B, KC.C, KC.D],     # Row 1 keymap
    [KC.E, KC.F, KC.G, KC.H],     # Row 2 keymap
]

# OLED setup
oled_ext = OLEDExtension(oled_sda=6, oled_scl=7)
keyboard.extensions.append(oled_ext)

if __name__ == '__main__':
    keyboard.go()
