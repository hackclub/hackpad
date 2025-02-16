## Breakdown of Firmware

First things first, the firmware runs on KMK!

To summarize the code:

Switches
Corresponding website shortcut when pressed for each key

Encoder #1
Turning Clockwise -> Volume Up
Turning Counterclockwise -> Volume Down
Click Down -> Turns LEDs On/Off

Encoder #2
Turning Clockwise -> Brightness Up
Turning Counterclockwise -> Brightness Down
Click Down -> Toggle Different LED Modes

OLED
Display Custom GIFS
Requires user to upload GIF file to microcontroller and name it user_gif.gif
The screen will continuously display GIF unless changed or powered off