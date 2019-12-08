import random
import math
import copy


def f(x, y, z=0, flag=False):
    a = 20
    b = 0.2
    c = 2 * math.pi
    n = 2
    if flag:
        n = 3

    return (-a * math.exp(-b * math.sqrt(1 / n * (x ** 2 + y ** 2 + z ** 2))) - math.exp(
        1 / n * (math.cos(c * x) + math.cos(c * y) + math.cos(c * y))) + a + math.exp(1))
    # return fit_val


class Specie:
    def __init__(self, min_x, max_x, n=False):
        self.x1 = round(random.uniform(min_x, max_x), 5)
        self.x2 = round(random.uniform(min_x, max_x), 5)
        self.x3 = 0
        if n:
            self.x3 = round(random.uniform(min_x, max_x), 5)
        # self.fit_val = self.x1 ** 2 + self.x2 ** 2 + self.x3 ** 2
        self.fit_val = f(self.x1, self.x2, self.x3, n)
        self.max_x = max_x
        self.min_x = min_x
        self.flag = n

    def __repr__(self):
        ans = ("Specie : x1= " + str(self.f1()) + " x2= " + str(self.f2()))
        if self.flag:
            ans += " x3= " + str(self.f3())
        ans += " f(x)= " + str(self.fit_fun())
        return ans

    def f1(self):
        return self.x1

    def f2(self):
        return self.x2

    def f3(self):
        return self.x3

    def fit_fun(self):
        # self.fit_val = self.x1 ** 2 + self.x2 ** 2 + self.x3 ** 2
        self.fit_val = f(self.x1, self.x2, self.x3, self.flag)
        return self.fit_val
