from lab5.side_functions import fitness_function
import numpy as np
from copy import deepcopy

MIN_X = -5.12
MAX_X = 5.12
GENERATIONS = 100
CHANGE_DISPERSION = 5
DNA_BOUND = [MIN_X, MAX_X]


class EvolutionStrategy:
    def __init__(self, list_input):
        self.list_of_x = list_input
        self.number_of_x = len(list_input)
        self.fitness_value = fitness_function(self.list_of_x)

    def __repr__(self):
        i = 0
        ans = ""
        for x in self.list_of_x:
            ans += ("X" + str(i) + "= " + str(x[0]) + " ")
            i += 1
        ans += "f(x)= " + str(fitness_function(self.list_of_x))
        return ans

    def strategy_1_1(self, array_for_check, array_for_cont):
        child = np.zeros([self.number_of_x, 2])
        i = 0
        # for gen in self.list_of_x:
        #     child[i][0] = gen[0] + gen[1] * np.random.rand(1)
        #     child[i][1] = gen[1]
        #     if child[i][0] > MAX_X or child[i][0] < MIN_X:
        #         return 1, array_for_cont
        #     i += 1

        for gen in self.list_of_x:
            if not i % 2:
                child[i][0] = gen[0] + gen[1]
            else:
                child[i][0] = gen[0] + gen[1]

            child[i][1] = gen[1]
            if child[i][0] > MAX_X or child[i][0] < MIN_X:
                return 1, array_for_cont
            i += 1
        child_fit = fitness_function(child)

        a = abs(self.fitness_value)
        b = abs(child_fit)
        # if abs(self.fitness_value) > abs(child_fit):
        if a > b:
            self.list_of_x = child
            self.fitness_value = child_fit
            # for i in range(0, self.number_of_x):
            array_for_check.append(child_fit)
            array_2 = np.concatenate((array_for_cont, self.list_of_x))
            return None, array_2
        else:
            return 1, array_for_cont

    # мутация
    # 1)Сразу менять список,не возвращая ничего,не удобно будет добавлять если вдруг захочу узнать сколько чисел вышло за границу
    # 2)Возвращать новый список если удачно, или старый если вышло за пределы,можно будет добавить доп параметры чтобы узнавать когда мы выходим за границу,не удобно  в принципе
    def mutation_inside(self):
        under_mut = deepcopy(self)
        for gen in under_mut.list_of_x:
            gen[0] = gen[0] + gen[1]
            if gen[0] > MAX_X or gen[0] < MIN_X:
                break
        under_mut.fitness_value = fitness_function(under_mut.list_of_x)
        self.list_of_x = under_mut.list_of_x
        self.number_of_x = under_mut.number_of_x
        self.fitness_value = under_mut.fitness_value

    def mutation_outside(self):
        under_mut = deepcopy(self)
        for gen in under_mut.list_of_x:
            gen[0] = gen[0] + gen[1]
            if gen[0] > MAX_X or gen[0] < MIN_X:
                return self
        under_mut.fitness_value = fitness_function(under_mut.list_of_x)

        return under_mut
        # for gen in self.list_of_x:
        #     gen[0] = gen[0] + gen[1]
        #     if MIN_X < gen[0] > MAX_X:
        #         return

# взять лист с особями,сгрупировать их по парам
