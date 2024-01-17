import unittest
from fe import GetStatus

class TestCalculateDateDiff(unittest.TestCase):
    
    def test_date_diff_calculation(self):
        # Create a temporary ini-file with a specific date
        result = GetStatus()
        expected_result = ['[true, 2, "15/01/2024"]', '[false, 1, "15/01/2024"]',  '[false, 0, "15/01/2024"]']

        # Assert that the result matches the expected difference
        self.assertIn(result, expected_result)

if __name__ == '__main__':
    unittest.main()
