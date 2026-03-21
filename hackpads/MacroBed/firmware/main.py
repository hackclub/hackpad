# Note: Currently the firmware is only for testing the hardware. Pins should be correct
import board
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

from kmk.extensions.display import Display, TextEntry, ImageEntry
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.extensions.RGB import RGB

from kmk.modules.encoder import EncoderHandler


# Inits
keyboard = KMKKeyboard()


# Modules
encoder_handler = EncoderHandler()

keyboard.modules = [encoder_handler]


# Extension - RGB
rgb = RGB(pixel_pin=board.GP46, num_pixels=12)
keyboard.extensions.append(rgb)


# Extension - Display
driver = SSD1306(
    i2c=busio.I2C(board.GP9, board.GP7),
)

display = Display(
    # Mandatory:
    display=driver,
    # Optional:
    width=128,  # screen size
    height=32,  # screen size
    flip=False,  # flips your display content
    flip_left=False,  # flips your display content on left side split
    flip_right=False,  # flips your display content on right side split
    brightness=1,  # initial screen brightness level
    dim_target=1,  # set level for brightness decrease
)

display.entries = [
    TextEntry(text="Hey!", x=0, y=0),
]

keyboard.extensions.append(display)


# Matrix config
keyboard.col_pins = (board.GP14, board.GP13, board.GP12)
keyboard.row_pins = (board.GP18, board.GP17, board.GP16, board.GP15)
keyboard.diode_orientation = DiodeOrientation.COL2ROW


# Encoder config
encoder_handler.pins = ((board.GP5, board.GP4, board.GP3, False),)


# Keymap (for testing only)
keyboard.keymap = [
    [KC.A, KC.B, KC.C],
    [KC.D, KC.E, KC.F],
    [KC.G, KC.H, KC.I],
    [KC.J, KC.K, KC.L],
]

encoder_handler.map = [
    ((KC.UP, KC.DOWN, KC.MUTE),),
]


# Loop
if __name__ == "__main__":
    keyboard.go()
