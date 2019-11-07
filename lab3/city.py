import random
import copy
import numpy as np


class City:

    def __init__(self, x, y, id_number):
        self.x = round(float(x), 4)
        self.y = round(float(y), 4)
        self.id = int(id_number)

    def __repr__(self):
        ans = 'id= ' + str(self.id) + 'x = ' + str(self.x) + ' y = ' + str(self.y)
        return ans

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_id(self):
        return self.id

    def distance(self, city):
        xDis = abs(city.x - self.x)
        yDis = abs(city.y - self.y)
        distance = np.sqrt((xDis ** 2) + (yDis ** 2))
        return distance
