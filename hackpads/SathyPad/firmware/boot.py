import supervisor
import board
import digitalio
import storage
import usb_cdc
import usb_hid
import usb_midi

supervisor.set_next_stack_limit(4096 + 4096)

button = digitalio.DigitalInOut(board.D4)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

if button.value:
    storage.disable_usb_drive() 
    usb_cdc.disable() 
    usb_midi.disable() 
    usb_hid.enable(boot_device=1) 
    
    
button.deinit()
