import random
from src.utils import get_slice_indexes


def pmx_crossover(solution_1: list, solution_2: list, index_1: int, index_2: int) -> list:
    """ Does the Partially Mapped Crossover PMX on the first provided solution """
    result = [i for i in solution_2]
    map = {}

    for i in range(index_1, index_2):
        result[i] = solution_1[i]
        map[solution_1[i]] = solution_2[i]

    for i in list(range(index_1)) + list(range(index_2, len(solution_1))):
        while result[i] in map:
            result[i] = map[result[i]]

    return result


def crossover(population: list, crossover_prob: float, slice_1: int = None, slice_2: int = None) -> list:
    """ Does the crossover on the population """
    new_population = []
    solution_length = len(population[0])

    for i in range(0, len(population), 2):
        if population[i] != population[i + 1] and random.random() < crossover_prob:

            if slice_1 is None or slice_2 is None:
                [slice_1, slice_2] = get_slice_indexes(solution_length)

            solution_1 = pmx_crossover(population[i], population[i + 1], slice_1, slice_2)
            solution_2 = pmx_crossover(population[i + 1], population[i], slice_1, slice_2)
            new_population.extend([solution_1, solution_2])

        else:
            new_population.extend([population[i], population[i + 1]])
    return new_population
