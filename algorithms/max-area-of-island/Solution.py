"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:
[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
"""
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def count_connected(grid, i, j, visited):
            q = [(i, j)]
            r = 0
            while q:
                if q[0] in visited:
                    del q[0]
                    continue
                n, m = q[0]
                r += 1
                visited.add(q[0])
                if n - 1 >= 0 and grid[n - 1][m] == 1 and (n - 1, m) not in visited:
                    q.append((n - 1, m))
                if n + 1 < len(grid) and grid[n + 1][m] == 1 and (n + 1, m) not in visited:
                    q.append((n + 1, m))
                if m - 1 >= 0 and grid[n][m - 1] == 1 and (n, m - 1) not in visited:
                    q.append((n, m - 1))
                if m + 1 < len(grid[0]) and grid[n][m + 1] == 1 and (n, m + 1) not in visited:
                    q.append((n, m + 1))
                del q[0]
            return r

        m = 0
        visited = set()
        for i, row in enumerate(grid):
            for j, el in enumerate(row):
                if el != 1:
                    continue
                if (i, j) in visited:
                    continue
                r = count_connected(grid, i, j, visited)
                m = max(m, r)
        return m

