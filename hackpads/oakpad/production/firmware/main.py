print("Starting")

# Basic imports
import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import MatrixScanner, KeysScanner
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

from kmk.modules.macros import Macros, Press, Release, Tap

from kmk.extensions.statusled import statusLED
from kmk.extensions.layers import Layers


class MyKeyboard(KMKKeyboard):
    def __init__(self):
        self.matrix = [
            MatrixScanner(
                cols=(board.D0, board.D1),
                rows=(board.D10, board.D9, board.D8),

                columns_to_anodes = DiodeOrientation.ROW2COL,
            ),
            KeysScanner(
                pins=[board.D6]
            )
        ]

        self.coord_mapping = [
            0, 1, 2,
            3, 4, 5, 6
        ]

        '''
        Comment Line (single line comment), Go To Line, Multi cursor
        Trim trailing whitespace,           Cycle tabs, Open command console, Change layer
        '''
        self.keymap = [
            # VSCode (Windows/Linux)
            [
                KC.LCTL(KC.KP_SLASH),
                KC.LCTL(KC.G),
                KC.LCTL(KC.LSFT(KC.L)),

                KC.MACRO(
                    Press(KC.LCTL),
                    Tap(KC.K),
                    Tap(KC.X),
                    Release(KC.LCTL)
                ),
                KC.LCTL(KC.TAB),
                KC.F1,
                KC.DF(1),
            ],
            # VSCode (MacOS)
            [
                KC.LCTL(KC.KP_SLASH),
                KC.LCTL(KC.G),
                KC.LGUI(KC.LSFT(KC.L)),

                KC.MACRO(
                    Press(KC.LGUI),
                    Tap(KC.K),
                    Tap(KC.X),
                    Release(KC.LGUI)
                ),
                KC.LCTL(KC.TAB),
                KC.F1,
                KC.DF(2),
            ],
            # NeoVim
            [
                # relies on Comment.nvim (https://github.com/numToStr/Comment.nvim)
                KC.MACRO(
                    # enter visual linewise mode
                    on_press=(Press(KC.LCTL(KC.V))),
                    # toggle the region using linewise comment
                    on_release=("gc", Press(KC.ENTER)),
                ),
                KC.MACRO(
                    on_press=(Press(KC.ESC), ":"),
                    on_release=(Press(KC.ENTER))
                )
                # I asked around, they said multicursors aren't necessary on neovim
                KC.NO,

                # relies on trim.nvim (https://github.com/cappyzawa/trim.nvim)
                KC.MACRO(
                    Press(KC.ESC),
                    ":Trim",
                    Press(KC.ENTER)
                ),
                KC.NO,
                KC.MACRO(KC.ESC, ":")
                KC.DF(3),
            ],
            # Intellij IDEA (Mac)
            [
                KC.LCTL(KC.KP_SLASH),
                KC.LCTL(KC.G),
                KC.MACRO(
                    on_press=(Press(KC.LALT), Press(KC.LSHIFT))
                    on_release=(Release(KC.LALT), Release(KC.LSHIFT))
                ),

                # apparently jetbrains already does this by default
                KC.NO,
                KC.LCTL(KC.RIGHT)
                KC.NO,
                KC.DF(0)
            ],
        ]

keyboard = MyKeyboard()

# layer
keyboard.modules.append(Layers())

# layer indicators
statusLED = statusLED(led_pins=[board.D2, board.D3, board.D4, board.D5])
keyboard.extensions.append(statusLED)

# macros
macros = Macros()
keyboard.modules.append(macros)

if __name__ == '__main__':
    keyboard.go()