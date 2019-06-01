import operator, random, enum
from settings import Settings


class SelectionStrategy(enum.Enum):
	BEST = 'best'
	TOURNAMENT = 'tournament'


class Selection:

	def __init__(self, population, strategy):
		self.population = population
		self.limit: int = Settings.POPULATION_SIZE // 2 + 1 if Settings.POPULATION_SIZE // 2 % 2 != 0 else Settings.POPULATION_SIZE // 2
		getattr(self, strategy)()

	def best(self):
		self.population.individuals = sorted(self.population.individuals, key=operator.attrgetter('fitness'))[:self.limit]

	def tournament(self):
		while len(self.population.individuals) != Settings.POPULATION_SIZE // 2:

			x, y = None, None
			while x == y:
				x = random.randint(0, len(self.population.individuals) - 1)
				y = random.randint(0, len(self.population.individuals) - 1)

			individual1 = self.population.individuals[x]
			individual2 = self.population.individuals[y]

			if individual1.fitness > individual2.fitness:
				self.population.individuals.pop(y)
			else:
				self.population.individuals.pop(x)

	def pop(self):
		return self.population.individuals.pop(index=random.randint(self.population.individuals))
