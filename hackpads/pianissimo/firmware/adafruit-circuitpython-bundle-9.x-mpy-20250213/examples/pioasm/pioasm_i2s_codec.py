# SPDX-FileCopyrightText: 2024 Tim Chinowsky
# SPDX-License-Identifier: MIT

import array
import board
import rp2pio

import adafruit_pioasm

# Implement extended multichannel I2S interface like that used by audio codecs
# such as the TAC5212.  In extended I2S, "Left" and "Right" can each contain
# multiple channels, so for instance 8 channels of audio can be sent as a "left"
# containing 4 channels and a "right" containing 4 channels.

# In this implementation the number of bits per sample, sample rate, and
# number of channels can be independently specified.  The number of channels must
# be even, to divide evenly between left and right.

# Ramped test data containing the requested number of sample sets (one set = one
# sample for each channel) and spanning the specified number of bits will be generated
# and sent out over I2S on the specified pins.

# Data will be preceded and followed by a set of zeros for convenience.
# (Some protocol analyzers have trouble analyzing serial data at the the beginning
# and end of a data set)

# At the same time that I2S data is sent out the out_pin, I2S data will be received
# on the in_pin.  If the output is looped back (connected) to the input, the data
# received should be the same as the data sent.

# Some samples run in loopback configuration:

# bits per sample: 16
#     sample rate: 48000
#        channels: 4
#     sample sets: 4

# actual sample frequency   47984.6 Hz
#               bit clock 3071017.0 Hz

# write: 00000000  00000000  00000000  00000000
#  read: 00000000  00000000  00000000  00000000

# write: 00000000  00001111  00002222  00003333
#  read: 00000000  00001111  00002222  00003333

# write: 00004444  00005555  00006666  00007777
#  read: 00004444  00005555  00006666  00007777

# write: 00008888  00009999  0000aaaa  0000bbbb
#  read: 00008888  00009999  0000aaaa  0000bbbb

# write: 0000cccc  0000dddd  0000eeee  0000ffff
#  read: 0000cccc  0000dddd  0000eeee  0000ffff

# write: 00000000  00000000  00000000  00000000
#  read: 00000000  00000000  00000000  00000000

# bits per sample: 24
#     sample rate: 24000
#        channels: 8
#     sample sets: 5

# actual sample frequency   23987.7 Hz
#               bit clock 4605642.0 Hz

# write: 00000000  00000000  00000000  00000000  00000000  00000000  00000000  00000000
#  read: 00000000  00000000  00000000  00000000  00000000  00000000  00000000  00000000

# write: 00000000  00069069  000d20d2  0013b13b  001a41a4  0020d20d  00276276  002df2df
#  read: 00000000  00069069  000d20d2  0013b13b  001a41a4  0020d20d  00276276  002df2df

# write: 00348348  003b13b1  0041a41a  00483482  004ec4ec  00555554  005be5be  00627626
#  read: 00348348  003b13b1  0041a41a  00483482  004ec4ec  00555554  005be5be  00627626

# write: 00690690  006f96f8  00762762  007cb7ca  00834834  0089d89c  00906904  0096f96c
#  read: 00690690  006f96f8  00762762  007cb7ca  00834834  0089d89c  00906904  0096f96c

# write: 009d89d8  00a41a40  00aaaaa8  00b13b10  00b7cb7c  00be5be4  00c4ec4c  00cb7cb4
#  read: 009d89d8  00a41a40  00aaaaa8  00b13b10  00b7cb7c  00be5be4  00c4ec4c  00cb7cb4

# write: 00d20d20  00d89d88  00df2df0  00e5be58  00ec4ec4  00f2df2c  00f96f94  00ffffff
#  read: 00d20d20  00d89d88  00df2df0  00e5be58  00ec4ec4  00f2df2c  00f96f94  00ffffff

# write: 00000000  00000000  00000000  00000000  00000000  00000000  00000000  00000000
#  read: 00000000  00000000  00000000  00000000  00000000  00000000  00000000  00000000


def i2s_codec(  # pylint: disable=too-many-arguments
    channels=2,
    sample_rate=48000,
    bits=16,
    bclk_pin=None,
    out_pin=None,
    in_pin=None,
):
    i2s_clock = sample_rate * channels * bits
    pio_clock = 4 * i2s_clock
    pio_code = """
        .program i2s_codec
        .side_set 2
                            ; at program start we initialize the bit count top
                            ; (which may be >32) with data
                            ; pulled from the input fifo
            pull noblock    ; first empty the input fifo
            pull noblock
            pull noblock
            pull noblock
            out null, 32    ; then clear OSR so we can get a new value
            pull block      ; then get the bit count top value from the fifo
                            ;        /--- LRCLK
                            ;        |/-- BCLK
                            ;        ||
            mov x, osr;       side 0b01 [1] ; save it in x
            out null, 32      side 0b00 [1]
            mov y, x          side 0b01 [1] ; start of main loop (wrap target=8)
        bitloop1:
            out pins 1        side 0b00
            in pins 1         side 0b00
            jmp y-- bitloop1  side 0b01 [1]
            out pins 1        side 0b10
            in pins 1         side 0b10
            mov y, x          side 0b11 [1]
        bitloop0:
            out pins 1        side 0b10
            in pins 1         side 0b10
            jmp y-- bitloop0  side 0b11 [1]
            out pins 1        side 0b00
            in pins 1         side 0b00
    """
    pio_params = {
        "frequency": pio_clock,
        "first_out_pin": out_pin,
        "first_in_pin": in_pin,
        "first_sideset_pin": bclk_pin,
        "sideset_pin_count": 2,
        "auto_pull": True,
        "auto_push": True,
        "out_shift_right": False,
        "in_shift_right": False,
        "pull_threshold": bits,
        "push_threshold": bits,
        "wait_for_txstall": False,
        "wrap_target": 8,
    }
    pio_instructions = adafruit_pioasm.assemble(pio_code)
    i2s_clock = sample_rate * channels * bits
    pio_clock = 4 * i2s_clock
    pio = rp2pio.StateMachine(pio_instructions, **pio_params)
    return pio


def spaced_samples(length, bits):
    max_int = (1 << bits) - 1
    if length == 1:
        return [0]
    step = max_int / (length - 1)
    result = [round(i * step) for i in range(length)]
    result[0] = 0
    result[-1] = max_int
    return result


while True:
    print()
    BITS = int(input("# bits per sample: "))
    SAMPLE_RATE = int(input("#     sample rate: "))
    CHANNELS = int(input("#        channels: "))
    SAMPLE_SETS = int(input("#     sample sets: "))

    n_samples = CHANNELS * SAMPLE_SETS
    buffer_type = "L"
    buffer_width = 32
    data = [0] * CHANNELS + spaced_samples(n_samples, BITS) + [0] * CHANNELS
    # initialize pio bit count top value by sending it at the start of output data
    bit_count_top = BITS * (CHANNELS // 2) - 2
    buffer_out = array.array(
        buffer_type, [bit_count_top] + [d << (buffer_width - BITS) for d in data]
    )
    buffer_in = array.array(buffer_type, [0] * len(data))

    PIO = i2s_codec(
        channels=CHANNELS,
        bits=BITS,
        sample_rate=SAMPLE_RATE,
        out_pin=board.D9,
        in_pin=board.D10,
        bclk_pin=board.D5,  # L/R signal will be one pin higher, i.e. D6
    )
    print()
    print(f"# actual sample frequency {PIO.frequency/4/CHANNELS/BITS:9.1f} Hz")
    print(f"#               bit clock {PIO.frequency/4:9.1f} Hz")
    print()
    PIO.write_readinto(buffer_out, buffer_in)
    start = 0
    line_length = CHANNELS

    while start < len(buffer_in):
        print("# write: ", end="")
        for i in range(start, min(len(data), start + line_length)):
            print(f"{data[i]:0{buffer_width/4}x} ", end=" ")
        print()
        print("#  read: ", end="")
        for i in range(start, min(len(buffer_in), start + line_length)):
            print(f"{buffer_in[i]:0{buffer_width/4}x} ", end=" ")
        print()
        print()
        start += line_length
    PIO.deinit()
    del PIO
