from kmk.kmk_keyboard import KMKKeyboard
from kmk.modules import usb
from kmk.modules import matrix
from kmk.keys import KC

keyboard = KMKKeyboard()
keyboard.modules.append(usb.USB)

rows = [6, 7, 0]  
cols = [26, 27, 28, 29]

keyboard.modules.append(matrix.Matrix(rows=rows, cols=cols))

keymap = [
    [KC.N1, KC.N2, KC.N3, KC.N4],
    [KC.N5, KC.N6, KC.N7, KC.N8],
    [KC.N9, KC.N0, KC.KP_MINUS, KC.KP_PLUS]
]

keyboard.keymap = keymap

if __name__ == "__main__":
    keyboard.go()