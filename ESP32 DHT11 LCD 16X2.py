from machine import Pin, I2C
from esp8266_i2c_lcd import I2cLcd
import dht
import time

i2c = I2C(scl=Pin(22), sda=Pin(21), freq=400000)

# Configuración del LCD 16x2 a través de I2C
lcd = I2cLcd(i2c, 0x27, 2, 16)

# Configuración del sensor DHT11
dht_sensor = dht.DHT11(Pin(23)) 

# Función para escribir en el LCD
def write_to_lcd(lcd, message):
    lcd.clear()
    lcd.putstr(message)

# Función para leer datos del sensor DHT11
def read_dht11_sensor():
    try:
        dht_sensor.measure()
        temperature = dht_sensor.temperature()
        humidity = dht_sensor.humidity()
        return temperature, humidity
    except OSError as e:
        print("Error al leer el sensor DHT11:", e)
        return None, None

# Leer datos del sensor y mostrarlos en el LCD
while True:
    try:
        temp, hum = read_dht11_sensor()
        if temp is not None and hum is not None:
            message = "Temp: {}C, Hum: {}%".format(temp, hum)
            write_to_lcd(lcd, message)
            time.sleep(2)
    except KeyboardInterrupt:
        break

# Limpiar el LCD antes de terminar
lcd.clear()
