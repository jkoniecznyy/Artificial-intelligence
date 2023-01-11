import random
from src.utils import get_slice_indexes
from src.types import Mutation


def mutate_replace(solution: list):
    for i in range(len(solution)):
        j = random.randrange(len(solution))
        solution[i], solution[j] = solution[j], solution[i]
    return solution


def mutate_inversion(solution: list):
    [x1, x2] = get_slice_indexes(solution)
    solution[x1:x2] = solution[x1:x2][::-1]
    return solution


def mutate(population, mutation_type: Mutation, mutation_rate: float = 0.02):
    new_population = []
    for solution in population:
        if random.random() > mutation_rate:
            new_population.append(solution)
        else:
            # print(f'Before mutation: {solution}')
            if mutation_type == Mutation.INVERSION:
                new_population.append(mutate_inversion(solution))
            else:
                new_population.append(mutate_replace(solution))
            # print(f'After mutation: {new_population[-1]}')
    return new_population
