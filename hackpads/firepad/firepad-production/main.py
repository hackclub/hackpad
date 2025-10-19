import board  # pyright: ignore[reportMissingImports]
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC, Key
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.rgb import RGB
from kmk.utils import Debug

debug = Debug(__name__)
debug.enabled = True

keyboard = KMKKeyboard()


class PrevKey(Key):
    def __init__(self):
        pass

    def on_press(self, keyboard, coord_int=None):
        keyboard.add_key(  # pyright: ignore[reportAttributeAccessIssue]
            KC.MEDIA_PREV_TRACK
        )
        keyboard.add_key(KC.MEDIA_REWIND)  # pyright: ignore[reportAttributeAccessIssue]

    def on_release(self, keyboard, coord_int=None):
        keyboard.remove_key(  # pyright: ignore[reportAttributeAccessIssue]
            KC.MEDIA_PREV_TRACK
        )
        keyboard.remove_key(  # pyright: ignore[reportAttributeAccessIssue]
            KC.MEDIA_REWIND
        )


class NextKey(Key):
    def __init__(self):
        pass

    def on_press(self, keyboard, coord_int=None):
        keyboard.add_key(  # pyright: ignore[reportAttributeAccessIssue]
            KC.MEDIA_NEXT_TRACK
        )
        keyboard.add_key(  # pyright: ignore[reportAttributeAccessIssue]
            KC.MEDIA_FAST_FORWARD
        )

    def on_release(self, keyboard, coord_int=None):
        keyboard.remove_key(  # pyright: ignore[reportAttributeAccessIssue]
            KC.MEDIA_NEXT_TRACK
        )
        keyboard.remove_key(  # pyright: ignore[reportAttributeAccessIssue]
            KC.MEDIA_FAST_FORWARD
        )


class MuteKey(Key):
    def __init__(self):
        self.LED_ON = False

    def on_press(self, keyboard, coord_int=None):
        keyboard.add_key(KC.AUDIO_MUTE)  # pyright: ignore[reportAttributeAccessIssue]

    def on_release(self, keyboard, coord_int=None):
        keyboard.remove_key(  # pyright: ignore[reportAttributeAccessIssue]
            KC.AUDIO_MUTE
        )
        if self.LED_ON:
            self.LED_ON = False
            rgb.set_rgb((0, 0, 0), 1)
        else:
            self.LED_ON = True
            rgb.set_rgb((255, 0, 0), 1)


CUR_COLOR = [0, 255, 255]


def checkColor():
    global CUR_COLOR
    for i in range(3):
        if CUR_COLOR[i] > 255:
            CUR_COLOR[i] = CUR_COLOR[i] - 255


def changeColor():
    global CUR_COLOR
    checkColor()
    if CUR_COLOR[2] >= 255:
        if CUR_COLOR[1] >= 255:
            if CUR_COLOR[0] >= 255:
                CUR_COLOR = [0, 0, 0]
            else:
                CUR_COLOR = [CUR_COLOR[0] + 1, 0, 0]
        else:
            CUR_COLOR[1] = CUR_COLOR[1] + 1
            CUR_COLOR[2] = 0
    else:
        CUR_COLOR[2] = CUR_COLOR[2] + 1


def unpackColor() -> tuple[int, int, int]:
    global CUR_COLOR
    return (CUR_COLOR[0], CUR_COLOR[1], CUR_COLOR[2])


class ColorKey(Key):
    def __init__(self, keycode):
        global CUR_COLOR
        self.keycode = keycode

    def on_press(self, keyboard, coord_int=None) -> None:
        global CUR_COLOR
        keyboard.add_key(self.keycode)  # pyright: ignore[reportAttributeAccessIssue]
        changeColor()
        checkColor()
        rgb.set_rgb(unpackColor(), 0)

    def on_release(self, keyboard, coord_int=None) -> None:
        keyboard.remove_key(self.keycode)  # pyright: ignore[reportAttributeAccessIssue]


ENCPINS = (board.GP28, board.GP29, board.GP3)
PIXPIN = board.GP27
KEYPINS = [
    board.GP4,
    board.GP2,
    board.GP1,
    board.GPB0,
    board.GPB1,
    board.GPB2,
    board.GPB3,
    board.GPB4,
    board.GPB5,
    board.GPB6,
    board.GPB7,
    board.GPA0,
    board.GPA1,
    board.GPA2,
    board.GPA3,
]
# Keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# Custom Keys: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keys.md
KEYMAP = [
    KC.MEDIA_PLAY_PAUSE,
    PrevKey,
    NextKey,
    KC.F13,
    KC.F14,
    KC.F15,
    KC.F16,
    KC.F17,
    KC.F18,
    KC.F19,
    KC.F20,
    KC.F21,
    KC.F22,
    KC.F23,
    KC.F24,
]
ENCMAP = ((KC.AUDIO_VOL_UP, KC.AUDIO_VOL_DOWN, MuteKey),)

rgb = RGB(pixel_pin=PIXPIN, num_pixels=2)
encoder_handler = EncoderHandler()
keyboard.extensions.append(MediaKeys())
keyboard.extensions.append(rgb)
keyboard.modules.append(encoder_handler)

keyboard.matrix = KeysScanner(  # pyright: ignore[reportAttributeAccessIssue]
    pins=KEYPINS,
    value_when_pressed=False,
)
encoder_handler.pins = (ENCPINS,)  # pyright: ignore[reportAttributeAccessIssue]

keyboard.keymap = [
    KEYMAP,
]
encoder_handler.map = [  # pyright: ignore[reportAttributeAccessIssue]
    ENCMAP,
]

if __name__ == "__main__":
    keyboard.go()
