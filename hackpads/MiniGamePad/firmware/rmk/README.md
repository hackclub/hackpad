# RMK

Keyboard firmware for cortex-m, with layer/dynamic keymap/[vial](https://get.vial.today) support, written in Rust.

## Checklist after generating the firmware project

- [ ] Update `memory.x` for your microcontroller(if needed)

- [ ] Update your `keyboard.toml`

- [ ] Create your `vial.json` by your layout: https://get.vial.today/docs/porting-to-via.html, replace the default one

- [ ] Check the chip name of `probe-rs` is right, if you don't use `cargo run`, you can skip this step

- [ ] Update the family ID of your microcontroller in `Makefile.toml`, if you want to generate .uf2 firmware. The available family ID can be found in `scripts/uf2conv.py`

