import numpy as np
import math
from lab6.work_dir.Ant import Ant


class SACO:
    def __init__(self, alpha, beta, epsilon, city_map, rho=0.1, init_pheromeon=1):
        self.alpha = alpha
        self.beta = beta
        self.epsilon = epsilon  # Отклонения от алгоритма
        self.cities = city_map
        self.rho = rho
        self.number_cities = len(city_map)
        self.pheromone_matrix_aka_TAU = np.full((self.number_cities, self.number_cities), init_pheromeon)
        self.attract_matrix = np.zeros((self.number_cities, self.number_cities))
        # self.routing_map = np.full((self.number_cities, self.number_cities), 1.00 / (self.number_cities - 1))
        self.distance_matrix = self.__distance_matrix()  # Матрица расстояния
        self.eta_matrix = self.__eta_matrix_calculate()

    def __eta_matrix_calculate(self):
        eta_matrix = np.zeros((self.number_cities, self.number_cities))
        for row_i, row_city_dist in enumerate(self.distance_matrix):
            for column_i, column_city in enumerate(self.distance_matrix):
                if row_city_dist[column_i] != 0:
                    eta_matrix[row_i, column_i] = 1 / row_city_dist
                else:
                    eta_matrix[row_i, column_i] = 0
                # dist_matrix[row_i, column_i] = self.__calculate_dist(row_city, column_city)
        return eta_matrix

    def __calculate_dist(self, city1, city2):
        distance = math.sqrt(
            math.pow(city1.x - city2.x, 2) + math.pow(city1.y - city2.y, 2)
        )
        return distance

    def __distance_matrix(self):
        dist_matrix = np.zeros((self.number_cities, self.number_cities))
        for row_i, row_city in enumerate(self.cities):
            for column_i, column_city in enumerate(self.cities):
                dist_matrix[row_i, column_i] = self.__calculate_dist(row_city, column_city)
        return dist_matrix

    def path_create(self, ant):
        ant.reset(self)
        while ant.unvisited:
            if np.random.random() < self.epsilon:
                next_city = ant.unvisited.pop(np.random.randint(0, len(ant.unvisited) - 1))
                ant.path.append(next_city)
                ant.currCity = next_city
            else:
                # Вычисляем для каждого непосященного узла вероятность перехода на них
                # Вытягиваем рандомное числа и смотрим на рулетку коммутативности
                #
                for city_m in ant.unvisited:
                    denominator = 0
                    numerator = (math.pow(self.pheromone_matrix_aka_TAU[ant.currCity.index, city_m.index], self.alpha) *
                                 self.eta_matrix[ant.currCity.index, city_m.index], self.beta)
                    for city in ant.unvisited:
                        denominator += (math.pow(self.pheromone_matrix_aka_TAU[ant.currCity.index, city.index],
                                                 self.alpha) *
                                        math.pow(self.eta_matrix[ant.currCity.index, city.index], self.beta))
                    p_ij = numerator / denominator
                    ant.transition_prob.append(p_ij)


def start(self, population=10, generations=10):
    GENERATIONS = generations
    POP = population
    ants = []
    for i in range(0, POP):
        ants.append(Ant(i, self))
    for generation in range(0, GENERATIONS):
        print('Gen ' + str(generations))
        for ant in ants:
            self.path_create(ant)
