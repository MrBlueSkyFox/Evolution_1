import time

import numpy as np
from lab5.side_functions import random_double
from lab5.evolutionary_strategy import EvolutionStrategy
from lab5.evolutionary_strategy import MAX_X, MIN_X, GENERATIONS, CHANGE_DISPERSION
# from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt


def init_strategy(n):
    the_strategy = np.zeros([n, 2])
    for i in range(0, n):
        the_strategy[i][0] = random_double(min_x=MIN_X, max_x=MAX_X)
        the_strategy[i][1] = np.random.normal(0, 1 / 3, 1)
    # dispersion(the_strategy)
    return EvolutionStrategy(the_strategy)


def reshaped_array(list_of_x, number_of_x):
    d = int(len(list_of_x))
    array = np.zeros([int(len(list_of_x) / number_of_x), number_of_x])
    j = 0
    for i in range(0, len(list_of_x)):
        array[int(i / number_of_x)][j] = list_of_x[i][0]
        if j + 1 == number_of_x:
            j = 0
        else:
            j += 1
    return array


def main():
    n = 3
    strategy = init_strategy(n)
    success_change = 0
    C_d = 0.82
    C_i = 1.22
    start_time = time.time()
    check_x_array = strategy.list_of_x
    fit_value = []
    # for i in range(0, 5):
    fit_value.append(strategy.fitness_value)
    print(strategy)
    for i in range(1, GENERATIONS):
        # print("Generation " + str(i) + " take time %s seconds" % (time.time() - start_time))
        check_for_change, check_x_array = strategy.strategy_1_1(fit_value, check_x_array, )
        if check_for_change is None:
            success_change += 1
        if not (i % CHANGE_DISPERSION):
            if success_change / CHANGE_DISPERSION > 1 / 5:
                for x1 in strategy.list_of_x:
                    x1[1] *= C_i
            elif success_change / CHANGE_DISPERSION < 1 / 5:
                for x in strategy.list_of_x:
                    x[1] *= C_d
            success_change = 0
    print("--- %s seconds ---" % (time.time() - start_time))
    print(strategy)
    # print(check_array)
    print("len array:= " + str(len(fit_value)))
    array_x = reshaped_array(check_x_array, strategy.number_of_x)
    # plt.plot(check_x_array[:, 0], fit_value, 'g^')
    for i in range(0, strategy.number_of_x):
        plt.figure(i)
        plt.plot(array_x[:, i], fit_value, 'g^')
    # print(check_x_array[:, 0])
    # print(check_x_array[:, 1])
    # print(check_x_array[:, 2])
    plt.show()


main()
