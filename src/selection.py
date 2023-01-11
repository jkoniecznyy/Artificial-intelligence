import random
from src.utils import get_best_score_index
from src.types import Selection


def tournament_selection(population, scores, selection_pressure=3):
    new_population = []
    for i in range(len(population)):
        indexes = random.sample(range(len(population)), selection_pressure)
        best = get_best_score_index(scores, indexes)
        new_population.append(population[best])
    return new_population


def probability_selection(population, scores):
    scores_reversed = [max(scores) + 1 - score for score in scores]
    return random.choices(population, scores_reversed, k=len(population))


def selection(selection_type, population: list, scores: list, selection_pressure: int = 3):
    return tournament_selection(population, scores, selection_pressure) \
        if selection_type == Selection.TOURNAMENT \
        else probability_selection(population, scores)
