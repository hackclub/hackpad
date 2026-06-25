# Hackpad Firmware (CircuitPython)

Firmware für den Hackpad-Macropad (Seeed XIAO RP2040). Liest eine `config.json`,
scannt die 3×3-Matrix, blättert per Encoder durch Profile (OLED-Feedback) und
führt pro Taste konfigurierbare Aktionen aus (Tastenkombis, getippte Strings,
Media-Tasten, Custom-Sequenzen).

## Aufbau

```
boot.py            Aktiviert HID (Tastatur + Media), Laufwerk bleibt host-beschreibbar
code.py            Hauptprogramm: Setup + Hauptschleife
config.json        Beispiel-Konfiguration (wird später von der App überschrieben)
hackpad/
  keymap.py        Tastennamen -> HID-Codes (gemeinsamer Wortschatz mit der App)
  config.py        config.json laden/validieren (mit Fallback)
  macros.py        Macro-Engine: führt eine Aktion aus
  profiles.py      Profil-Browser + NVM-Persistenz
  display.py       OLED-Statusanzeige (läuft auch ohne OLED)
lib/               Adafruit-Bibliotheken (siehe unten — NICHT im Repo)
```

Schema der `config.json`: siehe [`../docs/config-schema.md`](../docs/config-schema.md).

## Installation (wenn die Hardware da ist)

1. **CircuitPython flashen**
   - XIAO RP2040 per USB-C anstecken.
   - Den **BOOT**-Knopf gedrückt halten, kurz **RESET** tippen, BOOT loslassen
     (oder bei nur einem Knopf: BOOT halten beim Einstecken). Es erscheint ein
     Laufwerk `RPI-RP2`.
   - Die passende **`.uf2`** von circuitpython.org (Board: *Seeed XIAO RP2040*)
     auf `RPI-RP2` ziehen. Das Board startet neu → Laufwerk `CIRCUITPY`.

2. **Bibliotheken kopieren** (CircuitPython Library Bundle von
   circuitpython.org/libraries, passend zur CP-Version). Nach `CIRCUITPY/lib/`:
   - `adafruit_hid/`
   - `adafruit_displayio_ssd1306.mpy`
   - `adafruit_display_text/`
   - `adafruit_ticks.mpy`
   - (`i2cdisplaybus`/`displayio` sind in CircuitPython 9+ eingebaut)

3. **Firmware kopieren**: `boot.py`, `code.py`, `config.json` und den Ordner
   `hackpad/` nach `CIRCUITPY/`.

4. **Fertig** — das Board startet die Firmware automatisch. Änderungen an
   Dateien (auch an `config.json`) lösen einen Auto-Reload aus.

## Bring-up-Checkliste (erster Hardware-Test)

- [ ] Serielle Konsole öffnen (Mu-Editor, oder `tio`/`screen` auf das
      USB-Modem-Device) → Boot-Meldungen sichtbar?
- [ ] Jede der 9 Tasten in einem Texteditor drücken → kommt die erwartete
      Aktion? Falls falsche Taste reagiert: `KEY_MAP` in `code.py` anpassen.
- [ ] Falls **gar keine** Taste reagiert: `columns_to_anodes` in `code.py`
      umdrehen (Diodenrichtung).
- [ ] Encoder drehen → OLED zeigt Profil-Vorschau; Klick → Profil wird aktiv.
- [ ] OLED zeigt das aktive Profil. Falls dunkel: I2C-Adresse (0x3C/0x3D) in
      `hackpad/display.py` prüfen.

## Debuggen ohne Hardware

Die Python-Syntax lässt sich lokal prüfen:
```
python3 -m py_compile boot.py code.py hackpad/*.py
```
Echte Funktion (HID, Matrix, OLED) braucht das CircuitPython-Board.
