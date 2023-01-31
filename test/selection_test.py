import unittest
from src.selection import selection
from src.types import Selection


class SelectionTest(unittest.TestCase):

    def test_tournament_selection(self):
        population = [[1, 2, 3, 4, 5, 6], [2, 4, 6, 8, 10, 12], [3, 6, 9, 12, 15, 18]]
        scores = [1, 2, 3]
        selection_size = 2
        result = selection(Selection.TOURNAMENT, population, scores, selection_size)
        self.assertEqual(result, [[1, 2, 3, 4, 5, 6], [2, 4, 6, 8, 10, 12], [1, 2, 3, 4, 5, 6]])

    def test_probability_selection(self):
        population = [[1, 2, 3, 4, 5, 6], [2, 4, 6, 8, 10, 12], [3, 6, 9, 12, 15, 18]]
        scores = [1, 2, 3]
        result = selection(Selection.PROPORTIONAL, population, scores)
        self.assertEqual(result, [[3, 6, 9, 12, 15, 18], [3, 6, 9, 12, 15, 18], [3, 6, 9, 12, 15, 18]])
