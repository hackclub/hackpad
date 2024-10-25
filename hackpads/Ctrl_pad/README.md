![Ctrl_pad_img](https://github.com/user-attachments/assets/836ae5a9-e44c-481e-95a0-891602f4a99e)
# Ctrl_pad
A 3x3 macropad with an encoder and OLED display. Powered by [QMK](https://github.com/qmk/qmk_firmware).

### Modifications
PCB in black, case is all white, plate in transparent acrylic

### BOM
|            Part            | Amount |
|           :-----           | :----: |
| PCB                        | 1      |
| Acrylic Plate Piece        | 1      |
| 3D Printed Case Pieces     | 3      |
| M2X5 Screw                 | 1      |
| M3X12 Screws               | 2      |
| M3X6 Screws                | 2      |
| M2 Heat Set Inserts        | 1      |
| M3 Heat Set Inserts        | 4      |
| EC11 Encoder               | 1      |
| 0.96" SSD1306 OLED Display | 1      |
| Gateron Milky Yellows      | 8      |
| Mill-Max 0305s             | 16*    |
| 4.7K Through-hole Resistors| 2      |
| Through-hole 1N4148 Diodes | 9      |

*<sup> assuming one per socket

## Writeup (If this happens)

# Ctrl_pad
A macropad with 5 keys, an encoder and an 0.96" OLED display. It runs on QMK, hopes and dreams.
![Ctrl_pad_img](https://github.com/user-attachments/assets/ea17dad7-33b1-479b-87f6-5eb0091830cb)
It looks (approximately) like this. 

### Inspirations
The PCB is plain old standard for the most part, a rounded rectangular PCB because everyting is rounded these days and a few designs. The main design (attempt) takes from macOS and its shortcut symbols. The case follows on the PCB and so on. Why white? I took a look at black and decided, this ain't it.

### Challenges
Having done OnBoard, PCB design was (supposed to be) a lot better than my first time. Moving from EasyEDA to KiCAD was a bit wonky, but positioning and making parts work was the bulk of the challenge. Examples are, “Do I really need this resistor", “Did I wire this correctly" and "Is this spot okay". Making the case, it was mostly held back on what I could think. I did spend some chunk of my time on the specifics like holes, clearance, positioning and making sure this was possible to print. Firmware was also wonky. Most of it was easy until it wasn’t. Enabling LTO had a mini hold up, but with the abundance of documentation and a little help (the help being AI), it became a lot more manageable.

### Fun(?) Fact
- The name was supposed to be iCtrl, I decided maybe it isn't that kewl.
- I redid the switches, diodes and wiring about three times, maybe more.
- To _stand_ out, I made the biggest gamble on hoping I can pull off the removable **stand** (Pun not intended).
- Speaking of stands, I probably had 3 or more designs on how to attatch it.
- I took a break by rendering the model in Fusion, I also did some manufacturing simulation because I wanted to.
- I don't know C, I did not make the OLED code.

### What I learned
More PCB stuff, how to make a keyboard, how to 3D model, how to use QMK, KiCad, Fusion and a few more. I also learned that I have time as long as I want to do something enough. 
