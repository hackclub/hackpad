print("Starting")

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.rotary_encoder import RotaryEncoder
from kmk.extensions.display import Display, DisplayText
from digitalio import DigitalInOut, Direction, Pull

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP0, board.GP1, board.GP2)
keyboard.row_pins = (board.GP3, board.GP6, board.GP7)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.N7, KC.N8, KC.N9],
    [KC.N4, KC.N5, KC.N6],
    [KC.N1, KC.N2, KC.N3],
]

encoder = RotaryEncoder(pin_a=board.GP9, pin_b=board.GP10, divisor=4)

encoder_button = DigitalInOut(board.GP8)
encoder_button.direction = Direction.INPUT
encoder_button.pull = Pull.UP

display = Display(
    font=terminalio.FONT,
    text="Scottpad V1",
    timeout=0,
    color=0xFFFFFF,
    auto_center=True,
)

keyboard.extensions.append(display)

@encoder.handler
def volume_control(direction):
    if direction > 0:
        print("Volume Up")
        keyboard.send(KC.VOLU)
    elif direction < 0:
        print("Volume Down")
        keyboard.send(KC.VOLD)

keyboard.extensions.append(encoder)

def check_encoder_button():
    if not encoder_button.value:
        print("Encoder Button Pressed")
        display.set_text("Hello :)")
    else:
        display.set_text("Scottpad V1")

keyboard.before_matrix_scan = check_encoder_button

if __name__ == '__main__':
    keyboard.go()