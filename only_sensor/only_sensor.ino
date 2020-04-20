void setup() {
  // put your setup code here, to run once:
    Serial.begin(115200);
    pinMode(D1, OUTPUT);
    pinMode(D7, OUTPUT);
    digitalWrite(D1, HIGH);
}

void loop() {
  Serial.print(60);  // To freeze the lower limit
  Serial.print(" ");
  Serial.print(120);  // To freeze the upper limit
  Serial.print(" ");
  Serial.println(String(analogRead(A0)*0.0591133+59.47));
}
