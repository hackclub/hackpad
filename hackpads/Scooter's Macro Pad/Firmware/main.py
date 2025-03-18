<<<<<<< Updated upstream
print("Scooter's Macro Pad Starting ...")

import board
import busio
import displayio

from kb import ScooterMP
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys

from ScooterMP.ScooterMP_module import ScooterMPModule

# macropad settings
ScooterMP_rgb = True
ScooterMP_oled = True
ScooterMP_modules = False # If your using external expansions with the pogo pins, set this to True
layers_names = ['Layer 1', 'Layer 2', 'Layer 3']

displayio.release_displays()
i2c = busio.I2C(scl=board.SCL, sda=board.SDA, frequency=400000)

layers = Layers()
encoder_handler = EncoderHandler()

# config the main the macropad and pass the external modules
keyboard = ScooterMPMK2(i2c, layers_names, ScooterMP_rgb, ScooterMP_oled, ScooterMP_modules)
keyboard.modules = [layers, encoder_handler]

# this is the encoder on the macropad.
encoder_handler.pins = ((board.D9, board.D10, board.D8,),)

keyboard.extensions.append(MediaKeys())

# ---------------- Main macropad maps ---------------- 
keyboard.keymap = [
    [
        KC.NO,     KC.NO,      KC.NO,      KC.NO,
        KC.NO,     KC.NO,      KC.NO,      KC.NO,
        KC.NO,     KC.NO,      KC.NO,      KC.NO,
    ]   # Layer 1
]

encoder_handler.map = [ 
    (( KC.NO,     KC.NO,      KC.NO),), # Layer 1
    (( KC.NO,     KC.NO,      KC.NO),), # Layer 2
    (( KC.NO,     KC.NO,      KC.NO),), # Layer 3
    ]
# ----------------

if __name__ == '__main__':
=======
print("Scooter's Macro Pad Starting ...")

import board
import busio
import displayio

from kb import ScooterMP
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys

from ScooterMP.ScooterMP_module import ScooterMPModule

# macropad settings
ScooterMP_rgb = True
ScooterMP_oled = True
ScooterMP_modules = False # If your using external expansions with the pogo pins, set this to True
layers_names = ['Layer 1', 'Layer 2', 'Layer 3']

displayio.release_displays()
i2c = busio.I2C(scl=board.SCL, sda=board.SDA, frequency=400000)

layers = Layers()
encoder_handler = EncoderHandler()

# config the main the macropad and pass the external modules
keyboard = ScooterMPMK2(i2c, layers_names, ScooterMP_rgb, ScooterMP_oled, ScooterMP_modules)
keyboard.modules = [layers, encoder_handler]

# this is the encoder on the macropad.
encoder_handler.pins = ((board.D9, board.D10, board.D8,),)

keyboard.extensions.append(MediaKeys())

# ---------------- Main macropad maps ---------------- 
keyboard.keymap = [
    [
        KC.NO,     KC.NO,      KC.NO,      KC.NO,
        KC.NO,     KC.NO,      KC.NO,      KC.NO,
        KC.NO,     KC.NO,      KC.NO,      KC.NO,
    ]   # Layer 1
]

encoder_handler.map = [ 
    (( KC.NO,     KC.NO,      KC.NO),), # Layer 1
    (( KC.NO,     KC.NO,      KC.NO),), # Layer 2
    (( KC.NO,     KC.NO,      KC.NO),), # Layer 3
    ]
# ----------------

if __name__ == '__main__':
>>>>>>> Stashed changes
    keyboard.go()