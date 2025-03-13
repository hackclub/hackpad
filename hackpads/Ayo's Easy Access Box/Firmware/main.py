import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()

# Matrix pins
COL1 = board.D0
COL2 = board.D1
COL3 = board.D2

ROW1 = board.D3
ROW2 = board.D4
ROW3 = board.D5

# rotary encoder pins
ROTA = board.D7
ROTB = board.D8
PUSHBUTTON = board.D9

# Matrix settings
keyboard.col_pins = (COL1, COL2, COL3)
keyboard.row_pins = (ROW1, ROW2, ROW3)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Encoder settings
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
encoder_handler.pins = ((ROTA, ROTB, PUSHBUTTON, False),)
encoder_handler.map = (((KC.VOLD, KC.VOLU, KC.MUTE),),)

keyboard.keymap = [
    [KC.LCTRL(KC.Z), KC.LCTRL(KC.Y), KC.LCTRL(KC.S),  # Row 1
    [KC.LALT(KC.TAB), KC.LCTRL(KC.F), KC.LCTRL(KC.SHIFT(KC.T)),  # Row 2
    [KC.LCTRL(KC.T), KC.LCTRL(KC.C), KC.LCTRL(KC.V)) # Row 3

]


if __name__ == "__main__":
    keyboard.go()
