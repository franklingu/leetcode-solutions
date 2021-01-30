"""

Given an integer n, return true if it is a power of three. Otherwise, return false.
An integer n is a power of three, if there exists an integer x such that n == 3x.
 
Example 1:
Input: n = 27
Output: true
Example 2:
Input: n = 0
Output: false
Example 3:
Input: n = 9
Output: true
Example 4:
Input: n = 45
Output: false

 
Constraints:

-231 <= n <= 231 - 1

 
Follow up: Could you do it without using any loop / recursion?
"""


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n > 3:
            n, r = divmod(n, 3)
            if r != 0:
                return False
        return n == 1 or n == 3