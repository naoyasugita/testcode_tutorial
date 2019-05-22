import unittest

from fizzbuzz import SampleProblem


class TestFizzBuzz(unittest.TestCase):
    LOOP_COUNT = 300

    def test_three_five(self) -> None:
        expected = "fizz"
        sp = SampleProblem(self.LOOP_COUNT, 3, 5)
        actual = sp.fizzbuzz(12)
        self.assertEqual(expected, actual)

    def test_four_six(self) -> None:
        expected = "fizzbuzz"
        sp = SampleProblem(self.LOOP_COUNT, 4, 6)
        actual = sp.fizzbuzz(24)
        self.assertEqual(expected, actual)

    def test_three_five(self) -> None:
        expected = 11
        sp = SampleProblem(self.LOOP_COUNT, 3, 5)
        actual = sp.fizzbuzz(11)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

