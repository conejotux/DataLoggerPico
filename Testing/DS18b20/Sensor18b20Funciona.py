from machine import Pin

import onewire
import ds18x20
import time

# Configurar el pin GPIO donde está conectado el sensor (GPIO17 en este caso)
ds_pin = Pin(16)
#led = Pin(16, Pin.OUT)
# Inicializar el bus 1-Wire
ow = onewire.OneWire(ds_pin)

# Crear un objeto DS18X20
ds = ds18x20.DS18X20(ow)

# Buscar dispositivos en el bus
roms = ds.scan()
print("Dispositivos encontrados:", roms)

if not roms:
    print("No se encontró ningún sensor DS18B20")
    time.sleep(2) 
else:
    print("Sensor encontrado!!! DS18B20")
    sensor = roms[0]  # Usar el primer (y único) sensor encontrad
	
while True:
		# Iniciar la conversión de temperatura
	#led.toggle()
	ds.convert_temp()
	time.sleep_ms(750)  # Esperar el tiempo necesario para la conversión

		# Leer y mostrar la temperatura de cada dispositivo
	temp = ds.read_temp(sensor)
	print("Temperatura:", temp, "°C")

	time.sleep(1)  # Esperar antes de la próxima lectura
