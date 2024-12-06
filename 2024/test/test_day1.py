import unittest
from src.day1 import sort_array
from src.day1 import split_dataset
from src.day1 import calculate_length
from src.day1 import find_occurrences_in_list
from src.day1 import calculate_similarity_score


class TestDay1(unittest.TestCase):
    
    def test_sort_array_ascending(self):
        """Test sort_array is ascending"""
        result = sort_array([87, 1, 7, 8754, 45])
        self.assertEqual(result, [1, 7, 45, 87, 8754])

    def test_split_dataset(self):
        """Test split_dataset splits text into integer array"""
        result = split_dataset("2232   934853")
        self.assertEqual(result, [2232, 934853])

    def test_calculate_length(self):
        """Test that the correct length is calculated with calculate_length"""
        result  = calculate_length([23, 9, 1], [1, 87, 2])
        self.assertEqual(result, 101)

    def test_find_occurrences_in_list(self):
        """Test that all occurrences in list is found"""
        result = find_occurrences_in_list(23, [23, 6, 7, 89, 32, 23, 23, 67])
        self.assertEqual(result, 3)

    def test_find_no_occurrences_in_list(self):
        """Test that all occurrences in list is found"""
        result = find_occurrences_in_list(5, [23, 6, 7, 89, 32, 23, 23, 67])
        self.assertEqual(result, 0)

    def test_calculate_similarity_score(self):
        """Test that the correct similarity score is calculated"""
        result  = calculate_similarity_score([23, 9, 1, 4], [9, 87, 2, 23])
        self.assertEqual(result, 32)

if __name__ == '__main__':
    unittest.main()