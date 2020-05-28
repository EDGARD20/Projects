# import Adafruit_CharLCD as LCD
# import time
import random
# from threading import Thread
# import smbus

# # bus = smbus.SMBus(1)
# arduino = 12
# rs = 12
# en = 16
# D4 = 18
# D5 = 23
# D6 = 24
# D7 = 25
# lcd_columns = 16
# lcd_rows = 2
# lcd = LCD.Adafruit_CharLCD(rs, en, D4, D5, D6, D7, lcd_columns, lcd_rows)
#
# lcd.clear()
# lcd.set_cursor(0,1)
# lcd.message('1')
# lcd.set_cursor(10,1)
# lcd.message('3')
# lcd.set_cursor(6,0)
# lcd.message('2')
# #
# # result = None
# # # print('Press s or n to continue:')
# # #
# # # def clock_display():
# # #     lcd.clear()
# # #     s = str(datetime.datetime.now().time().second)
# # #     m = str(datetime.datetime.now().time().minute)
# # #     h = str(datetime.datetime.now().time().hour)
# # #     lcd.message(h + ":" + m + ":" + s)
# # #     time.sleep(.5)
# # #     lcd.clear()
# # #     Thread(target=user_type()).start()
# # #
# # #
# # # def user_type():
# # #     with keyboard.Events() as events:
# # #         if events:
# # #             lcd.clear()
# # #             # event = events.get(1e1)
# # #             event = events.start
# # #             if event.key == keyboard.KeyCode.from_char('a'):
# # #                 lcd.message("a")
# # #                 time.sleep(.05)
# # #             if event.key == keyboard.KeyCode.from_char('b'):
# # #                 lcd.message("b")
# # #             if event.key == keyboard.KeyCode.from_char('c'):
# # #                 lcd.message("c")
# # #             if event.key == keyboard.KeyCode.from_char('d'):
# # #                 lcd.message("d")
# # #             if event.key == keyboard.KeyCode.from_char('e'):
# # #                 lcd.message("e")
# # #             if event.key == keyboard.KeyCode.from_char('f'):
# # #                 lcd.message("f")
# # #
# # #     Thread(target=clock_display()).start()
# # #
# # # while 1:
# # #     Thread(target=clock_display()).start()
# # #     user_type()
# #
# # def func1(events):
# #     for events in events:
# #         if events.type == pygame.KEYDOWN:
# #             lcd.clear()
# #             lcd.message("Ky Down")
# #             time.sleep(1)
# #
# # def func2(events):
# #     for events in events:
# #         if events.type == pygame.MOUSEBUTTONDOWN:
# #             lcd.clear()
# #             lcd.message("Mouse button down")
# #             time.sleep(1)
# #
# # while 1:
# #     pygame_events = pygame.event.get()
# #     func1(pygame_events)
# #     func2(pygame_events)
