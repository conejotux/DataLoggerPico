from machine import Pin
import onewire
import ds18x20
import time

# Configuración del pin del sensor y del bus 1-Wire
ds_pin = Pin(16)
ow = onewire.OneWire(ds_pin)
ds = ds18x20.DS18X20(ow)
roms = ds.scan()

def sensor_init():
    """Inicializa el sensor DS18B20 y verifica si está conectado."""
    if not roms:
        print("No se encontró ningún sensor DS18B20")
        time.sleep(2)
        return None
    print("Sensor encontrado!!! DS18B20")
    return roms[0]  # Retornar el primer sensor encontrado

def read_temperature(sensor):
    """Convierte y lee la temperatura del sensor."""
    if sensor is None:
        return None
    ds.convert_temp()
    time.sleep(0.5)
    temp = ds.read_temp(sensor)
    return round(temp, 2)