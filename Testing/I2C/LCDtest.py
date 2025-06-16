import utime
from machine import I2C,Pin
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

#Dirección del I2C y tamaño del LCD
I2C_ADDR  =  0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

# Raspberry Pi Pico
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)

#Configuración LCD
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)



def lcd_str(message, col, row):
    lcd.move_to(col, row)
    lcd.putstr(message)



while True:
    lcd.clear()
    lcd_str("Ricardo  Diaz", 0, 0)
    lcd_str("Taller Control", 0, 1)
    utime.sleep(2.5)
    lcd.clear()
    lcd_str("Quimica", 4, 0)
    lcd_str("Computacio", 0, 1)
    utime.sleep(2.5)