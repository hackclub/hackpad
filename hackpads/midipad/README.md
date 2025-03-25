# MIDIpad

An independent venture into MIDI controllers.

## ✨ What 

In its current state, MIDIpad is as the name implies: a portable 12-key MIDI controller
with an admittedly non-standard key layout (order: left to right, top to bottom). There
are three knobs for interfacing with a Digital Audio Workstation (DAW), and when pressed,
for switching between three MIDI channels.

The future vision is to make a portable and minimal looper, able to load samples or
plugins from an SD card, while still functioning as a MIDI device.

## ❓ Why

Although I own a MIDI piano, I find the linear layout to be less intuitive for drumming.
I took great inspiration by Launchpads—I don't own one, but I value the grid-based
interface. However, although flashy, I don't need the full 64 keys that Launchpads offer,
so that became my initial motivation for this device.

## 📝 Bill of Materials

Electronics

- 1x Seeed XIAO RP2040 _(Microcontroller)_
- 1x MCP23017-E/SO _(IO expander)_
- 12x Choc V2 switches
- 12x Through-hole 1N4148 Diodes
- 3x SK6812 MINI-E LEDs
- 3x EC11 Rotary encoders
- 2x 4.7kΩ Resistors
- 1x 0.91 inch OLED display (HS HS91L02W2C01)

Physical

- 4x M3x5mx4mm heatset inserts
- 4x M3x16mm screws
- 4x M3 hex nuts
- 5x Blank DSA keycaps (Black)
- 7x Blank DSA keycaps (White)

## 📸 Pictures

![PCB view of midipad in KiCad](https://github.com/user-attachments/assets/e291a786-e8bb-4892-b345-8339b5e39b9f)

![3-D view of the entire case](https://github.com/user-attachments/assets/bb3579b9-1218-4698-a2f8-db43de450aad)

![3-D view of the PCB](https://github.com/user-attachments/assets/9d02af57-4bf4-4724-8494-3c31c4919a5e)


![Half of the schematic view of midipad](https://github.com/user-attachments/assets/3db30f81-78f0-42c3-90d1-1a9fae4ef9c9)

![The other half of the schematic view of midipad](https://github.com/user-attachments/assets/7542dc9c-3ca8-418c-934b-b8694c95423f)
