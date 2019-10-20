import math
import random
import copy
# из 10 в 2
#Добавить в конце bin(x)
def toint(x, minx, maxx, n):
    x = float(x)
    minx = float(minx)
    maxx = float(maxx)
    x = x - minx
    x = x / (maxx - minx)
    x = int(round(x * 2 ** n))
    return x


# из 2 в 10
def fromint(x, minx, maxx, n):
    minx = float(minx)
    maxx = float(maxx)
    x = float(x) / 2 ** n
    x = x * (maxx - minx)
    x = x + minx
    return x


# Финтес функция
def fit_function(x):
    return (1.85 - x) * math.cos(3.5 * x - 0.5)


# x = -7
# minx = -10
# maxx = 10
# n = 16
#
# x1 = toint(x, minx, maxx, n)
# print(bin(x1))
# x2 = fromint(x1, minx, maxx, n)
# print(x2)
def reproductOne(species):
    sum = 0
    min = float("inf")
    # Сначала находим минимум, чтобы иметь детерминированную
    # работу в ситуации с отрицательными числами.
    for s in species:
        if s.f() < min:
            min = s.f()
    # Находим сумму всех f с учётом минимума
    for s in species:
        sum = sum + s.f() - min
    # Генерируем случайное число в пределах [0; sum]
    rnd = random.random() * sum
    csum = 0
    for s in species:
        csum = csum + s.f() - min
        if csum >= rnd:
            return copy.deepcopy(s)


def reproduct(species):
    offsprings = []
    for s in species:
        offsprings.append(reproductOne(species))
    return offsprings
