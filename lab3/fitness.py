class Fitness:
    def __init__(self, route):
        self.route = route
        self.distance = 0
        self.fitness = 0.0
        # self.route_fitness()

    def route_distance(self):
        if self.distance == 0:
            path_distance = 0
            for i in range(0, len(self.route)):
                from_city = self.route[i]
                to_city = None
                if i + 1 < len(self.route):
                    to_city = self.route[i + 1]
                else:
                    to_city = self.route[0]
                path_distance += from_city.distance(to_city)
            self.distance = path_distance
        return self.distance

    def route_fitness(self):
        if self.fitness == 0:
            self.fitness = 1 / float(self.route_distance())
        return self.fitness

    def __repr__(self):
        route_ans = []
        for i in self.route:
            route_ans.append(' ' + str(i.id) + ' ')

        return "fitness val= " + str(self.fitness) + " dist= " + str(self.distance) + str(route_ans) + "\n"
