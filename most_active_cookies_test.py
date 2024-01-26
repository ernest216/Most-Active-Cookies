import unittest
import csv
from most_active_cookies import most_active_cookie

class TestMostActiveCookie(unittest.TestCase):
    def setUp(self):
        # Create a CSV cookie log file
        with open('cookie_log.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['cookie', 'timestamp'])
            writer.writerow(['chocolate', '2022-01-01T12:00:00'])
            writer.writerow(['vanilla', '2022-01-01T13:00:00'])
            writer.writerow(['chocolate', '2022-01-01T14:00:00'])
            writer.writerow(['strawberry', '2022-01-01T15:00:00'])
            writer.writerow(['chocolate', '2022-01-01T16:00:00'])

        # Create an empty CSV file
        with open('empty_file.csv', 'w', newline='') as file:
            pass

    def tearDown(self):
        # Remove the created files
        import os
        os.remove('cookie_log.csv')
        os.remove('empty_file.csv')

    def test_most_active_cookie(self):
        # Test case 1: Check if the most active cookie is returned correctly
        filename = "cookie_log.csv"
        date = "2022-01-01"
        expected_result = ["chocolate"]
        self.assertEqual(most_active_cookie(filename, date), expected_result)

    def test_most_active_cookie_empty_file(self):
        # Test case 2: Check if the function handles an empty file correctly
        filename = "empty_file.csv"
        date = "2022-01-01"
        expected_result = []
        self.assertEqual(most_active_cookie(filename, date), expected_result)

    def test_most_active_cookie_nonexistent_file(self):
        # Test case 3: Check if the function handles a non-existent file correctly
        filename = "nonexistent_file.csv"
        date = "2022-01-01"
        # Use assertRaises to check if a specific exception is raised
        with self.assertRaises(FileNotFoundError):
            most_active_cookie(filename, date)

    def test_most_active_cookie_invalid_date(self):
        # Test case 4: Check if the function handles an invalid date correctly
        filename = "cookie_log.csv"
        date = "2022-01-32"
        expected_result = []
        self.assertEqual(most_active_cookie(filename, date), expected_result)



if __name__ == '__main__':
    unittest.main()