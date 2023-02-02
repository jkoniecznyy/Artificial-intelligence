import random
from src.utils import get_slice_indexes
from src.types import Mutation


def mutate_inversion(solution: list) -> list:
    """ Inverts the order of the elements inside the solution """
    [x1, x2] = get_slice_indexes(len(solution))
    solution[x1:x2] = solution[x1:x2][::-1]
    return solution


def mutate_replace(solution: list) -> list:
    """ Swaps places of random elements inside the solution. """
    for i in range(len(solution)):
        j = random.randrange(len(solution))
        solution[i], solution[j] = solution[j], solution[i]
    return solution


def mutate(mutation_type: Mutation, population: list, mutation_prob: float) -> list:
    """ Calls the appropriate mutation function. """
    new_population = []
    for solution in population:
        if random.random() < mutation_prob:
            if mutation_type == Mutation.INVERSION:
                new_population.append(mutate_inversion(solution))
            else:
                new_population.append(mutate_replace(solution))
        else:
            new_population.append(solution)
    return new_population
