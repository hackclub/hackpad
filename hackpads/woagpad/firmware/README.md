# RMK 

RMK is a feature-rich and easy-to-use keyboard firmware.

## Use the template

1. Install [probe-rs](https://github.com/probe-rs/probe-rs)

   ```shell
   # Linux/macOS
   curl --proto '=https' --tlsv1.2 -LsSf https://github.com/probe-rs/probe-rs/releases/latest/download/probe-rs-tools-installer.sh | sh

   # Windows
   irm https://github.com/probe-rs/probe-rs/releases/latest/download/probe-rs-tools-installer.ps1 | iex
   ```

2. Build the firmware

   ```shell
   cargo build --release
   ```

3. Flash using debug probe

   If you have a debug probe connected to your rp2040 board, flashing is quite simple: run the following command to automatically compile and flash RMK firmware to the board:

   ```shell
   cargo run --release
   ```

4. (Optional) Flash using USB

   If you don't have a debug probe, you can use `elf2uf2-rs` to flash your rp2040 firmware via USB. There are several additional steps you have to do:

   1. Install `elf2uf2-rs`: `cargo install elf2uf2-rs`
   2. Update `.cargo/config.toml`, use `elf2uf2` as the flashing tool
      ```diff
      - runner = "probe-rs run --chip RP2040"
      + runner = "elf2uf2-rs -d"
      ```
   3. Connect your rp2040 board holding the BOOTSEL key, ensure that rp's USB drive appears
   4. Flash
      ```shell
      cargo run --release
      ```
      Then, you will see logs like if everything goes right:
      ```shell
      Finished release [optimized + debuginfo] target(s) in 0.21s
      Running `elf2uf2-rs -d 'target\thumbv6m-none-eabi\release\rmk-rp2040'`
      Found pico uf2 disk G:\
      Transfering program to pico
      173.00 KB / 173.00 KB [=======================] 100.00 % 193.64 KB/s  
      ```