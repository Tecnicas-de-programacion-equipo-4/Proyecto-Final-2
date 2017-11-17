int room_one_led = 13;
int room_two_led = 12;
int living_led = 11;
int dining_led = 10;

void setup() {
   Serial.begin(115200);
   pinMode(room_one_led, OUTPUT);
   digitalWrite(room_one_led, LOW);
   pinMode(room_two_led, OUTPUT);
   digitalWrite(room_two_led, HIGH);
   pinMode(living_led, OUTPUT);
   digitalWrite(living_led, HIGH);
   pinMode(dining_led, OUTPUT);
   digitalWrite(dining_led, HIGH);
}

void loop() { }

void serialEvent() {
    char inChar = (char)Serial.read();
    int state = inChar == '1' ? HIGH : LOW;
    digitalWrite(room_one_led, state);
}
