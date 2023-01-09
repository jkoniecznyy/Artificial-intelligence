import csv


def read_distances_from_file(path: str, delimiter=" "):
    with open(path, newline="") as distances:
        next(distances)
        return [list(filter(None, row)) for row in csv.reader(distances, delimiter=delimiter)]


def create_distance_list(data: list[list[int]]) -> list[list[int]]:
    length = len(data)
    distance_list = [[None] * length for _ in range(length)]
    for x in range(length):
        for y in range(length):
            try:
                distance_list[x][y] = int(data[x][y])
            except IndexError:
                distance_list[x][y] = int(data[y][x])
    return distance_list
