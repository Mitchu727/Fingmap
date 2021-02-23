#define trigPin 12

 
void setup() {
  Serial.begin (9600);
  pinMode(trigPin, OUTPUT); //Pin, do którego podłączymy trig jako wyjście
  pinMode(9, INPUT); //a echo, jako wejście
  pinMode(10, INPUT); 
  pinMode(11, INPUT); 
}
  
void loop() {  
  int delay_value = 10;
  //int loop_number = 100;
  //Serial.println(" ");
  //for (int i=1; i <= loop_number; i++)
  //{
    
    //Serial.print(i);
    //Serial.print(",");
    
    Serial.print("czujnik1,");
    Serial.print(zmierzOdleglosc(9));
    Serial.print(", ");
    delay(delay_value);
    
    Serial.print("czujnik2,");
    Serial.print(zmierzOdleglosc(10));
    Serial.print(", ");
    delay(delay_value);
    
    Serial.print("czujnik3,");
    Serial.println(zmierzOdleglosc(11));
    delay(delay_value);
  //}
  
} 
 
float zmierzOdleglosc(int pin) {
  long czas;
  float dystans;
 
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
 
  czas = pulseIn(pin, HIGH);
  dystans = czas / 58.8;
 
  return dystans;
}
