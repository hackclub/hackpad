use rmk::action::KeyAction;
use rmk::{k, layer, mo};
pub(crate) const COLUMNS: usize = 3;
pub(crate) const ROWS: usize = 3;
pub(crate) const LAYERS: usize = 2;

#[rustfmt::skip]
pub const fn get_default_keymap() -> [[[KeyAction; COLUMNS]; ROWS]; LAYERS] {
    [
        layer!([
            [k!(Left), k!(Down), k!(Right)],
            [k!(RShift), k!(UP), k!(Enter)],
            [k!(Z), k!(X), mo!(2)]
        ]),
        layer!([
            [k!(MediaPrevTrack), k!(AudioVolDown), k!(MediaNextTrack)],
            [k!(MediaRewind), k!(AudioVolUp), k!(MediaFastForward)],
            [k!(MediaPlayPause), k!(AudioMute), mo!(1)]
        ]),
    ]
}

// #[rustfmt::skip]
// pub static KEYMAP: [[[KeyAction; COL]; ROW]; NUM_LAYER] = [
//     layer!([
//         [k!(A), k!(B), k!(C)],
//         [k!(Kp4), k!(LShift), k!(Kp6)],
//         [k!(Kp1), k!(Kp2), k!(Kp3)]
//     ]),
//     layer!([
//         [k!(Kp7), k!(Kp8), k!(Kp9)],
//         [k!(Kp4), k!(LCtrl), k!(Kp6)],
//         [k!(Kp1), k!(Kp2), k!(Kp3)]
//     ]),
// ];