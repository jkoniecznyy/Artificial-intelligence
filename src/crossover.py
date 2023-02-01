from src.utils import get_slice_indexes


def crossing_pmx(gen_1, gen_2, index_1, index_2):
    result = [i for i in gen_2]
    map = {}

    for i in range(index_1, index_2):
        result[i] = gen_1[i]
        map[gen_1[i]] = gen_2[i]

    for i in list(range(index_1)) + list(range(index_2, len(gen_1))):
        while result[i] in map:
            result[i] = map[result[i]]

    return result


def crossover(population: list, slice_1, slice_2) -> list:
    new_population = []
    length = len(population[0])

    for i in range(0, len(population), 2):
        if population[i] != population[i + 1]:

            if slice_1 is None or slice_2 is None:
                [slice_1, slice_2] = get_slice_indexes(length)

            gen1 = crossing_pmx(population[i], population[i + 1], slice_1, slice_2)
            gen2 = crossing_pmx(population[i + 1], population[i], slice_1, slice_2)
            new_population.extend([gen1, gen2])

        else:
            new_population.extend([population[i], population[i + 1]])
    return new_population
