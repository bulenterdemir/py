from bodev5self import *


import unittest
import numpy as np
import matplotlib.pyplot as plt

# Import the functions to be tested
#from your_module import get_linedistance, get_optimal_line, distance_to_opt

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

    def test_large_dataset(self):
        # Generate 100 random points
        points = [(np.random.rand(), np.random.rand()) for _ in range(100)]

        # Generate 50 random lines
        lines = [(np.random.rand(), np.random.rand()) for _ in range(50)]

        # Ensure get_linedistance can handle large datasets
        for line in lines:
            distance = get_linedistance(points, line)
            self.assertIsInstance(distance, (int, float), "get_linedistance should return a numeric value")

        # Test get_optimal_line with large dataset
        optimal_line = get_optimal_line(points)
        self.assertEqual(len(optimal_line), 2, "get_optimal_line should return a tuple of length 2")

        # Test distance_to_opt with large dataset
        diff = distance_to_opt(points, lines)
        self.assertIsInstance(diff, (int, float), "distance_to_opt should return a numeric value")

    def plot_line(self, ax, line, color='blue', label=None):
        # Extracting line parameters
        a, b = line
        x_vals = np.array(ax.get_xlim())
        y_vals = a * x_vals + b
        ax.plot(x_vals, y_vals, '--', color=color, label=label)

    def test_large_dataset_with_visualization(self):
        # Generate random points
        points = [(np.random.rand(), np.random.rand()) for _ in range(2)]
        x_points, y_points = zip(*points)

        # Generate  random lines
        lines = [(np.random.rand(), np.random.rand()) for _ in range(5)]

        # Visualize
        fig, ax = plt.subplots()
        ax.scatter(x_points, y_points, color='red')

        for line in lines:
            self.plot_line(ax, line)

        # Get and plot the optimal line
        optimal_line = get_optimal_line(points)
        self.plot_line(ax, optimal_line, color='green', label='Optimal Line')

        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.legend()
        plt.show()

if __name__ == '__main__':
    unittest.main()
