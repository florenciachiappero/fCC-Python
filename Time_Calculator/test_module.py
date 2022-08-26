import unittest
from time_calculator import add_time


class UnitTests(unittest.TestCase):
    maxDiff = None
    def test_same_period(self):
        actual = add_time("3:30 PM", "2:12")
        expected = "5:42 PM"
        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "3:30 PM", "2:12" to return "5:42 PM"')

    def test_different_period(self):
        actual = add_time("11:55 AM", "3:12")
        expected = "3:07 PM"
        self.assertEqual(actual, expected, 'Expected calling "add_time()" with "11:55 AM", "3:12" to return "3:07 PM"')

    def test_next_day(self):
        actual = add_time("9:15 PM", "5:30")
        expected = "2:45 AM (next day)"
        self.assertEqual(actual, expected, 'Expected time to end with "(next day)" when it is the next day.')
