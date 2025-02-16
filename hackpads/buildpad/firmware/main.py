import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.display import Display, TextEntry, ImageEntry
from kmk.extensions.display.ssd1306 import SSD1306
import busio

BUS = busio.I2C(board.GP_SCL, board.GP_SDA)

driver = SSD1306(i2c=BUS, device_address=0x3C)

display = Display(
    display=driver,
    width=128,
    height=32
)

display.entries = [
    TextEntry("Hello, World!"),
    ImageEntry("kmk_logo.pbm"),
]

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP3, board.GP4, board.GP2, board.GP1)
keyboard.row_pins = (board.GP26, board.GP27, board.GP28, board.GP29)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# I'm going to change this as I see fit when I get it physically
keyboard.keymap = [
    [
        [KC.MUTE, KC.VOLD, KC.VOLU, KC.PLAY_PAUSE],  # Media controls
        [KC.SCRN, KC.NEW_TAB, KC.WEB_SEARCH, KC.FIND],  # Productivity shortcuts
        [KC.COPY, KC.PASTE, KC.CUT, KC.UNDO],        # Editing shortcuts
        [KC.LCTRL, KC.LALT, KC.LSFT, KC.SPC],       # Modifier keys and space
    ],
]

if __name__ == '__main__':
    keyboard.go()