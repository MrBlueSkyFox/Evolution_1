import random
import numpy as np
from math import sqrt


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
