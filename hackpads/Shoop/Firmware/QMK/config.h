// Copyright 2023 QMK
// SPDX-License-Identifier: GPL-2.0-or-later

#define ENCODER_A_PINS { GP0 }
#define ENCODER_B_PINS { GP1 }

#pragma once

#define MATRIX_ROWS 2
#define MATRIX_COLS 4

// Set number of encoders if applicable
#define NUM_ENCODERS 2

// Define other configurations here as needed
#define ENCODER_RESOLUTION 4

// If you're using layers, set the max layer
#define MAX_LAYER 4
