import dht
import utime
from machine import I2C, Pin,ADC
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
import onewire
import ds18x20


#ADC:
adc = ADC(Pin(26))



# SENSOR DHT22 (temperatura + humedad)
pin_dht = Pin(18)
dht_sensor = dht.DHT22(pin_dht)

# LCD
I2C_ADDR = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

def lcd_str(message, col, row):
    lcd.move_to(col, row)
    lcd.putstr(message)

# Carácter ° personalizado
caracter_grado = bytearray([
    0b00110,
    0b01001,
    0b00110,
    0b00000,
    0b00000,
    0b00000,
    0b00000,
    0b00000
])
lcd.custom_char(0, caracter_grado)

# SENSOR DS18B20
ds_pin = Pin(16)
ow = onewire.OneWire(ds_pin)
ds_sensor = ds18x20.DS18X20(ow)
roms = ds_sensor.scan()

if not roms:
    print("No se encontró ningún sensor DS18B20")
else:
    print("Sensor encontrado:", roms)

while True:
    try:
        dht_sensor.measure()
        temperatura_dht = dht_sensor.temperature()
        humedad = dht_sensor.humidity()

        lcd.clear()
        lcd_str("Humedad: {:.2f} %".format(humedad), 0, 0)
        lcd_str("Tempera: {:.2f}{}".format(temperatura_dht, chr(0)) + "C", 0, 1)

        # Leer DS18B20 (solo si fue encontrado)
        if roms:
            ds_sensor.convert_temp()
            #utime.sleep_ms(750)
            temp_ds = ds_sensor.read_temp(roms[0])
            lcd_str("DS18B20: {:.2f}{}".format(temp_ds, chr(0)) + "C", 0, 2)

        valor = adc.read_u16()  # Lectura de 16 bits (0 a 65535)
        voltaje = valor * 3.3 / 65535  # Conversión a voltaje (3.3V es el Vref de la Pico)
        print("Valor ADC:", valor, " - Voltaje:", round(voltaje, 2), "V")
        lcd_str("ADC:{} Volt:{:.2f}V".format(valor, voltaje), 0, 3)
        
        
    except OSError as e:
        print("Error al leer sensores:", e)

    utime.sleep(1.5)
