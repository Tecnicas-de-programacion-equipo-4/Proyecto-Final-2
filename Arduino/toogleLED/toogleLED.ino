#include <Servo.h>
int door_pos = 0;
int garage_pos = 180;
Servo doorServo;
Servo garageServo;

int roomoneLed = 13;
int roomtwoLed = 12;
int livingroomLed = 11;
int diningroomLed = 10;

int ventilator_1 = 9;
int ventilator_2 = 8;

const int trigOut = 4;
const int echoOut = 3;
const int trigIn = 2;
const int echoIn = 1;

int sensor_temp_1 = A0;
int sensor_temp_2 = A1;

long durationOut, durationIn;
int distanceOut, distanceIn;

void setup() {
   Serial.begin(115200);
   pinMode(roomoneLed, OUTPUT);
   digitalWrite(roomoneLed, LOW);
   pinMode(roomtwoLed, OUTPUT);
   digitalWrite(roomtwoLed, LOW);
   pinMode(livingroomLed, OUTPUT);
   digitalWrite(livingroomLed, LOW);
   pinMode(diningroomLed, OUTPUT);
   digitalWrite(diningroomLed, LOW);
   doorServo.attach(6);
   doorServo.write(0);
   garageServo.attach(5);
   garageServo.write(180);

   pinMode(ventilator_1, OUTPUT);
   digitalWrite(ventilator_1, LOW);
   pinMode(ventilator_2, OUTPUT);
   digitalWrite(ventilator_2, LOW);

   pinMode(trigOut, OUTPUT); 
   pinMode(echoOut, INPUT);
   pinMode(trigIn, OUTPUT); 
   pinMode(echoIn, INPUT);  

}

void loop() {
  //Alarm--------
   digitalWrite(trigIn, LOW);
  delayMicroseconds(2);

  digitalWrite(trigIn, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigIn, LOW);

  durationIn = pulseIn(echoIn, HIGH);

  digitalWrite(trigOut, LOW);
  delayMicroseconds(2);

  digitalWrite(trigOut, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigOut, LOW);

  durationOut = pulseIn(echoOut, HIGH);


  distanceOut = durationOut * 0.034 / 2;
  distanceIn = durationIn * 0.034 / 2;

  delay(10);
  
  Serial.print(distanceOut);
  Serial.print(",");
  Serial.print(distanceIn);

  //-----------------------------Temp
  
  int value_1 = analogRead(sensor_temp_1);
  int value_2 = analogRead(sensor_temp_2);

  float celsius_1 = (value_1 / 1023.0) * 500;
  float celsius_2 = (value_2 / 1023.0) * 500;
  Serial.print(celsius_1);
  Serial.print(",");
  Serial.print(celsius_2);
  Serial.println("");
  
  //Serialprint -> dist_out,dist_in,celsius_1,celsius_2\n
  }

void serialEvent() {
  char value = (char)Serial.read();
  delay(100);
  if (value == '1'){
    digitalWrite(roomoneLed, HIGH);
  }
  else if (value == '2'){
    digitalWrite(roomoneLed, LOW);
  }
  else if (value == '3'){
    digitalWrite(roomtwoLed, HIGH);
  }
  else if (value == '4'){
    digitalWrite(roomtwoLed, LOW);
  }
  else if (value == '5'){
    digitalWrite(livingroomLed, HIGH);
  }
  else if (value == '6'){
    digitalWrite(livingroomLed, LOW);
  }
  else if (value == '7'){
    digitalWrite(diningroomLed, HIGH);
  }
  else if (value == '8'){
    digitalWrite(diningroomLed, LOW);
  }
  else if (value == 'a'){     //Apertura de puerta
    doorServo.write(90);
  }
  else if (value == 'b'){     //Cierre de puerta
    doorServo.write(0);
  }
  else if (value == 'c'){     //Apertura de garage
    garageServo.write(0);
  }
  else if (value == 'd'){     //Cierre de garage
    garageServo.write(180);
  }
  else if (value == 'e'){
    digitalWrite(ventilator_1, HIGH);
  }
  else if (value == 'f'){
    digitalWrite(ventilator_1, LOW);
  }
  else if (value == 'g'){
    digitalWrite(ventilator_2, HIGH);
  }
  else if (value == 'h'){
    digitalWrite(ventilator_2, LOW);
  }
  else if (value == 'i'){
    digitalWrite(ventilator_1, LOW);
    digitalWrite(ventilator_2, LOW);
  }
  
}
