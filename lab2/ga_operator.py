import copy
import random
from operator import attrgetter


# from lab2.lab2_main import max_x, min_x


def breeding(species, pop_length):
    of = copy.deepcopy(species)
    offsprings = []
    for s in range(0, pop_length):
        offsprings.append(breeding_one(of))
    return offsprings


def breeding_one(species):
    select1 = round(random.uniform(0, len(species) - 1))
    select2 = round(random.uniform(0, len(species) - 1))
    while select1 == select2:
        select2 = round(random.uniform(0, len(species) - 1))
    if species[select1].fit_fun() > species[select2].fit_fun():
        winner = copy.deepcopy(species[select2])
        del species[select2]
    else:
        winner = copy.deepcopy(species[select1])
        del species[select1]
    return winner


def find_elite(species):
    min_num = min(species, key=attrgetter('fit_val'))
    second_closest = copy.deepcopy(species[0])
    second_closest.fit_val = 999999
    for specie in species:
        if second_closest.fit_fun() > specie.fit_fun() and min_num.fit_fun() != specie.fit_fun():
            second_closest = copy.deepcopy(specie)
    # print('min_num: ', min_num)
    # print('elita 1:= ', first_closest)
    return [second_closest, copy.deepcopy(min_num)]


def couples(species):
    pool = copy.deepcopy(species)
    couple = []
    while len(pool) >= 2:
        a = pool.pop()
        k = random.randint(0, len(pool) - 1)
        b = pool.pop(k)
        couple.append([a, b])
    return couple


def sbx_crossover(specie1, specie2, chance_crossover, flag_for_3n=False):
    p1 = copy.deepcopy(specie1)
    p2 = copy.deepcopy(specie2)
    if random.random() <= chance_crossover:
        u = random.random()
        n = random.uniform(2, 5)
        if u <= 0.5:
            beta = 2 * u * (1 / n + 1)
        else:
            beta = (1 / 2 * (1 - u)) ** (1 / n + 1)
        p1.x1 = 0.5 * (1 - beta) * specie2.f1() + (1 + beta) * specie2.f1()
        p1.x2 = 0.5 * (1 - beta) * specie2.f2() + (1 + beta) * specie2.f2()
        p2.x1 = 0.5 * (1 - beta) * specie1.f1() + (1 + beta) * specie1.f1()
        p2.x2 = 0.5 * (1 - beta) * specie1.f2() + (1 + beta) * specie1.f2()
        if flag_for_3n:
            p1.x3 = 0.5 * (1 - beta) * specie2.f3() + (1 + beta) * specie2.f3()
            p2.x3 = 0.5 * (1 - beta) * specie1.f3() + (1 + beta) * specie1.f3()
        p1_x1_f = check_boundary(p1.x1, p1.min_x, p1.max_x)
        p1_x2_f = check_boundary(p1.x2, p1.min_x, p1.max_x)
        p1_x3_f = check_boundary(p1.x3, p1.min_x, p1.max_x)
        p2_x1_f = check_boundary(p2.x1, p2.min_x, p2.max_x)
        p2_x2_f = check_boundary(p2.x2, p2.min_x, p2.max_x)
        p2_x3_f = check_boundary(p2.x3, p2.min_x, p2.max_x)
        if not (p1_x1_f or p1_x2_f or p1_x3_f or p2_x1_f or p2_x2_f or p2_x3_f):
            return [copy.deepcopy(specie1), copy.deepcopy(specie2)]
    return [p1, p2]


def mutation(specie, chance_mutation, flag_for_3n=False):
    a = copy.deepcopy(specie)
    if random.random() <= chance_mutation:
        a.x1 = round(random.uniform(a.min_x, a.max_x), 5)
    if random.random() <= chance_mutation:
        a.x2 = round(random.uniform(a.min_x, a.max_x), 5)
    if flag_for_3n == True:
        if random.random() <= chance_mutation:
            a.x3 = round(random.uniform(a.min_x, a.max_x), 5)
            if not (check_boundary(a.x3, a.min_x, a.max_x)):
                a.x3 = specie.x3
    if not (check_boundary(a.x1, a.min_x, a.max_x)):
        a.x1 = specie.x1
    if not (check_boundary(a.x2, a.min_x, a.max_x)):
        a.x2 = specie.x2
    return a


def check_boundary(x, min_x, max_x):
    if x > min_x or x < max_x:
        return False
    else:
        return True
