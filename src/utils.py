import csv
import random
from typing import Tuple, Any, List


def read_distances_from_file(path: str, delimiter=" "):
    with open(path, newline="") as distances:
        next(distances)
        return [list(filter(None, row)) for row in csv.reader(distances, delimiter=delimiter)]


def create_distance_list(data: list[list[int]]):
    length = len(data)
    distance_list = [[None] * length for _ in range(length)]
    for x in range(length):
        for y in range(length):
            try:
                distance_list[x][y] = int(data[x][y])
            except IndexError:
                distance_list[x][y] = int(data[y][x])
    return distance_list


def initialize_population(size, nr_of_populations):
    points = [*range(size)]
    population = []
    for i in range(nr_of_populations):
        random.shuffle(points)
        population.append(points[:].copy())
    return population


def get_best_score(distance_table, population):
    scores = []
    for solution in population:
        solution_score = 0
        for i in range(len(solution) - 1):
            solution_score += distance_table[solution[i]][solution[i + 1]]
        solution_score += distance_table[solution[-1]][solution[0]]
        scores.append(solution_score)
    best_score = min(scores)
    best_solution = population[scores.index(best_score)]
    # print(f"Scores: {scores}")
    # print(f"Best solution: {scores.index(best_score)} with score {best_score}\n {best_solution}")
    return best_score, best_solution, scores
