# import initial library

import Adafruit_CharLCD as LCD
import time
import random
import smbus

# initiate i2c
bus = smbus.SMBus(1)
Arduino = 12

# initiate LCD
rs = 12
en = 16
D4 = 18
D5 = 23
D6 = 24
D7 = 25
LCD_columns = 16
LCD_rows = 2
lcd = LCD.Adafruit_CharLCD(rs, en, D4, D5, D6, D7, LCD_columns, LCD_rows)

# initiate Special character
carMap = [0b00000, 0b00000, 0b10100, 0b11110, 0b11111, 0b11110, 0b10100, 0b00000]
StageMap = [0b10001, 0b01010, 0b00100, 0b11111, 0b11111, 0b00100, 0b01010, 0b10001]
pointMap = [0b00100, 0b01111, 0b10100, 0b10100, 0b01111, 0b00101, 0b11110, 0b00100]
NegativeHeartMap = [0b00000, 0b01010, 0b10101, 0b10001, 0b10001, 0b01010, 0b00100, 0b00000]
HeartMap = [0b00000, 0b01010, 0b11111, 0b11111, 0b11111, 0b01110, 0b00100, 0b00000]

# create Special character
lcd.create_char(0, carMap)
lcd.create_char(1, StageMap)
lcd.create_char(2, pointMap)
lcd.create_char(3, HeartMap)
lcd.create_char(4, NegativeHeartMap)


# Global variable

Blocker_char = 1
Point_char = 2
Heart_char = 3
N_Heart_char = 4
# create a list of Items
Items = [Blocker_char, Point_char, Blocker_char, Heart_char,Blocker_char, N_Heart_char, Blocker_char]



























