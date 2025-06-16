from machine import Pin
import time

# Configurar el pin 17 como salida
led = Pin(18, Pin.OUT)

while True:
    led.toggle()       # Cambia el estado del LED
    time.sleep(0.5)    # Espera medio segundo
