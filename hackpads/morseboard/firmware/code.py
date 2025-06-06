import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import adafruit_matrixkeypad
import supervisor

# rotary encoder (A = GP3, B = GP4)
encoder_pin_a = digitalio.DigitalInOut(board.GP3)
encoder_pin_a.direction = digitalio.Direction.INPUT
encoder_pin_a.pull = digitalio.Pull.UP

encoder_pin_b = digitalio.DigitalInOut(board.GP4)
encoder_pin_b.direction = digitalio.Direction.INPUT
encoder_pin_b.pull = digitalio.Pull.UP

last_encoder_state = (encoder_pin_a.value, encoder_pin_b.value)


rows = [digitalio.DigitalInOut(board.GP1), digitalio.DigitalInOut(board.GP2)]
cols = [digitalio.DigitalInOut(board.GP27), digitalio.DigitalInOut(board.GP28), digitalio.DigitalInOut(board.GP29)]
keymap = [
    [Keycode.A, Keycode.B, Keycode.C],
    [Keycode.D, Keycode.E, Keycode.F]
]
keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keymap, value_when_pressed=False)

kbd = Keyboard(usb_hid.devices)

# positions [0][0] -> [1][0] used for morse code
SYMBOL_KEYS = [Keycode.A, Keycode.B, Keycode.C, Keycode.D]
key_indices = {k: i for i, k in enumerate(SYMBOL_KEYS)}
DOT_THRESHOLD = 0.3

# morse code to keycode
MORSE_MAP = {
    ".-": Keycode.A,
    "-...": Keycode.B,
    "-.-.": Keycode.C,
    "-..": Keycode.D,
    ".": Keycode.E,
    "..-.": Keycode.F,
    "--.": Keycode.G,
    "....": Keycode.H,
    "..": Keycode.I,
    ".---": Keycode.J,
    "-.-": Keycode.K,
    ".-..": Keycode.L,
    "--": Keycode.M,
    "-.": Keycode.N,
    "---": Keycode.O,
    ".--.": Keycode.P,
    "--.-": Keycode.Q,
    ".-.": Keycode.R,
    "...": Keycode.S,
    "-": Keycode.T,
    "..-": Keycode.U,
    "...-": Keycode.V,
    ".--": Keycode.W,
    "-..-": Keycode.X,
    "-.--": Keycode.Y,
    "--..": Keycode.Z
}

press_times = {}
pressed_last = set()
symbol_sequence = []

def decode_and_send():
    if not symbol_sequence:
        return
    code = "".join(symbol_sequence)
    print(f"Sequence complete: {code}")
    if code in MORSE_MAP:
        kbd.send(MORSE_MAP[code])
        print(f"Sent: {MORSE_MAP[code]}")
    else:
        print("Unknown Morse:", code)

# polling is great
while True:
    now = time.monotonic()
    currently_pressed = set(keypad.pressed_keys)

    # track press start times
    for key in currently_pressed - pressed_last:
        if key in SYMBOL_KEYS:
            press_times[key] = now

    # track releases
    for key in pressed_last - currently_pressed:
        if key in press_times and key in SYMBOL_KEYS:
            held_time = now - press_times[key]
            symbol = "." if held_time < DOT_THRESHOLD else "-"
            index = key_indices[key]
            # Ensure in-order input (ignore future keys if previous not pressed)
            if index == len(symbol_sequence):
                symbol_sequence.append(symbol)
                print(f"Registered symbol at pos {index}: {symbol}")
            else:
                print(f"Ignored out-of-order key at pos {index}")
            del press_times[key]
        elif key not in SYMBOL_KEYS:
            kbd.send(key)

    if not currently_pressed and symbol_sequence:
        decode_and_send()
        symbol_sequence = []

    pressed_last = currently_pressed

    current_state = (encoder_pin_a.value, encoder_pin_b.value)

    if current_state != last_encoder_state:
        if last_encoder_state == (1, 1):
            if current_state == (0, 1):
                kbd.send(Keycode.VOLUME_INCREMENT)
                print("Volume up")
            elif current_state == (1, 0):
                kbd.send(Keycode.VOLUME_DECREMENT)
                print("Volume down")

        last_encoder_state = current_state
    time.sleep(0.01)
