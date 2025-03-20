#include <Adafruit_SSD1306.h>
#include <Adafruit_GFX.h>
#include "pio_encoder.h"

#define SCREEN_WIDTH 128  // OLED display width, in pixels
#define SCREEN_HEIGHT 64  // OLED display height, in pixels

#define SCREEN_ADDRESS 0x3C  ///< See datasheet for Address; 0x3D for 128x64, 0x3C for 128x32
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);

PioEncoder encoder(3);

#define COL0 26
#define COL1 27
#define ROW0 28
#define ROW1 29

bool invert = false;

String menuTitle = "title";
String listItems[14] = {
  "a",
  "b",
  "c",
  "d",
  "e",
  "f",
  "g",
  "h",
  "i",
  "j",
  "k",
  "l",
  "m",
  "n"
};

bool buttonPress() {
  digitalWrite(COL1, HIGH);
  if (digitalRead(ROW1) == HIGH) {
    // while (digitalRead(ROW1) == HIGH) { ; }  // wait for release to do stuff
    digitalWrite(COL1, LOW);
    return true;
  }
  digitalWrite(COL1, LOW);
  return false;
}

void drawParameters() {
  display.setCursor(0, 0);
  display.setTextSize(2);
  display.print(menuTitle);
  display.setTextSize(1);
  for (int i = 0; i < 14; i++) {
    display.setCursor(0, 8 * i + 16);
    display.print(listItems[i]);
  }
}

void drawButton(bool inv) {
  int y = max(min(16 - 2 * encoder.getCount(), 120), 16);
  if (!inv) {
    display.drawRect(0, y, 64, 8, SSD1306_WHITE);
  } else {
    display.fillRect(0, y, 64, 8, SSD1306_WHITE);
    int id = y / 8 - 2;
    display.setCursor(0, y);
    display.setTextColor(BLACK, WHITE);
    display.print(listItems[id]);
    display.setTextColor(WHITE, BLACK);
  }
}

void displayUpdate() {
  display.clearDisplay();
  display.setTextColor(SSD1306_WHITE);

  drawParameters();
  drawButton(invert);

  display.display();
}

void setup() {
  Serial.begin(115200);

  display.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS);
  display.setRotation(1);
  display.clearDisplay();
  display.display();

  encoder.begin();

  pinMode(COL0, OUTPUT);
  pinMode(COL1, OUTPUT);

  digitalWrite(COL0, LOW);
  digitalWrite(COL1, LOW);

  pinMode(ROW0, INPUT);
  pinMode(ROW1, INPUT);
}

void loop() {
  Serial.println(encoder.getCount());
  displayUpdate();
  if (buttonPress()) {
    invert = true;
  } else {
    invert = false;
  }
}
