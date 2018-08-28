"""
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.


Example 1:

Input:
matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
Output: True
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
Example 2:

Input:
matrix = [
  [1,2],
  [2,2]
]
Output: False
Explanation:
The diagonal "[1, 2]" has different elements.

Note:

matrix will be a 2D array of integers.
matrix will have a number of rows and columns in range [1, 20].
matrix[i][j] will be integers in range [0, 99].

Follow up:

What if the matrix is stored on disk, and the memory is limited such that you can only load at most one row of the matrix into the memory at once?
What if the matrix is so large that you can only load up a partial row into the memory at once?
"""
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        if not matrix:
            return True
        l1, l2 = len(matrix), len(matrix[0])
        s1, s2 = 0, 0
        while s2 < l2:
            i, j = s1, s2
            p = None
            while i < l1 and j < l2:
                if p is None:
                    p = matrix[i][j]
                elif p != matrix[i][j]:
                    return False
                i += 1
                j += 1
            s2 += 1
        s1, s2 = 0, 0
        while s1 < l1:
            i, j = s1, s2
            p = None
            while i < l1 and j < l2:
                if p is None:
                    p = matrix[i][j]
                elif p != matrix[i][j]:
                    return False
                i += 1
                j += 1
            s1 += 1
        return True

