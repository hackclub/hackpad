import machine
import time

# Initialisierung der seriellen Kommunikation
uart = machine.UART(1, baudrate=115200, tx=17, rx=16)  # tx und rx auf die entsprechenden Pins setzen

while True:
    # Daten vom Seeed empfangen
    if uart.any():
        data = uart.read()
        print("Empfangene Daten:", data)
        
    # Daten an Seeed senden
    uart.write("Hello from ESP!\n")
    time.sleep(1)
