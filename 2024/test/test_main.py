import unittest
from src.main import greet


class TestGreet(unittest.TestCase):
    
    def test_greet_valid_name(self):
        """Test greet() with a valid name."""
        result = greet("Alice")
        self.assertEqual(result, "Hello, Alice!")

    def test_greet_empty_name(self):
        """Test greet() raises an exception for an empty name."""
        with self.assertRaises(ValueError):
            greet("")

    def test_greet_none_name(self):
        """Test greet() raises an exception for a None name."""
        with self.assertRaises(ValueError):
            greet(None)

if __name__ == '__main__':
    unittest.main()