const int pinA = 5;
const int pinB = 18;

const int sensor1 = 34;
const int sensor2 = 35;

unsigned long ultimoCambio = 0;
const unsigned long periodo = 700; // 700 ms

void setup() {
  pinMode(pinA, OUTPUT);
  pinMode(pinB, OUTPUT);
  pinMode(sensor1, INPUT);
  pinMode(sensor2, INPUT);

  Serial.begin(115200);

  digitalWrite(pinA, HIGH);
  digitalWrite(pinB, LOW);
}

void loop() {

  // --- 1) Cambiar los pines cada 700 ms
  unsigned long ahora = millis();
  if (ahora - ultimoCambio >= periodo) {
    ultimoCambio = ahora;
    
    digitalWrite(pinA, !digitalRead(pinA));
    digitalWrite(pinB, !digitalRead(pinB));
  }

  // --- 2) Leer ADC rápidamente (sin delay)
  int lectura1 = analogRead(sensor1);
  int lectura2 = analogRead(sensor2);

  float volt1 = (lectura1 / 4095.0) * 3.3;
  float volt2 = (lectura2 / 4095.0) * 3.3;

  Serial.print("V1:");
  Serial.print(volt1);
  Serial.print(",V2:");
  Serial.println(volt2);
}