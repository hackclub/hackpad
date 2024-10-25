#include "quantum.h"

#ifdef RGB_MATRIX_ENABLE
led_config_t g_led_config = {
    {
        // Key Matrix to LED Index
        { 0,  1,  2 },
        { 3,  4,  5 },
        { 6,  7,  8 },
        { 9, 10, 11 }
    },
    {
        // LED Index to Physical Position
        {  0,  0 }, { 56,  0 }, { 112,  0 },
        {  0, 32 }, { 56, 32 }, { 112, 32 },
        {  0, 64 }, { 56, 64 }, { 112, 64 },
        {  0, 96 }, { 56, 96 }, { 112, 96 }
    },
    {
        // LED Index to Flag
        4, 4, 4,
        4, 4, 4,
        4, 4, 4,
        4, 4, 4
    }
};
#endif