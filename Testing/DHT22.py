import machine
import dht
import time

# Configura el pin (por ejemplo GP15)
pin_sensor = machine.Pin(16)
sensor = dht.DHT22(pin_sensor)

while True:
    try:
        sensor.measure()
        temperatura = sensor.temperature()
        humedad = sensor.humidity()
        
        print("Temperatura: {:.1f} °C".format(temperatura))
        print("Humedad: {:.1f} %".format(humedad))
    except OSError as e:
        print("Error al leer el sensor:", e)
    
    time.sleep(2)  # espera 2 segundos entre lecturas
