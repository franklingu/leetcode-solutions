"""

Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.
Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.
Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.
Note:

The order of returned grid coordinates does not matter.
Both m and n are less than 150.

 
Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).

 

"""


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        def populate_candidates(stack, visited, matrix):
            directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
            while stack:
                curr = stack.pop()
                if curr in visited:
                    continue
                visited.add(curr)
                for yd, xd in directions:
                    yn, xn = curr[0] + yd, curr[1] + xd
                    if not (0 <= yn < len(matrix)):
                        continue
                    if not (0 <= xn < len(matrix[0])):
                        continue
                    if matrix[yn][xn] < matrix[curr[0]][curr[1]]:
                        continue
                    if (yn, xn) in visited:
                        continue
                    stack.append((yn, xn))
        
        if not matrix or not matrix[0]:
            return []
        pacific, atlantic = set(), set()
        stack1, stack2 = [], []
        for i in range(len(matrix)):
            stack1.append((i, 0))
            stack2.append((i, len(matrix[0]) - 1))
        for j in range(len(matrix[0])):
            stack1.append((0, j))
            stack2.append((len(matrix) - 1, j))
        populate_candidates(stack1, pacific, matrix)
        populate_candidates(stack2, atlantic, matrix)
        ret = []
        for curr in pacific:
            if curr in atlantic:
                ret.append(list(curr))
        return ret