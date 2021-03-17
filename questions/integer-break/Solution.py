"""

Given an integer n, break it into the sum of at least two positive integers and maximize the product of those integers.
Return the maximum product you can get.
 
Example 1:

Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.

Example 2:

Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.

 
Constraints:

2 <= n <= 58


"""


class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1 for _ in range(n + 1)]
        for i in range(3, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], dp[j] * dp[i - j], j * dp[i - j], j * (i - j))
        print(dp)
        return dp[-1]