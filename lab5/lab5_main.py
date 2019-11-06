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
        the_strategy[i][1] = np.around(a=np.random.normal(0, 1, 1), decimals=5)
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


def main():
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
                    # x1[1] *= C_i
                    x1[1] = round(x1[1] * C_i, 5)
            elif success_change / CHANGE_DISPERSION < 1 / 5:
                for x in strategy.list_of_x:
                    # x[1] *= C_d
                    x[1] = round(x[1] * C_d, 5)

            success_change = 0
    print("--- %s seconds ---" % (time.time() - start_time))
    print(strategy)

    print('Отклонение конечное')
    disp_repr(strategy.list_of_x)
    print("len array:= " + str(len(fit_value)))
    array_x = reshaped_array(check_x_array, strategy.number_of_x)
    for i in range(0, strategy.number_of_x):
        plt.figure(i)
        plt.plot(array_x[:, i], fit_value, 'g^')
    print('\n')
    plt.show()


main()
