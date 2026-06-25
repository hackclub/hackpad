"""Macro-Engine: fuehrt eine "action" aus der config.json aus.

Action-Typen (siehe docs/config-schema.md):
  combo    -> mehrere Tasten gleichzeitig druecken/loslassen  (z.B. Cmd+C)
  string   -> Text Zeichen fuer Zeichen tippen (super schnell)
  media    -> eine Media-/Consumer-Taste (z.B. Play/Pause)
  sequence -> Liste von Schritten nacheinander; jeder Schritt ist wieder
              key / combo / string / media

Die Firmware parst KEIN Skript-Textformat ("(Return)", "...") -- das macht die
App und schreibt fertige, strukturierte JSON. Hier wird nur ausgefuehrt.
"""

import time

from . import keymap

# Kleine Pause zwischen Sequenz-Schritten, damit der Host mitkommt.
STEP_DELAY = 0.01


class MacroEngine:
    def __init__(self, keyboard, layout, consumer):
        self._kbd = keyboard
        self._layout = layout
        self._cc = consumer

    def run(self, action):
        """Fuehrt eine einzelne Aktion aus. None / unbekannt = no-op."""
        if not action:
            return
        try:
            self._dispatch(action)
        except Exception as e:  # nie wegen einer Tastenbelegung abstuerzen
            print("Macro-Fehler bei %r: %s" % (action, e))

    # -- intern -----------------------------------------------------------

    def _dispatch(self, action):
        kind = action.get("type")
        if kind == "combo":
            self._combo(action.get("keys", []))
        elif kind == "key":
            self._combo([action.get("key")])
        elif kind == "string":
            self._string(action.get("text", ""))
        elif kind == "media":
            self._media(action.get("code"))
        elif kind == "sequence":
            self._sequence(action.get("steps", []))
        else:
            print("Unbekannter Action-Typ: %r" % kind)

    def _combo(self, names):
        codes = [keymap.resolve_key(n) for n in names if n]
        if not codes:
            return
        self._kbd.press(*codes)
        self._kbd.release_all()

    def _string(self, text):
        # KeyboardLayoutUS.write tippt den Text Zeichen fuer Zeichen.
        if text:
            self._layout.write(text)

    def _media(self, code_name):
        if code_name:
            self._cc.send(keymap.resolve_media(code_name))

    def _sequence(self, steps):
        for step in steps:
            self._dispatch(step)
            time.sleep(STEP_DELAY)
