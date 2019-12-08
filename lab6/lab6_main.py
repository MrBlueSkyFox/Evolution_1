import numpy as np
from lab6.City import City


def init_map():
    path = '/home/tigran/PycharmProjects/Evolution_1/lab6/d/inputData.txt'
    data_file = open(path, 'r')
    list_matrix = data_file.readlines()
    data_file.close()
    city_map = []
    for i in list_matrix:
        row = i.split()
        city = City(row[1], row[2], row[0])
        city_map.append(city)
    return city_map


d = init_map()
