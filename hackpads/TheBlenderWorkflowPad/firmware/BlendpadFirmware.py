from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()

encoder_handler = EncoderHandler()

keyboard.modules = [encoder_handler]

keyboard.row_pins = (11, 5, 8)  
keyboard.col_pins = (0, 1, 2)  

keyboard.diode_orientation = keyboard.DIODE_COL2ROW

keyboard.keymap = [
    [
                  KC.A, KC.B, KC.C, 
        KC.pause, KC.D, KC.E, KC.F   
    ]
]

encoder_handler.pins = ((7, 9))  

encoder_handler.map = [((KC.MS_WH_UP, KC.MS_WH_DOWN),)] 

if __name__ == '__main__':
    keyboard.go()
