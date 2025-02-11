from kmk.kmk_keyboard import KMKKeyboard
import board
import busio
from kmk.extensions.display import Display, TextEntry, ImageEntry
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.scanners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.encoder import GPIOEncoder
from kmk.modules.layers import Layers
from kmk.keys import KC
from kmk.modules.mouse_keys import MouseKeys

# Create the KMKKeyboard object
keyboard = KMKKeyboard()
keyboard.modules.append(Layers())

i2c_bus = busio.I2C(board.D5, board.D4)

keyboard.modules.append(GPIOEncoder())
encoder_handler = GPIOEncoder()

keyboard.extensions.append(MediaKeys())
keyboard.modules.append(MouseKeys())

driver = SSD1306(
    i2c=i2c_bus,
    device_address=0x3C,
)

display = Display(
    # Mandatory:
    display=driver,
    entries=[
        TextEntry(text="Layer: ", x=0, y=32, y_anchor="B"),
        TextEntry(text="DEFAULT", x=40, y=32, y_anchor="B", layer=0),
        TextEntry(text="FUNCTION", x=40, y=32, y_anchor="B", layer=1),
    ],
    # Optional:
    width=128,  # screen size
    height=32,  # screen size
    flip=False,  # flips your display content
    flip_left=False,  # flips your display content on left side split
    flip_right=False,  # flips your display content on right side split
    brightness=0.8,  # initial screen brightness level
    brightness_step=0.1,  # used for brightness increase/decrease keycodes
    # dim_time=20,  # time in seconds to reduce screen brightness
    # dim_target=0.1,  # set level for brightness decrease
    # off_time=60,  # time in seconds to turn off screen
    # powersave_dim_time=10,  # time in seconds to reduce screen brightness
    # powersave_dim_target=0.1,  # set level for brightness decrease
    # powersave_off_time=30,  # time in seconds to turn off screen
)
keyboard.extensions.append(display)

keyboard.row_pins = (board.D0, board.D1, board.D2, board.D3, board.D6, board.D7)
keyboard.col_pins = (
    board.D8,
    board.D9,
    board.D10,
    board.D11,
    board.D12,
    board.D13,
    board.D14,
    board.D15,
    board.D16,
    board.D17,
    board.D18,
    board.D19,
    board.D20,
    board.D21,
)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

encoder_handler.pin_a = board.D22
encoder_handler.pin_b = board.D26


LYR_DEF, LYR_FN = 0, 1


# fmt: off
keyboard.keymap = [
    # DEF LAYER
    [ 
        KC.MPLY, KC.F1, KC.F2 , KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, KC.DELETE,
        KC.ESC, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINS, KC.EQL, KC.BSPC,
        KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC, KC.BSLS, 
        KC.CAPS, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT, KC.ENTER, KC.PGDN,
        KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.UP, KC.RSFT, KC.HOME, KC.UP, 
        KC.LCTL, KC.LGUI, KC.LALT, KC.MO(LYR_FN), KC.SPC, KC.NO, KC.NO, KC.RALT, KC.RCTL, KC.LEFT, KC.DOWN, KC.RIGHT, KC.PGUP, KC.PSCR,
    ],
    # FN LAYER
    [
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, 
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, 
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, 
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, 
        KC.TRNS, KC.TRNS, KC.TRNS, KC.MO(LYR_FN), KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, 
    ],
]


# fmt: on
encoder_handler.divisor = 2
encoder_handler.map = [
    # DEF LAYER
    ((KC.VOLD, KC.VOLU),),  # VOL_DOWN	VOL_UP
    # FN LAYER
    ((KC.VOLD, KC.VOLU),),  # VOL_DOWN	VOL_UP
]

if __name__ == "__main__":
    keyboard.go()
