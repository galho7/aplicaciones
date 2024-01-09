from umqtt.simple import MQTTClient
import network
import time
from machine import Pin

# Configuración de WiFi
ssid = 'nombre de red'
password = 'clave red'
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)
while not wifi.isconnected():
    pass

# Configuración de Thinger.io
user = 'usuario de thinger.io'
device = 'Temp'
password_thinger = 'Sl1234.'

# Función de callback al recibir mensajes
def callback(topic, msg):
    print('Mensaje recibido en el tema {}: {}'.format(topic, msg))

#DHT11 en pin 14
from dht import DHT11
dht11 = DHT11(Pin(23))

# Medicion DHT
def readDht():
    dht11.measure()
    return dht11.temperature(), dht11.humidity()


# Lectura de datos DHT
def colectData():
    temp, hum, = readDht()
    return temp, hum

# Inicialización del cliente MQTT con usuario y contraseña
client = MQTTClient(client_id=device, server='backend.thinger.io', user=user, password=password_thinger, ssl=True)
client.set_callback(callback)

while(True):
    temp, hum,  = colectData()
    #print (temp)
    #print (hum)
    #payload = "field1="+str(temp)+"&field2="+str(hum)
        
    client.connect()

    # Valor numérico a enviar
    #valor_numerico = 42

    # Publicación del valor en Thinger.io
    # Tomar en cuenta el nombre del topic para generar el data bucket
    topic = 'v2/users/{}/devices/{}/Data/Temp'.format(user, device)
    message = '{{"field1":{}, "field2":{}}}'.format(temp, hum)
    client.publish(topic, message)
  

    # Espera para permitir que el mensaje se envíe antes de desconectar
    time.sleep(2)

    # Desconexión del cliente MQTT
    client.disconnect()