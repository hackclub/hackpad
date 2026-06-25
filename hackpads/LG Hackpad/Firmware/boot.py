"""boot.py -- laeuft einmal beim Einstecken, vor code.py.

Aktiviert genau die HID-Geraete, die das Hackpad braucht: Tastatur +
Consumer-Control (Media-Tasten). Maus wird nicht gebraucht und spart so einen
USB-Endpoint.

Das USB-Laufwerk bleibt absichtlich vom Host beschreibbar (kein
storage.remount), damit die Konfigurator-App die config.json schreiben kann.
"""

import usb_hid

usb_hid.enable((usb_hid.Device.KEYBOARD, usb_hid.Device.CONSUMER_CONTROL))
