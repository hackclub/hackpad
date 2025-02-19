from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.rgb import RGB

keyboard = KMKKeyboard()
layers = Layers()
rgb = RGB(pixel_pin=keyboard.rgb_pixel_pin, num_pixels=keyboard.rgb_num_pixels)

keyboard.modules.append(layers)
keyboard.extensions.append(MediaKeys())
keyboard.extensions.append(rgb)

# Define layers (basic example)
keyboard.keymap = [
    [
        KC.ESC, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, KC.PSCR, KC.SLCK, KC.PAUS, KC.INS, KC.HOME, KC.PGUP, 
        KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC, KC.BSPC, KC.DEL, KC.END, KC.PGDN,
        KC.CAPS, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT, KC.ENT,
        KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.RSFT, KC.UP,
        KC.LCTL, KC.LGUI, KC.LALT, KC.SPC, KC.RALT, KC.RGUI, KC.APP, KC.RCTL, KC.LEFT, KC.DOWN, KC.RIGHT,
        KC.NO  # 88th key to control NeoPixels
    ]
]

def toggle_neopixels(keyboard):
    rgb.enabled = not rgb.enabled
    rgb.update()

keyboard.keymap[0][-1] = KC.MO(1)  # Assign last key to switch layer
keyboard.keymap.append([KC.NO] * 87 + [KC.FUNCTION(toggle_neopixels)])

if __name__ == '__main__':
    keyboard.go()
