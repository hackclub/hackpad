import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.layers import Layers
from kmk.modules.dual_role import DualRoleLayerTap # for middle_key layer switching

keyboard = KMKKeyboard()

# Macro and layers
macros = Macros()
keyboard.modules.append(macros)
keyboard.modules.append(Layers())

# pins(Up>Right>Down>Left>Middle)
PINS = [board.GPIO4, board.GPIO2, board.GPIO1, board.GPIO3, board.GPIO26]

# no key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

middle_key = DualRoleLayerTap(1, KC.ENTER)

# 2-layers
# arrow keys, middle key can active the second layer if held
# up/down and sound controls
keyboard.keymap = [
    [KC.LEFT,    KC.RIGHT, KC.UP,   KC.DOWN, middle_key],
    [KC.VOLD,    KC.VOLU,  KC.UP,   KC.DOWN, KC.TRNS]
]

# start
if __name__ == '__main__':
    keyboard.go()

# TODO: LED layer indication
# TODO: Potentially port to QMK for mouse scrolling instead of arrow keys
