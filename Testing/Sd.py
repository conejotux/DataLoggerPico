import machine
import os
import sdcard
import uos

# Inicializar SPI1
spi = machine.SPI(1,
                  baudrate=1000000,
                  polarity=0,
                  phase=0,
                  sck=machine.Pin(10),
                  mosi=machine.Pin(11),
                  miso=machine.Pin(12))

cs = machine.Pin(15, machine.Pin.OUT)

# Inicializar SD
sd = sdcard.SDCard(spi, cs)

# Montar sistema de archivos
vfs = uos.VfsFat(sd)
uos.mount(vfs, "/sd")

# Escribir archivo
with open("/sd/datos.txt", "w") as f:
    f.write("¡Hola desde la Raspberry Pi Pico!\n")

# Leer archivo
with open("/sd/datos.txt", "r") as f:
    print("Contenido de la SD:")
    print(f.read())
