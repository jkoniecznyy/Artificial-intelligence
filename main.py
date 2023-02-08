from src.tsp import generic_algorithm
from src.types import Mutation, Selection
import time

if __name__ == '__main__':
    # CONFIGURATION
    FILE_PATH = "data/a280.txt"
    POPULATION_SIZE = 200
    GENERATIONS_AMOUNT = 200
    LAUNCHES = 1
    STEPS = 10
    # SELECTION
    SELECTION_TYPE = Selection.TOURNAMENT
    SELECTION_SIZE = 3
    # CROSSOVER
    CROSSOVER_PROB = 0.75
    # MUTATION
    MUTATION_TYPE = Mutation.INVERSION
    MUTATION_PROB = 0.05

    for i in range(LAUNCHES):
        start = time.time()

        best_score, best_solution = generic_algorithm(
            FILE_PATH, POPULATION_SIZE, GENERATIONS_AMOUNT,
            STEPS, SELECTION_TYPE, SELECTION_SIZE,
            CROSSOVER_PROB, MUTATION_TYPE, MUTATION_PROB)

        print(f'\nFinal score: {best_score}')
        print(f'Time: {round(time.time() - start, 2)} sec')
        print('Solution:')
        print('-'.join([str(i) for i in best_solution]) + ' ' + str(best_score))
