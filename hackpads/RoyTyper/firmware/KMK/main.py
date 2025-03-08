import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.extensions.media_keys import MediaKeys
from kmk.keys import KC
import neopixel
import rotaryio
import time
import subprocess

# defining all pins and stuff
rows=[board.GP26,board.GP27,board.GP28]
cols=[board.GP29,board.GP06,board.GP07]

pixelPin=board.GP0
encoderA=board.GPI03
encoderB=board.GPI04

numPixels=3

# Initializing all objs

keyboard=KMKKeyboard()

rotaryEncoder=rotaryio.IncrementalEncoder(encoderA,encoderB)

pixels=neopixel.NeoPixel(pixelPin,numPixels,brightness=0.5,auto_write=False)

rgb=RGB(pixels)

# Other vars

mode=0
"""
Mode numbers, they specify what the colors do and what the rotary encoder does
0-> blue, Volume
1-> red, Brightness
2-> Rizz Mode(Random RGB colors),Color brightness 
"""
blue=(137,180,250)
red=(243,139,168)
white=(255,255,255)
currentColor=blue
color_cycle_mode=False
colorBrightness=1
browser_name="zen-browser"
terminal_name="kitty"
mostrepeated="This is a sentence that I repeat the most, lol."


# All functions
def setColor(r,g,b):
    global currentColor
    currentColor=(r,g,b)
    for i in range(numPixels):
        pixels[i]=currentColor
    pixels.show()
def encoderCallback():
    global colorBrightness
    if mode==0:
        if rotaryEncoder.position > 0:
                kb.tap_key(KC.VOLU)
        elif rotaryEncoder.position <0:
                kb.tap_key(KC.VOLD)
    elif mode==1:
        if rotaryEncoder.position > 0:
                kb.tap_key(KC.BRIU)
        elif rotaryEncoder.position <0:
                kb.tap_key(KC.BRID)
    else:
        if rotaryEncoder.position > 0:
            colorBrightness=(colorBrightness+0.1)%1.1
        elif rotaryEncoder.position <0:
            colorBrightness=(colorBrightness-0.1)%1.1
        pixels.brightness=colorBrightness
def colorCycle():
    ## Will possibly have to use threading or something
    ## but will do that while testing the code
    while color_cycle_mode:
        for i in range(0,255):
            for j in range(0,255):
                for k in range(0,255):
                    setColor(i,j,k)
                    time.sleep(0.05)
def modeToggle():
    global mode, color_cycle_mode
    mode=(mode+1)%3
    if mode==0:
        setColor(blue)
        color_cycle_mode=False
    elif mode==1:
        setColor(red)
        color_cycle_mode=False
    else:
        color_cycle_mode=True
        colorCycle()
def openBrowser():
    subprocess.run([browser_name],check=True)

def openYoutube():
    subprocess.run([browser_name,"youtube.com"],check=True)

def openSlack():
    subprocess.run([browser_name,"https://app.slack.com/"],check=True)
def startTerminal():
    subprocess.run([terminal_name],check=True)
def killCurrent():
    subprocess.run(['qtile', 'cmd-obj', '-o', 'window', '-f' ,'kill'],check=True)

def fullScreenToggle():
    subprocess.run(['qtile', 'cmd-obj', '-o', 'window', '-f' ,'toggle_fullscreen'],check=True)

def toggleMouse():
    """
    Does nothing for now, but I will implement the function soon.
    It is supposed to turn the macropad to a mouse
    """
    pass


## adding modules and stuff
macros=Macros()
setColor(currentColor)
keyboard.modules.append(rotaryEncoder,encoderCallback())
keyboard.extensions.append(MediaKeys())
keyboard.modules.append(macros)

keymap=[
        [openBrowser, openYoutube, openSlack],
        [startTerminal, killCurrent, fullScreenToggle],
        [modeToggle, KC.MACRO(mostrepeated), toggleMouse],
        ]

keyboard.keymap=keymap

if __name__=="__main__":
    setColor(*currentColor)
    keyboard.go()

