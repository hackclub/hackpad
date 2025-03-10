import board
import digitalio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()
encoder_handler = EncoderHandler()
encoder_handler.pins = ((board.GP0, board.GP29, board.GP3),)
encoder_handler.map = [((KC.AUDIO_VOL_DOWN, KC.VOL_UP), KC.AUDIO_MUTE)]
encoder_handler.acceleration_interval = 100
keyboard.modules = [MediaKeys(), encoder_handler]

keyboard.keymap = [
    [
        KC.MEDIA_PREVIOUS_TRACK,
        KC.MEDIA_PLAY_PAUSE,
        KC.MEDIA_NEXT_TRACK
    ]
]

keyboard.gpio_pins = [board.GP4, board.GP2, board.GP1]

for pin in keyboard.gpio_pins:
    btn = digitalio.DigitalInOut(pin)
    btn.direction = digitalio.Direction.INPUT
    btn.pull = digitalio.Pull.UP

if __name__ == '__main__':
    keyboard.go()