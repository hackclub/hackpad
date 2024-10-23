#include <Wire.h>
#include "Keyboard.h"
#include "pcf8574.h"
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

//Number of Columns/Rows overall there are
#define COLS 4
#define ROWS 4

//Number of keys in the keypad itself, excluding the rotrary encoders
#define KEYPAD_ROWS 3
#define KEYPAD_COLS 4

//Number of arrangements for the pad itself
#define NUM_NUMPADS 1

//Number of rotrary encoders there are
#define NUM_ROTARIES 3

//Number of shortcuts there are
#define NUM_SHORTCUTS 16

//The address of the PCF8574A
#define PCF_ADDRESS 0x3F

#define TOP_BOARD_ADDRESS
#define SIDE_BOARD_ADDRESS

//Ignore char. Will ignore this char whenever it comes up in the shortcuts.
#define IGNORE_CHAR 'I'

//Release char. Will release all keys at the end of the shortcut if this is present.
#define RELEASE_CHAR 'R'

//Max number of strokes for a shortcut
#define SHORTCUT_MAX_STROKES 10

//The column ports for the switches/button matrix
byte cols[] = {D0,D1,D2,D3}; //cols are the inputs to the switches
//The row ports for the switches/button matrix
byte rows[] = {D10,D9,D8,D7}; //rows is what is returned

//Rotary encoders
byte rotaries[] = {0,1,2,3,4,5};

//ignore coordinate (3,3) when searching.
byte ignore[] = {3,3};

//If true, will only press once when key press down. If false, will change around.
bool stickyKeys = true;

//Nicknames for the numpads below.
String numpadAliases[] = {
    "Numpad",
    "Fusion360"
};

//Layouts for the numpads
String numpadLayouts[][KEYPAD_ROWS][KEYPAD_COLS] = {
    { //numpad
        {"SWITCH_BACK", "1","2","3"},
        {"ALL_MENU",      "4","5","6"},
        {"SWITCH",   "7","8","9"}
    },
    {
        {"SWITCH_BACK", "SAVE","COPY","PASTE"},
        {"SUB",         "e","m","v"}, //extrude, move, toggle visibility
        {"SWITCH",      "SCREEN_LEFT","ALL_MENU","SCREEN_RIGHT"}
    }
};

//shortcuts list
struct Shortcut {
    String id;
    char keys[SHORTCUT_MAX_STROKES];
};

Shortcut shortcuts[NUM_SHORTCUTS];

String rotarySwitchLayout[] = {
    "VOL_MUTE",
    "DND"
};

//[0] is when it increases, [1] is when it decreases
String rotaryLayouts[][2] = {
    {"VOL_UP", "VOL_DOWN"},
    {"BRIGHT_UP", "BRIGHT_DOWN"},
    {"ARR_LEFT", "ARR_RIGHT"}
};

//current numpad
int currentNumpad = 0;

//Array of which keys are down.
bool keysDown[ROWS][COLS];

//Array of the values of the rotrary encoders
int lastCLKValues[NUM_ROTARIES];
int currentCLKValues[NUM_ROTARIES];
int currentDTValues[NUM_ROTARIES];

//Positions
int positions[NUM_ROTARIES];
int lastPositions[NUM_ROTARIES];

//PCF object
PCF8574 pcfboard = PCF8574(PCF_ADDRESS);


//OLED display
#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 32

#define TOP_DISPLAY 0x3C
#define BOT_DISPLAY 0x3D

Adafruit_SSD1306 topDisplay(SCREEN_HEIGHT, SCREEN_WIDTH, &Wire, -1);
Adafruit_SSD1306 botDisplay(SCREEN_HEIGHT, SCREEN_WIDTH, &Wire, -1);

/**
* Copies the shortcuts over to the shortcuts list.
*/
void assignShortcut(int index, char *keys) {
    for (int i = 0; i < SHORTCUT_MAX_STROKES; i++) {
        if (i < sizeof(keys)) {
            shortcuts[index].keys[i] = keys[i];
        } else {
            shortcuts[index].keys[i] = IGNORE_CHAR;
        }
    }
}

/**
* Sets up all of the shortcuts 
*/
void initShortcuts() {
    //copy shortcut
    shortcuts[0].id = "COPY";
    char copy[] = {
        KEY_LEFT_GUI,
        'C',
        RELEASE_CHAR
    };
    assignShortcut(0, copy);

    shortcuts[1].id = "PASTE";
    char paste[] = {
        KEY_LEFT_GUI,
        'P',
        RELEASE_CHAR
    };
    assignShortcut(1, paste);


    shortcuts[2].id = "SCREEN_LEFT";
    char screenLeft[] = {
        KEY_LEFT_CTRL,
        KEY_LEFT_ARROW,
        RELEASE_CHAR
    };
    assignShortcut(2, screenLeft);

    shortcuts[3].id = "SCREEN_RIGHT";
    char screenRight[] = {
        KEY_LEFT_CTRL,
        KEY_RIGHT_ARROW,
        RELEASE_CHAR
    };
    assignShortcut(3, screenRight);

    shortcuts[4].id = "KEYBOARD_VIEWER";
    char assessibility[] = {
        KEY_LEFT_ALT,
        KEY_LEFT_GUI,
        KEY_F5,
        RELEASE_CHAR
    };
    assignShortcut(4, assessibility);
    
    shortcuts[5].id = "ALL_MENU";
    char allMenu[] = {
        KEY_LEFT_CTRL,
        KEY_UP_ARROW,
        RELEASE_CHAR
    };
    assignShortcut(5, allMenu);

    shortcuts[6].id = "VOL_UP";
    char volumeUp[] = {
        KEY_F12,
        RELEASE_CHAR
    };
    assignShortcut(6, volumeUp);

    shortcuts[7].id = "VOL_DOWN";
    char volumeDown[] = {
        KEY_F11,
        RELEASE_CHAR
    };
    assignShortcut(7, volumeDown);

    shortcuts[8].id = "BRIGHT_UP";
    char brightnessUp[] = {
        KEY_F2,
        RELEASE_CHAR
    };
    assignShortcut(8, brightnessUp);

    shortcuts[9].id = "BRIGHT_DOWN";
    char brightnessDown[] = {
        KEY_F1,
        RELEASE_CHAR
    };
    assignShortcut(9, brightnessDown);

    shortcuts[10].id = "ARR_LEFT";
    char arrowLeft[] = {
        KEY_LEFT_ARROW,
        RELEASE_CHAR
    };
    assignShortcut(10, arrowLeft);

    shortcuts[11].id = "ARR_RIGHT";
    char arrowRight[] = {
        KEY_RIGHT_ARROW,
        RELEASE_CHAR
    };
    assignShortcut(11, arrowRight);

    shortcuts[12].id = "VOL_MUTE";
    char muteVolume[] = {
        KEY_F10,
        RELEASE_CHAR
    };
    assignShortcut(12, muteVolume);

    shortcuts[13].id = "SUB";
    char subLatex[] = {
        '_',
        '{',
        '}',
        KEY_LEFT_ARROW,
        RELEASE_CHAR
    };
    assignShortcut(13, subLatex);

    shortcuts[14].id = "DND";
    char doNotDisturb[] = {
        KEY_F6,
        RELEASE_CHAR
    };
    assignShortcut(14, doNotDisturb);

    shortcuts[15].id = "SAVE";
    char save[] = {
        KEY_LEFT_GUI,
        's',
        RELEASE_CHAR
    };
    assignShortcut(15, save);

    Serial.println("[DEBUG] Created shortcuts.");
}

void setup() {
    //init shortcuts
    initShortcuts();

    //init the pins of the button matrix
    for (int i = 0; i < COLS; i++) {
        pinMode(cols[i], OUTPUT);
        digitalWrite(cols[i], HIGH);
    }

    for (int i = 0; i < ROWS; i++) {
        pinMode(rows[i], INPUT_PULLUP);
    }

    delay(500);

    for (int i = 0; i < NUM_ROTARIES; i += 2) {
        byte clk = rotaries[i];
        byte dt = rotaries[i + 1];

        pinMode(pcfboard, clk, INPUT);
        pinMode(pcfboard, dt, INPUT);

        lastCLKValues[i] = 0;
        currentCLKValues[i] = 0;
        currentDTValues[i] = 0;
        positions[i] = 0;
    }


    Serial.begin(9600);
    Serial.println("[DEBUG] Finished setup!");

    Keyboard.begin();

    Serial.println("[DEBUG] Started keyboard!");

    if (!topDisplay.begin(SSD1306_SWITCHCAPVCC, TOP_DISPLAY)) {
        Serial.println("[DEBUG] Top SSD1306 allocation failed!");

        for (;;);
    }

    if (!botDisplay.begin(SSD1306_SWITCHCAPVCC, BOT_DISPLAY)) {
        Serial.println("[DEBUG] Bot SSD1306 allocation failed!");

        for (;;);
    }

    Serial.println("[DEBUG] LCD Initialization complete!");
}

void loop() {
    //Read all of the buttons
    for (int x = 0; x < COLS; x++) {
        digitalWrite(cols[x], LOW);
        delayMicroseconds(5);

        for (int y = 0; y < ROWS; y++) {
            if (x == ignore[0] && y == ignore[1]) continue;

            if (digitalRead(rows[y]) == LOW) {
                onKeyPress(y, x);

                keysDown[y][x] = true;
            } else if (keysDown[y][x]) {
                onKeyRelease(y, x);

                keysDown[y][x] = false;
            }
        }

        digitalWrite(cols[x],HIGH);
        delayMicroseconds(500);
    }

    //Read all of the rotary
    for (int i = 0; i < NUM_ROTARIES; i += 2) {
        byte clk_p = rotaries[i];
        byte dt_p = rotaries[i + 1];

        int clk = digitalRead(pcfboard, clk_p);

        if (clk != lastCLKValues[i]) {
            int dt = digitalRead(pcfboard, dt_p);

            if (dt != currentDTValues[i]) {
                positions[i] += 1;
            } else {
                positions[i] -= 1;
            }
        }
        
        lastCLKValues[i] = clk;

        if (positions[i] != lastPositions[i]) {
            onRotate(i, lastPositions[i], positions[i]);

            lastPositions[i] = positions[i];
        }
    }
}

void onKeyPress(int row, int col) {
    if (!keysDown[row][col] || !stickyKeys) {
        if (row == 3) {
            pressKey(rotarySwitchLayout[col]);
        } else {
            pressKey(numpadLayouts[currentNumpad][row][col]);
        }
    }
}

void onKeyRelease(int row, int col) {
    if (keysDown[row][col]) {
        if (row == 3) {
            releaseKey(rotarySwitchLayout[col]);
        } else {
            releaseKey(numpadLayouts[currentNumpad][row][col]);
        }
    }
}

void onRotate(int encoder, int last, int knew) {
    if (knew > last) {
        pressKey(rotaryLayouts[encoder][0]);
    } else if (last < knew) {
        pressKey(rotaryLayouts[encoder][1]);
    }

    if (last != knew) {
        if (rotaryLayouts[encoder][0] == "VOL_UP") {
            displayAudio();
        } else if (rotaryLayouts[encoder][0] == "BRIGHT_UP") {
            displayBrightness();
        }
    }
}

void pressKey(String key) {
    for (int i = 0; i < NUM_SHORTCUTS; i++) {
        //if the key is a shortcut
        if (shortcuts[i].id == key) {
            bool rlFlag = false;
            //loop through and press the keys
            for (int j = 0; j < SHORTCUT_MAX_STROKES; j++) {
                char key = shortcuts[i].keys[j];
                if (key == IGNORE_CHAR) continue;
                if (key == RELEASE_CHAR) {
                    rlFlag = true;
                    continue;
                }

                Keyboard.press(key);

                //small delay?
                delayMicroseconds(10);
            }
            
            if (rlFlag) {
                //if the release flag is activated, go back and release all of the chars
                for (int j = SHORTCUT_MAX_STROKES - 1; j >= 0; j--) {
                    char key = shortcuts[i].keys[j];
                    if (key == IGNORE_CHAR) continue;
                    if (key == RELEASE_CHAR) continue;

                    Keyboard.release(key);

                    delayMicroseconds(10); //another small delay
                }
            }

            return;
        }
    }

    if (key == "SWITCH") {
        currentNumpad++;
        return;
    } else if (key == "SWITCH_BACK") {
        currentNumpad--;
        return;
    }

    if (currentNumpad < 0) {
        currentNumpad = NUM_NUMPADS - 1;
        handleNumpadChange();
    } else if (currentNumpad >= NUM_NUMPADS) {
        currentNumpad = 0;
        handleNumpadChange();
    }

    //if there's not a shortcut, just press the key itself.
    char L = key.charAt(0);
    Keyboard.press(L);
}

//occurs whenever the current numpad changes, updates the top numpad display to the alias
void handleNumpadChange() {
    topDisplay.clearDisplay();

    topDisplay.setTextSize(2);
    topDisplay.setTextColor(WHITE);
    topDisplay.setCursor(0, 0);
    topDisplay.println(numpadAliases[currentNumpad]);
    topDisplay.display();
}

//0 = bright, 1 = volume
int currentDisplay = -1;

int brightStartLine = 38;
int brightHeight = 43;
const unsigned char PROGMEM bright[] = {
        0b00000000, 0b00000000, 0b00000000, 0b00000000, 
        0b00000000, 0b00000010, 0b00000000, 0b00000000, 
        0b00000000, 0b00000010, 0b00000000, 0b00000000, 
        0b00000000, 0b00000010, 0b00000000, 0b00000000, 
        0b00000000, 0b00000010, 0b00000000, 0b00000000, 
        0b00000000, 0b00000010, 0b00000000, 0b00000000, 
        0b00000000, 0b00000010, 0b00000000, 0b00000000, 
        0b00000000, 0b00000000, 0b00000001, 0b10000000, 
        0b00000000, 0b00000000, 0b00000001, 0b00000000, 
        0b00000000, 0b00000000, 0b00000010, 0b00000000, 
        0b00000000, 0b00000000, 0b00000100, 0b00000000, 
        0b00000000, 0b00000000, 0b00000000, 0b00000000, 
        0b00000000, 0b00000000, 0b00000000, 0b00000000, 
        0b00000000, 0b00000000, 0b00000000, 0b00000000, 
        0b00000000, 0b00000111, 0b11111100, 0b00000000, 
        0b01100000, 0b00011000, 0b00000110, 0b00000000, 
        0b00010000, 0b00100000, 0b00000011, 0b00000000, 
        0b00001000, 0b00100000, 0b00000001, 0b00000000, 
        0b00000100, 0b01000000, 0b00000000, 0b10000000, 
        0b00000000, 0b01000000, 0b00000000, 0b10000000, 
        0b00000000, 0b11000000, 0b00000000, 0b10000000, 
        0b00000001, 0b01000000, 0b00000000, 0b10000000, 
        0b00000001, 0b11000000, 0b00000000, 0b10000010, 
        0b00000000, 0b11000000, 0b00000000, 0b10001110, 
        0b00000000, 0b01000000, 0b00000001, 0b00011000, 
        0b00000000, 0b01000000, 0b00000001, 0b00100000, 
        0b00000000, 0b01000000, 0b00000010, 0b00000000, 
        0b00000000, 0b01000000, 0b00000010, 0b00000000, 
        0b00000000, 0b01000000, 0b00000100, 0b00000000, 
        0b00000000, 0b01000000, 0b00000100, 0b00000000, 
        0b00000000, 0b01000000, 0b00001000, 0b00000000, 
        0b00000010, 0b00100000, 0b00010000, 0b00000000, 
        0b00000010, 0b00100000, 0b00100010, 0b00000000, 
        0b00000010, 0b00011111, 0b11000010, 0b00000000, 
        0b00000100, 0b00000000, 0b00000001, 0b00000000, 
        0b00000100, 0b00000000, 0b00000001, 0b00000000, 
        0b00001000, 0b00000001, 0b00000000, 0b10000000, 
        0b00001000, 0b00000010, 0b00000000, 0b11000000, 
        0b00000000, 0b00000010, 0b00000000, 0b00000000, 
        0b00000000, 0b00000010, 0b00000000, 0b00000000, 
        0b00000000, 0b00000010, 0b00000000, 0b00000000, 
        0b00000000, 0b00000010, 0b00000000, 0b00000000, 
        0b00000000, 0b00000000, 0b00000000, 0b00000000
};

void displayBrightness() {
    if (currentDisplay == 0) return;

    botDisplay.clearDisplay();
    botDisplay.drawBitmap(0, brightStartLine, bright, 32, brightHeight, 1);
    botDisplay.display();
    
    currentDisplay = 0;
}


//volume image
int audioStartLine = 47;
int audioHeight = 29;
const unsigned char PROGMEM audioImage[] = {
        0b00000000, 0b00000000, 0b00000000, 0b00000000, 
        0b00000000, 0b00000111, 0b10000110, 0b00000000, 
        0b00000000, 0b00111000, 0b00000111, 0b00000000, 
        0b00000001, 0b11000000, 0b00000111, 0b10000000, 
        0b00000011, 0b00000000, 0b00000111, 0b11000000, 
        0b00000100, 0b00000001, 0b10000111, 0b11100000, 
        0b00001000, 0b00001110, 0b00000111, 0b11111100, 
        0b00001000, 0b00001000, 0b00000111, 0b11111100, 
        0b00001000, 0b00110000, 0b01000111, 0b11111100, 
        0b00001000, 0b00100001, 0b10000111, 0b11111100, 
        0b00010000, 0b01100001, 0b00000111, 0b11111100, 
        0b00010000, 0b01000110, 0b00110111, 0b11111100, 
        0b00010000, 0b01000100, 0b00100111, 0b11111100, 
        0b00010000, 0b01100100, 0b00100111, 0b11111100, 
        0b00001000, 0b00100100, 0b00100111, 0b11111100, 
        0b00001000, 0b00100100, 0b00100111, 0b11111100, 
        0b00001000, 0b00100010, 0b00000111, 0b11111100, 
        0b00001000, 0b00110011, 0b10000111, 0b11111100, 
        0b00001000, 0b00010000, 0b10000111, 0b11111100, 
        0b00000100, 0b00011000, 0b00000111, 0b11111100, 
        0b00000100, 0b00000111, 0b00000111, 0b11111100, 
        0b00000100, 0b00000000, 0b00000111, 0b11111100, 
        0b00000010, 0b00000000, 0b00000111, 0b11100000, 
        0b00000001, 0b00000000, 0b00000111, 0b11000000, 
        0b00000000, 0b10000000, 0b00000111, 0b10000000, 
        0b00000000, 0b01111110, 0b00000111, 0b00000000, 
        0b00000000, 0b00000001, 0b00000110, 0b00000000, 
        0b00000000, 0b00000000, 0b00000100, 0b00000000, 
        0b00000000, 0b00000000, 0b00000000, 0b00000000
};

void displayAudio() {
    if (currentDisplay == 1) return;

    botDisplay.clearDisplay();
    botDisplay.drawBitmap(0, audioStartLine, audioImage, 32, audioHeight, 1);
    botDisplay.display();

    currentDisplay = 1;
}

void releaseKey(String key) {
    for (int i = 0; i < NUM_SHORTCUTS; i++) {
        if (shortcuts[i].id == key) {
            //loop through and release the keys
            for (int j = SHORTCUT_MAX_STROKES - 1; j >= 0; j--) {
                char key = shortcuts[i].keys[j];
                if (key == IGNORE_CHAR) continue;
                if (key == RELEASE_CHAR) {
                    //ignore releasing, since the keys should have already been released.
                    break;
                }

                Keyboard.release(key);
            }

            return;
        }
    }

    //Release the char 
    char L = key.charAt(0);
    Keyboard.release(L);
}
