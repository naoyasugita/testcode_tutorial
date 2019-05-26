class Solve:
    def __init__(self):
        pass

    def solve(self, _input: str) -> str:
        if 1 <= int(_input[:2]) <= 12 and 1 <= int(_input[2:]) <= 12:
            return "AMBIGUOUS"
        elif 0 <= int(_input[:2]) <= 99 and 1 <= int(_input[2:]) <= 12:
            return "YYMM"
        elif 1 <= int(_input[:2]) <= 12 and 0 <= int(_input[2:]) <= 99:
            return "MMYY"
        else:
            return "NA"

