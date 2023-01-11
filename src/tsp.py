from src.utils import read_distances_from_file, create_distance_list, \
    initialize_population, get_best_score
from src.selection import selection
from src.crossover import crossover
from src.mutation import mutate
from src.types import Mutation


def run_algorithm(file_path: str, population_size: int,
                  generations_amount: int, step_size: int,
                  selection_type, selection_size,
                  crossover_type, crossover_prob,
                  mutation_type, mutation_rate):
    """ TSP algorithm """
    distances = read_distances_from_file(file_path)
    distance_list = create_distance_list(distances)
    population = initialize_population(len(distance_list), population_size)
    best_score, best_solution, scores = get_best_score(distance_list, population)
    print(f'Initial best score: {best_score}')
    results = []
    step = generations_amount / step_size
    for i in range(generations_amount):
        # print(f"Population {population}")
        generation = selection(selection_type, population, scores, selection_size)
        # print(f"Generation {generation}")
        generation = crossover(generation, crossover_type, crossover_prob)

        generation = mutate(generation, mutation_type, mutation_rate)

        if i % 3 == 0:
            generation = mutate(generation, Mutation.REPLACEMENT, mutation_rate)
        else:
            generation = mutate(generation, Mutation.INVERSION, mutation_rate)

        best_score_generation, best_solution_generation, scores = get_best_score(distance_list, generation)

        if best_score_generation < best_score:
            best_score = best_score_generation
            best_solution = best_solution_generation

        population = generation

        if i % step == 0:
            print(f'{round(i / step)}/{step_size}, best score: {best_score}')
            results.append([i, best_score, best_solution])

    return best_score, best_solution, results
