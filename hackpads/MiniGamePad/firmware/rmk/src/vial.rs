// Use `build.rs` automatically generate vial config, according to `vial.json`
// Document for create your `vial.json`: https://get.vial.today/docs/porting-to-via.html
// TODO: Put your `vial.json` at your project's root
include!(concat!(env!("OUT_DIR"), "/config_generated.rs"));