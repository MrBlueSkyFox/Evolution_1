import time

import numpy as np
from lab5.side_functions import random_double, strategy_multiple, selection, fitness_function
from lab5.evolutionary_strategy import EvolutionStrategy
from lab5.evolutionary_strategy import MAX_X, MIN_X, GENERATIONS, CHANGE_DISPERSION
# from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt


def find_nearest_1(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx], idx


def init_multiply(range_pop, n):
    strategy_pull = []
    for i in range(0, range_pop):
        strategy = init_strategy(n)
        strategy_pull.append(strategy)
    return strategy_pull


def init_strategy(n):
    the_strategy = np.zeros([n, 2])
    for i in range(0, n):
        the_strategy[i][0] = random_double(min_x=MIN_X, max_x=MAX_X)
        the_strategy[i][1] = np.around(a=np.random.normal(0, 0.1, 1), decimals=5)
    return EvolutionStrategy(the_strategy)


def reshaped_array(list_of_x, number_of_x):
    array = np.zeros([int(len(list_of_x) / number_of_x), number_of_x])
    j = 0
    for i in range(0, len(list_of_x)):
        array[int(i / number_of_x)][j] = list_of_x[i][0]
        if j + 1 == number_of_x:
            j = 0
        else:
            j += 1
    return array


def disp_repr(list_of_x):
    ans = ''
    for x in list_of_x:
        ans += str(x[1]) + '\n'
    print(ans)


def run_strategy_multiply(pop, generations, variables=2):
    strategies = init_multiply(pop, variables)
    for strategy in strategies:
        print(strategy)
    start_time = time.time()
    for i in range(0, generations):
        b_gen_time = time.time()
        # new_pull = []
        couples = selection(strategies)
        # for j in range(0,len(couples)):
        for pair in couples:
            offspring = strategy_multiple(pair[0], pair[1])
            for el_offspring in offspring:
                strategies.append(EvolutionStrategy(el_offspring))
        fitness_array = []
        for strategy in strategies:
            strategy = strategy.mutation_outside()
            strategy.fitness_value = fitness_function(strategy.list_of_x)
            fitness_array.append(strategy.fitness_value)
        next_generation = []
        # strategies.extend()
        for j in range(0, pop + 1):
            _, index = find_nearest_1(fitness_array, 0)
            # next_generation.append(best_strategy)
            next_generation.append(strategies[index])
            fitness_array.pop(index)
            strategies.pop(index)
        strategies = next_generation
        # for s in strategies:
        #     print(s)
        print("Generation " + str(i) + " time --%s seconds-- " % (time.time() - b_gen_time))
    # for gen in strategies:
    print('Full time ' + " time --%s seconds-- " % (time.time() - start_time))
    # for strategy in strategies:
    #     print(strategy)
    for i in range(0, 1):
        print(strategies[i])


def run_strat_1():
    n = 2
    strategy = init_strategy(n)
    success_change = 0
    C_d = 0.82
    C_i = 1.22
    start_time = time.time()
    check_x_array = strategy.list_of_x
    fit_value = [strategy.fitness_value]
    print(strategy)
    print("Отклонение начальное")
    disp_repr(strategy.list_of_x)
    p_target = 1 / 5
    for i in range(1, GENERATIONS):
        # print("Generation " + str(i) + " take time %s seconds" % (time.time() - start_time))
        check_for_change, check_x_array = strategy.strategy_1_1(fit_value, check_x_array)
        # if check_for_change is None:
        #     success_change = 1
        # else:
        #     success_change = 0
        # for x in strategy.list_of_x:
        #     x[1] *= np.exp(1 / np.sqrt(strategy.number_of_x + 1) * (success_change - p_target) / (1 - p_target))
        if check_for_change is None:
            success_change += 1
        if not (i % CHANGE_DISPERSION):
            if success_change / CHANGE_DISPERSION > 1 / 5:
                for x1 in strategy.list_of_x:
                    x1[1] *= C_i
                    # x1[1] = round(x1[1] * C_i, 8)
                    print('Iter ' + str(i) + " To higher " + str(x1[1]))
            elif success_change / CHANGE_DISPERSION < 1 / 5:
                for x in strategy.list_of_x:
                    x[1] *= C_d
                    # x[1] = round(x[1] * C_d, 8)
                    print('Iter ' + str(i) + " To lower  " + str(x[1]))

            success_change = 0
    print("--- %s seconds ---" % (time.time() - start_time))
    print(strategy)

    print('Отклонение конечное')
    disp_repr(strategy.list_of_x)
    print("len array:= " + str(len(fit_value)))
    array_x = reshaped_array(check_x_array, strategy.number_of_x)
    # for i in range(0, strategy.number_of_x):
    #     plt.figure(i+1)
    #     plt.plot(array_x[:, i], fit_value, 'g^')
    # print('\n')
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    # numpy_fit = np.asarray(fit_value)
    x = array_x[:, 0]
    print(x, '\n')
    ax.scatter(array_x[:, 0], fit_value)
    # plt.plot(array_x[:, 0], fit_value, marker='o')
    # plt.plot(array_x[:, 1], fit_value, 'g^')
    plt.show()


# run_strat_1()
# run_strategy_multiply(30, 100)
run_strategy_multiply(4000, 500, variables=3)
