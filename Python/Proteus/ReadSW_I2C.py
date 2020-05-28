import smbus
import time

bus = smbus.SMBus(1)

Arduino_uno1 = 7
Arduino_uno2 = 8


def read_wire():
    return bus.read_i2c_block_data(Arduino_uno1, 1)


def write_wire(addr, value):
    bus.read_i2c_block_data(addr, value, 0)


while 1:
    try:
        write_wire(Arduino_uno2, read_wire())
        time.sleep(0.5)

    except KeyboardInterrupt:
        x = 0
