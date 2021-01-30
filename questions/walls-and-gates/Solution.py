"""

None
"""


from collections import deque


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        def find_neighbors(y, x, rooms):
            deltas = [(-1, 0), (0, -1), (0, 1), (1, 0)]
            for yd, xd in deltas:
                yn, xn = y + yd, x + xd
                if not (0 <= yn < len(rooms)):
                    continue
                if not (0 <= xn < len(rooms[0])):
                    continue
                if rooms[yn][xn] == -1:
                    continue
                yield (yn, xn)
            
        if not rooms or not rooms[0]:
            return
        queue = deque()
        for i, row in enumerate(rooms):
            for j, elem in enumerate(row):
                if elem == 0:
                    queue.append((i, j, 0))
        while queue:
            y, x, step = queue.popleft()
            if rooms[y][x] < step:
                continue
            rooms[y][x] = step
            for ne in find_neighbors(y, x, rooms):
                queue.append((ne[0], ne[1], step + 1))