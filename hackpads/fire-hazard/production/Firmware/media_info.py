import usb_hid
from PIL import Image
import displayio
import adafruit_imageload

class MediaInfo:
    def __init__(self):
        self.current_track = "No track info"
        self.default_image = self.create_default_image()
        
    def create_default_image(self):
        # Create a blank 32x32 bitmap
        bitmap = displayio.Bitmap(32, 32, 1)
        return bitmap

    def get_media_info(self):
        try:
            consumer = usb_hid.devices[1]
            if consumer:
                return self.current_track
            return "No track playing"
        except:
            return "Media Error"

    def get_album_art(self):
        try:
            return self.default_image
        except:
            return self.default_image
