"""

Nearly everyone has used the Multiplication Table. The multiplication table of size m x n is an integer matrix mat where mat[i][j] == i * j (1-indexed).
Given three integers m, n, and k, return the kth smallest element in the m x n multiplication table.
 
Example 1:


Input: m = 3, n = 3, k = 5
Output: 3
Explanation: The 5th smallest number is 3.

Example 2:


Input: m = 2, n = 3, k = 6
Output: 6
Explanation: The 6th smallest number is 6.

 
Constraints:

1 <= m, n <= 3 * 104
1 <= k <= m * n


"""


class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def count(x):
            return sum(min(x//i, n) for i in range(1,m+1))
			
        L, R, mid, ans = 0, m*n, 0, 0
        while L <= R:
            mid = (L + R) >> 1
            if count(mid) < k:
                L = mid + 1
            else:
                R, ans = mid - 1, mid
        return ans