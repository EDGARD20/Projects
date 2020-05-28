
// include the library code:
#include <LiquidCrystal.h>

char inKey;  // Character received from Serial input
uint8_t Cursor = 0;  // Position of cursor, 0 is top left, (rows*columns)-1 is bottom right
uint8_t rows = 2;  // Number rows, will be either 2 or 4
uint8_t columns = 16; // Number of columns, will be 16 or 20
uint8_t characters; // rows * columns

// initialize the library with the numbers of the interface pins
LiquidCrystal lcd(2,3,4,5,6,7);

void setup(){
    // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  // initialize the serial communications:
  Serial.begin(9600);
}

void loop()
{
  // when characters arrive over the serial port...
//  if (Serial.available()) {
    // wait a bit for the entire message to arrive
    delay(100);
    // clear the screen
    lcd.clear();
    Cursor = 0;
    // read all the available characters
//    while (Serial.available() > 0) {
      // display each character to the LCD
      inKey = "Reading Distance, wait";
      LCDDisplay(inKey);
//    }
//  }
}

void LCDDisplay(char character)
{
  int currentRow = 0;
  characters = rows * columns;
 
  // If Cursor is beyond screen size, get it right
  while (Cursor >= characters)
    Cursor -= characters;
  while (Cursor < 0)
    Cursor += characters;
 
  if (Cursor >= columns)
    currentRow = Cursor/columns;
   
  lcd.setCursor(Cursor%columns, currentRow);
  lcd.write(character);
 
  Cursor++;
}
