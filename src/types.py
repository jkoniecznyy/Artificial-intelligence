from enum import Enum, auto


class Mutation(Enum):
    REPLACEMENT = auto()
    INVERSION = auto()


class Selection(Enum):
    TOURNAMENT = auto()
    PROPORTIONAL = auto()
