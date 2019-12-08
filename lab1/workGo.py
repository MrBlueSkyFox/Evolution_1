from lab1.GeneticAlg import GeneticAlg
from lab1.GeneticAlg import breeding, couples, crossover, mutate
import numpy as np
import math
import matplotlib.pyplot as plt

# max_x = 10
# min_x = -10
max_x = 10
min_x = 0.5
n = 16


def init(number_species):
    map_s = []
    for i in range(0, number_species):
        specie = GeneticAlg(min_x, max_x, n)
        map_s.append(specie)
    return map_s


def generation(map_s):
    pop_len = len(map_s)
    chanceOfMutation = 0.1
    chanceOfCrossover = 0.9
    offsp_map = breeding(map_s)
    # for i in range(0, len(map_s)):
    #     print(map_source[i].f(), "  ", offsp_map[i].f())
    print('Размножение')
    print(offsp_map)
    pairs = couples(offsp_map)
    cros = []
    for pair in pairs:
        # print(pair[0])
        cros.extend(crossover(pair[0], pair[1], pop_len, chanceOfCrossover))
    print('Кроссинговер')
    for c in cros:
        c.x = c.from_int()
    print(cros)
    for cd in cros:
        cd.x = cd.to_int()
    mutation = []

    for mut in cros:
        mutation.append(mutate(mut, pop_len, chanceOfMutation))
    for m in mutation:
        m.x = m.from_int()
    print('Мутация')
    print(mutation)

    return mutation


def main_1():
    pop_len = 20
    map_source = init(pop_len)
    x_start = []
    y_start = []
    for x in map_source:
        x_start.append(x.x)
        y_start.append(x.fit_func())
    for i in range(0, 50):
        print('Generation ' + str(i))
        map_source = generation(map_source)
        print("\n")
    ylist = []
    xlist = []
    for x in map_source:
        xlist.append(x.x)
        ylist.append(x.fit_func())
    _, ax = plt.subplots()
    # x_graf = np.arange(-10, 10, 0.1)
    x_graf = np.arange(0.5, 10, 0.1)
    y_graf = []
    for x in x_graf:
        # y_graf.append((1.85 - x) * math.cos(3.5 * x - 0.5))
        y_graf.append(
            math.sin(x) / (1 + math.exp(-x))
        )
    ax.plot(x_graf, y_graf, lw=2, color='red')
    ax.plot(xlist, ylist, 'g^')
    ax.plot(x_start, y_start, 'bs')
    # ax.set_title("(1.85-x)*cos(3.5*x-0.5)")
    ax.set_title("sin(x) / (1+ exp(-x))")
    ax.set_ylabel('fin function val')
    ax.set_xlabel('x value')
    plt.show()


main_1()
