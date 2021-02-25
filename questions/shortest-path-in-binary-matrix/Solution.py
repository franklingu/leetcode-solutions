"""

Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.
A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).

The length of a clear path is the number of visited cells of this path.
 
Example 1:


Input: grid = [[0,1],[1,0]]
Output: 2

Example 2:


Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4

Example 3:

Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1

 
Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1


"""


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        n = len(grid)
        deltas = [-1, 0, 1]
        q = deque([((0, 0), 1)])
        visited = set()
        while q:
            pos, step = q.popleft()
            if pos in visited:
                continue
            visited.add(pos)
            if pos == (n - 1, n - 1):
                return step
            for dy in deltas:
                for dx in deltas:
                    new_pos = (pos[0] + dy, pos[1] + dx)
                    if new_pos in visited:
                        continue
                    if not (0 <= new_pos[0] < n):
                        continue
                    if not (0 <= new_pos[1] < n):
                        continue
                    if grid[new_pos[0]][new_pos[1]] != 0:
                        continue
                    q.append((new_pos, step + 1))
        return -1