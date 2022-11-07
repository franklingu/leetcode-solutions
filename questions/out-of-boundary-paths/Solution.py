"""

There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.
Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.
 
Example 1:


Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
Output: 6

Example 2:


Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
Output: 12

 
Constraints:

1 <= m, n <= 50
0 <= maxMove <= 50
0 <= startRow < m
0 <= startColumn < n


"""


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
		# define the dp array
        dp = [[[-1]*(maxMove+1) for _ in range(n+1)] for _ in range(m+1)]
        
        def solve(i, j, maxMove):
            if maxMove < 0:
                return 0
            if i < 0 or i >= m or j < 0 or j >= n:
                return 1
            
			# if the dp array at this position contains some value(not -1) then it means it has been computed earlier
			# so we don't need to compute again, hence return whatever value is present in dp.
            if dp[i][j][maxMove] != -1:
                return dp[i][j][maxMove]
            
			# otherwise compute the value
            a = solve(i-1, j, maxMove - 1)
            b = solve(i+1, j, maxMove - 1)
            c = solve(i, j-1, maxMove - 1)
            d = solve(i, j+1, maxMove - 1)
            
			# store the computed value in dp array so that we do not need to compute it again when the same input occurs again.
            dp[i][j][maxMove] = a + b + c + d
            return dp[i][j][maxMove]
        
        return solve(startRow, startColumn, maxMove) % 1000000007