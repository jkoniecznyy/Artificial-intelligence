from src.tsp import run_algorithm
from src.types import Crossover, Mutation, Selection

if __name__ == '__main__':
    # CONFIGURATION
    FILE_PATH = "data/berlin52.txt"
    POPULATION_SIZE = 200
    GENERATIONS_AMOUNT = 200
    STEP_SIZE = 10
    # SELECTION
    SELECTION_TYPE = Selection.TOURNAMENT
    SELECTION_PRESSURE = 5
    # CROSSOVER
    CROSSOVER_TYPE = Crossover.CX
    CROSSOVER_PROB = 0.5
    # MUTATION
    MUTATION_TYPE = Mutation.INVERSION
    MUTATION_RATE = 0.05

    best_score, best_solution, results = run_algorithm(
        FILE_PATH, POPULATION_SIZE, GENERATIONS_AMOUNT,
        STEP_SIZE, SELECTION_TYPE, SELECTION_PRESSURE, CROSSOVER_TYPE,
        CROSSOVER_PROB, MUTATION_TYPE, MUTATION_RATE)

    print(f'Best score: {best_score}, best solution: {best_solution}')

