"""

Given a matrix and a target, return the number of non-empty submatrices that sum to target.
A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.
Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.
 
Example 1:


Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
Output: 4
Explanation: The four 1x1 submatrices that only contain 0.

Example 2:

Input: matrix = [[1,-1],[-1,1]], target = 0
Output: 5
Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.

Example 3:

Input: matrix = [[904]], target = 0
Output: 0

 
Constraints:

1 <= matrix.length <= 100
1 <= matrix[0].length <= 100
-1000 <= matrix[i] <= 1000
-10^8 <= target <= 10^8


"""


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        ret = 0
        ss = [[0 for _ in row] for row in matrix]
        for i, row in enumerate(matrix):
            for j, el in enumerate(row):
                s = 0
                if i == 0 and j == 0:
                    s = el
                elif i == 0:
                    s = ss[i][j - 1] + el
                elif j == 0:
                    s = ss[i - 1][j] + el
                else:
                    s = ss[i][j - 1] + ss[i - 1][j] - ss[i - 1][j - 1] + el
                ss[i][j] = s
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                tr = {0: 1}
                ts = 0
                for k in range(len(matrix[0])):
                    t = 0
                    if k == 0:
                        t = ss[j][k] - ss[i][k] + matrix[i][k]
                    else:
                        t = ss[j][k] - ss[i][k] - ss[j][k - 1] + ss[i][k - 1] + matrix[i][k]
                    ts += t
                    ret += tr.get(ts - target, 0)
                    tr[ts] = tr.get(ts, 0) + 1
        return ret