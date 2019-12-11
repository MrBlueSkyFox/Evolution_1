class City:
    def __init__(self, x, y, id_number):
        self.x = round(float(x), 4)
        self.y = round(float(y), 4)
        self.index = int(id_number) - 1
        self.id_city = id_number

    def __repr__(self):
        ans = 'id= ' + str(self.id_city) + 'x = ' + str(self.x) + ' y = ' + str(self.y) + ' index= ' + str(self.index)
        return ans
