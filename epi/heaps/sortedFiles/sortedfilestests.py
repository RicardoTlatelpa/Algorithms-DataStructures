import unittest
from heaps.sortedFiles.mergedsortedfiles import Solution

class TestMergeSortedFiles(unittest.TestCase):
    
    def setUp(self):
        self.solution = Solution()
    
    def test_single_array(self):
        input_data = [[3, 1, 2]]
        expected_output = [1, 2, 3]
        self.assertEqual(self.solution.mergeSortedFiles(input_data), expected_output)
    
    def test_multiple_arrays(self):
        input_data = [[1, 3, 5], [2, 4, 6], [0, 7, 8]]
        expected_output = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(self.solution.mergeSortedFiles(input_data), expected_output)
    
    def test_empty_array(self):
        input_data = [[]]
        expected_output = []
        self.assertEqual(self.solution.mergeSortedFiles(input_data), expected_output)
    
    def test_mixed_empty_and_non_empty_arrays(self):
        input_data = [[], [3, 2, 1], []]
        expected_output = [1, 2, 3]
        self.assertEqual(self.solution.mergeSortedFiles(input_data), expected_output)
    
    def test_all_empty_arrays(self):
        input_data = [[], [], []]
        expected_output = []
        self.assertEqual(self.solution.mergeSortedFiles(input_data), expected_output)
    
    def test_duplicate_elements(self):
        input_data = [[1, 2, 2], [2, 3, 3]]
        expected_output = [1, 2, 2, 2, 3, 3]
        self.assertEqual(self.solution.mergeSortedFiles(input_data), expected_output)
    
    def test_negative_numbers(self):
        input_data = [[-1, -3, -2], [0, -4, -5]]
        expected_output = [-5, -4, -3, -2, -1, 0]
        self.assertEqual(self.solution.mergeSortedFiles(input_data), expected_output)
    
    def test_large_numbers(self):
        input_data = [[100000, 50000], [75000, 25000]]
        expected_output = [25000, 50000, 75000, 100000]
        self.assertEqual(self.solution.mergeSortedFiles(input_data), expected_output)

if __name__ == '__main__':
    unittest.main()
