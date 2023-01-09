import random
from src.utils import read_distances_from_file, create_distance_list
from src.selection import selection
from src.crossover import crossover


def initialize_population(size, nr_of_populations):
    points = [*range(size)]
    population = []
    for i in range(nr_of_populations):
        random.shuffle(points)
        population.append(points[:])
    return population


def fitness(cost_array: list, solution: list) -> int:
    mark = sum([cost_array[solution[index]][solution[index + 1]] for index in
                range(len(solution) - 1)])
    return mark + cost_array[solution[-1]][solution[0]]


def test_fitness():
    l = [int(i) for i in
         "1-6-41-29-22-20-16-2-17-30-21-0-48-31-44-18-40-7-8-9-42-32-50-10-51-13-12-46-25-26-27-11-24-3-5-14-4-37-39-38-35-34-33-36-23-47-45-43-15-49-19-28".split(
             '-')]

    print(fitness(create_distance_list(read_distances_from_file('berlin52.txt')), l))


def run_algorithm(file, generations, selection_type, k, crossover_type, crossover_prob):
    distances = read_distances_from_file(file)
    # print(distances)
    distance_table = create_distance_list(distances)
    # print(distance_table)
    current_population = initialize_population(len(distance_table))
    # print(current_population)
    marks = [fitness(distance_table, solution) for solution in
             current_population]

    min_distance = min(marks)
    min_distance_index = marks.index(min_distance)
    min_solution = current_population[min_distance_index]

    results = []
    i = 0
    length = len(generations)
    step = length / 50
    for generation in range(generations):
        print(f'Iteration nr {i}') if i % step == 0 else None
        i += 1

        current_generation = selection(
            selection_type,
            population=current_population,
            marks=marks,
            k=k
        )
        current_generation = crossover(current_generation, crossover_type, crossover_prob)

        marks = [fitness(distance_table, solution) for solution in current_generation]

        tmp_min_distance = min(marks)

        if tmp_min_distance < min_distance:
            min_distance, min_distance_index = tmp_min_distance, \
                marks.index(tmp_min_distance)
            min_solution = current_population[min_distance_index]

        current_population = current_generation

        if generation % 20 == 0:
            results.append(tmp_min_distance)

    return min_solution, min_distance, results
