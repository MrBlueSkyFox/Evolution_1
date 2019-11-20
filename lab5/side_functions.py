import random
import numpy as np
from math import sqrt
from copy import deepcopy


# TODO
# инициализация
# мутация

def fitness_function(list_of_x):
    fit_val = 0
    for x in list_of_x:
        fit_val += x[0] ** 2
    return fit_val


def random_double(min_x, max_x):
    return round(random.uniform(min_x, max_x), 4)


def dispersion(x_list):
    math_expected = (np.mean(a=x_list, axis=0)[0]) / len(x_list)
    for x in x_list:
        x[1] = sqrt((x[0] - math_expected) ** 2)


def selection(list):
    pool = deepcopy(list)
    couple = []
    while len(pool) >= 2:
        a = pool.pop()
        k = random.randint(0, len(pool) - 1)
        b = pool.pop(k)
        couple.append([a, b])
    return couple


# закидываю список с объектами и оцениваю каждый объект
def re_evaluate(list):
    for obj in list:
        obj.fitness_value = fitness_function(obj.list_of_x)


def strategy_multiple(parent1, parent2):
    N = parent1.number_of_x
    child1 = np.zeros([N, 2])
    child2 = np.zeros([N, 2])
    for i in range(0, N):
        if not i % 2:
            child1[i][0] = parent1.list_of_x[i][0]
            child1[i][1] = parent1.list_of_x[i][1]
            child2[i][0] = parent2.list_of_x[i][0]
            child2[i][1] = parent2.list_of_x[i][1]
        else:
            child1[i][0] = parent2.list_of_x[i][0]
            child1[i][1] = parent2.list_of_x[i][1]
            child2[i][0] = parent1.list_of_x[i][0]
            child2[i][1] = parent1.list_of_x[i][1]
    return [child1, child2]
