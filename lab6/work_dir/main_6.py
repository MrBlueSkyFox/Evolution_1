from lab6.work_dir.SACO import SACO
from lab6.work_dir.City import City


def init_map():
    # path = '/home/tigran/PycharmProjects/Evolution_1/lab6/d/inputData.txt'
    # path = '/lab6/d/inputData.txt'
    path = 'C:/Users/User1/Documents/Evolution_1/lab6/d/inputData.txt'
    data_file = open(path, 'r')
    list_matrix = data_file.readlines()
    data_file.close()
    city_map = []
    for i in list_matrix:
        row = i.split()
        city = City(row[1], row[2], row[0])
        city_map.append(city)
    return city_map


def main():
    ALPHA = 1
    BETA = 3
    EPSILON = 0.01
    RHO = 0.6  # Evaporation Constant
    INIT_PHEROMEON = 1
    city_map = init_map()
    SACO_repr = SACO(alpha=ALPHA, beta=BETA, epsilon=EPSILON, rho=RHO,
                     city_map=city_map, init_pheromeon=INIT_PHEROMEON)


main()
