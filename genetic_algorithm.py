import operator
from settings import Settings
from population import Population


class GeneticAlgorithm:
    GOAL = Settings.BOARD_SIZE * (Settings.BOARD_SIZE - 1) / 2

    def __init__(self):
        self.population = None

    def start(self):
        current_generation = 0
        self.population = Population(Settings.POPULATION_SIZE)

        print('Fitness GOAL is', self.GOAL)

        print(f'Generating first population with {Settings.POPULATION_SIZE} individuals.')
        self.population.initial()
        current_generation += 1

        print('Calculating fitness for every and each individual')
        self.population.calculate_fitness()

        best_fitness = self.population.best_fitness
        print('Best Fitness belongs to', best_fitness['amount'], best_fitness['individual'])
        print(best_fitness['individual'].draw())

        if self.has_goal():
            print('Solution has been found!')
            print(self.population.best_fitness['individual'])
            print(self.population.best_fitness['individual'].draw())
            return

        while True:
            if self.has_goal():
                print(f'Solution has been found! Generation Nº {current_generation}')
                print(self.population.best_fitness['individual'])
                print(self.population.best_fitness['individual'].draw())
                return

            if current_generation == Settings.GENERATION_SIZE:
                print('Oops, no good results! The solution could not be found.')
                print(f'The best individual had {self.population.best_fitness["individual"].fitness}')
                return

            print(f'Generation {current_generation + 1}')

            self.population = self.population.next_generation(self.population)
            print(f'Total of {len(self.population.individuals)} individuals')
            self.population.calculate_fitness()
            print('Mode of individuals is', self.population.mode().fitness, 'with', self.population.mode())

            best_fitness = self.population.best_fitness
            print('Best Fitness belongs to', best_fitness['amount'], best_fitness['individual'])

            if self.has_goal():
                print(f'Solution has been found! Generation Nº {current_generation}')
                print(self.population.best_fitness['individual'])
                print(self.population.best_fitness['individual'].draw())
                return

            self.population.kill_worst_individuals()

            current_generation += 1

            print('\n')

    def has_goal(self):
        if self.population.best_fitness['amount'] == self.GOAL:
            return True
        return False
