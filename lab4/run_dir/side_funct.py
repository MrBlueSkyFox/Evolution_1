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
    range_f = np.linspace(MIN_VALUE, MAX_VALUE, num=80, endpoint=True)
    for x in range_f:
        f_data.append([x, fitness_function(x, x, x, x, x, x, x, x, x, x)])
    return f_data


def dt_gen():
    f_data = []
    for i in range(0, 120):
        x = np.random.uniform(MIN_VALUE, MAX_VALUE, 2)
        ins = np.append(x, fit_new_func(x))
        f_data.append(ins)
        print(
            ins
        )
    return f_data


def fit_new_func(x):
    out = 0
    for i in x:
        out += i ** 2
    return out


def second_impl_dataset_generate():
    dataset = []
    for x in range(-100, 101, 2):
        x /= 100
        dataset.append([x, fitness_function(x, x, x, x, x, x, x, x, x, x)])
    return dataset


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


def init_pop_test():
    pop = []
    for i in range(int(POPULATION_SIZE / 2)):
        t = GeneticProgrammingTree()
        t.generate_full_tree(max_depth=MAX_DEPTH)
        pop.append(t)
    for j in range(int(POPULATION_SIZE / 2)):
        t = GeneticProgrammingTree()
        t.generate_grow_tree(max_depth=MAX_DEPTH)
        pop.append(t)
    return pop
