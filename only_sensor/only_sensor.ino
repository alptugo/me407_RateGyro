void setup() {
  // put your setup code here, to run once:
    Serial.begin(115200);

}

void loop() {
  Serial.print(60);  // To freeze the lower limit
  Serial.print(" ");
  Serial.print(120);  // To freeze the upper limit
  Serial.print(" ");
  Serial.println(String(analogRead(A0)*0.05859+60));
}
