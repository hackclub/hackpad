#include <Wire.h>
#include <Adafruit_MCP23008.h>
#include <Encoder.h>
#include <Adafruit_NeoPixel.h>

#define I2C_ADDRESS 0x20
#define NUM_BUTTONS 16
#define NUM_LEDS 8
#define LED_PIN 0

Encoder encoder1(26, 27);
Encoder encoder2(1, 2);

Adafruit_MCP23008 mcp;
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUM_LEDS, LED_PIN, NEO_GRB + NEO_KHZ800);

long encoder1Position = 0;
long encoder2Position = 0;
int lastButtonState[NUM_BUTTONS] = {0};

void readButtonMatrix() {
  for (int row = 4; row < 8; row++) {
    mcp.pinMode(row, OUTPUT);
    mcp.digitalWrite(row, LOW);
    
    for (int col = 0; col < 4; col++) {
      mcp.pinMode(col, INPUT);
      int buttonIndex = (row - 4) * 4 + col;
      int buttonState = !mcp.digitalRead(col);
      
      if (buttonState != lastButtonState[buttonIndex]) {
        if (buttonState) {
          Serial.print("Bouton appuyé: ");
          Serial.println(buttonIndex);
        } else {
          Serial.print("Bouton relâché: ");
          Serial.println(buttonIndex);
        }
        lastButtonState[buttonIndex] = buttonState;
      }
    }
    
    mcp.digitalWrite(row, HIGH);
  }
}

void setup() {
  Serial.begin(115200);
  
  Wire.begin();
  mcp.begin(I2C_ADDRESS);

  strip.begin();
  strip.show();

  for (int row = 4; row < 8; row++) {
    mcp.pinMode(row, OUTPUT);
    mcp.digitalWrite(row, HIGH);
  }
  for (int col = 0; col < 4; col++) {
    mcp.pinMode(col, INPUT);
  }
}

void loop() {
  readButtonMatrix();

  long newEncoder1Pos = encoder1.read();
  long newEncoder2Pos = encoder2.read();

  if (newEncoder1Pos != encoder1Position) {
    Serial.print("Encoder 1 position: ");
    Serial.println(newEncoder1Pos);
    encoder1Position = newEncoder1Pos;
  }

  if (newEncoder2Pos != encoder2Position) {
    Serial.print("Encoder 2 position: ");
    Serial.println(newEncoder2Pos);
    encoder2Position = newEncoder2Pos;
  }
}
