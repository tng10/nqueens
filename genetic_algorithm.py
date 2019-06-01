from settings import Settings
from population import Population


class GeneticAlgorithm:
	GOAL = Settings.BOARD_SIZE * (Settings.BOARD_SIZE - 1) / 2
	
	def start(self):
		current_generation = 0
		population = Population(Settings.POPULATION_SIZE)

		print(f'Generating first population with {Settings.POPULATION_SIZE} individuals.')
		population.initial()
		current_generation += 1

		print('Calculating fitness for every and each individual')
		population.calculate_fitness()

		best_fitness = population.best_fitness
		print('Best Fitness belongs to', best_fitness['amount'], best_fitness['individual'])
		print(best_fitness['individual'].draw())

		if self.has_goal(population):
			print('Solution has been found!')
			print(population.best_fitness['individual'])
			print(population.best_fitness['individual'].draw())
			return

		while True:
			previous_population = population
			if self.has_goal(previous_population):
				print('Solution has been found!')
				print(population.best_fitness['individual'])
				print(population.best_fitness['individual'].draw())
				return

			if current_generation == Settings.GENERATION_SIZE:
				print('Oops, no good results! The solution could not be found.')
				return

			print(f'Generation {current_generation + 1}')

			population = population.next_generation(population)
			print(f'Total of {len(population.individuals)} individuals')
			population.calculate_fitness()
			print('Mode of individuals is', population.mode().fitness, 'with', population.mode())

			best_fitness = population.best_fitness
			print('Best Fitness belongs to', best_fitness['amount'], best_fitness['individual'])
			#print(best_fitness['individual'].draw())

			current_generation += 1

			print('\n')

	def has_goal(self, population):
		if population.best_fitness['amount'] == self.GOAL:
			return True
		return False
