"""OLED-Statusanzeige (SSD1306, 128x64, I2C).

Zwei Ansichten:
  Status  -> zeigt das aktive Profil ("> Coding")
  Browser -> wenn man am Encoder dreht, zeigt es das Vorschau-Profil + Hinweis
             "Klick = OK", damit man bestaetigen kann.

Wenn kein OLED gefunden wird, laeuft alles weiter (self.ok == False) -- das
Hackpad funktioniert dann ohne Anzeige.
"""

try:
    import board
    import displayio
    import i2cdisplaybus
    import terminalio
    from adafruit_display_text import label
    import adafruit_displayio_ssd1306
    _HAVE_LIBS = True
except ImportError:
    _HAVE_LIBS = False

WIDTH = 128
HEIGHT = 64
ADDR = 0x3C


class Display:
    def __init__(self):
        self.ok = False
        self._title = None
        self._line1 = None
        self._line2 = None
        if not _HAVE_LIBS:
            print("Display-Libs fehlen -> ohne OLED")
            return
        try:
            displayio.release_displays()
            i2c = board.I2C()  # nutzt board.SCL / board.SDA
            bus = i2cdisplaybus.I2CDisplayBus(i2c, device_address=ADDR)
            self._disp = adafruit_displayio_ssd1306.SSD1306(
                bus, width=WIDTH, height=HEIGHT)
            self._build()
            self.ok = True
        except Exception as e:
            print("OLED-Init fehlgeschlagen (%s) -> ohne OLED" % e)

    def _build(self):
        group = displayio.Group()
        self._title = label.Label(terminalio.FONT, text="Hackpad", x=2, y=8)
        self._line1 = label.Label(terminalio.FONT, text="", x=2, y=30)
        self._line2 = label.Label(terminalio.FONT, text="", x=2, y=50)
        group.append(self._title)
        group.append(self._line1)
        group.append(self._line2)
        self._disp.root_group = group

    def show_status(self, name, index, total):
        if not self.ok:
            print("[OLED] Profil: %s (%d/%d)" % (name, index + 1, total))
            return
        self._title.text = "Hackpad"
        self._line1.text = "> %s" % name
        self._line2.text = "Profil %d/%d" % (index + 1, total)

    def show_browser(self, name, index, total):
        if not self.ok:
            print("[OLED] Browse: %s (%d/%d)" % (name, index + 1, total))
            return
        self._title.text = "Profil waehlen"
        self._line1.text = "  %s" % name
        self._line2.text = "%d/%d  Klick=OK" % (index + 1, total)
