import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import MatrixScanner
from kmk.modules.layers import Layers
from kmk.modules.steno import StenoMode

keyboard = KMKKeyboard()

# Define the key matrix (adjust GPIOs later)
keyboard.matrix = MatrixScanner(
    columns=[board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5],
    rows=[board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11, board.GP12],
)

# Enable Steno Mode
steno = StenoMode()
keyboard.modules.append(steno)

if __name__ == '__main__':
    keyboard.go()
