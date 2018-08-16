"""
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).



Example 1:

Input: [[4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]]
Output: 1
Explanation:
The following subgrid is a 3 x 3 magic square:
438
951
276

while this one is not:
384
519
762

In total, there is only one magic square inside the given grid.
Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
0 <= grid[i][j] <= 15
"""
class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def is_magic(grid, y, x):
            s = None
            for i in xrange(y, y + 3):
                ss = 0
                for j in xrange(x, x + 3):
                    if grid[i][j] < 1 or grid[i][j] > 9:
                        return False
                    ss += grid[i][j]
                if s is not None and ss != s:
                    return False
                else:
                    s = ss
            for i in xrange(x, x + 3):
                ss = 0
                for j in xrange(y, y + 3):
                    ss += grid[j][i]
                if ss != s:
                    return False
            ss = grid[y][x] + grid[y + 1][x + 1] + grid[y + 2][x + 2]
            if ss != s:
                return False
            ss = grid[y][x + 2] + grid[y + 1][x + 1] + grid[y + 2][x]
            if ss != s:
                return False
            return True

        l1 = len(grid[0]) - 3 + 1
        l2 = len(grid) - 3 + 1
        ret = 0
        for y in xrange(l2):
            for x in xrange(l1):
                if is_magic(grid, y, x):
                    ret += 1
        return ret

