import random

from settings import Settings
from individual import Individual


class Mutation:

    def __init__(self, individual: Individual):
        self.individual: Individual = individual
        self.rate = 15

    def mutate(self):
        if random.randint(0, 100) < self.rate:
            x, y = None, None
            while x == y:
                x = random.randint(0, Settings.BOARD_SIZE - 1)
                y = random.randint(0, Settings.BOARD_SIZE - 1)
            self.individual.genes[x], self.individual.genes[y] = self.individual.genes[y], self.individual.genes[x]
        return self.individual
