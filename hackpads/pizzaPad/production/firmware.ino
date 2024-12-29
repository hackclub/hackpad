#include <Keyboard.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET -1
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

const int keys[] = {0, 1, 2, 3, 9, 10, 6, 7, 8};
const char keyMapping[] = {'1', '2', '3', '4', '5', '6', '7', '8', '9'};

void setup() {
  Keyboard.begin();

  display.begin(SSD1306_I2C_ADDRESS, OLED_RESET);
  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);
  
  for (int i = 0; i < 9; i++) {
    pinMode(keys[i], INPUT_PULLUP);
  }

  display.setCursor(0, 0);
  display.println("pizzaPad Ready!");
  display.display();
}

void loop() {
  for (int i = 0; i < 9; i++) {
    if (digitalRead(keys[i]) == LOW) {
      Keyboard.press(keyMapping[i]);
      delay(100); 
      Keyboard.release(keyMapping[i]);
      display.clearDisplay();
      display.setCursor(0, 0);
      display.print("Pressed: ");
      display.print(keyMapping[i]);
      display.display();
      delay(500);
    }
  }
}
