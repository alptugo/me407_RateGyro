#include <ESP8266WiFi.h>
#include <Servo.h>
#include <ESP8266WebServer.h>

WiFiServer wifiServer(80);

Servo servo;
int my_delay = 100;
String my_delay_var;
boolean i_broke;
void setup()
{
  boolean result = WiFi.softAP("ESPsoftAP_01", "en_iyi_407");
  
  if(result == true)
  {
    wifiServer.begin();
  }
  else
  {
  }
  servo.attach(13); //D7
  servo.write(90);

  
}

void loop()
{
    WiFiClient client = wifiServer.available();
 
  if (client) {
 
    while (client.connected()) {
 
      while (client.available()>0) {
//        char c = client.read();
//        Serial.write(c);
//        servo.write(c.toInt());
          my_delay_var = client.readStringUntil('s');
          if (my_delay != my_delay_var.toInt())
          my_delay = my_delay_var.toInt();
          i_broke=false;
          //Serial.print(s);
          //Serial.print("\n");
          
          
          }
      for(int i=65; i<=115;i++) {
            servo.write(i);
            if(client.available() > 0){
              i_broke=true;
              break;
            }
            delay(my_delay);
      }
      if(i_broke==false){
            for(int i=115; i>=65;i--) {
            servo.write(i);
            if(client.available() > 0)
              break;
            delay(my_delay);
            }
      }
 
      delay(10);
    }
 
    client.stop();
  }
  delay(3000);
}
