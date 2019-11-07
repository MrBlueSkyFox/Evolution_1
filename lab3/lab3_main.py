import operator

from lab3.city import City
from lab3.fitness import Fitness
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import copy


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


def init_dist_matrix(the_list):
    dist_matrix = np.zeros([len(the_list), len(the_list)])
    for i in range(0, len(the_list)):
        for j in range(0, len(the_list)):
            if i == j:
                val = 0
            else:
                val = np.sqrt(
                    (the_list[j].get_x() - the_list[i].get_x()) ** 2 + (the_list[j].get_y() - the_list[i].get_y()) ** 2)
            dist_matrix[i][j] = val
    return dist_matrix


def create_route(the_list):
    route = random.sample(the_list, len(the_list))
    # route.append(copy.deepcopy(route[0]))
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
    return sorted(
        fitness_result_creating.items(), key=operator.itemgetter(1), reverse=True
    )


def selection(popRanked, eliteSize):
    selectionResults = []
    df = pd.DataFrame(np.array(popRanked), columns=["Index", "Fitness"])
    df['cum_sum'] = df.Fitness.cumsum()
    df['cum_perc'] = 100 * df.cum_sum / df.Fitness.sum()

    for i in range(0, eliteSize):
        selectionResults.append(popRanked[i][0])
    for i in range(0, len(popRanked) - eliteSize):
        pick = 100 * random.random()
        for i in range(0, len(popRanked)):
            if pick <= df.iat[i, 3]:
                selectionResults.append(popRanked[i][0])
                break
    return selectionResults


def matingPool(population, selectionResults):
    matingpool = []
    for i in range(0, len(selectionResults)):
        index = selectionResults[i]
        matingpool.append(population[index])
    return matingpool


def breed(parent1, parent2):
    child = []
    childP1 = []
    childP2 = []

    geneA = int(random.random() * len(parent1))
    geneB = int(random.random() * len(parent1))

    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)

    for i in range(startGene, endGene):
        childP1.append(parent1[i])

    childP2 = [item for item in parent2 if item not in childP1]

    child = childP1 + childP2
    return child


def breed_population(mating_pool, elite_size):
    children = []
    length = len(mating_pool) - elite_size
    pool = random.sample(mating_pool, len(mating_pool))

    for i in range(0, elite_size):
        children.append(mating_pool[i])

    for i in range(0, length):
        child = breed(pool[i], pool[len(mating_pool) - i - 1])
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


def mutate_population(population, mutation_rate):
    mutated_pop = []

    for ind in range(0, len(population)):
        mutated_ind = mutate(population[ind], mutation_rate)
        mutated_pop.append(mutated_ind)
    return mutated_pop


def next_generation(current_gen, elite_size, mutation_rate):
    pop_ranked = rank_routes(current_gen)
    selection_results = selection(pop_ranked, elite_size)
    mating_pool = matingPool(current_gen, selection_results)
    children = breed_population(mating_pool, elite_size)
    next_generation_pop = mutate_population(children, mutation_rate)
    return next_generation_pop


def ga(population, pop_size, elite_size, mutation_rate, generations):
    pop = init_route(pop_size, population)
    print("Initial distance: " + str(1 / rank_routes(pop)[0][1]))

    for i in range(0, generations):
        pop = next_generation(pop, elite_size, mutation_rate)

    final_dist = str(1 / rank_routes(pop)[0][1])
    print("Final distance: " + final_dist)
    best_route_index = rank_routes(pop)[0][0]
    best_route_in = pop[best_route_index]
    return best_route_in, final_dist


def ga_plot_process(population, pop_size, elite_size, mutation_rate, generations, process_name='process_default.png'):
    pop = init_route(pop_size, population)
    progress = []
    progress.append(1 / rank_routes(pop)[0][1])
    print('Initial distance: ' + str(1 / rank_routes(pop)[0][1]))
    for i in range(0, generations):
        pop = next_generation(pop, elite_size, mutation_rate)
        progress.append(1 / rank_routes(pop)[0][1])
    final_dist = str(1 / rank_routes(pop)[0][1])
    print("Final distance: " + final_dist)
    best_route_index = rank_routes(pop)[0][0]
    best_route_in = pop[best_route_index]
    fig1, ax1 = plt.subplots()
    ax1.plot(progress)
    ax1.set_ylabel('Distance')
    ax1.set_xlabel('Generation')
    plt.savefig(str(process_name))
    # plt.plot(progress)
    # plt.ylabel('Distance')
    # plt.xlabel('Generation')
    plt.show()
    return best_route_in, final_dist


def ga_plot(routes, name='route_default.png', tittle='default'):
    # x_data, y_data = [(data.x, data.y) for data in route]
    x_data = []
    y_data = []
    plt.figure(num=2, figsize=(9, 9), dpi=400)
    for rout in routes:
        x_data.append(rout.x)
        y_data.append(rout.y)
    for i in range(0, len(routes) - 1):
        plt.plot([routes[i].x, routes[i + 1].x], [routes[i].y, routes[i + 1].y])
    plt.plot([routes[len(routes) - 1].x, routes[0].x], [routes[len(routes) - 1].y, routes[0].y])
    plt.scatter(x_data, y_data)
    plt.title(tittle)
    plt.xlabel('X')
    plt.ylabel('Y')
    # plt.show()
    plt.savefig(str(name))
    plt.close()


start = 20
the_map = init_map()

for i in range(start, start + 10):
    best_route, dist_tittle = ga_plot_process(population=the_map, pop_size=200, elite_size=20, mutation_rate=0.01,
                                              generations=400, process_name=str("test_progress_" + str(i)))
    ga_plot(best_route, name=str('test_route_with_progress_' + str(i)), tittle=dist_tittle)
