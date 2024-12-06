import unittest
from src.day2 import is_sorted
from src.day2 import calculate_report_safety
from src.day2 import calculate_report_safety_with_dampener


class TestDay1(unittest.TestCase):
    
    def test_is_sorted(self):
        """Test that a list is sorted"""
        result = is_sorted([1, 3, 5, 7, 9, 56])
        self.assertEqual(result, True)
    
    def test_is_not_sorted(self):
        """Test that a list is not sorted"""
        result = is_sorted([1, 5, 2, 7, 9, 3])
        self.assertEqual(result, False)

    def test_calculate_safety(self):
        """Test to calculate a safe report"""
        result = calculate_report_safety("7 6 4 2 1")
        self.assertEqual(result, True)
    
    def test_calculate_no_safety(self):
        """Test to calculate a safe report"""
        result = calculate_report_safety("1 2 7 8 9")
        self.assertEqual(result, False)

    def test_is_sorted_with_dampener(self):
        """Test that a list is sorted with dampener"""
        result = calculate_report_safety_with_dampener("1 3 5 82 8 10")
        self.assertEqual(result, True)
    
    def test_is_not_sorted_with_dampener(self):
        """Test that a list is not sorted with dampener"""
        result = calculate_report_safety_with_dampener("1 5 2 7 9 3")
        self.assertEqual(result, False)

    def test_validate_level_difference_with_dampener(self):
        """Test that a level has correct amount of difference between them"""
        result = calculate_report_safety_with_dampener("1 3 5 2 6 7")
        self.assertEqual(result, True)

    def test_validate_level_difference_with_dampener_dampened(self):
        """Test that a level has correct amount of difference between them"""
        result = calculate_report_safety_with_dampener("1 3 5 45 6 7")
        self.assertEqual(result, True)

    def test_validate_level_difference_with_dampener_dampened_fail(self):
        """Test that a level has correct amount of difference between them"""
        result = calculate_report_safety_with_dampener("35 36 38 39 38 39")
        self.assertEqual(result, False)

    def test_calculate_safety_with_dampener_unsorted(self):
        """Test to calculate a safe report with dampener"""
        result = calculate_report_safety_with_dampener("9 7 6 12 4 1")
        self.assertEqual(result, True)

    def test_calculate_safety_with_dampener_sorted(self):
        """Test to calculate a safe report with dampener"""
        result = calculate_report_safety_with_dampener("1 3 5 6 7 10 45")
        self.assertEqual(result, True)
    
    def test_calculate_no_safety_with_dampener(self):
        """Test to calculate a not safe report with dampener"""
        result = calculate_report_safety_with_dampener("1 2 7 8 23")
        self.assertEqual(result, False)

    def test_calculate_no_safety_with_dampener(self):
        """Test to calculate a not safe report with dampener"""
        result = calculate_report_safety_with_dampener("35 36 38 39 38 39")
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()