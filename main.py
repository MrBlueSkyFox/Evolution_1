import numpy as np
import random

from tigr import fromint, toint, fit_function

max_x = -10
min_x = 10
n = 16


#  TODO
# Оснвной алгоритм действий :
# * Реализовать 3 оператора ГА
# 6)Генерация 10-го числа в пределах заданых рамок(границ функции)
# 4)Сделать функция перехода из 10-го вида в 2-ый
# 5)Сделать функцию перехода из 2-го в 10-ый
# 3)Реализовать оператор mutate(мутация)
# 1)Реализовать оператор fintes(финтес функция)(репродукция)
# 2)Реализовать оператор crossover(кроссинговер)
# 7)Сделать функция для псевдоРандомного выборо точки для выбора точки кроссовинга(ОК),
#   которая также будут работать для ОМ в инверсии бита
# 8)Функция создающая матрицу на основе заданной начальной популяции и заполняющяя её рандомными значениями
# (инициализация другими словами)
def initialize(N):
    pop_map = np.zeros((N, 2))
    for i in range(0, N):
        pop_map[i][0] = random_number(min_x, max_x)
        pop_map[i][1] = fit_function(pop_map[i][0])
        # for j in range(0, 2):
        #     pop_map[i][j] = random_number(min_x, max_x)
        #     pop_map[j][i] = pop_map[i][j]
    return pop_map


# 6)Генерация 10-го числа в рамках функции
def random_number(min, max):
    return round(random.uniform(min, max), 5)


# 1)Реализовать оператор fintes(финтес функция)(репродукция)
def op_reproduction(the_pop_map):
    # Найтри средне значение финтекс функции ддя всех хромосом :
    # (сложить значения всех финтекс функций и поделить на кол-во родителей)
    # Для каждой хромосомы найти вероятность попадания в пул родителей :
    # Взять Значения финтес функции поделить на среднее от финтекс функции,
    # Полученная цифра определяет вероятность того что хромосома попадет в пул родителей ,
    # если меньше 0.50 -> ни одного  обычные правилы округления
    parent_chance = np.zeros((len(the_pop_map), 1))
    # print("lengh: ", len(the_pop_map))
    for i in range(0, len(the_pop_map)):
        parent_chance[i][0] = abs(the_pop_map[i][1])
    # print(parent_chance)
    medium_f = np.sum(parent_chance, axis=0)
    print(medium_f, ' medium function')
    for i in range(0, len(the_pop_map)):
        print(parent_chance[i][0])
        parent_chance[i][0] = parent_chance[i][0] / medium_f
    print(parent_chance, ' array after calc')
    parent_chance = (np.around(parent_chance, decimals=2))
    print(parent_chance, ' array after round calc')
    print(np.sum(parent_chance, axis=0, dtype=float), ' summ')
    return 1


def op_repr(source_map):
    parent_chance = np.zeros((len(source_map), 1))
    for i in range(0, len(source_map)):
        parent_chance[i][0] = (source_map[i][1])
    min_fitness = np.amin(parent_chance)
    sum_fitness = np.sum(parent_chance) - min_fitness
    rnd = random.random() * sum_fitness
    csum = 0
    for s in parent_chance:
        csum=csum+parent_chance[s][0]-min_fitness
        if csum>=rnd:
            return s
    print(parent_chance)
    print(min_fitness)
    return 1


work_map = initialize(13)
print(work_map)
op_repr(work_map)
