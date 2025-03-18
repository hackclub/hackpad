from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.rotary_encoder import RotaryEncoder

from kmk.extensions.oled import Oled, OledDisplayMode
from kmk.modules.midi import MidiKeys

keyboard = KMKKeyboard()
keyboard.modules.append(MidiKeys())


key_change = 0
note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

keyboard.row_pins = (11,10,9) #push switches / keys
keyboard.diode_orientation = DiodeOrientation.COL2ROW


def calculate_keymap():
    global key_change
    return[
        [KC.MIDI_NOTE(60 + key_change,127)], #c
        [KC.MIDI_NOTE(64 + key_change,127)], #e
        [KC.MIDI_NOTE(67 + key_change,127)], #g
    ]


keyboard.keymap = calculate_keymap() #original

def update_key_change(x):
    global key_change
    key_change += x
    key_change = max(min(key_change, 24), -24)
    keyboard.keymap = calculate_keymap()

def midi_note_to_name(midi_note):
    octave = (midi_note // 12) - 1
    note = note_names[midi_note % 12]
    return f"{note}{octave}"

encoder = RotaryEncoder(
    pins=(1,8),  
    up=lambda: update_key_change(1),
    down=lambda: update_key_change(-1)
)
keyboard.extensions.append(encoder)

def oled_update(oled):
    oled.clear()
    note1 = midi_note_to_name(60 + key_change)
    note2 = midi_note_to_name(64 + key_change)
    note3 = midi_note_to_name(67 + key_change)
    oled.write_line(f"key: {note1}")
    oled.write_line(f"notes: {note1}, {note2}, {note3}")

oled_ext = Oled(
    OledDisplayMode.LAYER,
    flip=False,
    sda=5,
    scl=6,
    i2c_addr=0x3C
)

oled_ext.on_oled_update = oled_update
keyboard.extensions.append(oled_ext)

if __name__ == '__main__':
    keyboard.go()
