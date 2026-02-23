#include <WiFi.h>
#include <ThingerESP32.h>
/* ========= THINGER.IO ========= */
#define USERNAME "TU_USUARIO"
#define DEVICE_ID "TU_ID_DISPOSITIVO"
#define DEVICE_CREDENTIAL "TU_CREDENCIAL_DISPOSITIVO"
/* ========= WIFI ========= */
#define SSID "NOMBRE_DE_TU_WIFI"
#define SSID_PASSWORD "CONTRASEÑA_DE_TU_WIFI" // Reemplaza por tu clave
/* ========= LED ========= */
#define LED_PIN 2 // LED interno del ESP32 (GPIO2)
ThingerESP32 thing(USERNAME, DEVICE_ID, DEVICE_CREDENTIAL);
void setup() {
 Serial.begin(115200);
 delay(1000);
 pinMode(LED_PIN, OUTPUT);
 digitalWrite(LED_PIN, LOW);
 thing.add_wifi(SSID, SSID_PASSWORD);
 // Recurso para control desde Thinger (Switch)
 thing["led"] << digitalPin(LED_PIN);
 Serial.println("ESP32 iniciado. Revisa Thinger.io (ONLINE).");
}
void loop() {
 thing.handle();
}
