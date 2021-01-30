"""
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ### method 1: tracking limits on all directions
        # directions = [
        #     (0, 1),
        #     (1, 0),
        #     (0, -1),
        #     (-1, 0),
        # ]
        # res = [[0] * n for _ in range(n)]
        # pos = [0, 0]
        # direction = 0
        # left, right, up, down = 0, n - 1, 0, n - 1
        # for i in range(n * n):
        #     res[pos[0]][pos[1]] = i + 1
        #     if direction == 0 and pos[1] == right:
        #         up += 1
        #         direction = (direction + 1) % 4
        #     elif direction == 1 and pos[0] == down:
        #         right -= 1
        #         direction = (direction + 1) % 4
        #     elif direction == 2 and pos[1] == left:
        #         down -= 1
        #         direction = (direction + 1) % 4
        #     elif direction == 3 and pos[0] == up:
        #         left += 1
        #         direction = (direction + 1) % 4
        #     pos[0], pos[1] = pos[0] + directions[direction][0], pos[1] + directions[direction][1]
        # return res
        ### method 2: relying on the fact that a filled position
        ###   means we need to turn
        A = [[0] * n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for k in range(n * n):
            A[i][j] = k + 1
            if A[(i + di) % n][(j + dj) % n]:
                di, dj = dj, -di
            i += di
            j += dj
        return A
