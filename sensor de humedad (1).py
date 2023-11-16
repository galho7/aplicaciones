import machine
from time import sleep
import dht
import network
import urequests

# Configura el pin del sensor DHT11
dht_pin = machine.Pin(4)

# Configura la conexión Wi-Fi
SSID = "Smartlink Fmlia_Atancuri"
PASSWORD = "21929526ATA"

def connect_wifi():
    station = network.WLAN(network.STA_IF)

    if not station.isconnected():
        print("Conectando a Wi-Fi...")
        station.active(True)
        station.connect(SSID, PASSWORD)
        while not station.isconnected():
            pass
    print("Conexión Wi-Fi establecida")
    print(station.ifconfig())

def read_sensor_data():
    sensor = dht.DHT11(dht_pin)
    sensor.measure()
    temperature = sensor.temperature()
    humidity = sensor.humidity()
    return temperature, humidity

def send_data_to_thingspeak(api_key, temperature, humidity):
    url = "https://api.thingspeak.com/update.json"
    params = "?api_key={}&field1={}&field2={}".format(api_key, temperature, humidity)
    response = urequests.get(url + params)
    print("Respuesta de ThingSpeak:", response.text)

def main():
    connect_wifi()
    while True:
        temperature, humidity = read_sensor_data()
        print("Temperatura: {:.1f}°C".format(temperature))
        print("Humedad: {:.1f}%".format(humidity))
        send_data_to_thingspeak("EYLB3MNDJTOLDW4O", temperature, humidity)
        sleep(5)  

if __name__ == '__main__':
    main()