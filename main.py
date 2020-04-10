import math
from matplotlib import pyplot as plt
from GA import GA
from utils import Utils


def main():
    network = Utils.read_berlin("exemplu.txt")

    gaParam = {
        'popSize': 200,
        'noGen': 2000,
        'pc': 0.8,
        'pm': 0.1
    }

    problParam = {
        'min': 1,
        'max': network['noNodes'],
        'fitness_function': Utils.modularity,
        'noNodes': network['noNodes'],
        'matrix': network['matrix']
    }

    ga = GA(gaParam, problParam)

    for g in range(gaParam['noGen']):
        ga.generate_newGeneration()
        bestChromo = ga.best_chromosome()
        worstChromo = ga.worst_chromosome()
        print('Best solution in generation ' + str(g) + ' is: x = ' + str(bestChromo.repres) + ' f(x) = ' + str(
            bestChromo.fitness))
        print('Worst solution in generation ' + str(g) + ' is: x = ' + str(worstChromo.repres) + ' f(x) = ' + str(
            worstChromo.fitness))
        print()

main()