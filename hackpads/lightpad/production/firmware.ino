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
*/

#include <Wire.h>
#include <MCP23017.h>
#include <Adafruit_NeoPixel.h>
#include <MIDI.h>
#include <Bounce2.h>

/**** NEOPIXELS ****/
#define NEOPIXEL_PIN D0 // GP26
#define NUMPIXELS 16
Adafruit_NeoPixel pixels(NUMPIXELS, NEOPIXEL_PIN, NEO_GRB + NEO_KHZ800);


/**** ENCODERS ****/
#define NUMENCODERS 3

const int ENCODER_PIN_A[NUMENCODERS] = {1, 3, 7}; //GP28 GP29 GP1
const int ENCODER_PIN_B[NUMENCODERS] = {3, 6, 9}; //GP29 GP0 GP4

int encoder_value_a[NUMENCODERS]; // current values of pin a's
int encoder_value_b[NUMENCODERS]; // current values of pin b's

bool encoder_moving[NUMENCODERS]; // whether the encoder is moving or not

int encoder_gross_count[NUMENCODERS] = {0, 0, 0}; // total encoder steps
int encoder_net_count[NUMENCODERS] = {0, 0, 0}; // cw-ccw
int encoder_full_revolutions[NUMENCODERS] = {0, 0, 0}; // num of full revolutions
int encoder_surplus_steps[NUMENCODERS] = {0, 0, 0};  // part revs
bool CW[NUMENCODERS];

byte encoder_cycles_per_rev = 30; //DOUBLE CHECK THIS LATER, COULD BE 18, 30, 36

// Encoder Debouncing
Bounce encoder_debouncers_a[NUMENCODERS] = {Bounce(), Bounce(), Bounce()};
Bounce encoder_debouncers_b[NUMENCODERS] = {Bounce(), Bounce(), Bounce()};


/**** MIDI ****/
MIDI_CREATE_DEFAULT_INSTANCE(); 

int encoder_midi_values[NUMENCODERS] = {0, 0, 0}
int encoder_midi_cc[NUMENCODERS] = {1, 2, 3}
int encoder_midi_channel = 1

/**** IO EXPANDER ****/
MCP23017 mcp = MCP23017(0x20);

void setup() {
  // put your setup code here, to run once:
  Wire.begin();
  Serial.begin(115200);

  setPinModes();

  // Neopixels
  pixels.begin(); // init neopixel strip object
  pixels.clear(); // clear colors
  for (int i = 0; i < NUMPIXELS; i++) {
    pixels.setPixelColor(i, pixels.Color(0, 125, 0));
  }
  pixels.show();
}

void loop() {
  // put your main code here, to run repeatedly:
  encoders();
}

void setPinModes() {
  // ENCODERS
  for (int pin : ENCODER_PIN_A) {
    pinMode(pin, INPUT_PULLUP);
  }

  for (int pin: ENCODER_PIN_B) {
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


}

void encoders() {
  // Update the debouncers
  updateEncoderDebounce();
  // Read the encoder switches (not the button, the other ones)
  readEncoderDebounce();
  // Determine direction and update counter
  updateEncoderCounter();
  // Output Midi
  outputEncoderMidi();
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
    if(encoder_value_a[i] && encoder_value_b[i] && encoder_moving[i]) // In a detent and just arrived
    {
      if (CW[i])
      {
        encoder_gross_count[i] = encoder_gross_count[i] + 1;
        encoder_net_count[i] = encoder_net_count[i] + 1;
      }
      else //CCW
      {
        encoder_gross_count[i] = encoder_gross_count[i] + 1;
        encoder_net_count[i] = encoder_net_count[i] - 1;
      }
      encoder_moving[i] = false;
      encoder_full_revolutions[i] = encoder_net_count[i] / encoder_cycles_per_rev;
      encoder_surplus_steps[i] = encoder_net_count[i] % encoder_cycles_per_rev;
    }

    if (encoder_value_a[i] && !encoder_value_b[i] && !encoder_moving[i]) // just started cw
    {
      CW[i] = true;
      encoder_moving[i] = true;
    }

    if (!encoder_value_a[i] && encoder_value_b[i] && !encoder_moving[i]) // just started ccw
    {
      CW[i] = false;
      encoder_moving[i] = true;
    }
  }
}

void outputEncoderMidi() {

}