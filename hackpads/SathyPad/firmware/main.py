import board
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.RGB import RGB, AnimationModes
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.oled import OLED, OLED_12Bx64
from adafruit_pcf8574 import PCF8574
from kmk.handlers.consumer_control import send_consumer

i2c = busio.I2C(board.SCL, board.SDA)
pcf = PCF8574(i2c, address=0x38)


COL0 = board.D10
COL1 = board.D9
COL2 = board.D8
COL3 = board.D7
ROW0 = board.D0
ROW1 = board.D1
ROW2 = board.D2
ROW3 = board.D3
OLED_1 = board.D4
OLED_2 = board.D5
NEOPIXEL = board.D6

oled = OLED_12Bx64(oled_pin_sda=OLED_1, oled_pin_scl=OLED_2)
layer_names = ["Layer 1", "Layer 2", "Layer 3", "Layer 4"]


keyboard = KMKKeyboard()
keyboard.col_pins = (COL0, COL1, COL2, COL3)
keyboard.row_pins = (ROW0, ROW1, ROW2, ROW3)

def update_oled_display(oled, layer):
    layer_name = layer_names[layer]
    oled.oled.fill(0)
    oled.oled.text(layer_name, 0, 0, 1)
    oled.oled.show()

rgb_ext = RGB(
    pixel_pin=NEOPIXEL,
    num_pixels=9,
    hue_default=30,  
    sat_default=255,
    val_default=255,  
    val_limit=255,    
    animation_speed=0,
    animation_mode=AnimationModes.rainbow,  
    refresh_rate=30,
)

keyboard.extensions.append(rgb_ext)
keyboard.extensions.append(MediaKeys())


encoder_handler = EncoderHandler()
encoder_handler.pins = [
    (pcf.get_pin(0), pcf.get_pin(1)),  
    (pcf.get_pin(2), pcf.get_pin(3)),  
    (pcf.get_pin(4), pcf.get_pin(5)),  
    (pcf.get_pin(6), pcf.get_pin(7)),  
]
encoder.rotate_callbacks = [
    lambda direction: send_consumer(KC.VOLU if direction == 1 else KC.VOLD), 
    lambda direction: send_consumer(KC.MNXT if direction == 1 else KC.MPRV), 
    lambda direction: send_consumer(KC.MPLY),                                
    lambda direction: print("Encoder 4 turned", direction),                  
]
keyboard.modules.append(encoder_handler)



keyboard.keymap = [
    [
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
    ]
]


def layer_switch_handler(keyboard, row, col, pressed):
    if row == 0 and col == 0 and pressed:
        current_layer = (keyboard.active_layers[0] + 1) % 4
        keyboard.active_layers = [current_layer]
        update_oled_display(oled, current_layer)

if __name__ == '__main__':
    keyboard.go()
