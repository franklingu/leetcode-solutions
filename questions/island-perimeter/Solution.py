"""

You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.
Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
 
Example 1:


Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.

Example 2:

Input: grid = [[1]]
Output: 4

Example 3:

Input: grid = [[1,0]]
Output: 4

 
Constraints:

row == grid.length
col == grid[i].length
1 <= row, col <= 100
grid[i][j] is 0 or 1.


"""


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        r = 0
        n1, n2 = len(grid), len(grid[0])
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 0:
                    continue
                r += 4
                if i > 0 and grid[i - 1][j] == 1:
                    r -= 1
                if j > 0 and grid[i][j - 1] == 1:
                    r -= 1
                if i < n1 - 1 and grid[i + 1][j] == 1:
                    r -= 1
                if j < n2 - 1 and grid[i][j + 1] == 1:
                    r -= 1
        return r