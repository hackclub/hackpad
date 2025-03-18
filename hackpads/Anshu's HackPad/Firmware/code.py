#THIS CODE IS NOT FINAL WILL BE CHANGES IN ACCORDANCE TO THE ACTUAL BOARD

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.extensions.rgb import RGB
from kmk.modules.rotary_encoder import RotaryEncoderHandler
import board
import time

keyboard = KMKKeyboard()

rgb = RGB(
    pixel_pin=board.D6,   
    num_pixels=8,         
    val_limit=50          
)

encoder_handler = RotaryEncoderHandler()

keyboard.extensions.append(rgb)
keyboard.modules.append(encoder_handler)

keyboard.row_pins = (board.D5, board.D4, board.D3)  
keyboard.col_pins = (board.D10, board.D9, board.D8)  
keyboard.diode_orientation = keyboard.DIODE_COL2ROW

keyboard.keymap = [
    [KC.N1, KC.N2, KC.N3],
    [KC.N4, KC.N5, KC.N6],
    [KC.N7, KC.N8, KC.N9]
]

encoder_handler.pins = ((board.D2, board.D1, board.D0),)  
encoder_handler.map = [
    (KC.VOLU, KC.VOLD)
]
encoder_handler.button_map = [KC.MUTE]  

if __name__ == '__main__':
    brightness = 0
    increment = 5
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255)]
    color_index = 0
    color_change_interval = 100  
    cycle_count = 0

    while True:
        keyboard.process() 

        r, g, b = colors[color_index]
        rgb.set_rgb(int(r * brightness / 50), int(g * brightness / 50), int(b * brightness / 50))
        brightness += increment

        if brightness >= 50 or brightness <= 0:
            increment = -increment 

        cycle_count += 1
        if cycle_count >= color_change_interval:
            color_index = (color_index + 1) % len(colors)
            cycle_count = 0

        time.sleep(0.05)

    keyboard.go()
