// Tristan Caetano
// Remote Power to Server

// Server Power Pin
#define PWR_PIN 8

void setup() {

  pinMode(PWR_PIN, OUTPUT);

  digitalWrite(PWR_PIN, HIGH);
  delay(100);
  digitalWrite(PWR_PIN, LOW);
}

void loop(){
  
}
