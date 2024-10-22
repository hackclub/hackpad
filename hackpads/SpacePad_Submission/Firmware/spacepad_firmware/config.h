/* Copyright 2024 Sprext
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program. If not, see <http://www.gnu.org/licenses/>.
 */

#pragma once

// Define the number of rows and columns
#define MATRIX_ROWS 3
#define MATRIX_COLS 4

// Debounce time (in milliseconds)
#define DEBOUNCE 5

// USB polling rate (default is 1ms)
#define USB_POLLING_INTERVAL_MS 1

// Define other features as needed


#include "quantum.h"  // Or QMK_KEYBOARD_H if needed