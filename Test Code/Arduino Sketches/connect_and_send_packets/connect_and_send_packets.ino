#include <WiFi.h>

// Replace with your network credentials (STATION)
const char* ssid = "haley";
const char* password = "currence";
const char* host = "192.168.73.48";

void initWiFi() {
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
//  Serial.print("Connecting to WiFi ..");
//  while (WiFi.status() != WL_CONNECTED) {
//    Serial.print('.');
//    delay(1000);
//  }
//  Serial.println(WiFi.localIP());
}

void setup() {
  Serial.begin(115200);
  initWiFi();
}

void loop() 
{
  WiFiClient client;
  const int httpPort = 80;
  client.connect(host, httpPort);

  client.print("Hi! - From Rodrigo the Cobot");
  delay(1000);
  
//  unsigned long timeout = millis();
//  while (client.available() == 0) {
//      if (millis() - timeout > 5000) {
//          //Serial.println(">>> Client Timeout !");
//          //client.stop();
//          //return;
//      }
//  }
}
