from lab4.functions import MIN_VALUE, MAX_VALUE, MAX_DEPTH, POPULATION_SIZE

from lab4.ga_tree import GeneticProgrammingTree
import numpy as np


def dataset_generate():
    ds_data = [[MIN_VALUE,
                fitness_function(MIN_VALUE, MIN_VALUE, MIN_VALUE, MIN_VALUE, MIN_VALUE, MIN_VALUE, MIN_VALUE,
                                 MIN_VALUE, MIN_VALUE, MIN_VALUE)], [MAX_VALUE,
                                                                     fitness_function(MAX_VALUE, MAX_VALUE, MAX_VALUE,
                                                                                      MAX_VALUE, MAX_VALUE, MAX_VALUE,
                                                                                      MAX_VALUE,
                                                                                      MAX_VALUE, MAX_VALUE, MAX_VALUE)]]
    return ds_data


def bit_dataset_generate():
    f_data = []
    range_f = np.linspace(MIN_VALUE, MAX_VALUE, num=8, endpoint=True)
    for x in range_f:
        f_data.append([x, fitness_function(x, x, x, x, x, x, x, x, x, x)])
    return f_data


def fitness_function(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10):
    out = (
            x1 ** 2 + x2 ** 2 + x3 ** 2 + x4 ** 2 + x4 ** 2 + x4 ** 2 + x5 ** 2 + x6 ** 2 + x7 ** 2 + x8 ** 2 + x9 ** 2 + x10 ** 2)
    return out


def initialization_population():
    pop = []
    for current_max_depth in range(4, MAX_DEPTH + 1):
        for i in range(int(POPULATION_SIZE / 6)):
            t = GeneticProgrammingTree()
            # t.generate_tree(full_type=True, max_depth=current_max_depth)
            t.generate_full_tree(max_depth=current_max_depth)
            pop.append(t)
        for j in range(int(POPULATION_SIZE / 6)):
            t = GeneticProgrammingTree()
            t.generate_grow_tree(max_depth=current_max_depth)
            # t.generate_tree(full_type=False, max_depth=current_max_depth)
            pop.append(t)
    return pop
