
const int trigOut = 12;
const int echoOut = 13;
const int trigIn = 10;
const int echoIn = 11;
long durationOut, durationIn;
int distanceOut, distanceIn;

void setup() {
  pinMode(trigOut, OUTPUT); 
  pinMode(echoOut, INPUT);
  pinMode(trigIn, OUTPUT); 
  pinMode(echoIn, INPUT);  
  Serial.begin(115200); 
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
