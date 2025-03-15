
#define NUM_ENCODERS 1 // Number of encoders
#define ENCODER_A_PINS { GP2 } // A and B pins that are hooked up to the microcontroller
#define ENCODER_B_PINS { GP4 } // Replace these with your values.#define I2C1_SDA_PIN GP6
#define I2C1_SCL_PIN GP7 // Define which pins are SDA and SCL on your microcontroller model.
#define OLED_DISPLAY_128x64 // Set the right resolution
#define OLED_DRIVER_ENABLE

// You may need to add these if the OLED doesn't work at first.

#define OLED_I2C_ADDRESS 0x3C  // or 0x3D, depending on your OLED
#define OLED_DISPLAY_ON 1
