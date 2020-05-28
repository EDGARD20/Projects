#include <Wire.h>
#include <LiquidCrystal.h>


LiquidCrystal lcd(2,3,4,5,6,7);


void setup() {
  Wire.begin(8);
  Serial.begin(9600);
  Wire.onReceive(receiveEvent);
  lcd.begin(16,2);
  lcd.setCursor(0,0);
  
  
  }

void loop() {
  delay(100);
}

void receiveEvent(int howMany){
  int c;
  while(1 < Wire.available()){
    c = Wire.read();

    if(c){
          Serial.print(c);
    Serial.println();
      if (c == 1)
        lcd.print("Green is pushed");
      if (c == 2)
        lcd.print("Red is pushed");
      if (c == 3)
        lcd.print("Black is pushed");
      if (c == 4)
        lcd.clear();
      if (c == 5){
        lcd.print("Idleing");
        delay(300000);
        lcd.clear();
        lcd.print("Idleing.");
        delay(300000);
        lcd.clear();
        lcd.print("Idleing..");
        delay(300000);
        lcd.clear();
        lcd.print("Idleing...");
        delay(300000);
        lcd.clear();
        lcd.print("Idleing....");
        delay(300000);
        lcd.clear();
        delay(10000);
        lcd.print("Exit");
        delay(300000);
        lcd.clear();        
      }
    }
  }
  int x = Wire.read();
}
