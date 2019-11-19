import math


# def add(x, y):
#     return x + y
def add(x, y):
    out = ((x) + (y))
    return out


# def minus(x, y): return x - y
def minus(x, y):
    out = ((x) - (y))
    return out


def multiply(x, y): return x * y


def division(x, y):
    # if x == math.inf or x == -math.inf:
    #     return x
    if y == 0:
        return x
    return x / y


def abs_call(x): return abs(x)


def sin(x):
    out = 0
    if x == math.inf or x == -math.inf:
        return x
    try:
        out = math.sin(x)
    except Exception as e:
        print(str(e) + ' in sin\n')
    finally:
        return out


def cos(x):
    out = 0
    if x == math.inf or x == -math.inf:
        return x
    try:
        out = math.cos(x)
    except Exception as e:
        print(str(e) + ' in cos\n')
    finally:
        return out


# def cos(x): return math.cos(x)


def exp(x): return math.exp(x)


# def pow_by_two(x): return x ** 2
def pow_by_two(x):
    out = 0
    try:
        out = (x ** 2)
    except Exception:
        out = math.inf
    finally:
        return out


# FUNCTIONS = [add, minus, multiply, division, abs_call, pow_by_two]
# FUNCTIONS_WITH_ONE_ARG = [abs_call, pow_by_two]
# TERMINALS = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10', -5.12, 5.12]
TERMINALS = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10']
MAX_DEPTH = 10
MIN_DEPTH = 6
POPULATION_SIZE = 80
TOURNAMENT_SIZE = 2
GENERATIONS = 500
MIN_VALUE = -5.12
MAX_VALUE = 5.12
CROSSOVER_CHANCE = 0.9
MUTATE_CHANCE = 0.01

FUNCTIONS = [add, pow_by_two]
FUNCTIONS_WITH_ONE_ARG = [pow_by_two]
