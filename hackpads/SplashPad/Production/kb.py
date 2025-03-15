import board
from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import MatrixScanner, DiodeOrientation
from kmk.scanners.digital import RotaryEncoder

class KMKKeyboard(_KMKKeyboard):
    def __init__(self):
        super().__init__()

        # Define row and column GPIO pins
        self.col_pins = (board.GP3, board.GP4, board.GP2)
        self.row_pins = (board.GP6, board.GP7, board.GP0)

        # Diode orientation
        self.diode_orientation = DiodeOrientation.COL2ROW  

        # Define rotary encoder
        self.rotary_encoder = RotaryEncoder(
            pin_a=board.GP26,  # A pin
            pin_b=board.GP27,  # B pin
            divisor=4,
        )

        # Define encoder button pin
        self.encoder_button_pin = board.GP28

        # LED Configuration
        self.num_leds = 14  # SK6812 MINI LEDs
        self.leds = neopixel.NeoPixel(board.GP1, self.num_leds, brightness=0.5, auto_write=False, pixel_order=neopixel.GRBW)

        # LED (x, y) positions
        self.led_positions = [
            (11, 0.5),
            (2, 27.5), (2, 46.5), (2, 65.5),
            (20.475, 27.5), (220.475, 46.5), (20.475, 65.5),
            (39.525, 27.5), (39.525, 46.5), (39.525, 65.5),
            (58, 27.5), (58, 46.5), (58, 65.5),
            (49.25, 0.5)
        ]