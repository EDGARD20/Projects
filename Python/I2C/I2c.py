## Library
import smbus
import time
import RPi.GPIO as GPIO
import json

## Common
GPIO.setmode(GPIO.BCM)

## I2C
bus = smbus.SMBus(1)
arduino = 0x08
GPIO.setwarnings(False)

## Ultrasonic
ECHO = 5
TRIG = 6
pulse_start = 0
pulse_end = 0
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
dis=0


def distance():
    global dis, pulse_start, pulse_end
    GPIO.output(TRIG, False)
    time.sleep(0.1)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
    dis = round((pulse_end - pulse_start) * 17150, 2)
    print dis

    return dis


t=0
while(t < 10):
    try:
        dist = distance()

        if  dist < 10 :
            String = 'Warning Too close >>>' + str(dist) + ' cm'+ '  '
            t = 10
        else:
            String = raw_input('Enter String: ')+'  '
        # String = 'abcdefghi'
        def split(word):
            return [char for char in word]
        string_List = split(String)
        print string_List
        def string2digit(word):
            value = []
            for i in range(len(word)):
                value.append(ord(word[i]))
            return value

        list_num= string2digit(string_List)
        bus.write_i2c_block_data(arduino,0,list_num)

        print (list_num)
        t=t+1

    except:KeyboardInterrupt()




# bus.write_byte_data(arduino,1,0x2F)










# # bus.write_byte_data(arduino,0x08,0x3)
# Array = [97,98,99,100,101,102,103,104,105]
# print(len(Array),Array)
# bus.write_i2c_block_data(arduino,Array[0],Array[1:len(Array)])
# print (Array[1:len(Array)])
# sleep(3)
#
# bus.write_byte_data(arduino,0,0x25)



# # bus.write_byte_data(arduino,0x08,0x3)
# Array = "18"
# ff =int(Array)
# print(ff)
# # bus.write_i2c_block_data(arduino,Array[0],Array[1:len(Array)])
# # print (Array[1:len(Array)])
# sleep(3)
#
# bus.write_byte_data(arduino,0,0x25)
# string_List = (json.dumps(string_List))
# string_List = [int(i+1) for i in string_List]

