'''
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
'''

'''
Starting from first row, iterate each cell in the row and
compute what is the highest bar starting from current cell.
For the array of heights, try to apply the idea of find the maximum
rectangle formed by bars.
'''


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix[0])
        heights = [0] * (n + 1)
        area = 0
        for row in matrix:
            for i, elem in enumerate(row):
                heights[i] = heights[i] + 1 if elem == '1' else 0
            stack = [-1]
            for i in range(n + 1):
                while stack and heights[i] < heights[stack[-1]]:
                    index = stack.pop()
                    height = heights[index]
                    width = i - stack[-1] - 1
                    area = max(area, height * width)
                stack.append(i)
        return area
