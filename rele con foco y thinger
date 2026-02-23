#include <WiFi.h>
#include <ThingerESP32.h>
/* ========= THINGER.IO ========= */
#define USERNAME "jordyquizhpi23"
#define DEVICE_ID "foco"
#define DEVICE_CREDENTIAL "20260026"
/* ========= WIFI ========= */
#define SSID "MECATRONICA_3ABC"
#define SSID_PASSWORD "MEC2025@." // Reemplaza por tu clave
/* ========= LED ========= */
#define RELE 2 // RELE interno del ESP32 (GPIO2)
ThingerESP32 thing(USERNAME, DEVICE_ID, DEVICE_CREDENTIAL);
void setup() {
 Serial.begin(115200);
 delay(1000);
 pinMode(RELE, OUTPUT);
 digitalWrite(RELE, LOW);
 thing.add_wifi(SSID, SSID_PASSWORD);
 // Recurso para control desde Thinger (Switch)
 thing["RELE"] << digitalPin(RELE);
 Serial.println("ESP32 iniciado. Revisa Thinger.io (ONLINE).");
}
void loop() {
 thing.handle();
}
