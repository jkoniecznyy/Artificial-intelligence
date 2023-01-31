from src.utils import get_slice_indexes
from src.types import Crossover



def crossing_ox(solution0, solution1):
    [x1, x2] = get_slice_indexes(solution0)
    left = solution0[:x1], solution1[:x1]
    middle = solution0[x1:x2], solution1[x1:x2]
    right = solution0[x2:], solution1[x2:]
    print(f'solution1: {solution0}, x1: {x1}, x2: {x2}\nsolution2: {solution1}, ')
    print(f'right: {right}, left: {left}, middle: {middle}, ')
    # Insert middle parts
    new_solution0 = [[None] * x1, middle[0], [None] * (len(solution0) - x2)]
    new_solution1 = [[None] * x1, middle[1], [None] * (len(solution1) - x2)]
    print(f'new_solution0: {new_solution0}')
    print(f'new_solution1: {new_solution1}')

    starting_index = x2 + 1
    for i in range(len(solution0)):
        if starting_index >= len(solution0):
            starting_index = 0

        print(f'solution1[starting_index]: {solution1[starting_index]}')
        print(f'not in new_solution0: {solution1[starting_index] not in new_solution0}')
        # while solution1[starting_index] not in new_solution0:
        #     print()
        starting_index += 1

    # print(f'solution1: {solution0}, new_solution0: {new_solution0}')
    # print(f'solution2: {solution1}, new_solution1: {new_solution1}')
    return new_solution0, new_solution1


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


def crossover(population: list, crossover_type: Crossover,
              pk: float = 0.95) -> list:
    new_population = []
    for i in range(0, len(population), 2):
        gen1, gen2 = population[i][:], population[i + 1][:]
        if gen1 != gen2:
            match crossover_type:
                # case Crossover.PMX:
                #     gen1, gen2 = crossing_pmx(population[i], population[i + 1])
                case Crossover.CX:
                    gen1, gen2 = crossing_cx(population[i], population[i + 1])
                case Crossover.OX:
                    gen1, gen2 = crossing_ox(population[i], population[i + 1])
        new_population.extend([gen1, gen2])
    return new_population
