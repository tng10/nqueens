import random
from typing import List
from settings import Settings


class Individual:

	def __init__(self, genes: List[int] = None):
		self.genes: List = genes if genes else self.generate_genes()
		self.fitness = None

	def __repr__(self):
		return str(self.genes)

	def draw(self):
		output = ''
		for i in range(Settings.BOARD_SIZE):
			for c in range(Settings.BOARD_SIZE):
				if i == self.genes[c]:
					output += '| Q '
				else:
					output += '| - '
			output += "\n"
		return output

	@classmethod
	def generate_genes(cls):
		genes = list(range(Settings.BOARD_SIZE))
		random.Random(random.randint(0, 1000)).shuffle(genes)
		return genes

	def calculate_fitness(self):
		_fitness = 0

		for i in range(0, Settings.BOARD_SIZE):
			for j in range(0, Settings.BOARD_SIZE):
				if i != j:
					if self.genes[i] == self.genes[j]:
						_fitness += 1

		for c in range(0, Settings.BOARD_SIZE):
			for i in range(0, Settings.BOARD_SIZE):
				for j in range(0, Settings.BOARD_SIZE):
					if i - c == j - self.genes[c] and self.genes[i] == j and self.genes[i] != self.genes[c]:
						_fitness += 1

		for c in range(0, Settings.BOARD_SIZE):
			for i in range(0, Settings.BOARD_SIZE):
				for j in range(0, Settings.BOARD_SIZE):
					if i + j == self.genes[c] + c and self.genes[i] == j and self.genes[i] != self.genes[c]:
						_fitness += 1

		self.fitness = ((Settings.BOARD_SIZE * (Settings.BOARD_SIZE - 1)) / 2) - (_fitness / 2)
		return self.fitness
