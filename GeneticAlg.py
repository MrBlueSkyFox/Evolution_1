import math
import random
import copy


def random_number(min_x, max_x):
    return round(random.uniform(min_x, max_x), 5)


def breeding(species):
    offsprings = []
    for s in species:
        offsprings.append(breeding_one(species))
    return offsprings


def breeding_one(species):
    sum_fit_func = 0
    min_fit_func = float("inf")
    for s in species:
        if s.fit_func() < min_fit_func:
            min_fit_func = s.fit_func()
    for s in species:
        sum_fit_func = sum_fit_func + s.fit_func() - min_fit_func
    rnd = random.random() * sum_fit_func
    csum = 0
    for s in species:
        csum = csum + s.fit_func() - min_fit_func
        if csum >= rnd:
            return copy.deepcopy(s)


def couples(species):
    pool = copy.deepcopy(species)
    couple = []
    while (len(pool) >= 2):
        a = pool.pop()
        k = random.randint(0, len(pool) - 1)
        b = pool.pop(k)
        couple.append([a, b])
    return couple


def crossover(specie1, specie2, pop_len, chance_of_crossover):
    k = random.randint(0, pop_len - 1)
    a = copy.deepcopy(specie1)
    b = copy.deepcopy(specie2)
    # print(k, " k val")
    if random.random() <= chance_of_crossover:
        # print(specie1.x, " spec1 x ", bin(specie1.to_int()), ' spec1 x_bin')
        # print(specie2.x, " spec2 x ", bin(specie2.to_int()), ' spec2 x_bin')
        # print('-----')
        #  print(sd, "  a to bin ", sd << k, " <<k")
        # print(s, " int")
        a.x = (a.to_int() & (~(1 << k))) | (specie2.to_int() & (1 << k))
        b.x = (b.to_int() & (~(1 << k))) | (specie1.to_int() & (1 << k))
        # print(bin(a.x), " a.x_bin ", a.from_int(), " a.int ")
        # print(bin(b.x), " b.x_bin ", b.from_int(), " b.int")
        if (a.from_int() > a.max_x or a.from_int() < a.min_x):
            a.x = specie1.to_int()
        if (b.from_int() > b.max_x or b.from_int() < b.min_x):
            b.x = specie2.to_int()
    return [a, b]


def mutate(specie, pop_len, chance_of_mutation):
    k = random.randint(0, pop_len - 1)
    a = copy.deepcopy(specie)
    if random.random() <= chance_of_mutation:
        a.x = a.x ^ (1 << k)
    if (a.from_int() > a.max_x or a.from_int() < a.min_x):
        a = copy.deepcopy(specie)
    return a


#   if random.random()<=chance_of_crossover:


class GeneticAlg:
    def __init__(self, min_x, max_x, n):
        self.min_x = min_x
        self.max_x = max_x
        self.n = n
        self.x = random_number(min_x, max_x)

    def __repr__(self):
        return "Specie : x= " + str(self.f()) + " f(x)= " + str(self.fit_func())

    def f(self):
        return self.x

    def fit_func(self):
        return (1.85 - self.x) * math.cos(3.5 * self.x - 0.5)

    def to_int(self):
        x = float(self.x)
        minx = float(self.min_x)
        maxx = float(self.max_x)
        x = x - minx
        x = x / (maxx - minx)
        x = int(round(x * 2 ** self.n))
        return x

    def from_int(self):
        minx = float(self.min_x)
        maxx = float(self.max_x)
        x = self.x
        x = float(x) / 2 ** self.n
        x = x * (maxx - minx)
        x = x + minx
        return x
