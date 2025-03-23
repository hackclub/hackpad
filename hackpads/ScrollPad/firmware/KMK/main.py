import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.holdtap import HoldTap
from kmk.extensions.rgb import RGB
from kmk.modules.mouse_keys import MouseKeys

keyboard = KMKKeyboard()
holdtap = HoldTap()

# pins
RGB_PIN = board.GPIO6
# Up>Right>Down>Left>Middle
PINS = [board.GPIO1, board.GPIO2, board.GPIO3, board.GPIO4, board.GPIO7]

class LayerRGB(RGB):
    def on_layer_change(self, layer):
        if layer == 0:
            self.set_hsv_fill(185, 100, self.val_default)
        elif layer == 1:
            self.set_hsv_fill(325, 100, self.val_default)
        self.show()

rgb = LayerRGB(
    pixel_pin=RGB_PIN,
    num_pixels=4,
    rgb_order=(0, 1, 2),
    hue_default=0,
    sat_default=0,
    val_default=100,
)

class RGBLayers(Layers):
    def activate_layer(self, keyboard, layer, idx=None):
        super().activate_layer(keyboard, layer, idx)
        rgb.on_layer_change(layer)

    def deactivate_layer(self, keyboard, layer):
        super().deactivate_layer(keyboard, layer)
        rgb.on_layer_change(keyboard.active_layers[0])

# add modules and extensions
keyboard.modules.append(RGBLayers())
keyboard.modules.append(holdtap)
keyboard.modules.append(MouseKeys())
keyboard.extensions.append(rgb)

# no key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

middle_key = KC.LT(1, KC.ENTER)

# 2-layers
# arrow keys, middle key can active the second layer if held
# up/down and sound controls
keyboard.keymap = [
    [MS_WHLU,    MS_WHLR, MS_WHLD,   MS_WHLL, middle_key],
    [KC.VOLU,    KC.MNXT,  KC.VOLD,   KC.MPRV, KC.TRNS]
]

if __name__ == '__main__':
    keyboard.go()