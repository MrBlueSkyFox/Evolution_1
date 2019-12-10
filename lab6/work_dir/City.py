class City:
    def __init__(self, x, y, id_number):
        self.x = round(float(x), 4)
        self.y = round(float(y), 4)
        self.index = int(id_number) - 1
        self.i = self.index + 1

    def __repr__(self):
        ans = 'id= ' + str(self.index) + 'x = ' + str(self.x) + ' y = ' + str(self.y)
        return ans
