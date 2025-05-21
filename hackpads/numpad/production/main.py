# This is currently just boilerplate; 
# I'll have to do a lot of tweaking around. 
# My goal is to get it to fully function, 
# type, control the mouse, etc. 
# Frees up my right hand. 

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DirectPins
from kmk.keys import KC

import board

keyboard = KMKKeyboard()

keyboard.matrix = DirectPins(
    pins=[
        board.D1,  # A
        board.D2,  # B
        board.D3,  # C
        board.D4,  # D
        board.D5,  # E
        board.D6,  # F
        board.D7,  # G
        board.D8,  # H
        board.D9,  # I
        board.D10, # J
        board.D11  # K
    ]
)

keyboard.keymap = [
    [
        KC.A, KC.B, KC.C, KC.D, KC.E,
        KC.F, KC.G, KC.H, KC.I, KC.J, KC.K
    ]
]

if __name__ == '__main__':
    keyboard.go()