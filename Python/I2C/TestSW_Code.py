import time
import win32api


for i in range(10):
   print(win32api.GetLastInputInfo())
   time.sleep(1)