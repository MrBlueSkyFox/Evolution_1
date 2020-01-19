import math
from lab6.d.aco import ACO, Graph
from lab6.d.plot import plot


def distance(city1: dict, city2: dict):
    return math.sqrt((city1['x'] - city2['x']) ** 2 + (city1['y'] - city2['y']) ** 2)


var = "vlad"


def path1():
    cities = []
    points = []
    with open("./data/%s1.txt" % var) as f:
        for line in f.readlines():
            city = line.split(' ')
            cities.append(dict(index=int(city[0]), x=int(city[1]), y=int(city[2])))
            points.append((int(city[1]), int(city[2])))
    cost_matrix = []
    rank = len(cities)
    for i in range(rank):
        row = []
        for j in range(rank):
            row.append(distance(cities[i], cities[j]))
        cost_matrix.append(row)
    aco = ACO(10, 5, 1.0, 10.0, 0.5, 10, 2)
    graph = Graph(cost_matrix, rank)
    path, cost = aco.solve(graph)
    path.append(path[0])
    print('cost: {}, path: {}'.format(cost, path))
    plot(points, path)


def path2():
    cities = []
    points = []
    with open("./data/%s2.txt" % var) as f:
        for line in f.readlines():
            city = line.split(' ')
            cities.append(dict(index=int(city[0]), x=float(city[1]), y=float(city[2])))
            points.append((float(city[1]), float(city[2])))
    cost_matrix = []
    rank = len(cities)
    for i in range(rank):
        row = []
        for j in range(rank):
            row.append(distance(cities[i], cities[j]))
        cost_matrix.append(row)
    aco = ACO(20, 50, 1.0, 10.0, 0.5, 10, 0)
    graph = Graph(cost_matrix, rank)
    path, cost = aco.solve(graph)
    print('cost: {}, path: {}'.format(cost, path))
    path.append(path[-1])
    plot(points, path)

if __name__ == '__main__':
    path1()
    path2()
