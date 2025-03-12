import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import MatrixScanner
from kmk.keys import KC
from kmk.extensions.RGB import RGB
from kmk.modules.macros import Press, Release, Tap, Macros

keyboard = KMKKeyboard()
macros = Macros()
keyboard.modules.append(macros)

COL_PINS = [board.GP26, board.GP27, board.GP28, board.GP29]
ROW_PINS = [board.GP3, board.GP4, board.GP2, board.GP1]

keyboard.matrix = MatrixScanner(
  column_pins = COL_PINS,
  row_pins = ROW_PINS
)

ALT_F4_MACRO = KC.MACRO(
  Press(KC.LALT),
  Tap(KC.F4),
  Release(KC.LALT)
)

keyboard.keymap = [
  [KC.NUMLOCK, KC.KP_8, KC.KP_9,   KC.BSPACE],
  [KC.KP_7,    KC.KP_5, KC.KP_6,   ALT_F4_MACRO],
  [KC.KP_4,    KC.KP_2, KC.KP_3,   KC.PSCREEN],
  [KC.KP_1,    KC.KP_0, KC.KP_DOT, KC.KP_ENTER],
]

rgb = RGB(pixel_pin=board.GP0, num_pixels=16)
rgb.set_rgb_fill(255, 255, 255)
keyboard.extensions.append(rgb)

if __name__ == "__main__":
    keyboard.go()