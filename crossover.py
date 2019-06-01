import random
from typing import List
from settings import Settings
from mating import Mating
from individual import Individual


class Crossover:

	def __init__(self, mating: Mating):
		self.mating = mating
		self.new_generation: List[Individual] = []
		self.reproduce()

	def reproduce(self):
		for pair in self.mating.pairs:
			x = random.randint(2, Settings.BOARD_SIZE/2)
			first_child_genes = pair.individual1.genes[:x] + pair.individual2.genes[x:]
			second_child_genes = pair.individual2.genes[:x] + pair.individual1.genes[x:]
			first_child = Individual(genes=first_child_genes)
			second_child = Individual(genes=second_child_genes)
			self.new_generation.append(first_child)
			self.new_generation.append(second_child)
		self.mating.selection.population.individuals.extend(self.new_generation)
