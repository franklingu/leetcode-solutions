"""

You are given an m x n integer array grid where grid[i][j] could be:

1 representing the starting square. There is exactly one starting square.
2 representing the ending square. There is exactly one ending square.
0 representing empty squares we can walk over.
-1 representing obstacles that we cannot walk over.

Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.
 
Example 1:


Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)

Example 2:


Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)

Example 3:


Input: grid = [[0,1],[2,0]]
Output: 0
Explanation: There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.

 
Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 20
1 <= m * n <= 20
-1 <= grid[i][j] <= 2
There is exactly one starting cell and one ending cell.


"""


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        state = 0
        state_len = 0
        total_len = len(grid) * len(grid[0])
        start = None
        for i, row in enumerate(grid):
            for j, elem in enumerate(row):
                if elem == -1:
                    state = state | (1 << (i * len(row) + j))
                    state_len += 1
                elif elem == 1:
                    start = (i, j)
        stk = [(start, state, state_len)]
        ret = 0
        while stk:
            curr, curr_state, curr_len = stk.pop()
            mask = (1 << (curr[0] * len(grid[0]) + curr[1]))
            if curr_state & mask != 0:
                continue
            curr_state = curr_state | mask
            curr_len += 1
            if grid[curr[0]][curr[1]] == 2:
                if curr_len == total_len:
                    ret += 1
                continue
            elif grid[curr[0]][curr[1]] == -1:
                continue
            for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ny, nx = curr[0] + dy, curr[1] + dx
                if not (0 <= ny < len(grid)):
                    continue
                if not (0 <= nx < len(grid[0])):
                    continue
                stk.append(((ny, nx), curr_state, curr_len))
        return ret
