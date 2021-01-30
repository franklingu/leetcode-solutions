"""

Given an m x n integers matrix, return the length of the longest increasing path in matrix.
From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).
 
Example 1:


Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:


Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

Example 3:

Input: matrix = [[1]]
Output: 1

 
Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 231 - 1


"""


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def find_neighbors(matrix, y, x):
            curr = matrix[y][x]
            deltas = [(-1, 0), (0, -1), (0, 1), (1, 0)]
            for yd, xd in deltas:
                yn, xn = y + yd, x + xd
                if not (0 <= yn < len(matrix)):
                    continue
                if not (0 <= xn < len(matrix[0])):
                    continue
                if matrix[yn][xn] > curr:
                    yield (yn, xn)
            
        def find_longest_increasing_path(matrix, i, j, track):
            if (i, j) in track:
                return track[(i, j)]
            curr_len = 1
            for neighbor in find_neighbors(matrix, i, j):
                curr_len = max(curr_len, find_longest_increasing_path(matrix, neighbor[0], neighbor[1], track) + 1)
            ## cache the result here is very important for speedup
            track[(i, j)] = curr_len
            return curr_len
            
        if not matrix or not matrix[0]:
            return 0
        mm = 0
        track = {}
        for i, row in enumerate(matrix):
            for j, elem in enumerate(row):
                curr_len = find_longest_increasing_path(matrix, i, j, track)
                mm = max(mm, curr_len)
        return mm