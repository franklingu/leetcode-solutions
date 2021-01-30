"""

Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.
 
Example 1:

Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5

Example 2:

Input: c = 3
Output: false

Example 3:

Input: c = 4
Output: true

Example 4:

Input: c = 2
Output: true

Example 5:

Input: c = 1
Output: true

 
Constraints:

0 <= c <= 231 - 1


"""


class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        t = int(c ** 0.5) + 1
        for n in xrange(0, t):
            m = c - n * n
            a = int(m ** 0.5)
            if a * a == m:
                return True
        return False