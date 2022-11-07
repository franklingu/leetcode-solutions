"""

You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.

Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 109 + 7.
In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.
 
Example 1:


Input: n = 3
Output: 5
Explanation: The five different ways are show above.

Example 2:

Input: n = 1
Output: 1

 
Constraints:

1 <= n <= 1000


"""


class Solution:
    def numTilings(self, n: int) -> int:
        @cache
        def solve(i, previous_gap):
            if i > n: return 0
            if i == n: return not previous_gap
            if previous_gap:
                return solve(i+1, False) + solve(i+1, True)
            return solve(i+1, False) + solve(i+2, False) + 2*solve(i+2, True)
        return solve(0, False) % 1_000_000_007