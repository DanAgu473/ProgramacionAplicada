const int pinADC = 34;   
float tiempo = 0;
float intervalo = 0.5;  

void setup() {
  Serial.begin(115200);
  delay(2000);

  Serial.println("Tiempo(s),Lectura_ADC,Voltaje(V)");
}

void loop() {
  int lectura = analogRead(pinADC);
  float voltaje = (lectura / 4095.0) * 3.3;

  Serial.print(tiempo, 2);
  Serial.print(",");
  Serial.print(lectura);
  Serial.print(",");
  Serial.println(voltaje, 3);

  tiempo += intervalo;
  delay(intervalo * 1000);
}