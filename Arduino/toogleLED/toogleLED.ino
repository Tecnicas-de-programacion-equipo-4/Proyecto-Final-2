#include <Servo.h>
int door_pos = 0;
int garage_pos = 0;
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
   doorServo.write(0);
   garageServo.attach(5);
   garageServo.write(0);
   
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
    doorServo.write(90);
  }
  else if (value == 'b'){     //Cierre de puerta
    doorServo.write(0);    
  }
  else if (value == 'c'){     //Apertura de garage
    if (garage_pos == 0){
      for (garage_pos = 0; garage_pos <= 180; garage_pos += 1) {
        garageServo.write(garage_pos);              
        delay(15);
      }
    }
  }
  else if (value == 'd'){     //Cierre de garage
    if (garage_pos == 180){
      for (garage_pos = 180; garage_pos >= 0; garage_pos -= 1) {
        garageServo.write(garage_pos);              
        delay(15);
      }
    }
  }
  
}

