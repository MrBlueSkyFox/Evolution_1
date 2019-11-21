from lab4.functions import MIN_VALUE, MAX_VALUE, MAX_DEPTH, POPULATION_SIZE

from lab4.ga_tree import GeneticProgrammingTree
import numpy as np


def dt_gen(n):
    f_data = []
    for i in range(0, 101):
        x = np.random.uniform(MIN_VALUE, MAX_VALUE, n)
        ins = np.append(x, fit_new_func(x))
        f_data.append(ins)
    return f_data


def fit_new_func(x):
    out = 0
    for i in x:
        out += i ** 2
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
