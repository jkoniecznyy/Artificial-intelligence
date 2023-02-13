from src.utils import read_distances_from_file, create_distance_list, initialize_population, get_best_score
from src.selection import selection
from src.crossover import crossover
from src.mutation import mutation
from src.types import Mutation, Selection


def generic_algorithm(file_path: str, population_size: int, generations_amount: int, steps: int,
                      selection_type: Selection, selection_size: int, crossover_prob: float, mutation_type: Mutation,
                      mutation_prob: float) -> tuple[int, list]:
    """     Runs the generic algorithm for the Traveling Salesman Problem.    """
    distance_list = create_distance_list(read_distances_from_file(file_path))
    population = initialize_population(len(distance_list), population_size)
    best_score_population, best_solution_population, scores_population = get_best_score(distance_list, population)

    step = round(generations_amount / steps)
    crossover_decrease = (crossover_prob - 0.4) / steps
    mutation_decrease = mutation_prob / steps

    for i in range(generations_amount):
        generation = selection(selection_type, population, scores_population, selection_size)
        generation = crossover(generation, crossover_prob)
        generation = mutation(mutation_type, generation, mutation_prob)

        best_score_generation, best_solution_generation, scores_generation = get_best_score(distance_list, generation)

        if best_score_population > best_score_generation:
            best_score_population = best_score_generation
            best_solution_population = best_solution_generation

        population = generation
        scores_population = scores_generation

        if i % step == 0:
            crossover_prob -= crossover_decrease
            mutation_prob -= mutation_decrease
            print(f'{round(100 * i / generations_amount)}% done, generation best score: {best_score_generation}')

    return best_score_population, best_solution_population
