from src.utils import read_distances_from_file, create_distance_list, \
    initialize_population, get_best_score
from src.selection import selection
from src.crossover import crossover


def run_algorithm(file_path: str, population_size: int, generations_amount: int,
                  step_size: int, selection_type, k, crossover_type, crossover_prob):
    """ TSP algorithm """
    distances = read_distances_from_file(file_path)
    distance_list = create_distance_list(distances)
    population = initialize_population(len(distance_list), population_size)
    best_score, best_solution, scores = get_best_score(distance_list, population)
    results = []
    step = generations_amount / step_size
    for i in range(generations_amount):
        print(f"Population {population}")
        generation = selection(selection_type, population, scores, k)
        print(f"Generation {generation}")
    #     # generation = crossover(generation, crossover_type, crossover_prob)

        best_score_generation, best_solution_generation, scores = get_best_score(distance_list, generation)

        if best_score_generation < best_score:
            best_score = best_score_generation
            best_solution = best_solution_generation

        population = generation

        # if i % step == 0:
        #     print(f'{round(i / step)}/{step_size}, best score: {best_score}')
        #     results.append([i, best_score, best_solution])

    return True
