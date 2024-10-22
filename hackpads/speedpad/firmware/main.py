import board
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.modules.capsword import CapsWord
from kmk.modules.macros import Macros, Press, Release, Tap, Delay
from kmk.modules.rapidfire import RapidFire
from kmk.modules.mouse_keys import MouseKeys

from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.display import Display, TextEntry
from kmk.extensions.display.ssd1306 import SSD1306

i2c_bus = busio.I2C(board.SCL, board.SDA)

driver = SSD1306(i2c=i2c_bus, device_address=0x3C)
display = Display(display=driver, width=128, height=32)
display.entries = [
    TextEntry(text="0 1 2 3 4 5", x=0, y=0, x_anchor="L", y_anchor="T"),
    TextEntry(text="0", x=0, y=0, x_anchor="R", y_anchor="T", inverted=True, layer=0),
    TextEntry(text="1", x=12, y=0, x_anchor="R", y_anchor="T", inverted=True, layer=1),
    TextEntry(text="2", x=24, y=0, x_anchor="R", y_anchor="T", inverted=True, layer=2),
    TextEntry(text="3", x=36, y=0, x_anchor="R", y_anchor="T", inverted=True, layer=3),
    TextEntry(text="4", x=48, y=0, x_anchor="R", y_anchor="T", inverted=True, layer=4),
    TextEntry(text="5", x=60, y=0, x_anchor="R", y_anchor="T", inverted=True, layer=5),
    TextEntry(text="Standard", x=64, y=16, x_anchor="M", y_anchor="M", layer=0),
    TextEntry(text="F360", x=64, y=16, x_anchor="M", y_anchor="M", layer=1),
    TextEntry(text="Minecraft", x=64, y=16, x_anchor="M", y_anchor="M", layer=2),
    TextEntry(text="Discord", x=64, y=16, x_anchor="M", y_anchor="M", layer=3),
    TextEntry(text="Space Engineers", x=64, y=16, x_anchor="M", y_anchor="M", layer=4),
    TextEntry(text="No Man's Sky", x=64, y=16, x_anchor="M", y_anchor="M", layer=5),
]

encoder_handler = EncoderHandler()
layers = Layers()
caps_word = CapsWord()
macros = Macros()
rapidfire = RapidFire()
mouse_keys = MouseKeys()

keyboard = KMKKeyboard()

keyboard.col_pins = [board.D3, board.D6, board.D7]
keyboard.row_pins = [board.D2, board.D1, board.D0]
keyboard.diode_orientation = DiodeOrientation.COL2ROW
keyboard.extensions.append(MediaKeys())
keyboard.extensions.append(display)


keyboard.modules = [encoder_handler, layers, caps_word, macros, rapidfire, mouse_keys]


encoder_handler.pins = (
    (board.D10, board.D9, board.D8,),
)

#layers
LYR_STD, LYR_F360, LYR_MC, LYR_DC, LYR_SE, LYR_NMS = 0, 1, 2, 3, 4, 5

TO_STD = KC.TO(LYR_STD)
TO_F360 = KC.TG(LYR_F360)
TO_MC = KC.TG(LYR_MC)
MT_DC = KC.TT(LYR_DC)
TO_SE = KC.TG(LYR_SE)
TO_NMS = KC.TG(LYR_NMS)

xxx = KC.NO
___ = KC.TRNS

# Media Keys
VOL_D = KC.RF(KC.VOLD)
VOL_U = KC.RF(KC.VOLU)

# F360 keys
MOVE = KC.M
CIRCLE = KC.C
EXTRUDE = KC.E
APPEARANCE = KC.A
HOLE = KC.H
SKETCH = KC.MACRO(
    Press(KC.LCTL),
    Press(KC.ALT),
    Tap(KC.S),
    Release(KC.ALT),
    Release(KC.LCTL)
)
F360_ROT_CW = KC.R

# Minecraft Keys
CHUNK_BORDERS = KC.MACRO(
    Press(KC.F3),
    Tap(KC.G),
    Release(KC.F3)
)
RAPID_CLICK = KC.RF(KC.MB_LMB, interval=60, enable_interval_randomization=True, randomization_magnitude=20, toggle=True)
PICK_BLOCK = KC.MB_MMB
INC_RENDR = KC.MACRO(
    Press(KC.F3),
    Tap(KC.F),
    Release(KC.F3)
)
DEC_RENDR = KC.MACRO(
    Press(KC.F3),
    Tap(KC.LSFT(KC.F)),
    Release(KC.F3)
)
RELOAD = KC.MACRO(
    Press(KC.F3),
    Tap(KC.A),
    Release(KC.F3)
)

# Discord Keys
MUTE = KC.LCTL(KC.LSFT(KC.M))
DEAFEN = KC.LCTL(KC.LSFT(KC.D))
ACCEPT_CALL = KC.LCTL(KC.ENTER)
TGL_SNDBRD = KC.LCTL(KC.LSFT(KC.B))
OPEN_SNDBRD = KC.LCTL(KC.LALT(KC.B))

# Space Engineers Keys
HAND = KC.N0
ROT_R = KC.PGDOWN
ROT_L = KC.DEL
ROT_U = KC.HOME
ROT_D = KC.END
ROT_CCW = KC.INS
ROT_CW = KC.PGUP

# No Man's Sky Keys
SWITCH_PWR = KC.PMNS
CHNG_WPN = KC.G
NXT_TRGT = KC.PDOT
NEAR_TRGT = KC.MB_MMB
PREV_TRGT = KC.COMM
ACT_PULSE = KC.MACRO(
    Press(KC.SPACE),
    Delay(6000),
    Release(KC.SPACE)
)


keyboard.keymap = [
    # 0: Standard layer
    [
        VOL_D, KC.MEDIA_PLAY_PAUSE, VOL_U,
        KC.CW, TO_F360, TO_NMS,
        MT_DC, TO_MC, TO_SE,
    ],
    # 1: Fusion 360 layer
    [
        TO_STD, ___, CIRCLE,
        EXTRUDE, APPEARANCE, HOLE,
        ___, SKETCH, MOVE,
    ],
    # 2: Minecraft layer
    [
        TO_STD, ___, xxx,
        PICK_BLOCK, RAPID_CLICK, CHUNK_BORDERS,
        ___, xxx, xxx,
    ],
    # 3: Discord layer
    [
        TO_STD, ___, xxx,
        ACCEPT_CALL, TGL_SNDBRD, OPEN_SNDBRD,
        ___, MUTE, DEAFEN,
    ],
    # 4: Space Engineers layer
    [
        TO_STD, ___, HAND,
        ROT_L, ROT_U, ROT_R,
        ___, ROT_D, xxx,
    ],
    # 5: No Man's Sky layer
    [
        TO_STD, ___, xxx,
        SWITCH_PWR, PREV_TRGT, NXT_TRGT,
        ___, CHNG_WPN, ACT_PULSE,
    ],

]

encoder_handler.map = [
    ((KC.VOLD, KC.VOLU, KC.MEDIA_PLAY_PAUSE),), # Standard
    ((KC.LCTL(KC.LEFT), KC.LCTL(KC.RIGHT), KC.LSFT),), # Fusion 360
    ((DEC_RENDR, INC_RENDR, RELOAD),), # Minecraft
    ((KC.LALT(KC.UP), KC.LALT(KC.DOWN), KC.LCTL),), # Discord
    ((ROT_CCW, ROT_CW, KC.MB_LMB),), # Space Engineers
    ((KC.Q, KC.E, KC.MB_RMB),), # No Man's Sky
]

if __name__ == '__main__':
    keyboard.go()