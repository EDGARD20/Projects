#include <Wire.h>
#include <LiquidCrystal.h>


LiquidCrystal lcd(2,3,4,5,6,7);

byte A[8] = {
  B10000,
  B10000,
  B10000,
  B10000,
  B10000,
  B10000,
  B11111,
};
byte B[8] = {
  B11111,
  B10000,
  B10000,
  B10000,
  B10000,
  B10000,
  B10000,
};
byte C[8] = {
  B11111,
  B10001,
  B10001,
  B00001,
  B00001,
  B00000,
  B00000,
};

byte D[8] = {
  B00111,
  B00001,
  B00001,
  B00001,
  B00001,
  B00001,
  B00111,
};
byte E[8] = {
  B00000,
  B00000,
  B00001,
  B00001,
  B10001,
  B10001,
  B11111,
};



void setup() {

  lcd.createChar(0, A);
  lcd.begin(16, 2); 
  lcd.setCursor(7,2);
  lcd.write(byte(0));
  delay(1000);
  lcd.createChar(0, B);
  lcd.write(byte(0));
}

void loop() {}
