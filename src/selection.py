import random


def get_best_score_index(scores, indexes):
    selected_scores = [scores[i] for i in indexes]
    best_score = min(selected_scores)
    return indexes[selected_scores.index(best_score)]


def tournament_selection(population, scores, k=3):
    new_population = []
    for i in range(len(population)):
        indexes = random.sample(range(len(population)), k)
        best = get_best_score_index(scores, indexes)
        new_population.append(population[best])
    return new_population


def probability_selection(population, scores):
    scores_reversed = [max(scores) + 1 - score for score in scores]
    return random.choices(population, scores_reversed, k=len(population))


def selection(selection_type, population: list, scores: list, k: int = 3):
    return tournament_selection(population, scores, k) if \
        selection_type == "T" else probability_selection(population,
                                                         scores)
