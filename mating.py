import math
from typing import List
from collections import namedtuple

from selection import Selection


Pair = namedtuple('Pair', ('individual1', 'individual2'))


class Mating:

    def __init__(self, selection: Selection):
        self.selection = selection
        self.pairs: List[Pair] = []

    def apply(self):
        for i in range(len(self.selection.selected) // 2):
            self.pairs.append(Pair(self.selection.selected[i], self.selection.selected[i + 1]))
        return self.pairs

    @classmethod
    def round_up_to_even(cls, number):
        return math.ceil(number / 2.) * 2
