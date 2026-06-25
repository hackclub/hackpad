"""Namen -> HID-Codes.

Das ist der gemeinsame "Wortschatz" zwischen Firmware und Konfigurator-App.
Die App schreibt in der config.json Tastennamen (z.B. "GUI", "C", "ENTER",
"LEFT_ARROW"); hier werden sie in echte HID-Codes aufgeloest.

Konvention: Die Namen entsprechen den Attributnamen von adafruit_hid.Keycode
(z.B. Keycode.LEFT_ARROW -> Name "LEFT_ARROW"). Zusaetzlich gibt es ein paar
freundliche Aliase (z.B. "Return" -> ENTER, "Cmd" -> GUI), damit die
Custom-Script-Syntax aus dem PDF ("(Return)", "(Left arrow)") funktioniert.
"""

from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode

# Freundliche Aliase -> kanonischer Keycode-Attributname.
# (Erst hier nachschlagen, sonst getattr(Keycode, NAME) versuchen.)
_KEY_ALIASES = {
    "RETURN": "ENTER",
    "CMD": "GUI",
    "COMMAND": "GUI",
    "WIN": "GUI",
    "WINDOWS": "GUI",
    "SUPER": "GUI",
    "META": "GUI",
    "CTRL": "CONTROL",
    "OPT": "ALT",
    "OPTION": "ALT",
    "ESC": "ESCAPE",
    "DEL": "DELETE",
    "BACKSPACE": "BACKSPACE",
    "LEFT": "LEFT_ARROW",
    "RIGHT": "RIGHT_ARROW",
    "UP": "UP_ARROW",
    "DOWN": "DOWN_ARROW",
    "SPACE": "SPACEBAR",
    "PAGEUP": "PAGE_UP",
    "PAGEDOWN": "PAGE_DOWN",
    # Ziffern als Tasten: "1" -> Keycode.ONE usw.
    "1": "ONE",
    "2": "TWO",
    "3": "THREE",
    "4": "FOUR",
    "5": "FIVE",
    "6": "SIX",
    "7": "SEVEN",
    "8": "EIGHT",
    "9": "NINE",
    "0": "ZERO",
}

# Media-/Consumer-Tasten (separater HID-Report).
_CONSUMER = {
    "PLAY_PAUSE": ConsumerControlCode.PLAY_PAUSE,
    "MUTE": ConsumerControlCode.MUTE,
    "VOLUME_UP": ConsumerControlCode.VOLUME_INCREMENT,
    "VOLUME_DOWN": ConsumerControlCode.VOLUME_DECREMENT,
    "VOLUME_INCREMENT": ConsumerControlCode.VOLUME_INCREMENT,
    "VOLUME_DECREMENT": ConsumerControlCode.VOLUME_DECREMENT,
    "NEXT_TRACK": ConsumerControlCode.SCAN_NEXT_TRACK,
    "PREV_TRACK": ConsumerControlCode.SCAN_PREVIOUS_TRACK,
    "SCAN_NEXT_TRACK": ConsumerControlCode.SCAN_NEXT_TRACK,
    "SCAN_PREVIOUS_TRACK": ConsumerControlCode.SCAN_PREVIOUS_TRACK,
    "STOP": ConsumerControlCode.STOP,
}


def _normalize(name):
    return name.strip().upper().replace(" ", "_").replace("-", "_")


def resolve_key(name):
    """Tastennamen -> Keycode-Wert. Wirft KeyError bei unbekanntem Namen."""
    key = _normalize(name)
    key = _KEY_ALIASES.get(key, key)
    try:
        return getattr(Keycode, key)
    except AttributeError:
        raise KeyError("Unbekannte Taste: %r" % name)


def resolve_media(name):
    """Media-Tastenname -> ConsumerControlCode. Wirft KeyError bei unbekannt."""
    key = _normalize(name)
    try:
        return _CONSUMER[key]
    except KeyError:
        raise KeyError("Unbekannte Media-Taste: %r" % name)
