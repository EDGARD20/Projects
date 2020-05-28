#include <Wire.h>
#include <LiquidCrystal.h>
#define BUZZ 11

bool alramActivated = false;
bool GreenBTN = true;
bool RedBTN = false;
bool BlackBTN = false;
bool DistanceInisitation = true;
bool DistanceRequest = true;

byte Skeleton0[8] = {B11000,  B11000,  B00100,  B00111,  B01000,  B10000,  B10110,  B10110};
byte Skeleton1[8] = {B10001,  B10000,  B10010,  B01001,  B00100,  B00110,  B11001,  B11000};
byte Skeleton2[8] = {B00011,  B00011,  B00100,  B11100,  B00010,  B00001,  B01101,  B01101};
byte Skeleton3[8] = {B10001,  B00001,  B01001,  B10010,  B00100,  B01100,  B10011,  B00011};

byte heart_Empty4[8]    = {B00000,  B00000,  B01010,  B10101,  B10001,  B01010,  B00100,};
byte heart_Full5[8]     = {B00000,  B00000,  B01010,  B11111,  B11111,  B01110,  B00100,};

LiquidCrystal lcd(2 ,3 ,4 ,5 ,6 ,7);


void setup(){
  Wire.begin(8);
  Serial.begin(9600);
  Wire.onReceive(receiveEvent);
//  Wire.onRequest(sendEvent);
  LCD_Defenition();
  pinMode(BUZZ, OUTPUT);
  
}

void loop(){
  delay(100);
  LCD_DisplayOUT();
}


void LCD_Defenition(){
  lcd.begin(16, 2);
  lcd.setCursor(0,0);
  lcd.print("Initialising");
  delay(800);
  lcd.clear();
  lcd.print("Initialising.");
  delay(800);
  lcd.clear();
  lcd.print("Initialising..");
  delay(800);
  lcd.clear();
  lcd.print("Initialising...");
  delay(800);
  lcd.clear();
}

void LCD_DisplayOUT(){
  if(RedBTN == true){
    lcd.clear();
    lcd.print("Red Button");
    delay(100);
    LCD_Dispaly();
    tone(BUZZ, 2000, 300);
    delay(300);
  }
  else if (GreenBTN == true){
    lcd.clear();
    lcd.print("System Running");
    LCD_Dispaly();
    delay(100);
  }
  else if (BlackBTN == true){
    
  }
}


void LCD_Dispaly(){
  if(RedBTN){
    lcd.createChar(0, Skeleton0);
    lcd.createChar(1, Skeleton1);
    lcd.createChar(2, Skeleton2);
    lcd.createChar(3, Skeleton3);
    lcd.setCursor(14,0);
    lcd.write(byte(0));
    lcd.setCursor(14,1);
    lcd.write(byte(1));
    lcd.setCursor(15,0);
    lcd.write(byte(2));
    lcd.setCursor(15,1);
    lcd.write(byte(3));
  }
  if (GreenBTN){
    lcd.createChar(4, heart_Empty4);
    lcd.setCursor(15,1);
    lcd.write(byte(4));
    delay(200);
    lcd.createChar(5, heart_Full5);
    lcd.setCursor(15,1);
    lcd.write(byte(5));
    delay(200);
  }
}

void Distance(){
  if( DistanceInisitation){
    lcd.clear();
    lcd.begin(16, 2);
    lcd.setCursor(0,0);
    String RDis = String("Reading Sensor.........");
    int RDisSize = RDis.length(), numChar = 0;
    Serial.print(RDisSize);
    Serial.println();
    while(numChar < RDisSize){
        lcd.print(RDis[numChar]);
        numChar++;
      if(numChar == 14){
        lcd.setCursor(0,1);
      }      
      if(numChar >= 15){
        delay(30000);
      }
    }
  }
}

void blackButton(){
    lcd.clear();
    delay(100);
    int dist = Wire.read();
    Distance();
    delay(99999);
    lcd.clear();
    lcd.print("Distance: ");
    lcd.print(dist);
    lcd.print(" cm");
    delay(190000);
    if( 5 < dist){
      BlackBTN = false;
      GreenBTN = true; 
    }
    else{
      BlackBTN = false;
      GreenBTN = false;
      RedBTN = true;
      
    }
}

void receiveEvent(int howMany){
  int btn;
  while(1 < Wire.available()){
    btn = Wire.read();
    if(btn == 24){ // Green Button is pressed 
      RedBTN = false;
      BlackBTN = false; 
      alramActivated = false;
      GreenBTN = true;
    }
    else if (btn == 23){// Read Button is pressed
      GreenBTN = false;
      BlackBTN = false;
      RedBTN = true;
      alramActivated = true;
    }
    else if (btn == 18){ // Black Button is pressed
      GreenBTN = false;
      RedBTN = false;
      alramActivated = false;
      BlackBTN = true;
    }
    else if (btn == 250){// force to LCD clear from Raspberry pi
      lcd.clear();
    }
    else if (btn == 98){
      GreenBTN = false;
      RedBTN = false;
      blackButton();
    }
  }
  int x = Wire.read();
}


//void sendEvent(){
//  if (DistanceRequest){
//    uint8_t Buffer[1];
//    Buffer[1] = 99;
//    Wire.write(Buffer,1);
//  } 
//}
