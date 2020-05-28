import Adafruit_CharLCD as LCD
from threading import Thread, Timer
import time
import datetime


rs = 12
en = 16
D4 = 18
D5 = 23
D6 = 24
D7 = 25
lcd_columns = 16
lcd_rows = 2
lcd = LCD.Adafruit_CharLCD(rs, en, D4, D5, D6, D7, lcd_columns, lcd_rows)

result = None


def clock_display():
    lcd.clear()
    s = str(datetime.datetime.now().time().second)
    m = str(datetime.datetime.now().time().minute)
    h = str(datetime.datetime.now().time().hour)
    lcd.message(h + ":" + m + ":" + s)
    time.sleep(.5)
    lcd.clear()

#
# def inp_timer():
#     global result
#     timer = 1
#     t = Timer(timer, print, ['/'])
#     t.start()
#     prompt = "%d\n" %timer
#     result = str(input(prompt))
#     t.cancel()
#     lcd.clear()
#     return result


def user_type(result):
    print("here")
    lcd.clear()
    lcd.message(result)
    time.sleep(1)
    # Thread(target=clock_display()).start()


# while 1:
#     while result is None:
#         lcd.clear()
#         Thread(target=clock_display()).start()


while 1:
    try:
        Thread(target=clock_display()).start()
    except KeyboardInterrupt:
        # Thread(target=user_type(input("user: "))).start()
        lcd.clear()
        lcd.message(input("user: "))
        time.sleep(1)
