print("Hexapad, hardware version 0.0.1, firmware version 0.0.1. Visit https://v.gd/hexapad for more info.")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.macros import Macros
from kmk.modules.macros import Press, Release, Tap
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.rgb import RGB
from kmk.extensions.rgb import AnimationModes
import adafruit_pcf8574
import busio
from kmk.extensions.display import Display, TextEntry, ImageEntry

# For SSD1306
from kmk.extensions.display.ssd1306 import SSD1306

# Replace SCL and SDA according to your hardware configuration.
i2c_bus = busio.I2C(board.SCL, board.SDA)

driver = SSD1306(
    # Mandatory:
    i2c=i2c_bus,
    # Optional:
    device_address=0x3C,
)
display = Display(
    # Mandatory:
    display=driver,
    # Optional:
    width=128, # screen size
    height=32, # screen size
    flip = False, # flips your display content
    flip_left = False, # flips your display content on left side split
    flip_right = False, # flips your display content on right side split
    brightness=0.6, # initial screen brightness level
    brightness_step=0.1, # used for brightness increase/decrease keycodes
    dim_time=30, # time in seconds to reduce screen brightness
    dim_target=0.1, # set level for brightness decrease
    off_time=60, # time in seconds to turn off screen
    powersave_dim_time=10, # time in seconds to reduce screen brightness
    powersave_dim_target=0.1, # set level for brightness decrease
    powersave_off_time=30, # time in seconds to turn off screen
)

display.entries = [
    ImageEntry(image="layer-1.bmp", layer=0),
    ImageEntry(image="layer-2.bmp", layer=1),
    ImageEntry(image="layer-3.bmp", layer=2),
    ImageEntry(image="layer-4.bmp", layer=3),
]


i2c = board.I2C()
pcf = adafruit_pcf8574.PCF8574(i2c)


encoder_handler = EncoderHandler()
macros = Macros()


keyboard = KMKKeyboard()
keyboard.extensions.append(MediaKeys())
keyboard.modules.append(macros)
keyboard.modules.append(MouseKeys())
keyboard.modules.append(encoder_handler)
keyboard.extensions.append(display)

keyboard.col_pins = (board.D7,board.D8,board.D9,board.D10)
keyboard.row_pins = (board.D0,board.D1,board.D2,board.D3)
keyboard.diode_orientation = DiodeOrientation.COL2ROW\


rgb = RGB(pixel_pin=pcf.get_pin(5), num_pixels=3, animation_mode=AnimationModes.RAINBOW)
keyboard.extensions.append(rgb)

encoder_handler.pins = encoder_handler.pins = (
    (pcf.get_pin(0), pcf.get_pin(1),pcf.get_pin(2))
)

# Macros
SHRUG = KC.MACRO(" ̄\\_(ツ)_/ ̄")
SUS = KC.MACRO("ಠ_ಠ")

E_SKULL = KC.MACRO("💀")
E_PARTY = KC.MACRO("🎉")
E_THUMBSUP = KC.MACRO("👍")
E_FIRE = KC.MACRO("🔥")
E_CHECK = KC.MACRO("✅")
E_CROSS = KC.MACRO("❌")
E_SOB = KC.MACRO("😭")
E_SMILE = KC.MACRO("😊")

# Hack Club Slack emojis
S_PARROT = KC.MACRO(":ultrafastparrot:")
S_EYES = KC.MACRO(":earthquakyeyes:")

# Quicktype
# Shell commands
NIX_SHELL = KC.MACRO("nix shell nixpkgs#")
GIT_ADD_ALL = KC.MACRO("git add .")
GIT_COMMIT = KC.MACRO("git commit -m \"")
GIT_PUSH = KC.MACRO("git push")

MD_IMAGE = KC.MACRO("![image](https://example.com)")
MD_LINK = KC.MACRO("[Link](https://example.com)")
HAI = KC.MACRO("hai!")
HEY = KC.MACRO("hey!")

LOREM = KC.MACRO("Qui amet sint et nulla illo. Esse nobis architecto vel nemo numquam vitae qui sit. Beatae explicabo sunt velit sed in. Placeat ab vel earum quam non cum ipsum aliquid. Incidunt et nihil qui sed et temporibus tempora est. Magni natus sint dolorem laboriosam voluptas. Laboriosam ullam maxime et eum aut modi unde. Inventore ducimus quisquam hic. Laboriosam aut quasi magnam vero quibusdam. Magni ut quas quod inventore. Amet sit omnis minus maxime.")

SIGMA = KC.MACRO("erm what the sigma")

HTML_A = KC.MACRO("<a href=\"https://example.com\">Link</a>")
HTML_DIV = KC.MACRO("<div class=""></div>")



# KEYMAP

keyboard.keymap = [
    # 0 Default
    [KC.MPLY, KC.VOLD, KC.VOLU, KC.MUTE, # Play/Pause, Volume Down, Volume Up, Mute
     KC.LCTL(KC.C), KC.LCTL(KC.V), KC.LCTL(KC.X), KC.LWIN, # Ctrl+C, Ctrl+V, Ctrl+X, Super
     KC.LCTL(KC.Z), KC.LCTL(KC.Y), KC.PSCR, KC.LALT(KC.TAB), # Ctrl+Z, Ctrl+Y, Print Screen, Alt+Tab
     KC.NO, KC.DF(1), KC.DF(2), KC.DF(3),], # Layers
    # 1 Emoji
    [S_PARROT, S_EYES, E_SKULL, E_PARTY,
     E_THUMBSUP, E_FIRE, E_CHECK, E_CROSS,
     E_SOB, E_SMILE, SHRUG, SUS,
     KC.DF(0), KC.NO, KC.DF(2), KC.DF(3)],
    # 2 Shortcuts
    [KC.LCTL(KC.S), KC.LCTL(KC.LSFT(KC.T)), KC.LCTL(KC.T), KC.LCTL(KC.W), # Save, Restore Tab, New Tab, Close Tab
     KC.LGUI(KC.PGUP), KC.LGUI(KC.PGDN), KC.F11, KC.LALT(KC.F4), # Toggle Maximize, Minimize, Fullscreen, Close Window
     KC.LCTL(KC.LSFT(KC.P)), KC.LCTL(KC.SPACE),KC.LCTL(KC.LSFT(KC.I)) , KC.LGUI(KC.TAB), # VSCode Command Palette, Ctrl + Space, Browser DevTools, Switch Activity
     KC.DF(0), KC.DF(1), KC.NO, KC.DF(3),],
    # 3 Quicktype
    [NIX_SHELL, GIT_ADD_ALL, GIT_COMMIT, GIT_PUSH,
     HTML_A, HTML_DIV, MD_IMAGE, MD_LINK,
     HAI, HEY, LOREM, SIGMA,
     KC.DF(0), KC.DF(1), KC.DF(2),KC.NO,]
]

encoder_handler.map = ((KC.MW_DN,KC.MW_UP,KC.MB_RMB),
                       (KC.BSPC,KC.SPC,KC.ENTER),
                       (KC.MNXT,KC.MPRV,KC.MSTP),
                       (KC.DOT, KC.SPACE, KC.ENTER),)

if __name__ == '__main__':
    
    keyboard.go()