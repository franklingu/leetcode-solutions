"""

You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.
Return the size of the largest island in grid after applying this operation.
An island is a 4-directionally connected group of 1s.
 
Example 1:

Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.

Example 2:

Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
Example 3:

Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.

 
Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 500
grid[i][j] is either 0 or 1.

"""


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        DIR = [0, 1, 0, -1, 0]
        m, n, nextColor = len(grid), len(grid[0]), 2
        componentSize = defaultdict(int)

        def paint(r, c, color):
            if r < 0 or r == m or c < 0 or c == n or grid[r][c] != 1: return
            grid[r][c] = color
            componentSize[color] += 1
            for i in range(4):
                paint(r + DIR[i], c + DIR[i + 1], color)

        ans = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0: continue
                paint(r, c, nextColor)
                ans = max(ans, componentSize[nextColor])
                nextColor += 1

        for r in range(m):
            for c in range(n):
                if grid[r][c] != 0: continue
                neiColors = set()
                for i in range(4):
                    nr, nc = r + DIR[i], c + DIR[i + 1]
                    if nr < 0 or nr == m or nc < 0 or nc == n or grid[nr][nc] == 0: continue
                    neiColors.add(grid[nr][nc])
                sizeFormed = 1  # Start with 1, which is matrix[r][c] when turning from 0 into 1
                for color in neiColors:
                    sizeFormed += componentSize[color]
                ans = max(ans, sizeFormed)

        return ans