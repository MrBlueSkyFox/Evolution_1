import random
import math
import copy


class Specie:
    def __init__(self, n=False):
        self.x1 = round(random.uniform(-5.12, 5.12), 5)
        self.x2 = round(random.uniform(-5.12, 5.12), 5)
        self.x3 = 0
        if n:
            self.x3 = round(random.uniform(-5.12, 5.12), 5)
        self.fit_val = self.x1 ** 2 + self.x2 ** 2 + self.x3 ** 2
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
        self.fit_val = self.x1 ** 2 + self.x2 ** 2 + self.x3 ** 2
        return self.fit_val
