int room_one_led = 13;
int room_two_led = 12;
int living_led = 11;
int dining_led = 10;
int bathroom_led = 9;

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
}

void loop() { }

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

