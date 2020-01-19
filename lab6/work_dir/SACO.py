import time

import numpy as np
import math
from lab6.work_dir.Ant import Ant
from multiprocessing import Process, Queue


class SACO:
    def __init__(self, alpha, beta, epsilon, city_map, rho=0.1, init_pheromone=1, pheromone_add=2, strat=0):
        self.alpha = alpha
        self.beta = beta
        self.epsilon = epsilon  # Отклонения от алгоритма
        self.cities = city_map
        self.rho = rho
        self.number_cities = len(city_map)
        self.pheromone_add = pheromone_add
        self.pheromone_matrix_aka_TAU = np.full((self.number_cities, self.number_cities), init_pheromone, dtype=float)
        self.attractiveness = np.zeros((self.number_cities, self.number_cities))
        self.distance_matrix = self.__distance_matrix()  # Матрица расстояния
        self.eta_matrix = self.__eta_matrix_calculate()
        self.strategy = strat

    def __eta_matrix_calculate(self):
        eta_matrix = np.zeros((self.number_cities, self.number_cities))
        for row_i, row_city_dist in enumerate(self.distance_matrix):
            for column_i, column_city in enumerate(self.distance_matrix):
                if row_city_dist[column_i] != 0:
                    eta_matrix[row_i, column_i] = 1 / row_city_dist[column_i]
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
            for city_1 in ant.unvisited:
                denominator = 0
                numerator = (self.pheromone_matrix_aka_TAU[ant.currCity.index][city_1.index] ** self.alpha) * (
                        self.eta_matrix[ant.currCity.index, city_1.index] ** self.beta)
                for city in ant.unvisited:
                    denominator += (self.pheromone_matrix_aka_TAU[ant.currCity.index, city.index] ** self.alpha) * (
                            self.eta_matrix[ant.currCity.index, city.index] ** self.beta)
                prob = numerator / denominator
                ant.transition_prob.append(prob)
            next_city = np.random.choice(ant.unvisited, 1, p=ant.transition_prob)
            next_city = next_city[0]
            ant.transition_prob = []
            ant.path.append(next_city)
            ant.currCity = next_city
            ant.unvisited.remove(next_city)

    def __update_attr(self, ant):
        self.attractiveness = np.zeros((self.number_cities, self.number_cities))
        for i in range(0, len(ant.path) - 1):
            row_id = ant.path[i].index
            col_id = ant.path[i + 1].index
            if self.strategy == 0:
                self.attractiveness[row_id][col_id] = self.pheromone_add / ant.path_length
            elif self.strategy == 1:
                self.attractiveness[row_id][col_id] = self.pheromone_add / self.distance_matrix[row_id][col_id]

    def __update_pheromone(self):
        self.pheromone_matrix_aka_TAU *= self.rho
        self.pheromone_matrix_aka_TAU += self.attractiveness


    def start(self, population=10, generations=10):
        GENERATIONS = generations
        POP = population
        ants = []
        generated_paths = []
        generated_paths_value = []
        best_of_the_run = 0
        for i in range(0, POP):
            ants.append(Ant(i, self))
        for generation in range(0, GENERATIONS):
            # generation_time_start = time.time()
            for ant in ants:
                self.path_create(ant)
            for ant in ants:
                ant.calc_dist()
                self.__update_attr(ant)
                self.__update_pheromone()
                generated_paths.append(ant.path)
                generated_paths_value.append(ant.path_length)
            best_of_the_run = min(generated_paths_value)
            # print("Generation: ", generation, " time --%s seconds--" % (time.time() - generation_time_start))
            # best_path=generated_paths[generated_paths_value]
            # print('best of the run ' + str(best_of_the_run))
        best_index = generated_paths_value.index(min(generated_paths_value))
        best_path = generated_paths[best_index]
        print('Best of run  ' + str(best_of_the_run))
        ans = self._print_path(best_path)
        print(ans)

    def _print_path(self, list_with_path):
        string_ans = ''
        for city in list_with_path:
            string_ans += str(city.id_city) + ' -> '
        return string_ans
