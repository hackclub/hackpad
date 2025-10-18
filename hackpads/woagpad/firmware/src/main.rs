#![no_main]
#![no_std]

#[macro_use]
mod keymap;
#[macro_use]
mod macros;
mod vial;

use defmt::*;
use defmt_rtt as _;
use embassy_executor::Spawner;
use embassy_rp::{
    bind_interrupts,
    flash::{Async, Flash},
    gpio::{AnyPin, Input, Output},
    peripherals::USB,
    usb::{Driver, InterruptHandler},
    Peripheral,
};
// use embassy_rp::flash::Blocking;
use panic_probe as _;
use rmk::{
    config::{KeyboardUsbConfig, RmkConfig, VialConfig},
    input_device::{rotary_encoder::RotaryEncoder, InputDevice},
    run_devices, run_rmk, run_rmk_with_async_flash,
};
use vial::{VIAL_KEYBOARD_DEF, VIAL_KEYBOARD_ID};

bind_interrupts!(struct Irqs {
    USBCTRL_IRQ => InterruptHandler<USB>;
});

const FLASH_SIZE: usize = 2 * 1024 * 1024;

#[embassy_executor::main]
async fn main(spawner: Spawner) {
    info!("RMK start!");
    // Initialize peripherals
    let p = embassy_rp::init(Default::default());

    // Create the usb driver, from the HAL
    let driver = Driver::new(p.USB, Irqs);

    // Pin config
    let (input_pins, output_pins) = config_matrix_pins_rp!(peripherals: p, input: [PIN_2, PIN_29, PIN_27], output: [PIN_28, PIN_0, PIN_1]);

    // Use internal flash to emulate eeprom
    // Both blocking and async flash are support, use different API
    // let flash = Flash::<_, Blocking, FLASH_SIZE>::new_blocking(p.FLASH);
    let flash = Flash::<_, Async, FLASH_SIZE>::new(p.FLASH, p.DMA_CH0);

    let keyboard_usb_config = KeyboardUsbConfig {
        vid: 0x4c4b,
        pid: 0x4643,
        manufacturer: "woagpad",
        product_name: "woagpad",
        serial_number: "vial:f64c2b3c:000001",
    };

    let vial_config = VialConfig::new(VIAL_KEYBOARD_ID, VIAL_KEYBOARD_DEF);

    let keyboard_config = RmkConfig {
        usb_config: keyboard_usb_config,
        vial_config,
        ..Default::default()
    };

    let mut pin_4 = AnyPin::from(p.PIN_4).into_ref();
    let pin_shared = Input::new(&mut pin_4, embassy_rp::gpio::Pull::Up);
    let pin_left_b = Input::new(AnyPin::from(p.PIN_3), embassy_rp::gpio::Pull::Up);
    let pin_right_b = Input::new(AnyPin::from(p.PIN_26), embassy_rp::gpio::Pull::Up);
    let mut left_encoder = RotaryEncoder::new(pin_shared, pin_left_b, 0);
    // TODO: Implement right encoder (currently, the pin cannot be shared like this)
    // let mut right_encoder = RotaryEncoder::new(pin_shared, pin_right_b, 1);

    // Start serving
    // Use `run_rmk` for blocking flash
    embassy_futures::join::join(
        run_rmk_with_async_flash(
            input_pins,
            output_pins,
            driver,
            flash,
            &mut keymap::get_default_keymap(),
            keyboard_config,
            spawner,
        ),
        // note: encoders aren't implemented yet, so this does basically nothing for now /shrug
        run_devices!(left_encoder),
        // run_devices!(left_encoder, right_encoder),
    )
    .await;
}
