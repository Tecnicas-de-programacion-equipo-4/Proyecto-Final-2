int sensorPin_1 = A0;
int sensorPin_2 = A1;
int ventilator_1 = 13;
int ventilator_2 = 12;


void setup() {
Serial.begin(9600); 
pinMode(ventilator_1, OUTPUT);
digitalWrite(ventilator_1, LOW);
pinMode(ventilator_2, OUTPUT);
digitalWrite(ventilator_2, LOW);
}

void loop() {
int value_1 = analogRead(sensorPin_1);
int value_2 = analogRead(sensorPin_2);

float celsius_1 = (value_1 / 1023.0) * 500;
float celsius_2 = (value_2 / 1023.0) * 500;
Serial.print(celsius_1);
Serial.print(",");
Serial.print(celsius_2);
Serial.println("");

}

void serialEvent() {
  char inChar = (char)Serial.read();
  int state_2 = inChar == '2' ? HIGH : LOW;
  digitalWrite(ventilator_2, state_2);
   
  int state_1 = inChar == '1' ? HIGH : LOW;
  digitalWrite(ventilator_1, state_1);
  
}


