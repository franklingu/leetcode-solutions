"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def find_neighbors(grid, curr):
            deltas = [(-1, 0), (0, -1), (1, 0), (0, 1)]
            for y_delta, x_delta in deltas:
                y, x = curr[0] + y_delta, curr[1] + x_delta
                if not (0 <= y < len(grid)):
                    continue
                if not (0 <= x < len(grid[0])):
                    continue
                if grid[y][x] == '1':
                    yield (y, x)
        
        if not grid:
            return 0
        count = 0
        visited = set()
        for i, row in enumerate(grid):
            for j, elem in enumerate(row):
                if elem == '0':
                    continue
                position = (i, j)
                if position in visited:
                    continue
                count += 1
                stack = [position]
                while stack:
                    curr = stack.pop()
                    if curr in visited:
                        continue
                    visited.add(curr)
                    for ne in find_neighbors(grid, curr):
                        if ne in visited:
                            continue
                        stack.append(ne)
        return count
