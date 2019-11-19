from statistics import mean

from lab4.functions import TOURNAMENT_SIZE, CROSSOVER_CHANCE, MUTATE_CHANCE
import copy
import random


def fitness(individual, dataset):
    # check = decimal.Decimal(dataset[0][0] - dataset[0][1])
    # for d in dataset:
    #     f = Decimal(d[0])
    #     s = Decimal(d[1])
    #     res = f - s
    # inverse mean absolute error over dataset normalized to [0,1]
    # a = []
    # for d in dataset:
    #     a.append(abs(individual.compute_tree((d[0]) - d[1])))
    # Как узнать насколько подходит дерево? подсчитать его результат.Сравнить результат с тем же значением
    # Каждый вычисленный резлуьтат поместить в 2 массива ( 1 для дерева решений,другой для моей фитнес функции) взять среднее каждого из массивов
    # поделить  a/b ,a- функции по дереву ,b- моя фитнес функция сравнивать лучше,кто ближе к 1
    tree_value = []
    fitness_value = []
    for ds in dataset:
        tree_value.append(individual.compute_tree(ds[0]))
        fitness_value.append(ds[1])
    a = mean(tree_value)
    b = mean(fitness_value)
    if 0.9 <= a / b <= 1.2:
        individual.print_tree_node()
    return mean(tree_value) / mean(fitness_value)
    # (mean([individual.compute_tree(ds[0]) for ds in dataset])) / (mean([ds[1] for ds in dataset]))
    # return 1 / (1 + mean([abs(individual.compute_tree((ds[0]) - (ds[1]))) for ds in dataset]))


# def fitness(individual, dataset, BLOAT_CONTROL=True):
#     if BLOAT_CONTROL:
#         return 1 / (1 + error(individual, dataset) + 0.01 * individual.size())
#     else:
#         return 1 / (1 + error(individual, dataset))
#

def error(individual, dataset):
    return mean([abs(individual.compute_tree(ds[0]) - ds[1]) for ds in dataset])


def selection(population, fitness_data):
    tournament = [random.randint(0, len(population) - 1) for i in
                  range(TOURNAMENT_SIZE)]  # select tournament contenders
    tournament_fitness = [fitness_data[tournament[i]] for i in range(TOURNAMENT_SIZE)]
    return copy.deepcopy(population[tournament[tournament_fitness.index(max(tournament_fitness))]])


def crossover(dominant, recessive):
    if random.random() < CROSSOVER_CHANCE:
        rec_tree = recessive.check_exchangeable(node_two=None, depth=[random.randint(1, recessive.size())])
        dominant.check_exchangeable(node_two=rec_tree, depth=[random.randint(1, dominant.size())])


def mutation(individual):
    if random.random() <= MUTATE_CHANCE:
        individual.generate_grow_tree(max_depth=2)
    elif individual.left:
        mutation(individual.left)
    elif individual.right:
        mutation(individual.right)


def cut_mutation(individual):
    if random.random() <= MUTATE_CHANCE:
        individual.cut_mutation()
