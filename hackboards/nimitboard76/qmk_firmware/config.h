#ifdef OLED_ENABLE
#define OLED_DISPLAY_128X32
#define OLED_TIMEOUT 30000  // Turns off OLED after 30 seconds of inactivity
#define OLED_BRIGHTNESS 120
#endif
#define I2C1_SDA_PIN GP8
#define I2C1_SCL_PIN GP9
#define I2C1_CLOCK_SPEED 400000

#define NUM_ENCODERS 1
#define ENCODER_RESOLUTION 4
