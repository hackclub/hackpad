import asyncio
import serial
from winrt.windows.media.control import \
    GlobalSystemMediaTransportControlsSessionManager as MediaManager
from winrt.windows.foundation import IAsyncOperation

PORT = "COM4"  # Replace with your actual serial port
BAUD = 9600
ser = serial.Serial(PORT, BAUD, timeout=1)

async def get_media_info():
    sessions = await MediaManager.request_async()
    current_session = sessions.get_current_session()
    if not current_session:
        return "No media playing"

    info = await current_session.try_get_media_properties_async()
    title = info.title
    artist = info.artist

    return f"{title} - {artist}"

async def main():
    last_sent = ""
    while True:
        try:
            media = await get_media_info()
            if media != last_sent:
                ser.write((media[:128] + '\n').encode('utf-8'))
                last_sent = media
        except Exception as e:
            ser.write(b"No media playing\n")
        await asyncio.sleep(1)

asyncio.run(main())