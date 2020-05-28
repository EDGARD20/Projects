#include<LiquidCrystal.h>
#include <Keypad.h>
String words;
char num1 = 0, num2 = 0;

//LiquidCrystal lcd(A0, A1, A2, A3, A4, A5);
//LiquidCrystal lcd(A0, A1, A5, A4, A3, A2);
//LiquidCrystal lcd(7,6, 5,4,3,2);
LiquidCrystal lcd(2,3,4,5,6,7);

const byte ROWS = 4;
const byte COLS = 4;

char hexaKeys[ROWS][COLS]{
  {'1','4','7','*'},
  {'2','5','8','0'},
  {'3','6','9','#'},
  {'A','B','C','D'}
};

byte rowPins[ROWS] = {13, 12, 11, 10};
byte colPins[COLS] = {9, 8, 7, 6};



Keypad customKeypad = Keypad(makeKeymap(hexaKeys),colPins, rowPins,  COLS, ROWS);


void setup()
{
    Serial.begin(9600);
    lcd.begin(16,2);
    lcd.setCursor(0,0);
    lcd.print("Initialising.");
    delay(800);
    lcd.clear();
    lcd.print("Initialising..");
    delay(800);
    lcd.clear();
    lcd.print("Initialising...");
    delay(800);
    lcd.clear();
    lcd.print("Calculator Begins");
    delay(1000);
    lcd.clear();
    lcd.print("A  B  C  D  #  *");
    lcd.setCursor(0,1);
    lcd.print("en +  -  /  =  *");
    delay(5000);
    digitalWrite(8, HIGH); 
    pinMode(A0,OUTPUT);
    

}

void loop()
{
    digitalWrite(A0,LOW);
    lcd.clear();
    char customKey = customKeypad.getKey();
    if(customKey){
      words = customKey;
      delay(500);
    lcd.setCursor(0,0);
    lcd.print(words);
    delay(500);
    Serial.println(customKey);
    }
}
