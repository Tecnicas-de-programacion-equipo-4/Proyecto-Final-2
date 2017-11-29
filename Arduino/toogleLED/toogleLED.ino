int roomoneLed = 13;
int roomtwoLed = 12;
int livingroomLed = 11;
int diningroomLed = 10;
int machineroomLed = 9;

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
   pinMode(machineroomLed, OUTPUT);
   digitalWrite(machineroomLed, LOW);
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
  else if (value == '9'){
    digitalWrite(machineroomLed, HIGH);
  }
  else if (value == 'a'){
    digitalWrite(machineroomLed, LOW);
  }
  
}

