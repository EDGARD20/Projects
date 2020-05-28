
import smbus
from time import sleep

bus = smbus.SMBus(1)
arduino = 0x08


String = raw_input('Enter String: ')+'  '


try:
    def split(word):
        return [char for char in word]


    string_List = split(String)
    print (string_List)


    def string2digit(word):
        value = []
        for i in range(len(word)):
            value.append(ord(word[i]))
        return value


    list_num = string2digit(string_List)
    bus.write_i2c_block_data(arduino, 0, list_num)
except KeyboardInterrupt:
    print ("Done")