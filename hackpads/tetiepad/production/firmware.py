import kmk
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.extensions.rgb import RGB
from kmk.modules.encoder import EncoderHandler

# custom keycodes per layer
layer0 = kmk.Layer(
    [
        KC.KEY_1,
        KC.KEY_2,
        KC.KEY_3,
        KC.KEY_4,
        KC.KEY_5,
        KC.KEY_6,
    ]
)
layer1 = kmk.Layer(
    [
        KC.KEY_Q,
        KC.KEY_W,
        KC.KEY_E,
        KC.KEY_R,
        KC.KEY_T,
        KC.KEY_Y,
    ]
)
layer2 = kmk.Layer(
    [
        KC.KEY_U,
        KC.KEY_I,
        KC.KEY_O,
        KC.KEY_P,
        KC.LBRC,
        KC.RBRC,
    ]
)

keymap = kmk.Keymap(layers=[layer0, layer1, layer2])

# pins: 0-5: keys, 6: SK6812 LED, 7-9: EC11 encoder
pins = (
    # CMX keys
    kmk.Pin(kmk.Row("D0"), kmk.Column("D0")),
    kmk.Pin(kmk.Row("D1"), kmk.Column("D1")),
    kmk.Pin(kmk.Row("D2"), kmk.Column("D2")),
    kmk.Pin(kmk.Row("D3"), kmk.Column("D3")),
    kmk.Pin(kmk.Row("D4"), kmk.Column("D4")),
    kmk.Pin(kmk.Row("D5"), kmk.Column("D5")),
    # SK6812
    kmk.Pin(kmk.Row("D10"), kmk.Column("D10")),
    # EC11 encoder
    kmk.Pin(kmk.Row("D6"), kmk.Column("D6")),  # A (rotary)
    kmk.Pin(kmk.Row("D7"), kmk.Column("D7")),  # B (rotary)
    kmk.Pin(kmk.Row("D8"), kmk.Column("D8")),  # D (push)
)

keyboard = kmk.Keyboard(keymap, pins)

# init layers
layers = Layers()
keyboard.modules.append(layers)

# leds
keyboard.rgb_pixel_pin = pins[6].pin  # use SK6812 pin
keyboard.rgb_num_pixel = 1  # 1 pixel
rgb = RGB(pixel_pin=keyboard.rgb_pixel_pin, num_pixels=keyboard.rgb_num_pixel)
keyboard.extensions.append(rgb)

# callback for encoder push
def on_encoder_push():
    current_layer = keyboard.modules.layers.active_layer
    next_layer = (current_layer + 1) % 3
    keyboard.modules.layers.activate_layer(next_layer)
    # update led colour
    if next_layer == 0:
        rgb.set_color((255, 0, 0))
    elif next_layer == 1:
        rgb.set_color((0, 255, 0))
    elif next_layer == 2:
        rgb.set_color((0, 0, 255))


# set up encoder handler
encoder_handler = EncoderHandler()
encoder_handler.pins = (
    (pins[7], pins[8], pins[9], False),
)  # encoder_A, encoder_B, push, invert
encoder_handler.on_push_do = lambda: on_encoder_push()  # callback for push
keyboard.extensions.append(encoder_handler)

if __name__ == "__main__":
    keyboard.go()
