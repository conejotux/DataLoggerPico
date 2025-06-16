from machine import Pin, I2C
import time

# I2C0 con SCL en GP17 y SDA en GP16 (puede cambiar según tu conexión)
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=100000)

print("Escaneando bus I2C...")
time.sleep(1)

devices = i2c.scan()

if devices:
    print(f"Se encontraron {len(devices)} dispositivo(s):")
    for d in devices:
        print("Dirección I2C encontrada:", hex(d))
else:
    print("No se detectaron dispositivos I2C.")
