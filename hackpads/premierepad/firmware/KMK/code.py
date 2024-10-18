from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.matrix import MatrixScanner
from kmk.keys import KC
from kmk.modules.layers import Layers
import board 

keyboard = KMKKeyboard()

LAYER_1 = 0  
LAYER_2 = 1  
LAYER_3 = 2  

layers = Layers()
keyboard.modules.append(layers)

keyboard.keymap = [

    [KC.A, KC.F, KC.P, KC.SPACE], 
    [KC.B, KC.E, KC.F],           
    [KC.C, KC.H, KC.I],            

    [KC.A, KC.Y, KC.Z, KC.SPACE],             
    [KC.B, KC.W, KC.R],   
    [KC.C, KC.T, KC.G],       

    [KC.A, KC.B, KC.C, KC.SPACE],  
    [KC.B, KC.M, KC.N],            
    [KC.C, KC.O, KC.P],             
]

keyboard.matrix = MatrixScanner(
    rows=[board.PA26, board.PA27, board.PA28], 
    cols=[board.PA03, board.PA04, board.PA02, board.PA08], 
)

layer_switch_map = {
    KC.A: LAYER_1,
    KC.B: LAYER_2,
    KC.C: LAYER_3,
}

def on_press_handler(key):
    if key in layer_switch_map:
        keyboard.set_layer(layer_switch_map[key])

keyboard.before_press.append(on_press_handler)

from kmk.scanners.encoder import RotaryEncoder

encoder = RotaryEncoder(
    pins=[board.PA29, board.PA6],  
    divisor=2,  
)
keyboard.modules.append(encoder)

encoder.map = [
    [(KC.LEFT), (KC.RIGHT)],  
]

if __name__ == '__main__':
    keyboard.go()
