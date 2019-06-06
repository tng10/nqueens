import operator, random, enum
from settings import Settings


class SelectionStrategy(enum.Enum):
	BEST = 'best'
	TOURNAMENT = 'tournament'


class Selection:

	def __init__(self, population, strategy):
		self.population = population
		self.limit: int = Settings.POPULATION_SIZE // 2 + 1 if Settings.POPULATION_SIZE // 2 % 2 != 0 else Settings.POPULATION_SIZE // 2
		self.selected = []
		self.strategy = strategy

	def apply(self):
		return getattr(self, self.strategy)()

	def best(self):
		self.population.individuals = sorted(self.population.individuals, key=operator.attrgetter('fitness'))[:self.limit]

	def tournament(self):
		for _ in range(Settings.POPULATION_SIZE // 2):

			individual1, individual2 = None, None
			while individual1 is None or individual2 is None:
				individual1 = self._tournament_choice()
				individual2 = self._tournament_choice()

			if individual1.fitness > individual2.fitness:
				self.selected.append(individual1)
			else:
				self.selected.append(individual2)
		return self.selected

	def _tournament_choice(self):
		chosen_one = random.choice(self.population.individuals)
		for _ in range(Settings.POPULATION_SIZE // 5):
			individual_chosen = random.choice(self.population.individuals)
			if individual_chosen.fitness > chosen_one.fitness:
				chosen_one = individual_chosen
		return chosen_one

	def pop(self):
		return self.population.individuals.pop(index=random.randint(self.population.individuals))
