import machine
import time
import ssd1306

# Initialisierung der OLED-Anzeige
i2c = machine.I2C(0, scl=machine.Pin(22), sda=machine.Pin(21))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Initialisierung der Tasten
buttons = [machine.Pin(i, machine.Pin.IN, machine.Pin.PULL_UP) for i in range(9)]


# Initialisierung der seriellen Kommunikation
uart = machine.UART(1, baudrate=115200, tx=1, rx=0)  # tx und rx auf die entsprechenden Pins setzen

# Initialisierung des Rotary Encoders
rotary_clk = machine.Pin(34, machine.Pin.IN)
rotary_dt = machine.Pin(35, machine.Pin.IN)
last_clk_state = rotary_clk.value()

# Funktion zur Anzeige der Tastenbelegung
def display_buttons(selected_button):
    oled.fill(0)  # Bildschirm löschen
    oled.text("Tastenbelegung", 0, 0)
    for i, button in enumerate(buttons):
        if i == selected_button:
            oled.text(f"> Button {i + 1}", 0, 10 + i * 10)
        else:
            oled.text(f"  Button {i + 1}", 0, 10 + i * 10)
    oled.show()

# Hauptschleife
selected_button = 0

while True:
        # Daten vom ESP empfangen
    if uart.any():
        data = uart.read()
        print("Empfangene Daten:", data)
        
    # Daten an ESP senden
    uart.write("Hello from Seeed!\n")
    time.sleep(1)
    # Überprüfen der Tasten
    for i, button in enumerate(buttons):
        if not button.value():  # Taste gedrückt
            print(f"Taste {i + 1} wurde gedrückt")
            selected_button = i
            display_buttons(selected_button)
            time.sleep(0.2)  # Entprellen

    # Überprüfen des Rotary Encoders
    current_clk_state = rotary_clk.value()
    if current_clk_state != last_clk_state:  # Zustand hat sich geändert
        if rotary_dt.value() != current_clk_state:  # Drehen im Uhrzeigersinn
            selected_button = (selected_button + 1) % len(buttons)
        else:  # Drehen gegen den Uhrzeigersinn
            selected_button = (selected_button - 1) % len(buttons)
        display_buttons(selected_button)

    last_clk_state = current_clk_state
    time.sleep(0.1)  # Verhindern von Flackern
