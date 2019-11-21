import copy
import time

import numpy as np

from lab4.Genetic_programming_operators import selection, crossover, fitness, mutation
from lab4.functions import POPULATION_SIZE, GENERATIONS, TERMINALS
from lab4.run_dir.side_funct import initialization_population, dt_gen


def find_nearest_1(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx], idx


def find_nearest(collection, num):
    return min(collection, key=lambda x: abs(x - num))


def next_generation(count_generation, population, fitness_data, dataset, best_of_run, best_of_run_f, best_of_run_gen):
    generation_time_start = time.time()
    next_population = []
    for i in range(POPULATION_SIZE):
        parent1 = selection(population, fitness_data)
        parent2 = selection(population, fitness_data)
        crossover(parent1, parent2)
        mutation(parent1)
        next_population.append(parent1)
    fitness_data = [fitness(population[i], dataset) for i in range(len(population))]
    print("Generation: ", count_generation, " time --%s seconds--" % (time.time() - generation_time_start))
    if min(fitness_data) < best_of_run_f:
        best_of_run_f, index = find_nearest_1(fitness_data, 0.0)
        best_of_run_gen = count_generation
        best_of_run = copy.deepcopy(population[index])
        print('_______________________')
        print("geneneration: ", count_generation, " best_of_run: ", round(best_of_run_f, 3))
        best_of_run.print_tree_node()

    return next_population, best_of_run, best_of_run_f, best_of_run_gen


def main(uniq_name_prefix="3"):
    dataset = dt_gen(len(TERMINALS))
    population = initialization_population()
    fit_time = time.time()
    fitness_data = [fitness(population[i], dataset) for i in range(len(population))]
    print("--- %s seconds ---" % (time.time() - fit_time))
    best_of_run = None
    best_of_run_f = 9999
    best_of_run_gen = 0
    for generation in range(GENERATIONS):
        population, best_of_run, best_of_run_f, best_of_run_gen = next_generation(population=population,
                                                                                  fitness_data=fitness_data,
                                                                                  dataset=dataset,
                                                                                  best_of_run=best_of_run,
                                                                                  best_of_run_f=best_of_run_f,
                                                                                  best_of_run_gen=best_of_run_gen,
                                                                                  count_generation=generation)
        if abs(best_of_run_f) <= 0.000000001:
            break
    print("\n\n_________________________________________________\nEND OF RUN\nbest_of_run attained at gen " + str(
        best_of_run_gen) +
          " and has f=" + str(round(best_of_run_f, 3)))
    message = "\n\nbest_of_run attained at gen " + str(best_of_run_gen) + "  " + str(round(best_of_run_f, 3))
    best_of_run.print_tree_node()
    # best_of_run.draw_tree("best_of_run_" + str(uniq_name_prefix), message)
    best_of_run.draw_tree(str(uniq_name_prefix), message)
    print('---%s sec for ALL' % (time.time() - fit_time))
    for x in dataset:
        print("tree val= " + str(best_of_run.comp_sec(x)) + " function val= " + str(x[len(x) - 1]))


# main('gen=100,pop=100,max_depth=15,func=3')
# main('test_depth=12,pop=80')
# main('depth=13,pop=80,funct=2')
# main('depth=13,pop=80,funct=2,Gen=600')
# main('depth=10,pop=80,funct=2,Gen=600,mut=0.01_test')
# main('fintess1/depth=13,pop=250')
# main('fintess1/max_d=11,min_d=6,pop=80')
main('fintess1/fourth_var')
