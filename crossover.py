import random
from typing import List
from settings import Settings
from mating import Mating
from individual import Individual


class Crossover:

    def __init__(self, mating: Mating):
        self.mating = mating
        self.new_generation: List[Individual] = []

    def apply(self):
        self.reproduce()

    def reproduce(self):
        for pair in self.mating.pairs:
            first_child_genes, second_child_genes = self.pmx(pair.individual1.genes, pair.individual2.genes)
            first_child = Individual(genes=first_child_genes)
            second_child = Individual(genes=second_child_genes)
            self.new_generation.append(first_child)
            self.new_generation.append(second_child)
        self.mating.selection.population.individuals.extend(self.new_generation)

    def _repeated(self, element, collection):
        c = 0
        for e in collection:
            if e == element:
                c += 1
        return c > 1

    def _swap(self, individual1_genes, individual2_genes, cross_points):
        c1, c2 = cross_points
        child1_genes = individual1_genes[:c1] + individual2_genes[c1:c2] + individual1_genes[c2:]
        child2_genes = individual2_genes[:c1] + individual1_genes[c1:c2] + individual2_genes[c2:]
        return child1_genes, child2_genes

    def _map(self, swapped, cross_points):
        c1, c2 = cross_points
        s1, s2 = swapped
        map_ = s1[c1:c2], s2[c1:c2]
        for i_gene in range(Settings.BOARD_SIZE):
            if not c1 < i_gene < c2:
                for i_son in range(2):
                    while self._repeated(swapped[i_son][i_gene], swapped[i_son]):
                        map_index = map_[i_son].index(swapped[i_son][i_gene])
                        swapped[i_son][i_gene] = map_[1 - i_son][map_index]
        return s1, s2

    def pmx(self, parent_a, parent_b):
        assert (len(parent_a) == len(parent_b))
        cross_points = sorted([random.randint(0, Settings.BOARD_SIZE) for _ in range(2)])
        swapped = self._swap(parent_a, parent_b, cross_points)
        mapped = self._map(swapped, cross_points)
        return mapped
