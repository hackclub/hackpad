#  artzelpad
import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.scanners import DiodeOrientation
from kmk.extensions.peg_oled_Display import Oled,OledDisplayMode,OledReactionType,OledData

# keyboard
keyboard = KMKKeyboard()

keyboard.col_pins = (board.D0, board.D1, board.D2)
keyboard.row_pins = (board.D3, board.D8, board.D10)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# macros
macros = Macros()
keyboard.modules.append(macros)

macros.define(
    "COPY_W",
    Press(KC.LCMD),
    Tap(KC.C),
    Release(KC.LCMD),
)

macros.define(
    "PASTE_W",
    Press(KC.LCMD),
    Tap(KC.V),
    Release(KC.LCMD),
)

macros.define(
    "UNDO_AAHH",
    Press(KC.LCMD),
    Tap(KC.Z),
    Release(KC.LCMD),
)

COPY_W = KC.COPY_W
PASTE_W = KC.PASTE_W
UNDO_AAHH = KC.UNDO_AAHH

# set up oled
oled_data = OledData()
oled_ext = Oled(
    oled_data=oled_data,
    flip=False,
)

# track pressed keys
pressed_keys = set()

# make oled display pressed keys
def update_oled():
    pressed_text = ", ".join(sorted(pressed_keys))
    oled_ext.display_text(pressed_text)

def process_event(key, pressed, keyboard):
    key_str = str(key)
    if pressed:
        pressed_keys.add(key_str)
    else:
        pressed_keys.discard(key_str)
    update_oled()

# updates oled after the matrix scan
keyboard.after_matrix_scan = update_oled

# sw1, sw2, sw3
# sw6, sw5, sw4
# sw7, sw8, sw9
keyboard.keymap = [
    [   UNDO_AAHH, KC.LEFT, KC.B,
        COPY_W, KC.DOWN, KC.UP,
        PASTE_W, KC.RIGHT, KC.E,
    ]
]

if __name__ == '__main__':
    keyboard.go()