import unittest
from src.crossover import crossover, crossing_pmx


class CrossoverTest(unittest.TestCase):

    def test_crossing_pmx1(self):
        list1 = [0, 1, 2, 3, 4, 5, 6]
        list2 = [4, 5, 1, 0, 3, 2, 6]

        result1 = crossing_pmx(list1, list2, 2, 5)
        result2 = crossing_pmx(list2, list1, 2, 5)

        correct_answer1 = [0, 5, 2, 3, 4, 1, 6]
        correct_answer2 = [4, 2, 1, 0, 3, 5, 6]
        self.assertEqual([correct_answer1, correct_answer2], [result1, result2])

    def test_crossover1(self):
        list1 = [0, 1, 2, 3, 4, 5, 6]
        list2 = [4, 5, 1, 0, 3, 2, 6]
        result1, result2 = crossover([list1, list2], 2, 5)

        correct_answer1 = [0, 5, 2, 3, 4, 1, 6]
        correct_answer2 = [4, 2, 1, 0, 3, 5, 6]
        self.assertEqual([correct_answer1, correct_answer2], [result1, result2])

    def test_crossing_pmx2(self):
        list1 = [1, 3, 4, 2, 5, 6, 0]
        list2 = [4, 5, 2, 1, 0, 3, 6]

        result1 = crossing_pmx(list1, list2, 2, 6)
        result2 = crossing_pmx(list2, list1, 2, 6)

        correct_answer1 = [1, 0, 4, 2, 5, 6, 3]
        correct_answer2 = [4, 6, 2, 1, 0, 3, 5]
        self.assertEqual([correct_answer1, correct_answer2], [result1, result2])

    def test_crossover2(self):
        list1 = [1, 3, 4, 2, 5, 6, 0]
        list2 = [4, 5, 2, 1, 0, 3, 6]

        result1, result2 = crossover([list1, list2], 2, 6)

        correct_answer1 = [1, 0, 4, 2, 5, 6, 3]
        correct_answer2 = [4, 6, 2, 1, 0, 3, 5]
        self.assertEqual([correct_answer1, correct_answer2], [result1, result2])

    def test_crossing_pmx3(self):
        list1 = [1, 3, 4, 2, 5, 6, 0]
        list2 = [4, 5, 2, 1, 0, 3, 6]

        result1 = crossing_pmx(list1, list2, 1, 4)
        result2 = crossing_pmx(list2, list1, 1, 4)

        correct_answer1 = [1, 3, 4, 2, 0, 5, 6]
        correct_answer2 = [4, 5, 2, 1, 3, 6, 0]
        self.assertEqual([correct_answer1, correct_answer2], [result1, result2])

    def test_crossover3(self):
        list1 = [1, 3, 4, 2, 5, 6, 0]
        list2 = [4, 5, 2, 1, 0, 3, 6]

        result1, result2 = crossover([list1, list2], 1, 4)

        correct_answer1 = [1, 3, 4, 2, 0, 5, 6]
        correct_answer2 = [4, 5, 2, 1, 3, 6, 0]
        self.assertEqual([correct_answer1, correct_answer2], [result1, result2])
