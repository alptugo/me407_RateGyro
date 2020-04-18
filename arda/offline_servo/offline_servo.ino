#include <ESP8266WiFi.h>
#include <Servo.h>
#include <ESP8266WebServer.h>

WiFiServer wifiServer(80);

Servo servo;
int my_delay = 100;
String my_delay_var;

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
  servo.attach(13); //D7
  
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
          my_delay_var = client.readStringUntil('s');
          if (my_delay != my_delay_var.toInt())
            my_delay = my_delay_var.toInt();
          //Serial.print(s);
          //Serial.print("\n");
          
          
          }
      for(int i=0; i<=160;i++) {
            servo.write(i);
            if(client.available() > 0)
              break;
            delay(my_delay);

      }
      
 
      delay(10);
    }
 
    client.stop();
    Serial.println("Client disconnected\n");
  }
  delay(3000);
}
