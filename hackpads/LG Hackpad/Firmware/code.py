"""Hackpad-Firmware (CircuitPython) -- Hauptprogramm.

Liest config.json, scannt die 3x3-Matrix, liest den Encoder und treibt das OLED.
Tastendruck -> fuehrt die konfigurierte Aktion des aktiven Profils aus.
Encoder drehen/klicken -> Profil waehlen.

CircuitPython laedt diese Datei automatisch neu, wenn sich Dateien auf dem
Laufwerk aendern (z.B. wenn die App eine neue config.json schreibt) -> neue
Konfiguration ist sofort aktiv. Das aktive Profil wird im NVM gehalten und
ueberlebt den Reload.

Pin-Mapping (aus dem Schaltplan):
  Spalten COL0/1/2 = D0/D1/D2
  Zeilen  ROW0/1/2 = D3/D6/D7
  Encoder A=D8, B=D9, Klick=D10
  OLED    SDA=D4, SCL=D5  (ueber board.I2C())
"""

import board
import keypad
import rotaryio
import usb_hid

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.consumer_control import ConsumerControl

from hackpad import config as config_mod
from hackpad import display as display_mod
from hackpad.macros import MacroEngine
from hackpad.profiles import ProfileManager

# --- Matrix ---------------------------------------------------------------
# COL2ROW: Diodenanode an der Spalte -> columns_to_anodes=True.
# Falls beim Bring-up keine/falsche Tasten kommen: diesen Wert umdrehen.
COLUMN_PINS = (board.D0, board.D1, board.D2)
ROW_PINS = (board.D3, board.D6, board.D7)

# keypad nummeriert: key_number = row * num_columns + column.
# KEY_MAP[key_number] = logische Taste 0..8 (Taste 1..9 in der App).
# Standard = identisch (Zeile oben, links->rechts). Beim Bring-up anpassen,
# falls die physische Anordnung anders ist.
KEY_MAP = (0, 1, 2, 3, 4, 5, 6, 7, 8)


def main():
    # HID-Geraete
    keyboard = Keyboard(usb_hid.devices)
    layout = KeyboardLayoutUS(keyboard)
    consumer = ConsumerControl(usb_hid.devices)
    engine = MacroEngine(keyboard, layout, consumer)

    # Konfiguration + Anzeige + Profile
    cfg, ok = config_mod.load()
    if not ok:
        print("Hinweis: Standard-Konfiguration aktiv (config.json fehlt/ungueltig)")
    oled = display_mod.Display()
    profiles = ProfileManager(cfg, oled)

    # Eingabe-Hardware
    matrix = keypad.KeyMatrix(
        row_pins=ROW_PINS,
        column_pins=COLUMN_PINS,
        columns_to_anodes=True,
    )
    encoder = rotaryio.IncrementalEncoder(board.D8, board.D9)
    enc_button = keypad.Keys((board.D10,), value_when_pressed=False, pull=True)
    last_position = encoder.position

    print("Hackpad bereit. Profile:", profiles.count)

    while True:
        # 1) Tasten der Matrix
        event = matrix.events.get()
        if event and event.pressed:
            key_index = KEY_MAP[event.key_number]
            engine.run(profiles.action_for(key_index))

        # 2) Encoder drehen
        position = encoder.position
        if position != last_position:
            profiles.on_encoder_turn(position - last_position)
            last_position = position

        # 3) Encoder klicken
        benv = enc_button.events.get()
        if benv and benv.pressed:
            profiles.on_encoder_press()


main()
