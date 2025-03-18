#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <Keypad.h>
#include <hardware/regs/sysinfo.h>
#include <hardware/structs/sysinfo.h>
#include <pico/bootrom.h>

// OLED display settings
#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET -1  // No reset pin

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

// Keypad settings
const byte ROWS = 4; // four rows
const byte COLS = 4; // four columns

// Define the connections to the row and column pins
byte rowPins[ROWS] = {7, 6, 5, 4};  // rows
byte colPins[COLS] = {11, 10, 9, 8};  // columns 

// Define the keys on the keypad
char keys[ROWS][COLS] = {
  {'7', '8', '9', '+'},
  {'4', '5', '6', '-'},
  {'1', '2', '3', '*'},
  {'.', '0', '/', 'E'}  // 'E' for 'enter' key 
};

Keypad keypad = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

String inputString = "";  // To store the sequence of key inputs
bool calculatorMode = true;  // Start in calculator mode

void setup() {
  // Initialize serial communication
  Serial.begin(115200);

  // Initialize the OLED display, if fails, stop program
  if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    Serial.println(F("SSD1306 allocation failed"));
    for (;;);  // Halt the program
  }

  // Show that it's working
  display.clearDisplay();
  display.setTextSize(2);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(0, 10);
  display.println("Welcome :D");
  display.display();  // Update the screen
}

void loop() {
  // Check if a key is pressed
  char key = keypad.getKey();
  
  if (key) {
    // Press '7', '8', and '9' to switch modes
    if (key == '7' && keypad.getKey() == '8' && keypad.getKey() == '9') {
      calculatorMode = !calculatorMode;  // Toggle between modes
      updateDisplayMode();
      return;
    }

    // Press '*' and '/' to enter bootloader mode
    if (key == '*' && keypad.getKey() == '/') {
      enterBootloader();  // Enter bootloader mode
    }

    if (calculatorMode) {
      // In Calculator Mode
      handleCalculatorMode(key);
    } else {
      // In Macro Mode
      handleMacroMode(key);
    }
  }
}

void updateDisplayMode() {
  // Update the display to show current mode
  display.clearDisplay();
  display.setTextSize(2);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(0, 10);
  if (calculatorMode) {
    display.println("Calculator Mode");
  } else {
    display.println("Macro Mode");
  }
  display.display();  // Update the screen

  // Display mode for 5 seconds
  delay(5000);

  // Clear display after 5 seconds
  display.clearDisplay();
  display.display();
}

void handleCalculatorMode(char key) {
  // In calculator mode: Launch calculator app if + and - is pressed
  if (key == '+' && key == '-') {
    launchCalculator();
  } else if (key == 'E') {
    Serial.println();  // Simulate Enter by printing a new line
  } else {
    Serial.println(key);  // Print the pressed key
  }
}

void handleMacroMode(char key) {
  // Handle keys in macro mode (define macros here as needed)
  if (key == 'E') {
    Serial.println();  // Simulate Enter in macro mode
  } else if(key == '7'){
    
  } else {
    inputString += key;
    Serial.println(key);  // Print the pressed key to serial monitor
  }
}

void launchCalculator() {
  // Launch the calculator app (Windows example, replace with other OS commands if needed)
  system("calc");  // This will open the calculator on a Windows system
}

void enterBootloader() {
  reset_usb_boot(0, 0);  // Enter bootloader mode
}
