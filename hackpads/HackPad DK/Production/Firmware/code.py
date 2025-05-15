from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.scanners.encoder import RotaryioEncoder
from kmk.keys import KC

keyboard = KMKKeyboard()

# Key Scanner Setup (including encoder button)
keyboard.matrix = KeysScanner(
    pins=[board.D10, board.D9, board.D8, board.D7, board.D0],  # Encoder button on D0
    value_when_pressed=False,  # Active low (pressed when pin reads LOW)
    pull=True,                 # Enables internal pull-up resistors
    interval=0.02,             # 20ms debounce time in seconds
    max_events=64              # Maximum number of events to store in buffer
)

# Rotary Encoder Setup with RotaryioEncoder (D5=A, D6=B)
encoder = RotaryioEncoder(
    pin_a=board.D5,  # Encoder pin A
    pin_b=board.D6,  # Encoder pin B
    divisor=4        # Divisor (optional, fine-tunes rotation sensitivity)
)

# Add RotaryioEncoder to the keyboard matrix scanning
keyboard.matrix.add_scanner(encoder)

# Define keymap for both switches and the rotary encoder
keyboard.keymap = [
    [KC.A, KC.B, KC.C, KC.D, KC.ENTER],  # Keys (D10, D9, D8, D7, Encoder button on D0)
]

# Rotary encoder keymap (handled separately)
keyboard.encoder_keymap = [
    (KC.VOLU, KC.VOLD),  # Clockwise: Volume Up, Counterclockwise: Volume Down
]

if __name__ == '__main__':
    keyboard.go()
