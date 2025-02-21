import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.matrix import MatrixScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.encoder import EncoderHandler

# Initialize KMK keyboard instance
keyboard = KMKKeyboard()

# Add macro module
macros = Macros()
keyboard.modules.append(macros)

# Add encoder module
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

# Setup Rotary Encoder (Volume Control)
encoder_handler.pins = ((board.D1, board.D2),)  
encoder_handler.map = [((KC.VOLU, KC.VOLD),)]  # Volume Up, Volume Down

# Define row and column pins
ROW_PINS = [board.D2, board.D3, board.D6]
COL_PINS = [board.D9, board.D8, board.D7]

keyboard.matrix = MatrixScanner(
    columns=COL_PINS,
    rows=ROW_PINS,
    columns_to_anodes=False,
)

# Define the keymap
keyboard.keymap = [
    [KC.MACRO(Press(KC.LCTRL), Tap(KC.C), Release(KC.LCTRL)), KC.MACRO(Press(KC.LCTRL), Tap(KC.V), Release(KC.LCTRL)), KC.MACRO(Press(KC.LCTRL), Tap(KC.Z), Release(KC.LCTRL))],
    [KC.MACRO(Press(KC.LCTRL), Tap(KC.S), Release(KC.LCTRL)), KC.F5, KC.MACRO(Press(KC.LSHIFT), Tap(KC.F5), Release(KC.LSHIFT))],  
    [KC.MACRO("git push\n"), KC.MACRO("git pull\n"), KC.MACRO("git log --oneline\n")],
]

# Start KMK
if __name__ == '__main__':
    keyboard.go()
