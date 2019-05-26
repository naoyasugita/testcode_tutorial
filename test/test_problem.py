import unittest

from problem_b import Solve


class TestSolve(unittest.TestCase):
    def utils(self, _input: str, expected: str) -> None:
        ans = Solve()
        actual = ans.solve(_input)
        print("\n====" + _input + " is " + actual + "====")
        self.assertEqual(expected, actual)

    def test_yymm_pattern(self) -> None:
        self.utils("1905", "YYMM")

    def test_mmyy_pattern(self) -> None:
        self.utils("0122", "MMYY")

    def test_both_pattern(self) -> None:
        self.utils("0112", "AMBIGUOUS")

    def test_na_pattern(self) -> None:
        self.utils("1700", "NA")

if __name__ == "__main__":
    unittest.main()

