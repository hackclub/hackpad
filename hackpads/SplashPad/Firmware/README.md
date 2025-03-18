# KMK Firmware – SplashPad

### The Brains Behind My Macropad

This folder contains the **KMK firmware** for my **SplashPad**.

---

## What's over here? 
- **`kb.py`** – Defines the hardware setup: key matrix, rotary encoder, LED setup, and pin assignments.
- **`main.py`** – The actual firmware logic: key mappings, rotary encoder functions, LED effects, and main loop.

---

## Default Keymap  
| Row   | Key 1  | Key 2      | Key 3           |
|-------|--------|------------|-----------------|
| **1** | Rewind | Play/Pause | Fast Forward    |
| **2** | Media  | Calculator | Cmd+R (Run)     |
| **3** | Left   | Right      | Cmd+L (Lock)    |

- **Rotary Encoder:**  
  - **Left** → Volume Down
  - **Right** → Volume Up
  - **Press** → Cycle LED Modes

---

## LED Modes  
- **Solid Mode** – A slow pulsing blue glow.
- **Rainbow Mode** – Cycling RGB for that *gamer aesthetic*.
- **Wave Mode** – Water flow effect (because vibes).
- **Grid Fade Mode** – A subtle pulsing effect inspired by sunlight through water.

*(Press the encoder button to switch modes.)*