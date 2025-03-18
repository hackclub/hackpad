import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.modules.macros import Press, Release, Tap
from kmk.modules.tapdance import TapDance
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.mouse_keys import MouseKeys

keyboard = KMKKeyboard()
encoder = EncoderHandler()
tapdance = TapDance()
media = MediaKeys()
mouse = MouseKeys()
keyboard.modules = [layers, encoder, tapdance, media, mouse]

encoder.pins = (
  (board.D8, board.D7) 
)

scrollvar = 0

encoder.map = [
  ( (KC.AUDIO_VOL_DOWN, KC.AUDIO_VOL_UP) ),
  ( (KC.AUDIO_VOL_DOWN, KC.AUDIO_VOL_UP) ),
  ( (KC.AUDIO_VOL_DOWN, KC.AUDIO_VOL_UP) ),
  ( (KC.MW_DOWN, KC.MW_DOWN) )
  ( (seScroll(scrollvar, -1), scrollvar(scrollvar, 1)) )
]

keyboard.col_pins = (board.D6, board.D10, board.D9)
keyboard.row_pins = (board.D0, board.D1, board.D2, board.D3)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

___ = KC.TRNS
x = KC.NO

def seScroll(store, inc):
  if store < 9 and inc > 0: 
    store += 1
  elif store > 0 and inc < 0:
    store -= 1
  elif inc == -1 and store == 1:
    store = 9
  return KC.MACRO(
    Press(KC.LCTL),
    f"{store}",
    Release(KC.LCTL)
  )

quicksearch = KC.MACRO(
  Press(KC.LCTL),
  Tap(KC.C),
  Tap(KC.T),
  Tap(KC.V),
  Release(KC.LCTL),
  Tap(KC.ENT)
)

windowswitch = KC.TD(
  KC.LALT(KC.TAB),
  KC.MACRO(
    Press(KC.LALT),
    Tap(KC.TAB),
    TAP(KC.TAB),
    Release(KC.TAB)
  ),
  KC.MACRO(
    Press(KC.LALT),
    Tap(KC.TAB),
    Tap(KC.TAB),
    Tap(KC.TAB),
    Release(KC.TAB)
  )
)

lbrack = KC.TD(
  KC.LPRN,
  KC.LCBR,
  KC.LBRC
)

rbrack = KC.TD(
  KC.RPRN,
  KC.RCBR,
  KC.RBRC
)

discord = KC.MACRO(
  Tap(KC.RGUI),
  KC.MACRO("discord"),
  Tap(KC.ENT)
)

litexl = KC.MACRO(
  Tap(KC.RGUI),
  KC.MACRO("litexl"),
  Tap(KC.ENT)
)

firefox = KC.MACRO(
  Tap(KC.RGUI),
  KC.MACRO("firefox"),
  Tap(KC.ENT)
)

steam = KC.MACRO(
  Tap(KC.RGUI),
  KC.MACRO("steam"),
  Tap(KC.ENT)
)

keyboard.keymap = [

  # base
  [
    KC.TO(1), KC.TO(2), KC.TO(3),
    discord,  litexl,   firefox,
    steam,    x,        x,
    x,        x,        x
  ]

  # standard use
  [
    KC.LCTL(KC.LSFT(KC.TAB)), KC.LCTL(KC.TAB),           KC.LGUI(KC.LCTL(KC.UP)),
    KC.AUDIO_VOL_UP,          quicksearch,               KC.LGUI(KC.LCTL(KC.DOWN)),
    KC.AUDIO_VOL_DOWN,        KC.RCTL(KC.RSFT(KC.LEFT)), KC.RCTL(KC.RSFT(KC.LEFT)),
    KC.MEDIA_PLAY_PAUSE,      windowswitch,              KC.TO(0)
  ],
  
  # programming and strings
  [
    KC.LCTL(KC.C), KC.LCTL(KC.BSPACE), KC.DEL,
    KC.LCTL(KC.V), KC.LCTL(KC.S),      x,
    KC.LCTL(KC.X), lbrack,             rbrack,
    ___,           x,                  ___
  ],
  
  # games
  [
    KC.E,    KC.W,     KC.Q,
    KC.A,    KC.S,     KC.D,
    KC.LSFT, KC.C,     KC.X
    KC.LCTL, KC.TO(4), ___
  ],

  # games2
  [
    KC.MW_LT, KC.UP,    KC.MW_RT,
    KC.LEFT,  KC.DOWN,  KC.RIGHT,
    ___,      ___,      ___,
    ___,      KC.TO(3), ___
  ]
]

if __name__ == '__main__':
  keyboard.go()
