from enum import Enum, auto


class Crossover(Enum):
    PMX = auto()
    CX = auto()
    OX = auto()


class Mutation(Enum):
    REPLACEMENT = auto()
    INVERSION = auto()


class Selection(Enum):
    TOURNAMENT = auto()
    PROPORTIONAL = auto()
