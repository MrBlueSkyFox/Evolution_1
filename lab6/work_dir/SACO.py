import numpy as np
import math
from lab6.work_dir.Ant import Ant
from multiprocessing import Process, Queue


class SACO:
    def __init__(self, alpha, beta, epsilon, city_map, rho=0.1, init_pheromone=1, pheromone_add=2):
        self.alpha = alpha
        self.beta = beta
        self.epsilon = epsilon  # Отклонения от алгоритма
        self.cities = city_map
        self.rho = rho
        self.number_cities = len(city_map)
        self.pheromone_add = pheromone_add
        self.pheromone_matrix_aka_TAU = np.full((self.number_cities, self.number_cities), init_pheromone, dtype=float)
        self.attractiveness = np.zeros((self.number_cities, self.number_cities))
        # self.attractiveness = numpy.zeros((num_cities, num_cities))
        # self.routing_map = np.full((self.number_cities, self.number_cities), 1.00 / (self.number_cities - 1))
        self.distance_matrix = self.__distance_matrix()  # Матрица расстояния
        self.eta_matrix = self.__eta_matrix_calculate()
        self.routing_table = np.full((self.number_cities, self.number_cities),
                                     (1.00 / (self.number_cities - 1)))  # initial even prob of any city

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

    def path_create(self, ant, q):
        ant.reset(self)
        while ant.unvisited:
            if np.random.random() < self.epsilon and len(ant.unvisited) > 1:
                next_city = ant.unvisited.pop(np.random.randint(0, len(ant.unvisited) - 1))
                ant.path.append(next_city)
                ant.currCity = next_city
            else:
                for c in ant.unvisited:
                    ant.transition_prob.append(ant.get_trans_prob(self, c))
                ant.transition_prob = ant.transition_prob / np.sum(ant.transition_prob)
                selection = np.random.choice(ant.unvisited, 1, p=ant.transition_prob)
                next_city = selection[0]
                ant.path.append(next_city)
                ant.currCity = next_city
                ant.unvisited.pop(ant.unvisited.index(next_city))
            ant.transition_prob = []
            # Вычисляем для каждого непосященного узла вероятность перехода на них
            # Вытягиваем рандомное числа и смотрим на рулетку коммутативности
            #

            # for city_m in ant.unvisited:
            #     denominator = 0
            #     numerator = (math.pow(self.pheromone_matrix_aka_TAU[ant.currCity.index, city_m.index], self.alpha) *
            #                  math.pow(self.eta_matrix[ant.currCity.index, city_m.index], self.beta))
            #     for city in ant.unvisited:
            #         denominator += (math.pow(self.pheromone_matrix_aka_TAU[ant.currCity.index, city.index],
            #                                  self.alpha) * math.pow(self.eta_matrix[ant.currCity.index, city.index],
            #                                                         self.beta))
            #     p_ij = numerator / denominator
            #     ant.transition_prob.append(p_ij)
            # next_city = np.random.choice(ant.unvisited, 1, p=ant.transition_prob)
            # next_city = next_city[0]
            # ant.transition_prob = []
            # ant.path.append(next_city)
            # ant.currCity = next_city
            # ant.unvisited.remove(next_city)

        ant.path.append(ant.path[0])
        q.put(ant)

    def update_pheromone_matrix(self, ant):
        for i in range(0, len(ant.path) - 1):
            current_pheromone = self.pheromone_matrix_aka_TAU[ant.path[i].index][ant.path[i + 1].index]
            self.pheromone_matrix_aka_TAU[ant.path[i].index][
                ant.path[i + 1].index] = current_pheromone + self.pheromone_add / ant.path_length
        # self.pheromone_matrix_aka_TAU = self.pheromone_matrix_aka_TAU * (1 - self.rho)

    def calc_attraction(self):
        city_list = self.cities
        for i, c in enumerate(city_list):
            for j, d in enumerate(city_list):
                distance = self.__calculate_dist(c, d)
                if distance > 0:
                    self.attractiveness[i][j] = 1 / distance
                else:
                    self.attractiveness[i][j] = 0

    def city_sum(self, city_x, city_y):
        calc = (math.pow(self.pheromone_matrix_aka_TAU[city_x.index][city_y.index], self.alpha)) * (
            math.pow(self.attractiveness[city_x.index][city_y.index], self.beta))
        return calc

    def update_routing_table(self, a):
        for c in a.path:
            temp_cities = list(a.path)
            temp_cities.remove(c)
            for t_c in temp_cities:
                numerator = self.city_sum(c, t_c)
                denom = 0.00
                other_temp_cities = list(temp_cities)
                other_temp_cities.remove(t_c)
                for o_t_c in other_temp_cities:
                    denom = denom + self.city_sum(c, o_t_c)

                if denom > 0:
                    self.routing_table[c.index][t_c.index] = numerator / denom
                else:
                    self.routing_table[c.index][t_c.index] = 0

    def start(self, population=10, generations=10):
        GENERATIONS = generations
        POP = population
        ants = []
        generated_paths = []
        generated_paths_value = []
        self.calc_attraction()

        for i in range(0, POP):
            ants.append(Ant(i, self))
        for generation in range(0, GENERATIONS):
            print('Gen ' + str(generation))
            for ant in ants:
                self.path_create(ant)
            for ant in ants:
                ant.calc_dist()
                self.update_pheromone_matrix(ant)
                self.update_routing_table(ant)
                generated_paths.append(ant.path)
                generated_paths_value.append(ant.path_length)
            best_of_the_run = min(generated_paths_value)
            # best_path=generated_paths[generated_paths_value]
            print('best of the run ' + str(best_of_the_run))

    def multi_proc_start(self, population=10, generations=10):
        GENERATIONS = generations
        POP = population
        ants = []
        procs = []
        generated_paths = []
        generated_paths_value = []
        self.calc_attraction()
        for i in range(0, POP):
            ants.append(Ant(i, self))

        for generation in range(0, GENERATIONS):
            print('Gen ' + str(generation))
            q = Queue()
            for ant in ants:
                p = Process(target=self.path_create, args=(ant, q,))
                # self.path_create(ant)
                procs.append(p)
                p.start()
            for p in procs:
                p.join()
            ants = []
            while q.empty() == False:
                ants.append(q.get())

            for ant in ants:
                ant.calc_dist()
                self.update_pheromone_matrix(ant)
                self.update_routing_table(ant)
                generated_paths.append(ant.path)
                generated_paths_value.append(ant.path_length)
            best_of_the_run = min(generated_paths_value)
            # best_path=generated_paths[generated_paths_value]
            print('best of the run ' + str(best_of_the_run))
