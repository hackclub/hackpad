from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.digital import MatrixScanner
from kmk.modules.encoder import EncoderHandler
from kmk.modules.rgb import RGB
from kmk.keys import KC
from kmk.handlers.stock import led_toggle

keyboard = KMKKeyboard()

# because I wired them in a matrix
keyboard.matrix = MatrixScanner(columns=[8, 9, 10], rows=[7, 6, 5])

encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
encoder_handler.pins = ((2, 3, 1),)  # (A, B, switch on schematic on kiCad)
encoder_handler.map = [
    ((KC.VOLD, KC.VOLU),),  # I may change what this does in the future
]

rgb = RGB(pixel_pin=4, num_pixels=9)
rgb.enabled = True
rgb.brightness = 128  # out of 255 but I'd rather not blind myself or blow up the LEDs
keyboard.modules.append(rgb)

keyboard.keymap = [
    [KC.Q, KC.W, KC.E],
    [KC.A, KC.S, KC.D],
    [KC.Z, KC.X, KC.C],
]

keyboard.keymap[1][1] = KC.LCTRL(
    led_toggle(rgb)
)  # when I press ctrl, the LEDs will toggle

if __name__ == "__main__":
    keyboard.go()
