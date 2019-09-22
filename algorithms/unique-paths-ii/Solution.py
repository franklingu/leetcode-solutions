"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

![Image](https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png)

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0
        results = [0] * len(obstacleGrid[0])
        results[0] = 1
        for ls in obstacleGrid:
            for idx in range(len(ls)):
                if ls[idx]:
                    results[idx] = 0
                    continue
                if idx == 0:
                    left = 0
                else:
                    left = results[idx - 1]
                up = results[idx]
                results[idx] = left + up
        return results[-1]
