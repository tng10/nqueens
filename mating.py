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
		# self.mating_population = Settings.POPULATION_SIZE // 2

	def apply(self):
		# random.Random(random.randint(0, 1000)).shuffle(self.selection.selected)
		for i in range(len(self.selection.selected) // 2):
			self.pairs.append(Pair(self.selection.selected[i], self.selection.selected[i+1]))
		return self.pairs

	@classmethod
	def round_up_to_even(cls, number):
		return math.ceil(number / 2.) * 2
