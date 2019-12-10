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
