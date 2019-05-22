from typing import Union


class FizzBuzz:
    def __init__(self, loop_count: int, num1: int, num2: int) -> None:
        self.loop_count = loop_count
        self.num1 = num1
        self.num2 = num2

    def fizzbuzz(self, index: int) -> Union[int, str]:
        arr = []
        for i in range(1, self.loop_count + 1):
            if i % self.num1 == 0 and i % self.num2 == 0:
                arr.append("fizzbuzz")
            elif i % self.num1 == 0:
                arr.append("fizz")
            elif i % self.num2 == 0:
                arr.append("buzz")
            else:
                arr.append(i)
        return arr[index - 1]

