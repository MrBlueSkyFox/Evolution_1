import numpy as np


def test(x):
    for i in range(0, x):
        print(np.random.normal(0, 1, 1))

MUT_STR = 5

def mutTest(ps):
    global MUT_STR
    DNA_SIZE = 1
    p_target = 1 / 5
    MUT_STR *= np.exp(1 / np.sqrt(DNA_SIZE + 1) * (ps - p_target) / (1 - p_target))
    return MUT_STR


# print(mutTest(0))
# print(mutTest(0))
# print(mutTest(0))
# print(mutTest(1))
# print(mutTest(1))
# print(mutTest(1))
test(10)