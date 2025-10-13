use rmk::action::KeyAction;
use rmk::{a, k, layer, mo};
pub(crate) const COL: usize = 3;
pub(crate) const ROW: usize = 3;
pub(crate) const NUM_LAYER: usize = 2;
pub(crate) const NUM_ENCODER: usize = 2;

#[rustfmt::skip]
pub fn get_default_keymap() -> [[[KeyAction; COL]; ROW]; NUM_LAYER] {
    [
        layer!([
            [k!(MediaPrevTrack), k!(MediaPlayPause), k!(MediaNextTrack)],
            [k!(Kp4), k!(LShift), k!(Kp6)],
            [mo!(1), k!(Kp2), k!(Kp3)]
        ]),
        layer!([
            [k!(Kp7), k!(Kp8), k!(Kp9)],
            [k!(Kp4), k!(Kp5), k!(Kp6)],
            [mo!(0), k!(SecureUnlock), k!(Bootloader)]
        ]),
    ]
}

pub fn get_default_encoder_map() -> [[(KeyAction, KeyAction); NUM_ENCODER]; NUM_LAYER] {
    [
        [
            (k!(KbVolumeUp), k!(KbVolumeDown)),
            (k!(KbVolumeUp), k!(KbVolumeDown)),
        ],
        [
            (k!(KbVolumeUp), k!(KbVolumeDown)),
            (k!(KbVolumeUp), k!(KbVolumeDown)),
        ],
    ]
}
