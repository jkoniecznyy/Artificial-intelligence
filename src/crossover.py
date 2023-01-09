import random
from enum import Enum, auto


class Crossover(Enum):
    PMX = auto()
    CX = auto()
    OX = auto()


def crossing_pmx(p1, p2):
    [x1, x2] = random.sample(range(len(p1)), 2)
    if x1 > x2:
        x1, x2 = x2, x1

    c2 = [i for i in p1]
    c1 = [i for i in p2]

    _map1 = {}
    _map2 = {}

    for i in range(x1, x2):
        c2[i] = p2[i]
        _map1[p2[i]] = p1[i]
        c1[i] = p1[i]
        _map2[p1[i]] = p2[i]

    for i in list(range(x1)) + list(range(x2, len(p1))):
        while c2[i] in _map1:
            c2[i] = _map1[c2[i]]

        while c1[i] in _map2:
            c1[i] = _map2[c1[i]]

    return c1, c2


def crossing_ox(p1, p2):
    [x1, x2] = random.sample(range(len(p1)), 2)
    if x1 > x2:
        x1, x2 = x2, x1

    c1 = [-9999999 for _ in p1]
    c2 = [-9999999 for _ in p2]

    for i in range(x1, x2):
        c1[i] = p1[i]
        c2[i] = p2[i]

    c1_i = [i for i in list(range(len(p1))) if i not in list(range(x1, x2))]
    c2_i = [i for i in list(range(len(p1))) if i not in list(range(x1, x2))]
    for i in list(range(x2, len(p1))) + list(range(x2)):
        if p2[i] not in c1:
            c1[c1_i.pop(0)] = p2[i]
        if p1[i] not in c2:
            c2[c2_i.pop(0)] = p1[i]

    return c1, c2


def crossing_cx(p1: list, p2: list):
    cycle = []
    cycle_index = []

    for i, val in enumerate(p1):
        if val == p2[i]:
            continue

        if val in cycle:
            break

        if len(cycle) == 0:
            cycle.append(val)
            cycle_index.append(i)
            break

    if len(cycle) == 0:
        return p1, p2

    t_val = cycle[0]
    while True:
        i = p2.index(t_val)

        t_val = p1[i]
        t_index = p1.index(t_val)

        if t_val in cycle:
            break

        cycle.append(t_val)
        cycle_index.append(t_index)

    c1 = [p1[i] if i in cycle_index else p2[i] for i in range(len(p1))]
    c2 = [p2[i] if i in cycle_index else p1[i] for i in range(len(p1))]

    return c1, c2


def crossover(population: list, alg: Crossover,
              pk: float = 0.95) -> list:
    new_population = []
    for i in range(0, len(population), 2):
        new_1, new_2 = population[i][:], population[i + 1][:]
        if random.random() < pk and new_1 != new_2:
            new_1, new_2 = crossing_ox(
                population[i],
                population[i + 1]) if alg == Crossover.OX else \
                crossing_cx(
                    population[i],
                    population[i + 1]) if alg == Crossover.CX else \
                    crossing_pmx(population[i],
                                 population[i + 1])
        new_population.extend([new_1, new_2])

    return new_population
