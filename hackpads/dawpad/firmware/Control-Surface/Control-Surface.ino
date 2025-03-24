#include <Control_Surface.h>
#include <AH/Arduino-Wrapper.h>
#include <AH/Hardware/ExtendedInputOutput/ExtendedInputOutput.hpp>
#include <AH/Hardware/RegisterEncoders.hpp>
#include <Adafruit_MCP23X17.h>
#include <Adafruit_NeoPixel.h>

// MCP configuration
const int MCP_PIN_INTA = 7;
const int MCP_PIN_INTB = 7;

// Encoder pins [A, B]
const int ENCODER_COUNT = 4;
const int ENCODER_PINS[ENCODER_COUNT][2] = {
  {0, 1},
  {2, 3},
  {4, 5},
  {6, 7},
};

// Key matrix
const int MATRIX_ROW_COUNT = 3;
const int MATRIX_COL_COUNT = 4;
const int MATRIX_ROWS[MATRIX_ROW_COUNT] = {
  8,
  9,
  10,
};
const int MATRIX_COLS[MATRIX_COL_COUNT] = {
  11,
  12,
  13,
  14,
};
const MIDIAddress BUTTON_ADDRESSES[3][4] {
  {
    {MIDI_Notes::A[0], Channel_1},
    {MIDI_Notes::B[0], Channel_1},
    {MIDI_Notes::C[0], Channel_1},
    {MIDI_Notes::D[0], Channel_1},
  },
  {
    {MIDI_Notes::E[0], Channel_1},
    {MIDI_Notes::F[0], Channel_1},
    {MIDI_Notes::G[0], Channel_1},
    {MIDI_Notes::A[1], Channel_1},
  },
  {
    {MIDI_Notes::B[1], Channel_1},
    {MIDI_Notes::C[1], Channel_1},
    {MIDI_Notes::D[1], Channel_1},
    {MIDI_Notes::E[1], Channel_1},
  },
};

// Encoder switch pins
const int ENCODER_SW_PINS[4] = {
  0,
  1,
  2,
  3,
};

// LED configuration
const int LED_COUNT = 16;
const int LED_PIN = 6;

//////////

// MIDI interface
USBMIDI_Interface midi;

// Hardware objects
Adafruit_MCP23X17 mcp;
Adafruit_NeoPixel pixels(LED_COUNT, LED_PIN, NEO_GRB + NEO_KHZ800);

// Encoders
using RegisterEncoderType = RegisterEncoders<uint16_t, 4, int32_t, false>;

RegisterEncoderType encs;

void setup() {
  // Set up LEDs
  pixels.begin();

  // Set up the MCP
  if (!mcp.begin_I2C()) {
    // If I2C setup failed, flash the first knob red forever.
    while (true) {
      pixels.setPixelColor(0, pixels.Color(255, 0, 0));
      pixels.show();
      delay(1000);

      pixels.setPixelColor(0, pixels.Color(0, 0, 0));
      pixels.show();
      delay(1000);
    }
  }

  mcp.setupInterrupts(false, false, LOW);

  // Set up the MCP interrupt pins
  pinMode(MCP_PIN_INTA, INPUT);
  pinMode(MCP_PIN_INTB, INPUT);

  // Set up the encoder pins
  for (int encoderIndex = 0; encoderIndex < ENCODER_COUNT; encoderIndex++) {
    for (int pinIndex = 0; pinIndex <= 1; pinIndex++) {
      int pin = ENCODER_PINS[encoderIndex][pinIndex];
      mcp.pinMode(pin, INPUT_PULLUP);
      mcp.setupInterruptPin(pin, CHANGE);
    }
  }
}

void loop() {
  // Read from encoders
  if (!digitalRead(MCP_PIN_INTA)) {
    encs.update(mcp.getCapturedInterrupt());
    delay(100); // Debounce
    mcp.clearInterrupts();
  }

  for (uint8_t row = 0; row < MATRIX_ROW_COUNT; row++) {
    mcp.digitalWrite(MATRIX_ROWS[row], HIGH);

    if (!digitalRead(MCP_PIN_INTB)) {
      uint16_t pins = mcp.getCapturedInterrupt();

      for (uint8_t col = 0; col < MATRIX_COL_COUNT; col++) {
        if (pins & (1 << MATRIX_COLS[col])) {
          midi.sendNoteOn(BUTTON_ADDRESSES[row][col], 0x7F);
        }
      }
    }

    mcp.digitalWrite(row, LOW);
    mcp.clearInterrupts();
  }
}
