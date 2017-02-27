const int outputPin = 11;

void setup() {
  pinMode(outputPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  while (Serial.available()) {
    char c = Serial.read();
    if (c == '1') {
      digitalWrite(outputPin, HIGH);
      delay(3000);
      digitalWrite(outputPin, LOW);
    }
  }
}

