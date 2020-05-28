
import RPi.GPIO as GPIO
import smbus
import time
arduino_Nano = 0x07
arduino_Uno01 = 0x08
arduino_Uno02 = 0x09

bus = smbus.SMBus(1)

#
# def StringToBytes(val):
#     retVal = []
#     for c in val:
#         retVal.append(ord(c))
#     return retVal
#
#
# def writeData(value):
#     byteValue = StringToBytes(value)
#     print(byteValue)
#     bus.write_i2c_block_data(arduino_Nano, 0x00, byteValue)
#
#
#
# while True:
#     print("sending")
#     writeData("test")
#     time.sleep(3)
#
#     print("OPEN")
#     writeData("OPEN")
#     time.sleep(3)
#
#     print("WIN")
#     writeData("WIN")
#     time.sleep(3)

address = 7


while True:
    try:
        bus.write_byte(arduino_Nano, 110)
        time.sleep(5)
        bus.write_byte(arduino_Nano, 40)
        rep = bus.read_i2c_block_data(address, 0)
    except:
        continue
    string = ""
    for i in range(0, 18):
        string += chr(rep[i])
    print(string)
    time.sleep(1)
