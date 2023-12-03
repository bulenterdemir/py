import unittest
import numpy as np

# Import the functions to be tested
#from your_module import get_linedistance, get_optimal_line, distance_to_opt
from bodev5self import *

class TestLineFunctions(unittest.TestCase):
    
    def test_get_linedistance(self):
        points = [(1, 2), (3, 4)]
        line = (1, 1)
        result = get_linedistance(points, line)
        expected = np.sum([(1*x[0] + 1 - x[1])**2 for x in points])
        self.assertEqual(result, expected, "Failed get_linedistance test")

    def test_get_optimal_line(self):
        points = [(1, 2), (3, 4), (5, 6)]
        result = get_optimal_line(points)
        xmean = np.mean([p[0] for p in points])
        ymean = np.mean([p[1] for p in points])
        a = np.sum([(p[0] - xmean) * (p[1] - ymean) for p in points]) / np.sum([(p[0] - xmean)**2 for p in points])
        b = ymean - a * xmean
        expected = (a, b)
        self.assertEqual(result, expected, "Failed get_optimal_line test")

    def test_distance_to_opt(self):
        points = [(1, 2), (3, 4), (5, 6)]
        lines = [(1, 1), (2, 2)]
        result = distance_to_opt(points, lines)
        optimal_line = get_optimal_line(points)
        optimal_distance = get_linedistance(points, optimal_line)
        min_distance = min([get_linedistance(points, line) for line in lines])
        expected = optimal_distance - min_distance
        self.assertEqual(result, expected, "Failed distance_to_opt test")

if __name__ == '__main__':
    unittest.main()
