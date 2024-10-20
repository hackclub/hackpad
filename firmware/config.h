#pragma once

// PCF8574 configuration
#define PCF8574_I2C_ADDRESS 0x20 // Set your I2C address for the PCF8574 here

// Encoder definitions
#define NUM_ENCODERS 2

//#define WS2812_DI_PIN D7
//#define WS2812_DI_PIN (PCF8574_ADDRESS << 1 | 7) // P7 on the PCF8574

// Define the pins for the encoders on PCF8574
// Assuming encoder 1 A and B are connected to PCF8574 pins 0 and 1
#define ENCODER_A_PIN_0 (PCF8574_ADDRESS << 1 | 0)  // PCF8574 pin 0
#define ENCODER_A_PIN_1 (PCF8574_ADDRESS << 1 | 1)  // PCF8574 pin 1
#define ENCODER_B_PIN_0 (PCF8574_ADDRESS << 1 | 3)  // PCF8574 pin 2
#define ENCODER_B_PIN_1 (PCF8574_ADDRESS << 1 | 2)  // PCF8574 pin 3

// Additional configuration for using PCF8574 as encoder inputs
#define ENCODER_ROTARY_0_ENCODER_TYPE PCF8574_ENCODER
#define ENCODER_ROTARY_1_ENCODER_TYPE PCF8574_ENCODER


// SSD1306 OLED display configuration
#define OLED_DRIVER_TYPE SSD1306
#define OLED_I2C_ADDRESS 0x3C // Set your I2C address for the SSD1306 here
#define OLED_DISPLAY_WIDTH 128
#define OLED_DISPLAY_HEIGHT 64

// Other configurations can be added below
//#define RGBLIGHT_LED_COUNT 16 // or however many LEDs you are using


