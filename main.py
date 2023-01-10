from src.tsp import run_algorithm

if __name__ == '__main__':
    FILE_PATH = "data/test.txt"
    SELECTION_TYPE = "T"
    POPULATION_SIZE = 10
    K = 2
    GENERATIONS_AMOUNT = 2
    STEP_SIZE = 1
    CROSSOVER_TYPE = "P"
    CROSSOVER_PROB = 0.5

    run_algorithm(FILE_PATH, POPULATION_SIZE, GENERATIONS_AMOUNT,
                  STEP_SIZE, SELECTION_TYPE, K, CROSSOVER_TYPE, CROSSOVER_PROB)
