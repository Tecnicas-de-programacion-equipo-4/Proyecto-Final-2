//leds
int room_one_led = 13;
int room_two_led = 12;
int living_led = 11;
int dining_led = 10;
int bathroom_led = 9;

//alarm
const int trigOut = 7;
const int echoOut = 8;
const int trigIn = 5;
const int echoIn = 6;
long durationOut, durationIn;
int distanceOut, distanceIn;

//temp
int sensorPin_1 = A0;
int sensorPin_2 = A1;
int ventilator_1 = 3;
int ventilator_2 = 4;

void setup() {
   Serial.begin(115200);

   //leds
   pinMode(room_one_led, OUTPUT);
   digitalWrite(room_one_led, LOW);
   pinMode(room_two_led, OUTPUT);
   digitalWrite(room_two_led, LOW);
   pinMode(living_led, OUTPUT);
   digitalWrite(living_led, LOW);
   pinMode(dining_led, OUTPUT);
   digitalWrite(dining_led, LOW);
   pinMode(bathroom_led, OUTPUT);
   digitalWrite(bathroom_led, LOW);

   //alarm
  pinMode(trigOut, OUTPUT); 
  pinMode(echoOut, INPUT);
  pinMode(trigIn, OUTPUT); 
  pinMode(echoIn, INPUT);  

  //temp
  pinMode(ventilator_1, OUTPUT);
  digitalWrite(ventilator_1, LOW);
  pinMode(ventilator_2, OUTPUT);
  digitalWrite(ventilator_2, LOW);  
}

void loop() { 

  //Alarm-----------------
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
  Serial.print(",");
  //----------------------

  //temp-----------------
  int value_1 = analogRead(sensorPin_1);
  int value_2 = analogRead(sensorPin_2);

  float celsius_1 = (value_1 / 1023.0) * 500;
  float celsius_2 = (value_2 / 1023.0) * 500;
  Serial.print(celsius_1);
  Serial.print(",");
  Serial.print(celsius_2);
  Serial.println("");

  //Serialprint -> dist_out,dist_in,celsius_1,celsius_2\n
  }

void serialEvent() {

  //Leds
  char room = (char)Serial.read();
  Serial.print(room);
  delay(100);
  if (room == '1'){
    char state = (char)Serial.read();
    int led_state = state == '1' ? HIGH : LOW;
    digitalWrite(room_one_led, led_state);
  }
  else if (room == '2'){
    char state = (char)Serial.read();
    int led_state = state == '1' ? HIGH : LOW;
    digitalWrite(room_two_led, led_state);
  }
  else if (room == '3'){
    char state = (char)Serial.read();
    int led_state = state == '1' ? HIGH : LOW;
    digitalWrite(living_led, led_state);
  }
  else if (room == '4'){
    char state = (char)Serial.read();
    int led_state = state == '1' ? HIGH : LOW;
    digitalWrite(dining_led, led_state);
  }
  else if (room == '3'){
    char state = (char)Serial.read();
    int led_state = state == '1' ? HIGH : LOW;
    digitalWrite(living_led, led_state);
  }
  if (room == '5'){
    char state = (char)Serial.read();
    int led_state = state == '1' ? HIGH : LOW;
    digitalWrite(bathroom_led, led_state);
  }
//Temp----------------------------------
  char inChar = (char)Serial.read();
  int state_2 = inChar == '2' ? HIGH : LOW;
  digitalWrite(ventilator_2, state_2);
   
  int state_1 = inChar == '1' ? HIGH : LOW;
  digitalWrite(ventilator_1, state_1);
}

