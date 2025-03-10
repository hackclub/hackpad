from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.direct import DirectScan

keyboard = KMKKeyboard()

# Define the pins your switches are connected to
keyboard.matrix = DirectScan(
    pins=[
        board.D0,
        board.D1,
        board.D2,
        board.D3,
        board.D4,
        board.D5,
        board.D6,
        board.D7,
        board.D8,
    ]
)

# Define keymap
keyboard.keymap = [
    [
        KC.A, KC.B, KC.C,
        KC.D, KC.E, KC.F,
        KC.G, KC.H, KC.I
    ]
]

if __name__ == '__main__':
    keyboard.go()
