#pragma once

#include <stdbool.h>
#include "i2c_master.h"
#define MCP23017_ADD (0x20 << 1)
#define MCP23017_TIMEOUT 200 // milliseconds
#define EXPANDER_PAUSE 0 // microseconds

enum EXPANDER_REGISTERS {
    EXPANDER_REG_IODIRA = 0x00,
    EXPANDER_REG_IODIRB = 0x01,
    EXPANDER_REG_IPOLA = 0x02,
    EXPANDER_REG_IPOLB = 0x03,
    EXPANDER_REG_GPINTENA = 0x04,
    EXPANDER_REG_GPINTENB = 0x05,
    EXPANDER_REG_DEFVALA = 0x06,
    EXPANDER_REG_DEFVALB = 0x07,
    EXPANDER_REG_INTCONA = 0x08,
    EXPANDER_REG_INTCONB = 0x09,
    EXPANDER_REG_IOCONA = 0x0A,
    EXPANDER_REG_IOCONB = 0x0B,
    EXPANDER_REG_GPPUA = 0x0C,
    EXPANDER_REG_GPPUB = 0x0D,
    EXPANDER_REG_INTFA = 0x0E,
    EXPANDER_REG_INTFB = 0x0F,
    EXPANDER_REG_INTCAPA = 0x10,
    EXPANDER_REG_INTCAPB = 0x11,
    EXPANDER_REG_GPIOA = 0x12,
    EXPANDER_REG_GPIOB = 0x13,
    EXPANDER_REG_OLATA = 0x14,
    EXPANDER_REG_OLATB = 0x15
};

#define GPA0 (0x0)
#define GPA1 (0x1)
#define GPA2 (0x2)
#define GPA3 (0x3)
#define GPA4 (0x4)
#define GPA5 (0x5)
#define GPA6 (0x6)
#define GPA7 (0x7)
#define GPB0 (0x8)
#define GPB1 (0x9)
#define GPB2 (0xA)
#define GPB3 (0xB)
#define GPB4 (0xC)
#define GPB5 (0xD)
#define GPB6 (0xE)
#define GPB7 (0xF)

const uint8_t MATRIX_ROW_PINS[MATRIX_ROWS] = { GPB4, GPB7, GPB6, GPB5 };
const uint8_t MATRIX_COL_PINS[MATRIX_COLS] = { GPA4, GPA3, GPA2, GPA1, GPA0 };
// void expander_init(void);
// void expander_select(uint8_t pin);
// void expander_unselect(uint8_t pin);
// void expander_unselect_all(void);

i2c_status_t expander_write(uint8_t pin, uint8_t state);
i2c_status_t expander_read(uint8_t pin, uint8_t *state);
