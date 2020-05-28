import smbus
import time
bus = smbus.SMBus(1)

ard_min = 0x0c

while 1:
    value = bus.read_byte(ard_min)
    # print(value)
    if value == 109:
        print("S")
    elif value == 76:
        print("L")
    elif value == 82:
        print("R")
    elif value == 85:
        print("U")
    elif value == 68:
        print("D")
    time.sleep(0.1)