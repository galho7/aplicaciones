#include <WiFi.h>
#include <ThingerESP32.h>
#define USERNAME "TU_USUARIO"
#define DEVICE_ID "TU_ID_DISPOSITIVO"
#define DEVICE_CREDENTIAL "TU_CREDENCIAL_DISPOSITIVO"
#define SSID "NOMBRE_DE_TU_WIFI"
#define SSID_PASSWORD "CONTRASEÑA_DE_TU_WIFI" // Reemplaza por tu clave
#define LED1 2 // LED 1 (interno o externo)
#define LED2 4 // LED 2 (externo recomendado)
ThingerESP32 thing(USERNAME, DEVICE_ID, DEVICE_CREDENTIAL);
void setup() {
 Serial.begin(115200);
 delay(1000);
 pinMode(LED1, OUTPUT);
 pinMode(LED2, OUTPUT);
 digitalWrite(LED1, LOW);
 digitalWrite(LED2, LOW);
 thing.add_wifi(SSID, SSID_PASSWORD);
 // Recursos para el Dashboard (dos switches)
 thing["led1"] << digitalPin(LED1);
 thing["led2"] << digitalPin(LED2);
}
void loop() {
 thing.handle();
}
