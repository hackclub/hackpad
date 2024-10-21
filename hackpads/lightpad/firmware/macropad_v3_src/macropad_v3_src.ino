/*
* ---------------------------------
*  
*           MACROPAD V3
*
* ---------------------------------
*/

/*
* This is a macropad which has 16 buttons in a standard matrix, + 3 encoder switches
* also in the matrix. The matrix is controlled via a  MCP23017_SP IO extender. 
* Alongside this, there is an oled display (i2c), 3 EC11 rotary encoders, and 
* an array of neopixels (ws2812b), all wired directly to the microcontroller (seeed studio xiao rp2040)
*
* I am using the midi over serial library, so need additional software (hairless midi + loopMidi), but qmk seems like a pain with the io expander lol.
* 
* NOTE - OLED is not yet implemented, as I do not know the specific model / brand
*
* When I inevitably forget how my matrix is wired, refer to this:
* https://electronics.stackexchange.com/questions/562412/4x4-keyboard-matrix-why-no-pull-down-resistors
*
*/

#include <Wire.h>
#include <MCP23017.h>
#include <Adafruit_NeoPixel.h>
#include <MIDI.h>
#include <Bounce2.h>

/**** NEOPIXELS ****/

#define NUMPIXELS 16
const int NEOPIXEL_PIN = A0;
Adafruit_NeoPixel pixels(NUMPIXELS, NEOPIXEL_PIN, NEO_GRB + NEO_KHZ800);


/**** ENCODERS ****/
#define NUMENCODERS 3

const int ENCODER_PIN_A[NUMENCODERS] = { 1, 3, 7 };  //GP28 GP29 GP1
const int ENCODER_PIN_B[NUMENCODERS] = { 3, 6, 9 };  //GP29 GP0 GP4

int encoder_value_a[NUMENCODERS];  // current values of pin a's
int encoder_value_b[NUMENCODERS];  // current values of pin b's

bool encoder_moving[NUMENCODERS];  // whether the encoder is moving or not

int encoder_gross_count[NUMENCODERS] = { 0 };       // total encoder steps
int encoder_net_count[NUMENCODERS] = { 0 };         // cw-ccw
int encoder_full_revolutions[NUMENCODERS] = { 0 };  // num of full revolutions
int encoder_surplus_steps[NUMENCODERS] = { 0 };     // part revs
bool CW[NUMENCODERS];

byte encoder_cycles_per_rev = 30;  //DOUBLE CHECK THIS LATER, COULD BE 18, 30, 36

// Encoder Debouncing
Bounce encoder_debouncers_a[NUMENCODERS] = { Bounce(), Bounce(), Bounce() };
Bounce encoder_debouncers_b[NUMENCODERS] = { Bounce(), Bounce(), Bounce() };


/**** KEY MATRIX ****/
#define MATRIXROWS 5
#define MATRIXCOLUMNS 4

const int MATRIX_PIN_ROWS[MATRIXROWS] = { 3, 2, 1, 0, 4 };
const int MATRIX_PIN_COLUMNS[MATRIXCOLUMNS] = { 8, 9, 10, 11 };

int button_c_state[MATRIXCOLUMNS][MATRIXROWS] = {};  // current button state
int button_p_state[MATRIXCOLUMNS][MATRIXROWS] = {};  // previous button state

// matrix debouncing
unsigned long last_debounce_time[MATRIXCOLUMNS][MATRIXROWS] = { 0 };  // the last time the button was pressed
unsigned long debounce_delay = 50;                                    // Debounce time


/**** MIDI ****/
MIDI_CREATE_DEFAULT_INSTANCE();

// Encoder
int encoder_midi_value[NUMENCODERS] = { 0 };
int encoder_midi_cc[NUMENCODERS] = { 1, 2, 3 };
int encoder_midi_channel = 1;

// Buttons
int button_midi_note[MATRIXCOLUMNS][MATRIXROWS] = {
  { 36, 40, 44, 48, 52 },
  { 37, 41, 45, 49, 53 },
  { 38, 42, 46, 50, 54 },
  { 39, 43, 47, 51, 55 },
};
int button_midi_channel = 1;

/**** IO EXPANDER ****/
#define MCP23017_ADDR 0x20
MCP23017 mcp = MCP23017(MCP23017_ADDR);

void setup() {
  // put your setup code here, to run once:
  Wire.begin();
  Serial.begin(115200);

  // Init the io expander
  mcp.init();

  // set the pin modes of all pins
  setPinModes();

  // Neopixels
  pixels.begin();  // init neopixel strip object
  pixels.clear();  // clear colors
  for (int i = 0; i < NUMPIXELS; i++) {
    pixels.setPixelColor(i, pixels.Color(0, 125, 0));
  }
  pixels.show();
}

void loop() {
  // put your main code here, to run repeatedly:
  encoders();
  keyMatrix();
}

void setPinModes() {
  // ENCODERS
  for (int pin : ENCODER_PIN_A) {
    pinMode(pin, INPUT_PULLUP);
  }

  for (int pin : ENCODER_PIN_B) {
    pinMode(pin, INPUT_PULLUP);
  }

  for (int i = 0; i < NUMENCODERS; i++) {
    encoder_debouncers_a[i].attach(ENCODER_PIN_A[i]);
    encoder_debouncers_a[i].interval(5);
  }

  for (int i = 0; i < NUMENCODERS; i++) {
    encoder_debouncers_b[i].attach(ENCODER_PIN_B[i]);
    encoder_debouncers_b[i].interval(5);
  }

  // Matrix
  for (int pin : MATRIX_PIN_ROWS) {
    mcp.pinMode(pin, OUTPUT);
  }
  for (int pin : MATRIX_PIN_COLUMNS) {
    mcp.pinMode(pin, INPUT_PULLUP);
  }
}


void encoders() {
  // Update the debouncers
  updateEncoderDebounce();
  // Read the encoder switches (not the button, the other ones)
  readEncoderDebounce();
  // Determine direction and update counter + send midi
  updateEncoderCounter();
}

void updateEncoderDebounce() {
  // A Debouncers
  for (Bounce debouncer : encoder_debouncers_a) {
    debouncer.update();
  }
  // B Debouncers
  for (Bounce debouncer : encoder_debouncers_b) {
    debouncer.update();
  }
}

void readEncoderDebounce() {
  // Read A Debouncers
  for (int i = 0; i < NUMENCODERS; i++) {
    encoder_value_a[i] = encoder_debouncers_a[i].read();
  }
  // Read B Debouncers
  for (int i = 0; i < NUMENCODERS; i++) {
    encoder_value_b[i] = encoder_debouncers_b[i].read();
  }
}

void updateEncoderCounter() {
  /*
  the possibilites are, where A = high a, b = low b, etc.:
   AB: in a detent
   if just arrived, update counter, clear motiondetected
   otherwise do nothing
   Ab: start of CW or end of CCW
   if start, set CW bool and set motionDetected
   if at end (know becasue motionDetected already set), do nothing
   aB: start of CCW or end of CW
   if start, clear CW bool and set motionDetected
   if at end (know becasue motionDetected already set), do nothing
   ab: in middle of either CW or CCW, do nothing
   */
  for (int i = 0; i < NUMENCODERS; i++) {
    if (encoder_value_a[i] && encoder_value_b[i] && encoder_moving[i])  // In a detent and just arrived
    {
      if (CW[i]) {
        encoder_gross_count[i] = encoder_gross_count[i] + 1;
        encoder_net_count[i] = encoder_net_count[i] + 1;
        // Update Midi
        encoder_midi_value[i] = constrain(encoder_midi_value[i] + 1, 0, 127);
        // Send Control Change
        MIDI.sendControlChange(encoder_midi_cc[i], encoder_midi_value[i], encoder_midi_channel);
      } else  //CCW
      {
        encoder_gross_count[i] = encoder_gross_count[i] + 1;
        encoder_net_count[i] = encoder_net_count[i] - 1;
        // Update Midi
        encoder_midi_value[i] = constrain(encoder_midi_value[i] - 1, 0, 127);
        // Send Control Change
        MIDI.sendControlChange(encoder_midi_cc[i], encoder_midi_value[i], encoder_midi_channel);
      }
      encoder_moving[i] = false;
      encoder_full_revolutions[i] = encoder_net_count[i] / encoder_cycles_per_rev;
      encoder_surplus_steps[i] = encoder_net_count[i] % encoder_cycles_per_rev;
    }

    if (encoder_value_a[i] && !encoder_value_b[i] && !encoder_moving[i])  // just started cw
    {
      CW[i] = true;
      encoder_moving[i] = true;
    }

    if (!encoder_value_a[i] && encoder_value_b[i] && !encoder_moving[i])  // just started ccw
    {
      CW[i] = false;
      encoder_moving[i] = true;
    }
  }
}


void keyMatrix() {
  /*
  * To read a key, pull one row low, all other rows high
  * then read column, run a debouncer on all keys.
  * I'm doing the order of a column at a time
  * e.g, column 1, rows 1-5, then column 2, rows 1-5 etc.
  */
  readMatrix();
  // more to come later
}

void readMatrix() {
  // init by setting all rows high
  for (int row_pin : MATRIX_PIN_ROWS) {
    mcp.digitalWrite(row_pin, HIGH);
  }

  // scan the matrix and update c state
  for (int x = 0; x < MATRIXCOLUMNS; x++) {
    for (int y = 0; y < MATRIXROWS; y++) {
      // pull the row we want to read low
      mcp.digitalWrite(MATRIX_PIN_ROWS[y], LOW);
      // read the associated column and store its value
      button_c_state[x][y] = mcp.digitalRead(MATRIX_PIN_COLUMNS[x]);
      // reset the row to idle at high
      mcp.digitalWrite(MATRIX_PIN_ROWS[y], HIGH);
      // debounce
      if ((millis() - last_debounce_time[x][y]) > debounce_delay) {
        // if state is different
        if (button_p_state[x][y] != button_c_state[x][y]) {
          // reset debounce timer
          last_debounce_time[x][y] = millis();
          // if button is low, send note on
          if (button_c_state[x][y] == LOW) {
            MIDI.sendNoteOn(button_midi_note[x][y], 127, button_midi_channel);
          } else  // note off
          {
            MIDI.sendNoteOff(button_midi_note[x][y], 0, button_midi_channel);
          }
        }
      }
    }
  }
}