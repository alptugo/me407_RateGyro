#include <ESP8266WiFi.h>
#include <Servo.h>
#include <ESP8266WebServer.h>

WiFiServer wifiServer(80);


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
}

void loop()
{
  Serial.printf("Stations connected = %d\n", WiFi.softAPgetStationNum());
    WiFiClient client = wifiServer.available();
   String current_angle = "a";
  if (client) {
    Serial.printf("i have a client");
 
    while (client.connected()) {
 
      while (client.available()>0) {
//        char c = client.read();
//        Serial.write(c);
//        servo.write(c.toInt());
          delay(5);
//          Serial.write((int)(analogRead(A0)*0.05859+60));
          Serial.print(String(analogRead(A0)*0.05859+60));
          
      }
 
      delay(10);
    }
 
    client.stop();
    Serial.println("Client disconnected");
  }
  delay(3000);
}
