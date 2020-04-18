#include <ESP8266WiFi.h>
#include <Servo.h>
#include <ESP8266WebServer.h>

WiFiServer wifiServer(80);

Servo servo;  

void setup()
{
  Serial.begin(115200);
  Serial.println();

  Serial.print("Setting soft-AP ... ");
  boolean result = WiFi.softAP("ESPsoftAP_01", "en_iyi_407");
  
  if(result == true)
  {
    Serial.println("Ready");
    wifiServer.begin();
  }
  else
  {
    Serial.println("Failed!");
  }
  servo.attach(13); //D1
}

void loop()
{
  Serial.printf("Stations connected = %d\n", WiFi.softAPgetStationNum());
    WiFiClient client = wifiServer.available();
 
  if (client) {
    Serial.printf("i have a client");
 
    while (client.connected()) {
 
      while (client.available()>0) {
//        char c = client.read();
//        Serial.write(c);
//        servo.write(c.toInt());
          String s = client.readStringUntil('s');
          Serial.print(s);
          servo.write(s.toInt());
      }
 
      delay(10);
    }
 
    client.stop();
    Serial.println("Client disconnected");
  }
  delay(3000);
}
