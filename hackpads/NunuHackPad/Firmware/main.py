
print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.rgb import RGB
from kmk.extensions.rgb import AnimationModes
from kmk.modules.encouder import EncoderHandler

keyboard = KMKKeyboard()
encoder_handler = EncoderHandler()
keyboard.modules = [layers, holdtap, encoder_handler]

keyboard.col_pins = (board.GP29,board.GP28,board.GP27)
keyboard.row_pins = (board.GP4,board.GP2,board.GP1)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

#neopixels

rgb = RGB(pixel_pin=board.GP26,
        num_pixels=4, 
        rgb_order=(1,0,2,3),
        breathe_center=1,
        )
keyboard.extensions.append(rgb)


#encoder stuff
encoder_handler.pins = (
        (board.GP7, board.GP6, board.GP0,),
)

encoder_handler.map = [ ((KC_VOLD, KC_VOLU, KC_MEDIA_PLAY_PAUSE),)]


#keyboard

keyboard.keymap = [
        [KC_NO],[KC_UNDO],[KC_COPY],
        [KC_WWW_HOME],   [KC_KB_MUTE],   [KC_PASTE],
        [KC_BRIGHTNESS_DOWN],   [KC_BRIGHTNESS_UP], [KC_WWW_REFRESH]
]



if __name__ == '__main__':
    keyboard.go()
