import random
from settings import Settings
from individual import Individual


class Mutation:

	def __init__(self, individual: Individual):
		self.individual: Individual = individual
		self.rate = 10

	def mutate(self):
		# if random.randint(0, 100) < self.rate:

		x, y, w, z = [None] * 4
		while x == y and w == z:
			x = random.randint(0, Settings.BOARD_SIZE - 1)
			y = random.randint(0, Settings.BOARD_SIZE - 1)
			w = random.randint(0, Settings.BOARD_SIZE - 1)
			z = random.randint(0, Settings.BOARD_SIZE - 1)

		self.individual.genes[x], self.individual.genes[y] = self.individual.genes[y], self.individual.genes[x]
		self.individual.genes[w], self.individual.genes[z] = self.individual.genes[z], self.individual.genes[w]
		return self.individual
