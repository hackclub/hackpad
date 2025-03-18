#pragma once

// Optional: Define the resolution of the encoder
#define ENCODER_RESOLUTION 4

// Direct pin configuration for switches
#define DIRECT_PINS { \
    { GP0, GP26 }, \
    { GP27, GP28 } \
}

// Debounce setting
#define DEBOUNCE 5