from kmk.bootcfg import bootcfg

bootcfg(
    # optional:
    sense: Optional[microcontroller.Pin, digitalio.DigitalInOut] = None,
    source: Optional[microcontroller.Pin, digitalio.DigitalInOut] = None,
    autoreload: bool = True,
    boot_device: int = 0,
    cdc_console: bool = True,
    cdc_data: bool = False,
    consumer_control: bool = True,
    keyboard: bool = True,
    midi: bool = True,
    mouse: bool = True,
    nkro: bool = False,
    pan: bool = True,
    storage: bool = True,
    usb_id: Optional[tuple[str, str]] = None,
    **kwargs,
) -> bool