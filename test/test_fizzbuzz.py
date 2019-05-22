import unittest

from fizzbuzz import FizzBuzz


class TestFizzBuzz(unittest.TestCase):
    LOOP_COUNT = 300

    def test_three_five(self) -> None:
        expected = "fizz"
        fb = FizzBuzz(self.LOOP_COUNT, 3, 5)
        actual = fb.fizzbuzz(12)
        self.assertEqual(expected, actual)

    def test_four_six(self) -> None:
        expected = "fizzbuzz"
        fb = FizzBuzz(self.LOOP_COUNT, 4, 6)
        actual = fb.fizzbuzz(24)
        self.assertEqual(expected, actual)

    def test_three_five(self) -> None:
        expected = 11
        fb = FizzBuzz(self.LOOP_COUNT, 3, 5)
        actual = fb.fizzbuzz(11)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

