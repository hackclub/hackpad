MCU = RP2040
ARCH = arm

OLED_ENABLE = yes
OLED_TRANSPORT = i2c
OLED_DRIVER = ssd1306


# Encoders
ENCODER_ENABLE = yes
ENCODER_MAP_ENABLE = yes


# required for rp2040
LTO_ENABLE = yes


# Custom matrix
SRC += matrix.c
CUSTOM_MATRIX = yes


I2C_DRIVER_REQUIRED = yes



#CFLAGS += -I"C:\QMK_MSYS\mingw64\avr\include"

# For ARM target
CFLAGS += -I$(TOOLCHAIN_ARM_PATH)/arm-none-eabi/include




# Silence random warnings
CFLAGS += -Wno-pointer-to-int-cast
CFLAGS += -Wno-error=int-to-pointer-cast

CFLAGS += -Wno-error=attributes