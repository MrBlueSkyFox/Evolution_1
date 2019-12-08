import random

from lab2.specie import Specie, f

# from lab2.ga_operator import find_elite, breeding,couples,sbx_crossover,mutation
from lab2.ga_operator import *
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np

max_x = 1
min_x = -1


def init(n, flag=False):
    map_s = []
    for i in range(0, n):
        specie = Specie(min_x, max_x, flag)
        map_s.append(specie)
    # for m in map_s:
    #     print('x1= ', m.f1(), ' x2= ', m.f2(), ' x3= ', m.f3(), ' fit_val= ', m.fit_fun())
    return map_s


def generation(map_species, n3, max_pop=50):
    chance_of_mutation = 0.1
    chance_of_crossover = 0.9
    pop_length = max_pop
    elite_map = find_elite(map_species)
    offspring_map = breeding(map_species, pop_length)
    offspring_map.extend(elite_map)
    # print('Размножение')
    # print(offspring_map)
    pairs = couples(offspring_map)
    crossover = []
    for pair in pairs:
        crossover.extend(sbx_crossover(pair[0], pair[1], chance_of_crossover, n3))
    # print('Кроссовер')
    # print(crossover)
    mut_map = []
    for mut in crossover:
        mut_map.append(mutation(mut, chance_of_mutation, n3))
    # print('Мутация')
    # print(mut_map)
    return mut_map


# def f(x, y):
#     return x ** 2 + y ** 2


def main(start=100, pop_max=40, generation_max=100, flag_3n=False):
    the_map = init(start, flag_3n)
    x_start = np.zeros((len(the_map) - 1))
    y_start = np.zeros((len(the_map) - 1))
    z_start = np.zeros((len(the_map) - 1))
    # y_start = np.arange(len(the_map) - 1)
    for i in range(0, len(the_map) - 1):
        x_start[i] = the_map[i].x1
        y_start[i] = the_map[i].x2
        z_start[i] = f(x_start[i], y_start[i])
    # z_start = f(x_start, y_start)

    for i in range(0, generation_max):
        print('Generation ' + str(i))
        the_map = generation(the_map, flag_3n, pop_max)
        # print('\n')
    # x = np.linspace(-5.12, 5.12, 100)
    # y = np.linspace(-5.12, 5.12, 100)
    print(the_map)
    x = np.linspace(-20, 20, 100)
    y = np.linspace(-20, 20, 100)
    X, Y = np.meshgrid(x, y)
    Z = np.zeros((100, 100))
    for i in range(0, X.shape[0]):
        for j in range(0, X.shape[1]):
            Z[i][j] = f(X[i][j], Y[i][j])

    # Z = f(X, Y)
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                    cmap='viridis', edgecolor='none')
    xdata = np.zeros((len(the_map) - 1))
    ydata = np.zeros((len(the_map) - 1))
    zdata = np.zeros((len(the_map) - 1))
    for i in range(0, len(the_map) - 1):
        xdata[i] = the_map[i].f1()
        ydata[i] = the_map[i].f2()
        zdata[i] = f(xdata[i], y_start[i])
    # zdata = f(xdata, ydata)
    ax.scatter3D(xdata, ydata, zdata, marker='o')
    ax.scatter3D(x_start, y_start, z_start, marker='^')
    # tittle = 'De Jo`s I '
    tittle = 'Ackley \' s Path function 10'
    if flag_3n:
        tittle += ' with 3n'
    ax.set_title(tittle)
    ax.set_xlabel('x1')
    ax.set_ylabel('x2')
    ax.set_zlabel('fit_func')

    plt.show()


main(start=200, pop_max=60, generation_max=4)
main(start=200, pop_max=60, generation_max=200, flag_3n=True)
# main(True)
