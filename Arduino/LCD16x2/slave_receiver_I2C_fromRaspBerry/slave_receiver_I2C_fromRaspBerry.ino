// Wire Slave Receiver
// by Nicholas Zambetti <http://www.zambetti.com>

// Demonstrates use of the Wire library
// Receives data as an I2C/TWI slave device
// Refer to the "Wire Master Writer" example for use with this

// Created 29 March 2006

// This example code is in the public domain.


#include <Wire.h>
#include <LiquidCrystal.h>
#include <Keypad.h>
String words;
char num1 = 0, num2 = 0;
LiquidCrystal lcd(A0, A1, A5, A4, A3, A2);


void setup() {
  Wire.begin(8);                // join i2c bus with address #8
  Wire.onReceive(receiveEvent); // register event
  pinMode(3, OUTPUT);
  Serial.begin(9600);           // start serial for output
  lcd.begin(16,2);
  lcd.setCursor(0,0);
  lcd.clear();
  delay(800);
}

void loop() {
  delay(100);
}

// function that executes whenever data is received from master
// this function is registered as an event, see setup()
void receiveEvent(int howMany) {

  while (1<Wire.available()) { // loop through all but the last
    
    char c = Wire.read(); // receive byte as a character
    lcd.setCursor(0,0);
    lcd.print("High");         // print the character
    delay(1000);

    digitalWrite(3, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(10000);                       // wait for a second
    digitalWrite(3, LOW);    // turn the LED off by making the voltage LOW
    delay(10000); 
  
  }
    

}
