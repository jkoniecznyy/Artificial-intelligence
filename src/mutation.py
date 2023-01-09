import random
from enum import Enum, auto


class Mutation(Enum):
    REPLACEMENT = auto()
    INVERSION = auto()


def mutate_replace(solution: list, mutation_rate: float = 0.01):
    for i in range(len(solution)):
        if random.random() <= mutation_rate:
            j = random.randrange(len(solution))
            solution[i], solution[j] = solution[j], solution[i]


def mutate_inversion(solution: list, mutation_rate: float = 0.01):
    if random.random() <= mutation_rate:
        [i, j] = random.sample(range(len(solution)), 2)

        if i > j:
            i, j = j, i

        solution[i:j] = solution[i:j][::-1]


def mutate(population, mutation: Mutation, mutation_rate: float = 0.05):
    for solution in population:
        mutate_inversion(solution,
                         mutation_rate) if mutation == Mutation.INVERSION \
            else mutate_replace(solution, mutation_rate)
