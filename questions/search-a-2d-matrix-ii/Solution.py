"""

Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

 
Example 1:


Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true

Example 2:


Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false

 
Constraints:

m == matrix.length
n == matrix[i].length
1 <= n, m <= 300
-109 <= matix[i][j] <= 109
All the integers in each row are sorted in ascending order.
All the integers in each column are sorted in ascending order.
-109 <= target <= 109


"""


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def search(row, target):
            start, end = 0, len(row) - 1
            while start < end - 1:
                mid = (start + end) // 2
                if row[mid] == target:
                    return mid
                elif target > row[mid]:
                    start = mid
                else:
                    end = mid - 1
            return end if row[end] == target else start
        
        ### method 1
        # if not matrix or not matrix[0]:
        #     return False
        # for row in matrix:
        #     if row[0] > target:
        #         break
        #     col_idx = search(row, target)
        #     if 0 <= col_idx < len(row) and row[col_idx] == target:
        #         return True
        # return False
        ### method 2
        if not matrix or not matrix[0]:
            return False
        col, row = len(matrix[0]) - 1, 0
        while col >= 0 and row < len(matrix):
            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                row += 1
            else:
                col -= 1
        return False