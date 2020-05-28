import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(22,GPIO.IN)
GPIO.setup(26,GPIO.OUT)

while True:
    i = GPIO.input(22)
    if i==0:
        print "no intuders", i
        GPIO.output(26, 0)
        time.sleep(0.01)
    elif i==1:
        print "Intruder detected",i
        GPIO.output(26,1)
        time.sleep(0.01)
