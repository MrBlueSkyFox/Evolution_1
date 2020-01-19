import operator

import matplotlib.pyplot as plt


def plot(points, path: list):
    x = []
    y = []
    for point in points:
        x.append(point[0])
        y.append(point[1])
    # noinspection PyUnusedLocal
    y = list(map(operator.sub, [max(y) for i in range(len(points))], y))
    plt.plot(x, y, 'go')

    for _ in range(1, len(path)):
        i = path[_ - 1]
        j = path[_]
        # noinspection PyUnresolvedReferences
        plt.arrow(x[i], y[i], x[j] - x[i], y[j] - y[i], color='b', linestyle="--", length_includes_head=False)

    # noinspection PyTypeChecker
    plt.xlim(-1, max(x) * 1.5)
    plt.ylim(-1, max(y) * 1.5)
    # noinspection PyTypeChecker
    plt.show()
