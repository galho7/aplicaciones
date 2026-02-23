#define THINGER_SERIAL_DEBUG
#include <ThingerESP32.h>

// --- Credenciales Thinger.io (Cámbialas por las tuyas) ---
#define USERNAME "TU_USUARIO"
#define DEVICE_ID "TU_ID_DISPOSITIVO"
#define DEVICE_CREDENTIAL "TU_CREDENCIAL_DISPOSITIVO"

// --- Credenciales WiFi ---
#define SSID "NOMBRE_DE_TU_WIFI"
#define SSID_PASSWORD "CONTRASEÑA_DE_TU_WIFI"

// Definición de pines para el sensor ultrasónico
const int TRIG_PIN = 5;
const int ECHO_PIN = 18;

ThingerESP32 thing(USERNAME, DEVICE_ID, DEVICE_CREDENTIAL);

void setup() {
  // Inicialización de monitor serie para ver errores de conexión
  Serial.begin(115200);

  // Configurar pines del sensor
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);

  // Conexión a WiFi
  thing.add_wifi(SSID, SSID_PASSWORD);

  // Definición del recurso que se enviará a Thinger.io
  thing["distancia"] >> [](pson& out){
    out = obtenerDistancia();
  };
}

void loop() {
  // Manejador de la conexión con la plataforma
  thing.handle();
}

// Función para realizar la lectura del sensor HC-SR04
float obtenerDistancia() {
  // Limpiar el pin Trigger
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  
  // Activar el sensor por 10 microsegundos
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  // Leer el tiempo que tarda en volver el eco
  long duracion = pulseIn(ECHO_PIN, HIGH);
  
  // Calcular la distancia en cm (Velocidad sonido / 2)
  float distancia = duracion * 0.034 / 2;
  
  // Filtro básico para lecturas fuera de rango
  if(distancia > 400 || distancia < 0) return 0; 
  
  return distancia;
}
