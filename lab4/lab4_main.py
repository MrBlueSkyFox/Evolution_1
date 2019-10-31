import random
from lab4.ga_tree import GeneticProgrammingTree, fitness_function, MAX_DEPTH, POPULATION_SIZE, TERMINALS
from lab4.Genetic_programming_operators import fitness, selection, crossover, mutation
from lab4.functions import MAX_VALUE, MIN_VALUE, GENERATIONS
import numpy as np
# import matplotlib.pyplot as plt
# import math
import copy
import time


def main():
    func_pop = dataset_generate()
    population = init_pop()
    # print(population[0].print_tree_node())
    # print('-----')
    fit_time = time.time()
    fitness_data = [fitness(population[i], func_pop) for i in range(len(population))]
    print("--- %s seconds ---" % (time.time() - start_time))
    print("--- %s seconds ---" % (time.time() - fit_time))
    print("--- %s seconds ---" % (fit_time - start_time))
    best_of_run = None
    best_of_run_f = 0
    best_of_run_gen = 0
    for generation in range(GENERATIONS):
        generation_time_start = time.time()
        next_population = []
        for i in range(POPULATION_SIZE):
            parent1 = selection(population, fitness_data)
            parent2 = selection(population, fitness_data)
            crossover(parent1, parent2)
            mutation(parent1)
            next_population.append(parent1)
        population = next_population
        fitness_data = [fitness(population[i], func_pop) for i in range(len(population))]
        print("Generation: ", generation, " time --%s seconds--" % (time.time() - generation_time_start))
        if max(fitness_data) > best_of_run_f:
            best_of_run_f = max(fitness_data)
            best_of_run_gen = generation
            best_of_run = copy.deepcopy(population[fitness_data.index(max(fitness_data))])
            print('_______________________')
            print("geneneration: ", generation, " best_of_run: ", round(max(fitness_data), 3), ', best_of_run:')
            best_of_run.print_tree_node()
        if best_of_run == 1: break
    print("\n\n_________________________________________________\nEND OF RUN\nbest_of_run attained at gen " + str(
        best_of_run_gen) + \
          " and has f=" + str(round(best_of_run_f, 3)))
    s = "\n\nbest_of_run attained at gen " + str(best_of_run_gen) + "  " + str(round(best_of_run_f, 3))
    best_of_run.print_tree_node()
    best_of_run.draw_tree("best_of_run_" + str(5), s)
    print('---%s sec for ALL' % (time.time() - fit_time))


def fitness_data_generate():
    f_data = []
    range_f = np.linspace(MIN_VALUE, MAX_VALUE, num=300, endpoint=True)
    for x in range_f:
        f_data.append([x, fitness_function(x, x, x, x, x, x, x, x, x, x)])
    return f_data


def dataset_generate():
    ds_data = [[MIN_VALUE,
                fitness_function(MIN_VALUE, MIN_VALUE, MIN_VALUE, MIN_VALUE, MIN_VALUE, MIN_VALUE, MIN_VALUE,
                                 MIN_VALUE, MIN_VALUE, MIN_VALUE)], [MAX_VALUE,
                                                                     fitness_function(MAX_VALUE, MAX_VALUE, MAX_VALUE,
                                                                                      MAX_VALUE, MAX_VALUE, MAX_VALUE,
                                                                                      MAX_VALUE,
                                                                                      MAX_VALUE, MAX_VALUE, MAX_VALUE)]]
    return ds_data


def init_pop():
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


start_time = time.time()
main()

# if any('x5' in s for s in TERMINALS[0:len(TERMINALS)-1]):
#     print('x1-2')
# x = 4000000
# d = np.exp(x)
# c = d / 1000
# print(d)
# print(c)
# print(math.exp(x))
# a = math.exp(5.12)
# a1 = np.exp(5.12)
# print('Экопонента от 5.12 ', a)
# print('Экопонента от 5.12 ,np', a1)
# b = math.exp(a)
# b1 = np.exp(a1)
# print('Экспонента от первой экоспеннты ', b)
# print('Экспонента от первой экоспеннты ', b1)
# try:
#     c = np.exp(b1)
#     # c1 = math.exp(b)
# except OverflowError:
#     print('too big')
# else:
#     print('Run')
