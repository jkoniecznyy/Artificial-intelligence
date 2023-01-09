import random
from enum import Enum, auto


class Selection(Enum):
    TOURNAMENT = auto()
    PROPORTIONAL = auto()


def best_index(marks, indexes):
    t = [marks[i] for i in indexes]
    min_mark = min(t)
    min_index = indexes[t.index(min_mark)]
    return min_index


def tournament_selection(population, marks, k=3):
    return [population[
                best_index(marks, random.sample(range(len(population)), k))
            ] for _ in population]


# Selekcja koła ruletki
def probability_selection(population, marks):
    return random.choices(population, weights=[
        max(marks) + 1 - mark for mark in marks
    ], k=len(population))


def selection(selection: Selection, population: list, marks: list, k: int = 3):
    return tournament_selection(population, marks, k) if \
        selection == Selection.TOURNAMENT else probability_selection(population,
                                                                     marks)
