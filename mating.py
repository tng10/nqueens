import random, math
from collections import namedtuple
from typing import List
from settings import Settings
from selection import Selection


Pair = namedtuple('Pair', ('individual1', 'individual2'))


class Mating:

	def __init__(self, selection: Selection):
		self.selection = selection
		self.pairs: List[Pair] = []
		# self.mating_population = self.round_up_to_even(random.uniform(0.6, 0.9) * Settings.POPULATION_SIZE // 2)
		self.mating_population = Settings.POPULATION_SIZE // 2
		self.pick()

	def pick(self):
		breeding = []
		for i in range(self.mating_population // 2):
			if len(self.selection.population.individuals) >= 2:
				individual1 = self.selection.population.individuals.pop()
				individual2 = self.selection.population.individuals.pop()
				self.pairs.append(Pair(individual1, individual2))
				breeding.append(individual1)
				breeding.append(individual2)

		self.selection.population.individuals.extend(breeding)
		return self.pairs

	def round_up_to_even(self, number):
		return math.ceil(number / 2.) * 2
