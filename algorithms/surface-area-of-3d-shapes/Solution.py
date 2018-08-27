"""
On a N * N grid, we place some 1 * 1 * 1 cubes.

Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

Return the total surface area of the resulting shapes.



Example 1:

Input: [[2]]
Output: 10
Example 2:

Input: [[1,2],[3,4]]
Output: 34
Example 3:

Input: [[1,0],[0,2]]
Output: 16
Example 4:

Input: [[1,1,1],[1,0,1],[1,1,1]]
Output: 32
Example 5:

Input: [[2,2,2],[2,1,2],[2,2,2]]
Output: 46


Note:

1 <= N <= 50
0 <= grid[i][j] <= 50
"""
class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        t = 0
        for row in grid:
            for cell in row:
                t += 6 * cell
        l1, l2 = len(grid), len(grid[0])
        for i in xrange(l1):
            for j in xrange(l2):
                cell = grid[i][j]
                for n in xrange(cell):
                    if i > 0:
                        if grid[i - 1][j] >= n + 1:
                            t -= 1
                    if i < l1 - 1:
                        if grid[i + 1][j] >= n + 1:
                            t -= 1
                    if j > 0:
                        if grid[i][j - 1] >= n + 1:
                            t -= 1
                    if j < l2 - 1:
                        if grid[i][j + 1] >= n + 1:
                            t -= 1
                    if n > 0 and n < cell - 1:
                        t -= 2
                    elif n > 0 and n >= cell - 1:
                        t -= 1
                    elif n <= 1 and n < cell - 1:
                        t -= 1
                    else:
                        pass
        return t
