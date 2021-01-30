"""

Write a program that outputs the string representation of numbers from 1 to n.
But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]


"""


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ret = []
        for i in range(1, n + 1):
            r3, r5 = i % 3, i % 5
            if r3 == 0 and r5 == 0:
                ret.append('FizzBuzz')
            elif r3 == 0:
                ret.append('Fizz')
            elif r5 == 0:
                ret.append('Buzz')
            else:
                ret.append(str(i))
        return ret