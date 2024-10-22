import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC
from kmk.modules.rotary_encoder import RotaryEncoder
from kmk.extensions.oled import Oled, OledDisplayMode


keyboard = KMKKeyboard()

# pin Setup
keyboard.col_pins = (
    board.PA02,  # C1
    board.PA04,  # C2
    board.PA10,  # C3
    board.PA11,  # C4
)

keyboard.row_pins = (
    board.PA08,  #r1
    board.PA09,  #r2
)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

# encodersetup??
encoder = RotaryEncoder(
    pin_a=board.PB08,  
    pin_b=board.PB09,  
    pin_switch=board.PA03,  
)

keyboard.modules.append(encoder)

oled_ext = Oled(
    oled_width=128, oled_height=64,
    scl=board.PA09, 
    sda=board.PA08,  
    display_mode=OledDisplayMode.SHOW_KEYMAP,  
)

keyboard.extensions.append(oled_ext)


keyboard.keymap = [
    # base layer
    [
        KC.A, KC.B, KC.C,
        KC.D, KC.E, KC.F,  
    ],
]


encoder.map = [
    (KC.VOLD, KC.VOLU)  
]

if __name__ == '__main__':
    keyboard.go()