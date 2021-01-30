'''
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1].
 For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.
'''

'''
First make sure signs of the result and convert to positive numbers.
Then check all the even number of multiples of divisor. For example, starting
from divisor * 16, then divisor * 8, then divisor * 4 ... until divisor.
For each iteration, check to substract current number from dividend, if possible
to substract, the return value will be added.
'''


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        is_negative = False
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            is_negative = True
        dividend = abs(dividend)
        divisor = abs(divisor)
        runner, index = divisor, 1
        track = []
        while runner <= dividend:
            track.append((runner, index))
            runner = runner + runner
            index += index
        ret = 0
        for index in range(len(track) - 1, -1, -1):
            val, idx = track[index]
            if dividend >= val:
                dividend -= val
                ret += idx
        if (not is_negative and ret >= 2147483648) or (is_negative and ret > 2147483648):
            return 2147483647
        return ret if not is_negative else -ret
