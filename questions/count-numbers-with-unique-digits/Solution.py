"""

Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:

Input: 2
Output: 91 
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, 
             excluding 11,22,33,44,55,66,77,88,99


 
Constraints:

0 <= n <= 8


"""


class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        elif n == 1:
            return 10
        ret = 9
        step = 9
        for i in xrange(n - 1):
            ret *= step
            step -= 1
        return ret + self.countNumbersWithUniqueDigits(n - 1)