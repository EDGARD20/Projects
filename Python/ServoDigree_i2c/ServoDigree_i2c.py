import smbus
import time

servo_call = 1

Ardunio_Nano = 0x07
bus = smbus.SMBus(1)
bus.write_byte_data(Ardunio_Nano, servo_call, 25)
for j in range(0, 5):
    for i in range(30, 130, 1):
        bus.write_byte_data(Ardunio_Nano, servo_call, i)
        print(i)
        time.sleep(.03)
    bus.write_byte_data(Ardunio_Nano, servo_call, 30)
bus.write_byte_data(Ardunio_Nano, servo_call, 85)
time.sleep(.2)
# bus.write_byte_data(Ardunio_Nano, 2, 85)

