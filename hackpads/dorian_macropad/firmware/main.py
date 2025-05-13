from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.handlers.sequences import send_string
from kmk.extensions.display import Display
from kmk.extensions.encoder import EncoderHandler
from kmk.scanners.digital import DiodeOrientation
from kmk.scanners.keypad import MatrixScanner
keyboard = KMKKeyboard()
keyboard.modules.append(Layers())
# Configuration de l'écran OLED
display = Display()
keyboard.extensions.append(display)
def show_logo():
    display.show_pbm("logo.pbm")  # Assurez-vous d'avoir un fichier 'logo.pbm' sur l'appareil
# Configuration des touches (Seed XIAO RP2040)
keyboard.matrix = MatrixScanner(
    column_pins=(1, 2, 3, 4, 5),  # Modifier selon ton câblage
    row_pins=(6, 7, 8),  # Modifier selon ton câblage
    diode_orientation=DiodeOrientation.COL2ROW
)
# Définition des couches (layouts)
layers = [
    [KC.F13, KC.F14, KC.F15, KC.F16, KC.F17, KC.F18, KC.F19, KC.F20, KC.F21, KC.F22, KC.F23, KC.F24, KC.F25, KC.F26, KC.F27],
    [KC.A, KC.B, KC.C, KC.D, KC.E, KC.F, KC.G, KC.H, KC.I, KC.J, KC.K, KC.L, KC.M, KC.N, KC.O],
    [KC.P, KC.Q, KC.R, KC.S, KC.T, KC.U, KC.V, KC.W, KC.X, KC.Y, KC.Z, KC.LSHIFT, KC.LCTRL, KC.LALT, KC.LGUI],
    [send_string('Hello'), send_string('World'), KC.ESC, KC.TAB, KC.SPACE, KC.ENTER, KC.BSPACE, KC.DELETE, KC.HOME, KC.END, KC.PGUP, KC.PGDN, KC.UP, KC.DOWN, KC.RIGHT]
]
# Bouton pour changer de mode
LAYER_TOGGLE = KC.MO(1)
# Gestion du potentiomètre (encodeur rotatif EC11)
encoder_handler = EncoderHandler()
keyboard.extensions.append(encoder_handler)
# Associe le potentiomètre au contrôle du volume
encoder_handler.pins = [(9, 10)]  # Modifier selon les broches réelles
encoder_handler.map = [(KC.VOLD, KC.VOLU)]
# Configuration des touches
keyboard.keymap = [
    [LAYER_TOGGLE] + layers[0],
    [LAYER_TOGGLE] + layers[1],
    [LAYER_TOGGLE] + layers[2],
    [LAYER_TOGGLE] + layers[3]
]
# Affichage du logo au démarrage
show_logo()
if _name_ == '_main_':
    keyboard.go()s