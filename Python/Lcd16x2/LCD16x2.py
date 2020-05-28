import Adafruit_CharLCD as LCD
from RPi import GPIO
import time

rs = 12
en = 16
D4 = 18
D5 = 23
D6 = 24
D7 = 25
lcd_columns = 16
lcd_rows = 2


lcd = LCD.Adafruit_CharLCD(rs, en, D4, D5, D6, D7)

lcd.message('Hello \n World')
time.sleep(5)
lcd.clear()
text = input("type something to be displayed: ")
lcd.message(text)
time.sleep(2)
lcd.clear()
lcd.message(time.clock())