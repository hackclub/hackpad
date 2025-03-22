import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

# Initialize keyboard
keyboard = KMKKeyboard()

# Set up keyboard matrix based on the schematic
# The schematic shows:
# COL1-COL12 connected to GP0-GP15
# ROW1-ROW8 connected to GP6-GP26
keyboard.col_pins = [
    board.GP0,  # COL1
    board.GP1,  # COL2
    board.GP2,  # COL3
    board.GP3,  # COL4
    board.GP4,  # COL5
    board.GP5,  # COL6
    board.GP10, # COL7
    board.GP11, # COL8
    board.GP12, # COL9
    board.GP13, # COL10
    board.GP14, # COL11
    board.GP15, # COL12
]

keyboard.row_pins = [
    board.GP6,  # ROW1
    board.GP7,  # ROW2
    board.GP8,  # ROW3
    board.GP9,  # ROW4
    board.GP20, # ROW5
    board.GP21, # ROW6
    board.GP22, # ROW7
    board.GP26, # ROW8
]

# Diodes are oriented from columns to rows based on the schematic
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Mac-specific key aliases
KC.LOPT = KC.LALT  # Option key (Alt)
KC.LCMD = KC.LGUI  # Command key (GUI)

# Create a keymap that matches the physical layout of the keyboard
# Based on the schematic with 40 switches (SW1-SW40)
# With specific assignments:
# SW34: Caps Lock, SW35: Shift, SW40: Spacebar, SW31: Spacebar, 
# SW38: Backspace, SW39: Enter/Return

# KMK expects a rectangular matrix where each row has the same number of columns
# We need to map the keys according to their physical positions in the matrix

# Looking at the schematic, we can see the following layout:
# Left side: SW1-SW21 (6+6+6+3 keys)
# Right side: SW16-SW40 (6+6+6+7 keys)

keyboard.keymap = [
    [
        # Row 1 (SW1-SW6) - Left side
        KC.ESC,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   
        # Row 5 (SW16-SW21) - Right side
        KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.MINS,
        
        # Row 2 (SW7-SW12) - Left side
        KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    
        # Row 6 (SW22-SW27) - Right side
        KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.LBRC,
        
        # Row 3 (SW13-SW18) - Left side
        KC.LCTL, KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    
        # Row 7 (SW28-SW33) - Right side
        KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOT,
        
        # Row 4 (SW19-SW21) - Left side
        KC.LOPT, KC.Z,    KC.X,    KC.NO,   KC.NO,   KC.NO,   
        # Row 8 (SW34-SW40) - Right side
        KC.CAPS, KC.LSFT, KC.C,    KC.V,    KC.B,    KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH, KC.SPC,  KC.ENT,
    ],
]

# Uncomment to enable debugging
# keyboard.debug_enabled = True

if __name__ == '__main__':
    keyboard.go()

