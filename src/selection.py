import random
from src.types import Selection


def get_best_score_index(scores: list, indexes: list) -> int:
    """ Returns the index of the best score """
    selected_scores = [scores[i] for i in indexes]
    best_score = min(selected_scores)
    return indexes[selected_scores.index(best_score)]


def tournament_selection(population: list, scores: list, selection_pressure: int) -> list:
    """ Selects the best individuals using tournament selection. """
    new_population = []
    for i in range(len(population)):
        indexes = random.sample(range(len(population)), selection_pressure)
        best = get_best_score_index(scores, indexes)
        new_population.append(population[best])
    return new_population


def probability_selection(population: list, scores: list) -> list:
    """ Selects the best individuals using probability selection. """
    scores_reversed = [max(scores) + 1 - score for score in scores]
    return random.choices(population, scores_reversed, k=len(population))


def selection(selection_type, population: list, scores: list, selection_pressure: int) -> list:
    """ Calls the appropriate selection function. """
    return tournament_selection(population, scores, selection_pressure) \
        if selection_type == Selection.TOURNAMENT else probability_selection(population, scores)
