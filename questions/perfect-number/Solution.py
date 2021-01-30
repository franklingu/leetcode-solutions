"""

A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.
Given an integer n, return true if n is a perfect number, otherwise return false.
 
Example 1:

Input: num = 28
Output: true
Explanation: 28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, and 14 are all divisors of 28.

Example 2:

Input: num = 6
Output: true

Example 3:

Input: num = 496
Output: true

Example 4:

Input: num = 8128
Output: true

Example 5:

Input: num = 2
Output: false

 
Constraints:

1 <= num <= 108


"""


class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        divs = set()
        for i in xrange(1, int(num ** 0.5) + 1):
            d, r = divmod(num, i)
            if r != 0:
                continue
            if i != num:
                divs.add(i)
            if d != num:
                divs.add(d)
        return sum(divs) == num