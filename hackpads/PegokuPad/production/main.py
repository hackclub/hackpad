import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.extensions.rotary_encoder import RotaryEncoder

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

encoder = RotaryEncoder(pin_a=board.D4, pin_b=board.D5)
keyboard.extensions.append(encoder)

encoder.map = [
    (KC.VOLU, KC.VOLD),
]

ROWS = [board.D0, board.D1, board.D2, board.D3]
COLS = [board.D10, board.D9, board.D8, board.D7]

keyboard.matrix = KeysScanner(
    rows=ROWS,
    cols=COLS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [KC.MACRO(Press(KC.LCMD), Tap(KC.T), Release(KC.LCMD)), KC.MACRO(Press(KC.LCMD), Tap(KC.S), Release(KC.LCMD)), KC.MACRO(Press(KC.LCMD), Tap(KC.C), Release(KC.LCMD)), KC.MACRO(Press(KC.LCTRL, KC.LCMD), Tap(KC.W), Release(KC.LCTRL, KC.LCMD))], 
    [KC.MACRO(Press(KC.LCMD), Tap(KC.E), Release(KC.LCMD)), KC.MACRO(Press(KC.LCMD), Tap(KC.W), Release(KC.LCMD)), KC.MACRO(Press(KC.LCMD), Tap(KC.X), Release(KC.LCMD)), KC.MACRO(Press(KC.LCTRL, KC.LCMD), Tap(KC.X), Release(KC.LCTRL, KC.LCMD))], 
    [KC.MACRO(Press(KC.LSHIFT, KC.LCMD), Tap(KC.X), Release(KC.LSHIFT, KC.LCMD)), KC.MACRO(Press(KC.LCMD), Tap(KC.G), Release(KC.LCMD)), KC.MACRO(Press(KC.LCMD), Tap(KC.K), Release(KC.LCMD)), KC.MACRO(Press(KC.LCMD), Tap(KC.I), Release(KC.LCMD))], 
    [KC.MACRO(Press(KC.LCTRL, KC.LCMD), Tap(KC.V), Release(KC.LCTRL, KC.LCMD)), KC.MACRO(Press(KC.LCTRL, KC.LSHIFT), Tap(KC.ESCAPE), Release(KC.LCTRL, KC.LSHIFT)), KC.MACRO(Press(KC.LCTRL, KC.LCMD), Tap(KC.T), Release(KC.LCTRL, KC.LCMD)), KC.MACRO(Press(KC.LCMD), Tap(KC.P), Release(KC.LCMD))] 
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()
    
