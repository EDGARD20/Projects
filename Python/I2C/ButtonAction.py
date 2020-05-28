import smbus
import time
import RPi.GPIO as GPIO



# Determine I2C
bus = smbus.SMBus(1)
arduino = 0x08

# Determine GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

## Buttons to GPIO
black = 18
red = 23
green = 24
green_Led = 26

## GPIO Direction for button
GPIO.setup(black,GPIO.IN)
GPIO.setup(red,GPIO.IN)
GPIO.setup(green,GPIO.IN)
GPIO.setup(green_Led,GPIO.OUT)

# Ultrasonic
ECHO = 5
TRIG = 6
start_pulse = 0
stop_pulse = 0
distance = 0
## GPIO direction for Ultrasonic

GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(TRIG,GPIO.OUT)

# Reading distance
def get_distance():
    global ECHO,TRIG, start_pulse, stop_pulse, distance
    GPIO.output(TRIG,False)
    time.sleep(.1)
    GPIO.output(TRIG,True)
    time.sleep(.00001)
    GPIO.output(TRIG,False)
    while GPIO.input(ECHO) == 0:
        start_pulse = time.time()
    while GPIO.input(ECHO) == 1:
        stop_pulse = time.time()
    distance = round((stop_pulse - start_pulse) * 17150 , 2 )
    return distance

# Reading buttons
def read_buttons():
    if GPIO.input(green):                   # if Green button pressed
        GPIO.output(green_Led,True)         # turn on Green Signal LED
        print "Green"
        bus.write_byte_data(arduino,24,0)   # Send 24 to Arduino
        time.sleep(.1)                          # wait for .5 sec

    if GPIO.input(red):                     # if Red Button pressed
        bus.write_byte_data(arduino,23,0)   # send 23 to Arduino
        print "RED"
        time.sleep(0.1)                     # wait for .5 sec

    if GPIO.input(black):                   # if  Black button pressed
        GPIO.output(green_Led,False)        # turn off the Green Signal LED
        print "Black"
        bus.write_byte_data(arduino,18,0)   # send 18 to Arduino
        time.sleep(.1)                      # wait for .5 sec
        # print int(get_distance())
        bus.write_byte_data(arduino,98,int(get_distance())) # Reading Distance and send it to Arduino



# setting up time period for loop
start_time = time.time()
print start_time
end_time =  start_time + 20
print end_time
duration_time = 0

# running the cord
try:
    while end_time > duration_time:
        read_buttons()
        duration_time = time.time()
    bus.write_byte_data(arduino, 250, 0)
except KeyboardInterrupt:
    bus.write_byte_data(arduino,250,0)