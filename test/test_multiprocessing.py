import unittest
from multiprocessing import Pool
from enum import Enum, auto
from itertools import repeat

from mp.multiprocessing_engine import MultiProcessing, MultiProcessingFunction


# Define a sample function to be called
def sample_function(x, y):
    return x + y


class TestMultiProcessing(unittest.TestCase):

    def test_multithreading(self):

        # Create an instance of MultiProcessing with the desired method
        multithreading = MultiProcessing(method=MultiProcessingFunction.STARMAP)

        # Set up the function and arguments to be passed
        primary_arg = [1, 2, 3]
        args = [10]

        # Call the mp function
        result = multithreading(sample_function, primary_arg, *args)

        # Get the expected result
        expected_result = [11, 12, 13]

        # Compare the result with the expected result
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()