"""

Implement pow(x, n), which calculates x raised to the power n (i.e. xn).
 
Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

 
Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
-104 <= xn <= 104


"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            is_negative = True
            n = -n
        elif n == 0:
            return 1
        else:
            is_negative = False
        runner = x
        ret = 1
        while n > 0:
            bit = n & 1
            n = n >> 1
            if bit > 0:
                ret *= runner
            runner *= runner
        if ret == 0:
            return 0
        return ret if not is_negative else 1/ ret