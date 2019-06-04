import operator
from settings import Settings
from copy import deepcopy
from typing import List, Dict
from mating import Mating
from crossover import Crossover
from individual import Individual
from mutation import Mutation
from selection import Selection, SelectionStrategy


class Population:

	def __init__(self, size:int):
		self.size: int = size
		self.individuals: List[Individual] = []
		self.max_fitness: Dict = {'amount': -1000, 'individual': None}

	def initial(self):
		self.individuals = [Individual() for _ in range(self.size)]

	def calculate_fitness(self):
		for individual in self.individuals:
			fitness = individual.calculate_fitness()
			if fitness > self.max_fitness['amount']:
				self.max_fitness['amount'] = fitness
				self.max_fitness['individual'] = individual

	def mode(self):
		return max(set(self.individuals), key=self.individuals.count)

	@property
	def best_fitness(self):
		return self.max_fitness

	def next_generation(self, population):
		selection = Selection(deepcopy(population), strategy=SelectionStrategy.TOURNAMENT.value)
		selection.apply()
		mating = Mating(selection)
		mating.apply()
		crossover = Crossover(mating)
		crossover.apply()

		for i, individual in enumerate(crossover.mating.selection.population.individuals):
			mutation = Mutation(individual)
			crossover.mating.selection.population.individuals[i] = mutation.mutate()

		print(f'Individuals: {len(self.individuals)}')
		print(f'New generation: {len(crossover.new_generation)}')
		return crossover.mating.selection.population

	def kill_worst_individuals(self, size=Settings.POPULATION_SIZE // 2):
		self.individuals = sorted(self.individuals, key=operator.attrgetter('fitness'))
		del self.individuals[:size]
