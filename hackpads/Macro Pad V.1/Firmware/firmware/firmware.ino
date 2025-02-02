#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <Adafruit_NeoPixel.h>
#include <Encoder.h>
#include <TimeLib.h>

// Pin definitions
#define ENCODER_A_PIN  0   // D0 (GP0) Volume Encoder A
#define ENCODER_B_PIN  1   // D1 (GP1) Volume Encoder B
#define LED_ENC_A_PIN  2   // D2 (GP2) LED Encoder A
#define LED_ENC_B_PIN  3   // D3 (GP3) LED Encoder B
#define SWITCH1_PIN    6   // D6 (GP6) Switch 1 (Ctrl+A)
#define SWITCH2_PIN    7   // D7 (GP7) Switch 2 (Ctrl+C)
#define SWITCH3_PIN    8   // D8 (GP8) Switch 3 (Ctrl+V)
#define LED_PIN         9   // D9 (GP9) LED Data In

// OLED display size
#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64

// I2C address for SSD1306
#define OLED_I2C_ADDR 0x3C  // Common address for 128x64 OLED displays

// Initialize OLED display
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);

// Initialize LED strip (using NeoPixel library)
Adafruit_NeoPixel strip = Adafruit_NeoPixel(1, LED_PIN, NEO_GRB + NEO_KHZ800);

// Initialize encoders
Encoder volumeEncoder(ENCODER_A_PIN, ENCODER_B_PIN);
Encoder ledEncoder(LED_ENC_A_PIN, LED_ENC_B_PIN);

// Variables for controlling LED brightness and volume
int ledBrightness = 128;   // LED brightness (0 to 255)
int volumeLevel = 50;      // Volume level (0 to 100)

// Last encoder positions
long lastVolumePos = -999;
long lastLedPos = -999;

// Variables for switches and color adjustments
bool switch1State = false;  // Ctrl+A
bool switch2State = false;  // Ctrl+C
bool switch3State = false;  // Ctrl+V
bool randomColor = false;   // Flag for random color mode

void setup() {
  // Initialize serial monitor
  Serial.begin(115200);

  // Initialize OLED display
  if (!display.begin(SSD1306_SWITCHCAPVCC, OLED_I2C_ADDR)) {
    Serial.println(F("SSD1306 allocation failed"));
    while (true);  // Infinite loop if initialization fails
  }
  display.clearDisplay();
  display.setTextColor(SSD1306_WHITE);
  display.setTextSize(1);

  // Initialize LED strip
  strip.begin();
  strip.setBrightness(ledBrightness);
  strip.show();

  // Set switch pins as input
  pinMode(SWITCH1_PIN, INPUT_PULLUP);
  pinMode(SWITCH2_PIN, INPUT_PULLUP);
  pinMode(SWITCH3_PIN, INPUT_PULLUP);

  // Set encoder pins as input
  pinMode(ENCODER_A_PIN, INPUT);
  pinMode(ENCODER_B_PIN, INPUT);

  // Set time (you can update this with a real-time clock module if desired)
  setTime(12, 0, 0, 1, 2, 2025);  // Set to 12:00 PM, Feb 1, 2025
}

void loop() {
  // Check switch states
  switch1State = digitalRead(SWITCH1_PIN) == LOW;
  switch2State = digitalRead(SWITCH2_PIN) == LOW;
  switch3State = digitalRead(SWITCH3_PIN) == LOW;

  // Update the volume encoder
  long volumePos = volumeEncoder.read();
  if (volumePos != lastVolumePos) {
    volumeLevel = constrain(map(volumePos, 0, 1000, 0, 100), 0, 100);
    lastVolumePos = volumePos;
  }

  // Update the LED encoder (for brightness)
  long ledPos = ledEncoder.read();
  if (ledPos != lastLedPos) {
    ledBrightness = constrain(map(ledPos, 0, 1000, 0, 255), 0, 255);
    strip.setBrightness(ledBrightness);
    strip.show();
    lastLedPos = ledPos;
  }

  // Update OLED display
  display.clearDisplay();
  display.setCursor(0, 0);
  display.print("Time: ");
  display.print(hour());
  display.print(":");
  display.print(minute());
  display.print(":");
  display.print(second());
  display.setCursor(0, 16);
  display.print("Volume: ");
  display.print(volumeLevel);
  display.setCursor(0, 32);
  display.print("Brightness: ");
  display.print(ledBrightness);

  // Color adjustment (random color or set color)
  if (switch1State) {
    randomColor = false;
    strip.setPixelColor(0, strip.Color(255, 0, 0)); // Red color
  } else if (switch2State) {
    randomColor = false;
    strip.setPixelColor(0, strip.Color(0, 255, 0)); // Green color
  } else if (switch3State) {
    randomColor = !randomColor;
  }

  if (randomColor) {
    // Generate random color
    int r = random(0, 256);
    int g = random(0, 256);
    int b = random(0, 256);
    strip.setPixelColor(0, strip.Color(r, g, b)); // Random color
  }

  strip.show();
  display.display();

  delay(100);  // Update screen and strip every 100 ms
}
