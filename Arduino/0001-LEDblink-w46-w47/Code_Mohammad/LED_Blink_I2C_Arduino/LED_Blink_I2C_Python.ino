/*
  Blink LED
  Mohammad Miriran
  Start up project
  w41-w42
  2019
  Sweden

*/
#include <Wire.h>
#define LED 10

void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED, OUTPUT);
  Wire.begin(8);
  Wire.onReceive(receiveEvent);
  Serial.begin(9600);
//  delay(500);
}

void loop() {
  delay(100);
}


void receiveEvent(int howMany){
  int c;
  while( Wire.available()){
    c = Wire.read();
    c = Wire.read();
    Serial.print(c);
    Serial.println();
    if (c == 1){
      digitalWrite(LED, HIGH);
    }
    if (c == 0 ){
      digitalWrite(LED, LOW);      
    }
  }
  c=0;
}
