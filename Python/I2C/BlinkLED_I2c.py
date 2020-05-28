
import smbus
from time import sleep
arduino = 0x8

bus = smbus.SMBus(1)


def ledBlink():
    for i in range(1,10,1):
        bus.write_byte_data(arduino, 0, 1)
        sleep(1)
        bus.write_byte_data(arduino, 0, 0)
        sleep(1)



if __name__=='__main__':
    ledBlink()

