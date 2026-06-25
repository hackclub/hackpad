"""Profil-Verwaltung + Encoder-Browser.

Bedienung (laut PDF):
  Encoder drehen -> Vorschau-Modus, blaettert durch die Profile (OLED zeigt das
                    Vorschau-Profil).
  Encoder klick  -> bestaetigt das Vorschau-Profil als aktiv.

Das aktive Profil wird in microcontroller.nvm (1 Byte) gespeichert. Das
uebersteht einen Neustart / Auto-Reload, OHNE das USB-Laufwerk fuer den Host
schreibgeschuetzt zu machen (anders als storage.remount).
"""

try:
    import microcontroller
    _NVM = microcontroller.nvm
except (ImportError, AttributeError):
    _NVM = None


def _nvm_read(default=0):
    if _NVM is None or len(_NVM) < 1:
        return default
    return _NVM[0]


def _nvm_write(value):
    if _NVM is None or len(_NVM) < 1:
        return
    if _NVM[0] != value:          # Flash schonen: nur bei Aenderung schreiben
        _NVM[0] = value & 0xFF


class ProfileManager:
    def __init__(self, config, display):
        self._profiles = config["profiles"]
        self._display = display
        # Aktives Profil aus NVM holen, sonst aus config, sonst 0.
        idx = _nvm_read(config.get("active_profile", 0))
        self._active = self._clamp(idx)
        self._preview = self._active
        self._browsing = False
        self.show_active()

    # -- Eigenschaften ----------------------------------------------------

    @property
    def count(self):
        return len(self._profiles)

    @property
    def active_profile(self):
        return self._profiles[self._active]

    def action_for(self, key_index):
        """Aktion fuer Taste 0..8 im aktuell aktiven Profil (oder None)."""
        keys = self.active_profile["keys"]
        if 0 <= key_index < len(keys):
            return keys[key_index].get("action")
        return None

    # -- Encoder-Ereignisse ----------------------------------------------

    def on_encoder_turn(self, delta):
        if delta == 0:
            return
        self._browsing = True
        self._preview = (self._preview + delta) % self.count
        self._display.show_browser(
            self._profiles[self._preview]["name"], self._preview, self.count)

    def on_encoder_press(self):
        if self._browsing:
            self._active = self._preview
            _nvm_write(self._active)
            self._browsing = False
        self.show_active()

    # -- intern -----------------------------------------------------------

    def show_active(self):
        self._preview = self._active
        self._display.show_status(
            self.active_profile["name"], self._active, self.count)

    def _clamp(self, idx):
        if idx < 0 or idx >= len(self._profiles):
            return 0
        return idx
