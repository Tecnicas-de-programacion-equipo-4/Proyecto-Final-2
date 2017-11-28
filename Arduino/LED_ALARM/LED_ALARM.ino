int room_one_led = 13;
int room_two_led = 12;
int living_led = 11;
int dining_led = 10;
int bathroom_led = 9;

const int trigOut = 7;
const int echoOut = 8;
const int trigIn = 5;
const int echoIn = 6;
long durationOut, durationIn;
int distanceOut, distanceIn;

void setup() {
   Serial.begin(115200);
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

  pinMode(trigOut, OUTPUT); 
  pinMode(echoOut, INPUT);
  pinMode(trigIn, OUTPUT); 
  pinMode(echoIn, INPUT);  
}

void loop() { 
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
  Serial.println(distanceIn);
  }

void serialEvent() {
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
}

