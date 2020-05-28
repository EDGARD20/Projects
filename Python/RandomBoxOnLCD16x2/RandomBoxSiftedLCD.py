import Adafruit_CharLCD as LCD
import time
import random
import smbus

# Arduino initialize
bus = smbus.SMBus(1)
Arduino = 12
# x_stage = 16
# x_goal = 16
# x_life = 16
# x_empty_heart = 16
lcd = LCD.Adafruit_CharLCD(12, 16, 18, 23, 24, 25, 16, 2)
car_shape = [0b00000, 0b00000, 0b10100, 0b11110, 0b11111, 0b11110, 0b10100, 0b00000]
block_stage = [0b10001, 0b01010, 0b00100, 0b11111, 0b11111, 0b00100, 0b01010, 0b10001]
goal_stage = [0b00100, 0b01111, 0b10100, 0b10100, 0b01111, 0b00101, 0b11110, 0b00100]
empty_heart = [0b00000, 0b01010, 0b10101, 0b10001, 0b10001, 0b01010, 0b00100, 0b00000]
life_stage = [0b00000, 0b01010, 0b11111, 0b11111, 0b11111, 0b01110, 0b00100, 0b00000]
lcd.create_char(0, car_shape)
lcd.create_char(1, block_stage)
lcd.create_char(2, goal_stage)
lcd.create_char(3, life_stage)
lcd.create_char(4, empty_heart)

class InitiateAll:
    def __init__(self):
        pass

    def characters(self):
        items = [1, 2, 3, 4]
        # block     goal    life    empty
        return random.choice(items)


class Conditions:
    def __init__(self, pos, x_pos, y_pos, x_stage, x_goal ,x_life , x_empty_heart):
        self.pos = pos
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_stage = x_stage
        self.x_goal = x_goal
        self.x_life = x_life
        self.x_empty_heart = x_empty_heart



    def get_car_pos(self):
        self.pos = bus.read_byte(Arduino)
        if self.pos == 76:
            self.y_pos = 0
        elif self.pos == 82:
            self.y_pos = 1
        self.x_pos = 1

        return self.x_pos, self.y_pos

    def rand_row_select(self):
        return random.randint(0, 1)


    def items_up_to_down(self):
        objects = InitiateAll.characters(None)
        # block     goal    life    empty
        if objects == 1:
            y_stage = self.rand_row_select()
            if self.x_stage == 1:
                self.x_stage = 17
            self.x_stage -= 1
            xpos,ypos = self.get_car_pos()
            DesignCharacter(xpos, ypos, self.x_stage, y_stage, objects).design()

        elif objects == 2:
            y_goal = self.rand_row_select()
            if self.x_goal == 1:
                self.x_goal = 17
            self.x_goal -= 1
            xpos, ypos = self.get_car_pos()
            DesignCharacter(xpos, ypos, self.x_goal, y_goal, objects).design()

        elif objects == 3:
            y_life = self.rand_row_select()
            if self.x_life == 1:
                self.x_life = 17
            self.x_life -= 1
            xpos, ypos = self.get_car_pos()
            DesignCharacter(xpos, ypos, self.x_life, y_life, objects).design()

        elif objects == 4:
            y_empty_heart = self.rand_row_select()
            if self.x_empty_heart == 1:
                self.x_empty_heart = 17
            self.x_empty_heart -= 1
            xpos, ypos = self.get_car_pos()
            DesignCharacter(xpos, ypos, self.x_empty_heart, y_empty_heart, objects).design()





class DesignCharacter:
    def __init__(self, x_pos_car, y_pos_car, x_objects, y_objects, item):
        self.x_pos_car = x_pos_car
        self.y_pos_car = y_pos_car
        self.x_objects = x_objects
        self.y_objects = y_objects
        self.item = item

    def design(self):
        lcd.set_cursor(self.x_pos_car, self.y_pos_car)
        lcd.write8(0, True)
        lcd.set_cursor(self.x_objects, self.y_objects)
        lcd.write8(self.item, True)
        time.sleep(0.1)
