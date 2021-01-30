"""

Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.
 
Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Explanation:


 
Note:
The total number of elements of the given matrix will not exceed 10,000.

"""


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        directions = [(-1, 1), (1, -1)]
        curr_dir = 0
        pos = [0, 0]
        ret = []
        while True:
            ret.append(matrix[pos[0]][pos[1]])
            if pos == [len(matrix) - 1, len(matrix[0]) - 1]:
                break
            if curr_dir == 0:
                if pos[1] == len(matrix[0]) - 1:
                    pos[0] += 1
                    curr_dir = 1
                elif pos[0] == 0:
                    pos[1] += 1
                    curr_dir = 1
                else:
                    pos = [
                        pos[0] + directions[curr_dir][0],
                        pos[1] + directions[curr_dir][1],
                    ]
            elif curr_dir == 1:
                if pos[0] == len(matrix) - 1:
                    pos[1] += 1
                    curr_dir = 0
                elif pos[1] == 0:
                    pos[0] += 1
                    curr_dir = 0
                else:
                    pos = [
                        pos[0] + directions[curr_dir][0],
                        pos[1] + directions[curr_dir][1],
                    ]
        return ret