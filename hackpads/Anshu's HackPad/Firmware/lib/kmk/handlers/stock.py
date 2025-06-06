from time import sleep


def passthrough(key, keyboard, *args, **kwargs):
    return keyboard


def reset(*args, **kwargs):
    import microcontroller

    microcontroller.reset()


def reload(*args, **kwargs):
    import supervisor

    supervisor.reload()


def bootloader(*args, **kwargs):
    import microcontroller

    microcontroller.on_next_reset(microcontroller.RunMode.BOOTLOADER)
    microcontroller.reset()


def gesc_pressed(key, keyboard, KC, *args, **kwargs):
    GESC_TRIGGERS = {KC.LSHIFT, KC.RSHIFT, KC.LGUI, KC.RGUI}

    if GESC_TRIGGERS.intersection(keyboard.keys_pressed):
        # First, release GUI if already pressed
        keyboard._send_hid()
        # if Shift is held, KC_GRAVE will become KC_TILDE on OS level
        keyboard.keys_pressed.add(KC.GRAVE)
        keyboard.hid_pending = True
        return keyboard

    # else return KC_ESC
    keyboard.keys_pressed.add(KC.ESCAPE)
    keyboard.hid_pending = True

    return keyboard


def gesc_released(key, keyboard, KC, *args, **kwargs):
    keyboard.keys_pressed.discard(KC.ESCAPE)
    keyboard.keys_pressed.discard(KC.GRAVE)
    keyboard.hid_pending = True
    return keyboard


def bkdl_pressed(key, keyboard, KC, *args, **kwargs):
    BKDL_TRIGGERS = {KC.LGUI, KC.RGUI}

    if BKDL_TRIGGERS.intersection(keyboard.keys_pressed):
        keyboard._send_hid()
        keyboard.keys_pressed.add(KC.DEL)
        keyboard.hid_pending = True
        return keyboard

    # else return KC_ESC
    keyboard.keys_pressed.add(KC.BKSP)
    keyboard.hid_pending = True

    return keyboard


def bkdl_released(key, keyboard, KC, *args, **kwargs):
    keyboard.keys_pressed.discard(KC.BKSP)
    keyboard.keys_pressed.discard(KC.DEL)
    keyboard.hid_pending = True
    return keyboard


def sleep_pressed(key, keyboard, KC, *args, **kwargs):
    sleep(key.meta.ms / 1000)
    return keyboard


def uc_mode_pressed(key, keyboard, *args, **kwargs):
    keyboard.unicode_mode = key.meta.mode

    return keyboard


def hid_switch(key, keyboard, *args, **kwargs):
    keyboard.hid_type, keyboard.secondary_hid_type = (
        keyboard.secondary_hid_type,
        keyboard.hid_type,
    )
    keyboard._init_hid()
    return keyboard


def ble_refresh(key, keyboard, *args, **kwargs):
    from kmk.hid import HIDModes

    if keyboard.hid_type != HIDModes.BLE:
        return keyboard

    keyboard._hid_helper.stop_advertising()
    keyboard._hid_helper.start_advertising()
    return keyboard


def ble_disconnect(key, keyboard, *args, **kwargs):
    from kmk.hid import HIDModes

    if keyboard.hid_type != HIDModes.BLE:
        return keyboard

    keyboard._hid_helper.clear_bonds()
    return keyboard


def any_pressed(key, keyboard, *args, **kwargs):
    from random import randint

    key.code = randint(4, 56)
    keyboard.keys_pressed.add(key)
    keyboard.hid_pending = True
