"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

![Image](https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png)

Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def select(total, down):
            if down > total - down:
                down = total - down
            ret = 1
            for i in range(total, total - down, -1):
                ret *= i
            for i in range(1, down + 1, 1):
                ret = ret // i
            return ret
            
        total, down = m + n - 2, n - 1
        return select(total, down)
