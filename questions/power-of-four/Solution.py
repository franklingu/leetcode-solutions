"""

Given an integer n, return true if it is a power of four. Otherwise, return false.
An integer n is a power of four, if there exists an integer x such that n == 4x.
 
Example 1:
Input: n = 16
Output: true
Example 2:
Input: n = 5
Output: false
Example 3:
Input: n = 1
Output: true

 
Constraints:

-231 <= n <= 231 - 1

 
Follow up: Could you solve it without loops/recursion?
"""


class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        if num == 1:
            return True
        s = bin(num)[2:]
        if s[0] != '1':
            return False
        p = s[1:]
        if int(p) != 0:
            return False
        return len(p) % 2 == 0