# lib/ — Adafruit-Bibliotheken

Dieser Ordner ist absichtlich (fast) leer. Die Adafruit-Bibliotheken kommen aus
dem offiziellen **CircuitPython Library Bundle**
(https://circuitpython.org/libraries), passend zur installierten
CircuitPython-Version. Sie werden NICHT im Git-Repo eingecheckt.

Benötigt (nach `CIRCUITPY/lib/` kopieren):

- `adafruit_hid/`
- `adafruit_displayio_ssd1306.mpy`
- `adafruit_display_text/`
- `adafruit_ticks.mpy`

`displayio`, `i2cdisplaybus`, `keypad`, `rotaryio`, `usb_hid` sind in
CircuitPython eingebaut und müssen nicht kopiert werden.
