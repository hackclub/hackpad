"""Laedt und validiert die config.json vom CIRCUITPY-Laufwerk.

Die Konfigurator-App schreibt /config.json auf das Geraet. Hier wird sie nur
gelesen. Bei fehlender oder kaputter Datei wird ein DEFAULT_CONFIG benutzt,
damit das Hackpad immer startet (nie "brickt").
"""

import json

CONFIG_PATH = "/config.json"

# Minimal-Fallback: 1 Profil, alle Tasten tippen ihre Nummer.
DEFAULT_CONFIG = {
    "version": 1,
    "active_profile": 0,
    "profiles": [
        {
            "name": "Default",
            "target_os": "mac",
            "keys": [
                {"label": str(i + 1),
                 "action": {"type": "string", "text": str(i + 1)}}
                for i in range(9)
            ],
        }
    ],
}


def _valid(cfg):
    """Sehr leichte Strukturpruefung (CircuitPython hat kein jsonschema)."""
    if not isinstance(cfg, dict):
        return False
    profiles = cfg.get("profiles")
    if not isinstance(profiles, list) or len(profiles) == 0:
        return False
    for p in profiles:
        keys = p.get("keys")
        if not isinstance(keys, list):
            return False
    return True


def load():
    """Gibt (config_dict, ok) zurueck. ok=False -> Fallback wurde benutzt."""
    try:
        with open(CONFIG_PATH, "r") as f:
            cfg = json.load(f)
    except (OSError, ValueError) as e:
        print("config.json nicht ladbar (%s) -> Default" % e)
        return DEFAULT_CONFIG, False

    if not _valid(cfg):
        print("config.json ungueltig -> Default")
        return DEFAULT_CONFIG, False

    # Jedes Profil auf genau 9 Tasten auffuellen (fehlende = nichts tun).
    for p in cfg["profiles"]:
        keys = p["keys"]
        while len(keys) < 9:
            keys.append({"label": "", "action": None})
    return cfg, True
