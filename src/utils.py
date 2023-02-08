import csv
import random


def read_distances_from_file(path: str) -> list:
    """ Reads the intercity distances from the file """
    with open(path, newline="") as distances:
        next(distances)
        return [list(filter(None, row)) for row in csv.reader(distances, delimiter=" ")]


def create_distance_list(data: list[list[int]]) -> list:
    """ Creates a 2 dimensional list of intercity distances """
    length = len(data)
    distance_list = [[None] * length for _ in range(length)]
    for x in range(length):
        for y in range(length):
            try:
                distance_list[x][y] = int(data[x][y])
            except IndexError:
                distance_list[x][y] = int(data[y][x])
    return distance_list


def initialize_population(size: int, nr_of_populations: int) -> list:
    """ Creates a list of random routes """
    points = [*range(size)]
    population = []
    for i in range(nr_of_populations):
        random.shuffle(points)
        population.append(points[:].copy())
    return population


def get_best_score(distance_table: list, population: list) -> tuple[int, list, list]:
    """ Returns best score, best solution and all scores from the population """
    scores = []
    for solution in population:
        solution_score = 0
        for i in range(len(solution) - 1):
            solution_score += distance_table[solution[i]][solution[i + 1]]
        solution_score += distance_table[solution[len(solution) - 1]][solution[0]]
        scores.append(solution_score)
    best_score = min(scores)
    best_solution = population[scores.index(best_score)]
    return best_score, best_solution, scores


def get_best_score_index(scores: list, indexes: list) -> int:
    """ Returns the index of the best score """
    selected_scores = [scores[i] for i in indexes]
    best_score = min(selected_scores)
    return indexes[selected_scores.index(best_score)]


def get_slice_indexes(length: int) -> list[int, int]:
    """ Returns two random numbers between 0 and "length" sorted ascending """
    index_1, index_2 = random.sample(range(length), 2)
    if index_1 > index_2:
        index_1, index_2 = index_2, index_1
    return [index_1, index_2]
