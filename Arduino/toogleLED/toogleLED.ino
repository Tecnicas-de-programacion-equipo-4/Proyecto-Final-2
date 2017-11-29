#include <Servo.h>
int pos = 0;
Servo doorServo;
Servo garageServo;

int roomoneLed = 13;
int roomtwoLed = 12;
int livingroomLed = 11;
int diningroomLed = 10;

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
   garageServo.attach(5);
   
}

void loop() { }

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
    for (pos = 0; pos <= 90; pos += 1) {
    doorServo.write(pos);              
    delay(15);
    }
  }
  else if (value == 'b'){     //Cierre de puerta
    for (pos = 90; pos >= 0; pos -= 1) {
    doorServo.write(pos);              
    delay(15);
    }
  }
  else if (value == 'c'){     //Apertura de garage
    for (pos = 0; pos <= 180; pos += 1) {
    garageServo.write(pos);              
    delay(15);
    }
  }
  else if (value == 'd'){     //Cierre de garage
    for (pos = 180; pos >= 0; pos -= 1) {
    garageServo.write(pos);              
    delay(15);
    }
  }
  
}

