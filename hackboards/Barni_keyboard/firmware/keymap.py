KEY_NONE = 0x00
KEY_A = 0x04
KEY_B = 0x05
KEY_C = 0x06
KEY_D = 0x07
KEY_E = 0x08
KEY_F = 0x09
KEY_G = 0x0A
KEY_H = 0x0B
KEY_I = 0x0C
KEY_J = 0x0D
KEY_K = 0x0E
KEY_L = 0x0F
KEY_M = 0x10
KEY_N = 0x11
KEY_O = 0x12
KEY_P = 0x13
KEY_Q = 0x14
KEY_R = 0x15
KEY_S = 0x16
KEY_T = 0x17
KEY_U = 0x18
KEY_V = 0x19
KEY_W = 0x1A
KEY_X = 0x1B
KEY_Y = 0x1C
KEY_Z = 0x1D
KEY_1 = 0x1E
KEY_2 = 0x1F
KEY_3 = 0x20
KEY_4 = 0x21
KEY_5 = 0x22
KEY_6 = 0x23
KEY_7 = 0x24
KEY_8 = 0x25
KEY_9 = 0x26
KEY_0 = 0x27
KEY_ENTER = 0x28
KEY_ESC = 0x29
KEY_BACKSPACE = 0x2A
KEY_TAB = 0x2B
KEY_SPACE = 0x2C
KEY_MINUS = 0x2D
KEY_EQUAL = 0x2E
KEY_LBRACKET = 0x2F
KEY_RBRACKET = 0x30
KEY_BACKSLASH = 0x31
KEY_SEMICOLON = 0x33
KEY_QUOTE = 0x34
KEY_GRAVE = 0x35
KEY_COMMA = 0x36
KEY_DOT = 0x37
KEY_SLASH = 0x38
KEY_CAPS_LOCK = 0x39
KEY_F1 = 0x3A
KEY_F2 = 0x3B
KEY_F3 = 0x3C
KEY_F4 = 0x3D
KEY_F5 = 0x3E
KEY_F6 = 0x3F
KEY_F7 = 0x40
KEY_F8 = 0x41
KEY_F9 = 0x42
KEY_F10 = 0x43
KEY_F11 = 0x44
KEY_F12 = 0x45
KEY_RIGHT = 0x4F
KEY_LEFT = 0x50
KEY_DOWN = 0x51
KEY_UP = 0x52

# Modifiers
MOD_LCTRL = 0x01
MOD_LSHIFT = 0x02
MOD_LALT = 0x04
MOD_LGUI = 0x08
MOD_RCTRL = 0x10
MOD_RSHIFT = 0x20
MOD_RALT = 0x40
MOD_RGUI = 0x80

# Special function keys
FN = 0xF0
LAYER_1 = 0xF1
LAYER_2 = 0xF2
LAYER_3 = 0xF3

LAYER_0 = [
    [(KEY_ESC, 0), (KEY_1, 0), (KEY_2, 0), (KEY_3, 0), (KEY_4, 0), (KEY_5, 0), (KEY_6, 0), (KEY_7, 0), (KEY_8, 0), (KEY_9, 0), (KEY_0, 0), (KEY_MINUS, 0), (KEY_EQUAL, 0), (KEY_BACKSPACE, 0)],
    [(KEY_TAB, 0), (KEY_Q, 0), (KEY_W, 0), (KEY_E, 0), (KEY_R, 0), (KEY_T, 0), (KEY_Y, 0), (KEY_U, 0), (KEY_I, 0), (KEY_O, 0), (KEY_P, 0), (KEY_LBRACKET, 0), (KEY_RBRACKET, 0), (KEY_BACKSLASH, 0)],
    [(KEY_CAPS_LOCK, 0), (KEY_A, 0), (KEY_S, 0), (KEY_D, 0), (KEY_F, 0), (KEY_G, 0), (KEY_H, 0), (KEY_J, 0), (KEY_K, 0), (KEY_L, 0), (KEY_SEMICOLON, 0), (KEY_QUOTE, 0), (KEY_ENTER, 0)],
    [(MOD_LSHIFT, 0), (KEY_Z, 0), (KEY_X, 0), (KEY_C, 0), (KEY_V, 0), (KEY_B, 0), (KEY_N, 0), (KEY_M, 0), (KEY_COMMA, 0), (KEY_DOT, 0), (KEY_SLASH, 0), (MOD_RSHIFT, 0)],
    [(MOD_LCTRL, 0), (MOD_LGUI, 0), (MOD_LALT, 0), (KEY_SPACE, 0), (MOD_RALT, 0), (FN, 0), (MOD_RCTRL, 0), (KEY_LEFT, 0), (KEY_DOWN, 0), (KEY_UP, 0), (KEY_RIGHT, 0)],
    [(KEY_NONE, 0)] * 21
]

LAYER_1 = [
    [(KEY_GRAVE, 0), (KEY_F1, 0), (KEY_F2, 0), (KEY_F3, 0), (KEY_F4, 0), (KEY_F5, 0), (KEY_F6, 0), (KEY_F7, 0), (KEY_F8, 0), (KEY_F9, 0), (KEY_F10, 0), (KEY_F11, 0), (KEY_F12, 0), (KEY_DELETE, 0)],
    [(KEY_NONE, 0)] * 14,
    [(KEY_NONE, 0)] * 13,
    [(KEY_NONE, 0)] * 12,
    [(KEY_NONE, 0)] * 11,
    [(KEY_NONE, 0)] * 21
]

def get_keycode(row, col, layer=0):
    try:
        if layer == 1:
            return LAYER_1[row][col]
        else:
            return LAYER_0[row][col]
    except IndexError:
        return (KEY_NONE, 0)
