import operator

from lab3.city import City
from lab3.fitness import Fitness
import random
import copy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def init_map():
    path = '/home/tigran/PycharmProjects/Evolution_1/lab3/inputData.txt'
    data_file = open(path, 'r')
    list_matrix = data_file.readlines()
    data_file.close()
    city_map = []
    for i in list_matrix:
        row = i.split()
        city = City(row[1], row[2], row[0])
        city_map.append(city)
    return city_map


def create_route(the_list):
    route = random.sample(the_list, len(the_list))
    return route


def init_route(city_size, the_list):
    route_map_creating = []
    for i in range(0, city_size):
        route_map_creating.append(create_route(the_list))
    return route_map_creating


def rank_routes(the_list):
    fitness_result_creating = {}
    for i in range(0, len(the_list)):
        fitness_result_creating[i] = Fitness(the_list[i]).route_fitness()
    # for i in the_list:
    #     fitness_result_creating.append(Fitness(i))
    return sorted(
        fitness_result_creating.items(), key=operator.itemgetter(1), reverse=True
    )
    # return fitness_result_creating
    # return sorted(fitness_result_creating, key=lambda fitness: fitness.distance
    #               )


def selection(pop_ranked, elite_size):
    selected = []
    df = pd.DataFrame(np.array(pop_ranked), columns=["Index", "Fitness"])
    df['cum_sum'] = df.Fitness.cumsum()
    df['cum_perc'] = 100 * df.cum_sum / df.Fitness.sum()
    for i in range(0, elite_size):
        selected.append(pop_ranked[i][0])
    for i in range(0, len(pop_ranked) - elite_size):
        pick = 100 * random.random()
        for j in range(0, len(pop_ranked)):
            if pick <= df.iat[i, 3]:
                selected.append(pop_ranked[i][0])
                break
    return selected


def couples(population, selected_res):
    couples_pool = []
    for i in range(0, len(selected_res)):
        index = selected_res[i]
        couples_pool.append(population[index])
    return couples_pool


def breed(parent1, parent2):
    child = []
    childP1 = []
    childP2 = []

    gen_a = int(random.random() * len(parent1))
    gen_b = int(random.random() * len(parent2))

    start_gen = min(gen_a, gen_b)
    end_gen = max(gen_a, gen_b)
    for i in range(start_gen, end_gen):
        childP1.append(parent1[i])
    childP2 = [item for item in parent2 if item not in childP2]

    child = childP1 + childP2
    return child


def breeding(couple_pool, elite_size, chance_crossover=1):
    children = []
    lenght = len(couple_pool) - elite_size
    pool = random.sample(couple_pool, len(couple_pool))

    for i in range(0, elite_size):
        children.append(couple_pool[i])
    for i in range(0, lenght):
        if 0.2 <= chance_crossover:
            child = breed(pool[i], pool[len(couple_pool) - i - 1])
        else:
            child = pool[i]
        children.append(child)
    return children


def mutate(individual, mutation_rate):
    for swapped in range(len(individual)):
        if random.random() < mutation_rate:
            swap_with = int(random.random() * len(individual))

            city1 = individual[swapped]
            city2 = individual[swap_with]

            individual[swapped] = city2
            individual[swap_with] = city1
    return individual


def mutate_population(children, mutation_rate=0.1):
    mutated_population = []
    for i in range(0, len(children)):
        mutated_ind = mutate(children[i], mutation_rate)
        mutated_population.append(mutated_ind)
    return mutated_population


def next_generation(current_gen, elite_size, mutation_rate, crossover_chance):
    pop_ranked = rank_routes(current_gen)
    selection_res = selection(pop_ranked, elite_size)
    couples_pool = couples(current_gen, selection_res)
    children = breeding(couples_pool, elite_size, crossover_chance)
    next_population = mutate_population(children, mutation_rate)
    return next_population


def ga(the_list, pop_size, elite_size, mutation_rate, chance_of_crossover, generations):
    pop = init_route(pop_size, the_list)
    print("Init dist " + str(1 / rank_routes(pop)[0][1]))
    for i in range(0, generations):
        pop = next_generation(pop, elite_size, mutation_rate, chance_of_crossover)
    print("End dist " + str(1 / rank_routes(pop)[0][1]))
    best_route_index = rank_routes(pop)[0][0]
    best_route = pop[best_route_index]
    return best_route


def ga_plot(best_route):
    # plt.scatter(best_route)
    plt.ylabel('Dist')
    plt.xlabel('Generation')
    plt.show()


the_map = init_map()
best_result = ga(the_list=the_map, pop_size=40, elite_size=4, mutation_rate=0.1, chance_of_crossover=1,
                 generations=100)
ga_plot(best_result)
print(best_result)
