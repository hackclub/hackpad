#![no_std]
#![no_main]

use gamepad_lib::prelude::*;

use defmt::*;
use defmt_rtt as _;

use embassy_rp::{
    bind_interrupts,
    flash::{Async, Flash},
    gpio::{AnyPin, Input, Output, Pull},
    peripherals::{FLASH, USB},
    usb::{Driver, InterruptHandler},
};

#[cfg(feature = "rp2040")]
use panic_probe as _;

bind_interrupts!(struct Irqs {
    USBCTRL_IRQ => InterruptHandler<USB>;
});

const FLASH_SIZE: usize = 2 * 1024 * 1024;

#[embassy_executor::main]
async fn main(spawner: embassy_executor::Spawner) {
    
    info!("Start!");
    // Initialize peripherals
    let p = embassy_rp::init(Default::default());

    // Create the usb driver, from the HAL
    let driver = Driver::new(p.USB, Irqs);



    spawner.spawn(token)

}
