

#include <Wire.h>
#include <LiquidCrystal.h>


LiquidCrystal lcd(2,3,4,5,6,7);








void setup() {
Wire.begin(8);
Wire.onReceive(receiveEvent);
lcd.begin(16,2);
lcd.setCursor(0,0);
Serial.begin(9600);

}

void loop() {
delay(100);
}


void receiveEvent(int howMany){
  char c;
  while(1 < Wire.available()){
    c = Wire.read();
    if(c){
    lcd.print(c);
    Serial.print(c);
    Serial.println();
    }
  }
  int x= Wire.read();
}
