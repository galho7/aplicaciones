#include <WiFi.h>
#include <WiFiClientSecure.h>
#include <PubSubClient.h>
#include <DHT.h>

// --- CONFIGURACIÓN DE RED Y THINGER.IO ---
const char* ssid = "MECATRONICA_3ABC";
const char* password = "MEC2025@.";

const char* thinger_user = "StalynGaona";
const char* thinger_device = "Temp";
const char* thinger_pass = "20260026"; // Password/Token del dispositivo
const char* mqtt_server = "backend.thinger.io";

// --- CONFIGURACIÓN DHT11 ---
#define DHTPIN 23      // El pin que definiste en tu Python
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

// Clientes de red
WiFiClientSecure espClient;
PubSubClient client(espClient);

// Función para conectar al WiFi
void setup_wifi() {
  delay(10);
  Serial.print("Conectando a ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi conectado");
}

// Función que recibe mensajes (callback)
void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Mensaje recibido [");
  Serial.print(topic);
  Serial.print("] ");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();
}

// Función para conectar a Thinger.io vía MQTT
void reconnect() {
  while (!client.connected()) {
    Serial.print("Intentando conexión MQTT...");
    // Intentamos conectar (ID de cliente, Usuario, Password)
    if (client.connect(thinger_device, thinger_user, thinger_pass)) {
      Serial.println("conectado");
    } else {
      Serial.print("falló, rc=");
      Serial.print(client.state());
      Serial.println(" intentando de nuevo en 5 segundos");
      delay(5000);
    }
  }
}

void setup() {
  Serial.begin(115200);
  dht.begin();
  setup_wifi();
  
  // Configuración de seguridad para Thinger.io (SSL)
  espClient.setInsecure(); // Permite conectar sin verificar certificado (más simple para pruebas)
  client.setServer(mqtt_server, 8883); // Puerto 8883 para MQTT con SSL
  client.setCallback(callback);
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  // Lectura de datos
  float hum = dht.readHumidity();
  float temp = dht.readTemperature();

  // Verificar si la lectura falló
  if (isnan(hum) || isnan(temp)) {
    Serial.println("Error al leer el sensor DHT11");
    return;
  }

  // Crear el tópico y el mensaje (JSON)
  // v2/users/USUARIO/devices/DISPOSITIVO/Data/Temp
  String topic = "v2/users/" + String(thinger_user) + "/devices/" + String(thinger_device) + "/Data/Temp";
  String payload = "{\"Temperatura\":" + String(temp) + ", \"Humedad\":" + String(hum) + "}";

  Serial.print("Publicando: ");
  Serial.println(payload);

  // Publicar datos
  client.publish(topic.c_str(), payload.c_str());

  // Espera de 2 segundos (como en tu código original)
  delay(2000);
}
