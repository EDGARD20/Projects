#include <Wire.h>
#include <LiquidCrystal.h>
#include <Keypad.h>

int Count =0;
int AryNum =0;
int SizeOfArray=0;


LiquidCrystal lcd(7,6, 5,4,3,2);
//LiquidCrystal lcd(A1,A0,A2,A3,A4,A5);

void setup() {
      Wire.begin(8);                // join i2c bus with address #8
  Wire.onReceive(receiveEvent); // register event
  pinMode(13, OUTPUT);

  Serial.begin(9600);           // start serial for output
  lcd.begin(16,2);
  lcd.setCursor(0,0);
  lcd.print("Initialising.");
  delay(800);
  lcd.clear();
  delay(5000);

}

void loop() {
  delay(100);
   
}


void receiveEvent(int howMany) {
  while(Wire.available()){
    if (Count = 0){
      int SizeOfArray = Wire.read();
//      int data[SizeOfArray];
      Count++;
    }
    if (AryNum < SizeOfArray){
        int Num = Wire.read();
        char c = Num;
        digitalWrite(13, HIGH);
        delay(100);
        digitalWrite(13, LOW);
        delay(100);
        Serial.print(c);
        Serial.println();
        lcd.print(c);
        AryNum++;
    }
    if (Wire.read()== 0x25){
      lcd.clear();
      AryNum =0;
      Count= 0;
    }

  }
}
