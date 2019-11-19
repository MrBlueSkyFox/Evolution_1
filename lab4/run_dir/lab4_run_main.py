from lab4.Genetic_programming_operators import selection, crossover, \
    cut_mutation, fitness, mutation
from lab4.run_dir.side_funct import initialization_population, bit_dataset_generate, \
    second_impl_dataset_generate, init_pop_test, dataset_generate
from lab4.functions import POPULATION_SIZE, GENERATIONS
import time
import copy
import numpy as np


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
        # cut_mutation(parent1)
        next_population.append(parent1)
    # population = next_population
    fitness_data = [fitness(population[i], dataset) for i in range(len(population))]
    # maximus = max(fitness_data)
    print("Generation: ", count_generation, " time --%s seconds--" % (time.time() - generation_time_start))
    # # if (find_nearest(fitness_data, 1.0)) > best_of_run_f:
    if abs((find_nearest_1(fitness_data, 1.0)[0]) - 1) < abs(best_of_run_f - 1):
        # d = find_nearest(fitness_data, 1)
        best_of_run_f, index = find_nearest_1(fitness_data, 1.0)
        best_of_run_gen = count_generation
        # best_of_run = copy.deepcopy(
        #     population[fitness_data.index(min(fitness_data, key=lambda x: abs(x - best_of_run_f)))])
        best_of_run = copy.deepcopy(population[index])
        print('_______________________')
        print("geneneration: ", count_generation, " best_of_run: ", round(best_of_run_f, 3))
        # best_of_run.print_tree_node()
    # if max(fitness_data) > best_of_run_f:
    #     best_of_run_f = max(fitness_data)
    #     best_of_run_gen = count_generation
    #     best_of_run = copy.deepcopy(population[fitness_data.index(max(fitness_data))])
    #     print('_______________________')
    #     print("geneneration: ", count_generation, " best_of_run: ", round(max(fitness_data), 3), ', best_of_run tree:')
    #     best_of_run.print_tree_node()
    # if best_of_run == 1

    return next_population, best_of_run, best_of_run_f, best_of_run_gen

    # if max(fitness_data) > best_of_run_f:
    #     best_of_run_f = max(fitness_data)
    #     best_of_run_gen = count_generation
    #     best_of_run = copy.deepcopy(population[fitness_data.index(max(fitness_data))])
    #     print('_______________________')
    #     print("geneneration: ", count_generation, " best_of_run: ", round(max(fitness_data), 3))
    #     best_of_run.print_tree_node()
    # return next_population, best_of_run, best_of_run_f, best_of_run_gen
    # if best_of_run == 1: break


def main(uniq_name_prefix="3"):
    # dataset = dataset_generate()
    dataset = bit_dataset_generate()
    population = initialization_population()
    fit_time = time.time()
    fitness_data = [fitness(population[i], dataset) for i in range(len(population))]
    print("--- %s seconds ---" % (time.time() - fit_time))
    best_of_run = None
    best_of_run_f = 0
    best_of_run_gen = 0
    for generation in range(GENERATIONS):
        population, best_of_run, best_of_run_f, best_of_run_gen = next_generation(population=population,
                                                                                  fitness_data=fitness_data,
                                                                                  dataset=dataset,
                                                                                  best_of_run=best_of_run,
                                                                                  best_of_run_f=best_of_run_f,
                                                                                  best_of_run_gen=best_of_run_gen,
                                                                                  count_generation=generation)
        if best_of_run == 1:
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
        print("x= " + str(x[0]) + " tree val= " + str(best_of_run.compute_tree(x[0])) + " function val= " + str(x[1]))


# main('gen=100,pop=100,max_depth=15,func=3')
# main('test_depth=12,pop=80')
# main('depth=13,pop=80,funct=2')
# main('depth=13,pop=80,funct=2,Gen=600')
# main('depth=10,pop=80,funct=2,Gen=600,mut=0.01_test')
main('fintess1/depth=13,pop=250')
