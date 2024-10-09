from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.scanners import DiodeOrientation
import board

# Initialisation de la carte
keyboard = KMKKeyboard()

# Matrice 4x3 (4 rangées x 3 colonnes)
keyboard.row_pins = (board.A9, board.A8, board.A10)  # Row0, Row1, Row2
keyboard.col_pins = (board.A1, board.A2, board.A3, board.A4)  # Column0, Column1, Column2, Column3
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Ajout de l'encodeur rotatif
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

# Configurer les pins pour l'encodeur rotatif
encoder_handler.pins = ((board.A5, board.A6, board.A7, False),)  # Pin A, Pin B, Clic, Inversé=False

# Assignation des actions à chaque position (Encoder 1)
encoder_handler.map = (
    ((KC.VOLD, KC.VOLU, KC.MUTE),),  # Rotation gauche, Rotation droite, Clic
)

# Configuration de la matrice de touches avec des exemples d'actions
keyboard.keymap = [
    [
        KC.A, KC.B, KC.C, KC.D,   # Ligne 0
        KC.E, KC.F, KC.G, KC.H,   # Ligne 1
        KC.I, KC.J, KC.K, KC.L    # Ligne 2
    ]
]

# Lancement du clavier
if __name__ == '__main__':
    keyboard.go()
