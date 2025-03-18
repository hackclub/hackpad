from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.key_matrix import KeyMatrix
from kmk.extensions.ioexpander import MCP23017
import board
import busio
from kmk.extensions.display import Display, TextEntry, ImageEntry
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.scanners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.keys import KC
from kmk.modules.mouse_keys import MouseKeys

# Create the KMKKeyboard object
keyboard = KMKKeyboard()
keyboard.modules.append(Layers())
# Initialize MCP23017 connected over I2C
i2c_bus = busio.I2C(board.D5, board.D4)
mcp = MCP23017(i2c_bus)

keyboard.modules.append(EncoderHandler())
encoder_handler = EncoderHandler()

keyboard.extensions.append(MediaKeys())
keyboard.modules.append(MouseKeys())

driver = SSD1306(
    i2c=i2c_bus,
    device_address=0x3C,
)

display = Display(
    # Mandatory:
    display=driver,
    entries=[
        TextEntry(text="Layer: ", x=0, y=32, y_anchor="B"),
        TextEntry(text="SWAP", x=40, y=32, y_anchor="B", layer=0),
        TextEntry(text="DEFAULT", x=40, y=32, y_anchor="B", layer=1),
        TextEntry(text="PROGRAMMING", x=40, y=32, y_anchor="B", layer=2),
        TextEntry(text="GAMING", x=40, y=32, y_anchor="B", layer=3),
        TextEntry(text="NUMPAD", x=40, y=32, y_anchor="B", layer=4),
    ],
    # Optional:
    width=128,  # screen size
    height=32,  # screen size
    flip=False,  # flips your display content
    flip_left=False,  # flips your display content on left side split
    flip_right=False,  # flips your display content on right side split
    brightness=0.8,  # initial screen brightness level
    brightness_step=0.1,  # used for brightness increase/decrease keycodes
    # dim_time=20,  # time in seconds to reduce screen brightness
    # dim_target=0.1,  # set level for brightness decrease
    # off_time=60,  # time in seconds to turn off screen
    # powersave_dim_time=10,  # time in seconds to reduce screen brightness
    # powersave_dim_target=0.1,  # set level for brightness decrease
    # powersave_off_time=30,  # time in seconds to turn off screen
)
keyboard.extensions.append(display)

keyboard.row_pins = (mcp.GPB0, mcp.GPB1, mcp.GPB2, mcp.GPB3)
keyboard.col_pins = (mcp.GPB4, mcp.GPB5, mcp.GPB6, mcp.GPA0, mcp.GPA1)
diode_orientation = DiodeOrientation.ROW2COL

encoder_handler.pins = (
    (board.D0, board.D1, None),  # Encoder 1
    (board.D2, mcp.GPA6, None),  # Encoder 2 (GPA6)
    (mcp.GPA5, mcp.GPA4, None),  # Encoder 3 (GPA5, GPA4)
    (mcp.GPA3, mcp.GPA2, None),  # Encoder 4 (GPA3, GPA2)
)

LYR_SWP, LYR_DEF, LYR_PRG, LYR_GAM, LYR_NUM = 0, 1, 2, 3, 4
xxxxxxx = KC.NO

# fmt: off
keyboard.keymap = [
    # SWP LAYER
    [ 
        KC.DF(LYR_DEF), KC.DF(LYR_PRG), KC.DF(LYR_GAM), KC.DF(LYR_NUM), xxxxxxx, # DEFAULT	PROGRAMMING	GAMING	NUMPAD	
        xxxxxxx,        xxxxxxx,        xxxxxxx,        xxxxxxx,        xxxxxxx, #
        xxxxxxx,        xxxxxxx,        xxxxxxx,        xxxxxxx,        xxxxxxx, #
        xxxxxxx,        xxxxxxx,        xxxxxxx,        xxxxxxx,        xxxxxxx, #
    ],
    # DEF LAYER
    [
        KC.ESC,                 KC.LGUI(KC.LSFT(KC.T)), KC.LGUI(KC.LCTL(KC.T)), KC.PSCR,                KC.MUTE,  # ESC	GUI+SHIFT+T	GUI+CTRL+T	PRINTSCR	MUTE
        KC.LALT(KC.N1),         KC.LALT(KC.N2),         KC.LALT(KC.N3),         KC.LALT(KC.N4),         KC.MPLY,  # ALT+1	ALT+2	ALT+3	ALT+4	PLAY/PAUSE
        KC.LCTL(KC.F),          KC.F5,                  KC.LCTL(KC.W),          KC.LCTL(KC.T),          xxxxxxx,  # CTRL+F	F5	CTRL+L	CTRL+W	        
        KC.LT(LYR_SWP,KC.LALT(KC.SPC)), KC.MB_BTN5,     KC.MB_BTN4,             KC.LCTL(KC.T),          KC.RALT,  # ALT+SPACE LT	BACK	FORWARD	CTRL+T	RIGHT_ALT       
    ],

    # PRG LAYER
    [
        KC.UNDS,                KC.MINS, KC.PLUS, KC.EQL,   KC.MUTE,          #  _	-	+	=	MUTE
        KC.LABK,                KC.RABK, KC.LPRN, KC.RPRN,  KC.MPLY,          # <	>	(	)	PLAY/PAUSE          
        KC.SLSH,                KC.HASH, KC.SCLN, KC.DQT,   KC.LALT(KC.LSFT), # /	#	;	"	ALT+SHIFT
        KC.LT(LYR_SWP,KC.LCBR), KC.RCBR, KC.LBRC, KC.RBRC,  KC.LALT(KC.SPC),  # { LT	}	[	]	ALT+SPACE                        
    ],

    # GAM LAYER
    [
        KC.ESC,                  KC.F11,                 KC.LALT(KC.ENT),  KC.F3,   KC.MUTE, # ESC	F11	ALT+ENTER	F3	MUTE
        KC.LCTL(KC.LSFT(KC.M)),  KC.LCTL(KC.LSFT(KC.D)), KC.LSFT(KC.SLSH), xxxxxxx, KC.MPLY, # DISCORD MUTE	DISCORD DEAFEN	DISCORD TOGGLE		PLAY/PAUSE
        xxxxxxx,                 xxxxxxx,                xxxxxxx,          xxxxxxx, xxxxxxx, #		
        KC.LT(LYR_SWP, xxxxxxx), xxxxxxx,                xxxxxxx,          xxxxxxx, xxxxxxx, # LT			
    ],

    # NUM LAYER
    [
        KC.PSLS,                 KC.P7,  KC.P8, KC.P9,   KC.MUTE, # /	7	8	9	MUTE
        KC.PAST,                 KC.P4,  KC.P5, KC.P6,   KC.MPLY, # *	4	5	6	PLAY/PAUSE
        KC.PMNS,                 KC.P1,  KC.P2, KC.P3,   xxxxxxx, # -	1	2	3	
        KC.LT(LYR_SWP, KC.PPLS), KC.EQL, KC.P0, KC.PENT, xxxxxxx, #  "+ LT"	=	0	ENTER	          
    ],
]


# fmt: on
encoder_handler.divisor = 2
encoder_handler.map = [
    # SWP LAYER
    ((), (), (), ()),
    # DEF LAYER
    (
        (KC.VOLD, KC.VOLU),  # VOL_DOWN	VOL_UP
        (KC.MPRV, KC.MNXT),  # PREVIOUS	NEXT
        (KC.BRID, KC.BRIU),  # BRIGHT_DOWN	BRIGHT_UP
        (KC.MW_DN, KC.MW_UP),  # SCROLL DOWN	SCROLL UP
    ),
    # PRG LAYER
    (
        (KC.VOLD, KC.VOLU),  # VOL_DOWN	VOL_UP
        (KC.MPRV, KC.MNXT),  # PREVIOUS	NEXT
        (KC.DOWN, KC.UP),  # DOWN	UP
        (KC.LEFT, KC.RGHT),  # LEFT	RIGHT
    ),
    # GAM LAYER
    (
        (KC.VOLD, KC.VOLU),  # VOL_DOWN	VOL_UP
        (KC.MPRV, KC.MNXT),  # PREVIOUS	NEXT
        (),  #
        (),  #
    ),
    # NUM LAYER
    (
        (KC.VOLD, KC.VOLU),  # VOL_DOWN	VOL_UP
        (KC.MPRV, KC.MNXT),  # PREVIOUS	NEXT
        (KC.DOWN, KC.UP),  # DOWN	UP
        (KC.LEFT, KC.RGHT),  # LEFT	RIGHT
    ),
]

if __name__ == "__main__":
    keyboard.go()
