import numpy as np


class Ant:
    def __init__(self, index, world):
        self.index = index
        self.path_length = 0
        self.currCity = world.cities[0]
        self.path = []
        self.path.append(world.cities[0])
        self.unvisited = []
        self.unvisited.extend(world.cities[1:])
        self.transition_prob = []

    def reset(self, world):
        self.path_length = 0
        self.currCity = world.cities[0]
        self.path = []
        self.path.append(world.cities[0])
        self.unvisited = []
        self.unvisited.extend(world.cities[1:])
        self.transition_prob = []

    def get_trans_prob(self, world, city):
        b = 0
        a = world.routing_table[self.currCity.index][city.index]
        for c in self.unvisited:
            b = b + world.routing_table[self.currCity.index][c.index]
        trans_prob = a / float(b)
        return trans_prob

    def calc_dist(self):
        dist = 0.00
        for city_1 in range(0, len(self.path) - 1):
            dist += ((self.path[city_1].x - self.path[city_1 + 1].x) ** 2) + \
                    ((self.path[city_1].y - self.path[city_1 + 1].y) ** 2)
        self.path_length = dist
