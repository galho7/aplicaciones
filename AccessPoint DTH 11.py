import dht
import machine
import network
import time

# Nombre de la red y contraseña para el Access Point
SSID = "NOMBRE DE LA RED"
PASSWORD = "CLAVE"

# Configuración del punto de acceso
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=SSID, password=PASSWORD)

ip_address = ap.ifconfig()[0]
print("ESP32 configurado como Access Point")
print("Dirección IP del Access Point:", ip_address)

# Señal del sensor en el pin 4
dht_sensor = dht.DHT11(machine.Pin(23))

while True:
    try:
        # Lectura de temperatura y humedad
        dht_sensor.measure()
        temperature = dht_sensor.temperature()
        humidity = dht_sensor.humidity()

        print("Temperatura: {}°C, Humedad: {}%".format(temperature, humidity))

        time.sleep(2)
        
    except OSError as e:
        print("Error al leer el sensor:", e)
        continue
