from lab1.tigr import toint


# p = np.zeros((3, 2))
# print(p)
# p[0][0] = 1
# p[0][1] = 2
# p[1][0] = 2
# print(p)

def p_p(x_i, x_j):
    d = x_i / (x_j[0] + x_j[1] + x_j[2])
    return d


def m_m(p):
    return p * 4


min_x = -10
max_x = 10
n = 16
a = 2.83566
b = -5.33592
a_x = bin(toint(a, min_x, max_x, n))
b_x = bin(toint(b, min_x, max_x, n))
print(a_x, " a -binary ", b_x, " b -binary")
for i in range(0, len(a_x)):
    print(a_x[i], " a ", b_x[i], ' b ', i, ' iter')
