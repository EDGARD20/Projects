import smbus
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

bus = smbus.SMBus(1)
arduino = 0x08


black = 18
red = 23
green = 24


GPIO.setup(black,GPIO.IN)
GPIO.setup(green,GPIO.IN)
GPIO.setup(red,GPIO.IN)


start_time = time.time()
print start_time
end_time =  start_time + 20
print end_time
duration_time = 0
try:
    while end_time > duration_time:
        time.sleep(0.1)
        if GPIO.input(green):
            bus.write_byte_data(arduino, 4, 0)
            print "Green"
            bus.write_byte_data(arduino, 24, 0)
            time.sleep(0.01)

        elif GPIO.input(red):
            print "Red"
            bus.write_byte_data(arduino, 4, 0)
            bus.write_byte_data(arduino, 23, 0)
            time.sleep(.01)
        elif GPIO.input(black):
            print "Black"
            bus.write_byte_data(arduino, 4, 0)
            bus.write_byte_data(arduino, 18, 0)
            time.sleep(.01)
        else:
            duration_time = time.time()

    bus.write_byte_data(arduino, 4, 0)
    time.sleep(0.1)
    bus.write_byte_data(arduino, 5, 0)
except KeyboardInterrupt:
    bus.write_byte_data(arduino,0,0)
