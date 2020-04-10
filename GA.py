from random import randint, random
import heapq
from Chromosome import Chromosome
import copy


class GA:
    def __init__(self, parameters, problem_parameters):
        self.parameters = parameters
        self.problem_parameters = problem_parameters
        self.population = heapq
        self.initialize_population()
        self.set_fitness_values()

    def initialize_population(self):
        chromosomes = []
        for _ in range(self.parameters['popSize']):
            chromosomes.append(Chromosome(self.problem_parameters))
        heapq.heapify(chromosomes)
        self.population = chromosomes

    def set_fitness_values(self):
        new_chromosomes = []
        for _ in range(self.parameters['popSize']):
            chromosome = heapq.heappop(self.population)
            chromosome.fitness = self.problem_parameters['fitness_function'](chromosome.repres, self.problem_parameters)
            new_chromosomes.append(chromosome)
        heapq.heapify(new_chromosomes)
        self.population = new_chromosomes

    def best_chromosome(self):
        return heapq.heappop(copy.copy(self.population))

    def worst_chromosome(self):
        best = self.best_chromosome()
        aux = copy.copy(self.population)
        for _ in range(self.parameters['popSize']):
            chromosome = heapq.heappop(aux)
            if chromosome.fitness > best.fitness:
                best = chromosome
        return best

    def get(self, position):
        auxiliary = copy.copy(self.population)
        for i in range(self.parameters['popSize']):
            chromosome = heapq.heappop(auxiliary)
            if position == i:
                return chromosome

    def select_chromosome(self):
        pos1 = randint(0, self.parameters['popSize'] - 1)
        pos2 = randint(0, self.parameters['popSize'] - 1)
        if self.get(pos1).fitness < self.get(pos2).fitness:
            return pos1
        else:
            return pos2


    def generate_newGeneration(self):
        new_population = []
        heapq.heapify(new_population)
        for _ in range(self.parameters['popSize']):
            p1 = self.get(self.select_chromosome())
            p2 = self.get(self.select_chromosome())
            off = p1.crossover(p2)
            off.mutation()
            heapq.heappush(new_population, off)

        self.population = new_population
        self.set_fitness_values()
