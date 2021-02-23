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
    
   
    Serial.print("Odczyt: ");
    Serial.println(zmierzOdleglosc());
    delay(delay_value);
  //}
  
} 
 
float zmierzOdleglosc() {
  long czas1, czas2, czas3 ;
  float dystans1, dystans2, dystans3;
 
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
 
  czas1 = pulseIn(9, HIGH);
  dystans1 = czas1 / 58.8;
  czas2 = pulseIn(10, HIGH);
  dystans2 = czas2 / 58.8;
  czas3 = pulseIn(11, HIGH);
  dystans3 = czas3 / 58.8;
  Serial.print(dystans1);
  Serial.print(dystans2);
  Serial.print(dystans3);
  Serial.print(czas1);
  Serial.print(czas2);
  Serial.print(czas3);
  return dystans1, dystans2, dystans3;
}
