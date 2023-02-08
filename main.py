from src.tsp import generic_algorithm
from src.types import Mutation, Selection
from src.utils import calculate_score, create_distance_list, read_distances_from_file
import time

if __name__ == '__main__':
    # CONFIGURATION
    FILE_PATH = "data/berlin52.txt"
    POPULATION_SIZE = 500
    GENERATIONS_AMOUNT = 2000
    LAUNCHES = 2
    STEPS = 5
    # SELECTION
    SELECTION_TYPE = Selection.TOURNAMENT
    SELECTION_SIZE = 3
    # CROSSOVER
    CROSSOVER_PROB = 0.65
    # MUTATION
    MUTATION_TYPE = Mutation.INVERSION
    MUTATION_PROB = 0.1

    for i in range(LAUNCHES):
        start = time.time()

        best_score, best_solution = generic_algorithm(
            FILE_PATH, POPULATION_SIZE, GENERATIONS_AMOUNT,
            STEPS, SELECTION_TYPE, SELECTION_SIZE,
            CROSSOVER_PROB, MUTATION_TYPE, MUTATION_PROB)

        distance_list = create_distance_list(read_distances_from_file(FILE_PATH))
        print('Solution:')
        print('-'.join([str(i) for i in best_solution]) + ' ' + str(calculate_score(distance_list, best_solution)))
        print(f'Time: {round(time.time() - start, 2)} sec')
