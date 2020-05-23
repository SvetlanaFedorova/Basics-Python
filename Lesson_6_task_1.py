# Lesson 6 Task 1

import time
import itertools

class TrafficLight:
    __color = [['красный', 7], ['желтый', 2], ['зеленый', 7]]

    def running(self):
        for switch in itertools.cycle(self.__color):
            print(switch[0])
            time.sleep(switch[1])

my_class = TrafficLight()
my_class.running()
