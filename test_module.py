
import unittest
from mean_var_std import calculate

class TestCalculate(unittest.TestCase):
    def test_calculate(self):
        self.assertEqual(calculate([2,6,2,8,4,0,1,5,7]), {
            'mean': [[3.6666666666666665, 5.0, 3.0], [3.3333333333333335, 4.0, 4.333333333333333], 3.888888888888889],
            'variance': [[8.222222222222221, 1.5555555555555554, 9.333333333333334], [2.888888888888889, 10.666666666666666, 6.222222222222222], 6.987654320987654],
            'standard deviation': [[2.8674417556808756, 1.247219128924647, 3.0550504633038935], [1.699673171197595, 3.265986323710904, 2.494438257849294], 2.6434188310023933],
            'max': [[8, 6, 7], [6, 8, 7], 8],
            'min': [[1, 4, 0], [2, 0, 1], 0],
            'sum': [[11, 15, 9], [10, 12, 13], 35]
        })

    def test_calculate_error(self):
        with self.assertRaises(ValueError):
            calculate([1, 2, 3])

if __name__ == "__main__":
    unittest.main()
