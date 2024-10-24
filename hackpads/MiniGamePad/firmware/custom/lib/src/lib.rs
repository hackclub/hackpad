#![cfg_attr(not(test), no_std)]

pub mod prelude {

    pub use embassy_time::{Timer, Duration, Delay, Instant};
    pub use defmt::{info,println,warn,error,debug,trace};

}