from lab7.Swarm import Swarm


def main_7(min, max, n, population, generations=100, strategy=1):
    # swarm = Swarm(-5.12, 5.12, 2, 10)
    swarm = Swarm(min, max, n, population, generations=generations, strategy_choice=strategy)
    swarm.start()
    print(swarm, '\n')


#main_7(-5.12, 5.12, 1, 10)
#main_7(-5.12, 5.12, 3, 50, generations=200)
main_7(-5.12, 5.12, 5, 10)
# main_7(-5.12, 5.12, 10, 10, generations=500)
