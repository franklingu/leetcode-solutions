'''
You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.
Example:

Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 7 

Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2),
             the point (1,2) is an ideal empty land to build a house, as the total 
             travel distance of 3+3+1=7 is minimal. So return 7.
Note:
There will be at least one building. If it is not possible to build such house according to the above rules, return -1.
'''

'''
BFS from all buildings and record down the starting point and current distance travelled.
Return the min sum of all recorded distances for current spot.
'''


from collections import deque


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        def find_neighbors(pos, grid, visited):
            deltas = [(-1, 0), (0, -1), (0, 1), (1, 0)]
            for yd, xd in deltas:
                y, x = pos[0] + yd, pos[1] + xd
                if not (0 <= y < len(grid)):
                    continue
                if not (0 <= x < len(grid[0])):
                    continue
                if (y, x) in visited:
                    continue
                if grid[y][x] == 0:
                    yield (y, x)
        
        buildings = []
        for i, row in enumerate(grid):
            for j, elem in enumerate(row):
                if elem == 1:
                    buildings.append((i, j))
        visited = dict((building, {}) for building in buildings)
        queue = deque()
        for building in buildings:
            queue.append((building, 0, building))
        while queue:
            pos, step, start = queue.popleft()
            if pos in visited[start]:
                continue
            visited[start][pos] = step
            for ne in find_neighbors(pos, grid, visited[start]):
                queue.append((ne, step + 1, start))
        mm = None
        track = {}
        for start, costs in visited.items():
            for pos, step in costs.items():
                if pos in visited:
                    continue
                if pos not in track:
                    track[pos] = [step, 1]
                else:
                    track[pos] = [track[pos][0] + step, track[pos][1] + 1]
                if track[pos][1] == len(visited):
                    if mm is None or track[pos][0] < mm:
                        mm = track[pos][0]
        return mm if mm else -1
