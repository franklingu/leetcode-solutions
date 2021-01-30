'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''

'''
Keeping track of limits and current direction. If any limit is reached,
change to next direction and continue exploration.
'''


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def get_next_pos(position, directions, curr_dir):
            return [position[0] + directions[curr_dir][0], position[1] + directions[curr_dir][1]]
        
        if not matrix:
            return []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        curr_dir = 0
        up, left, right, down = 0, 0, len(matrix[0]) - 1, len(matrix) - 1
        position = [0, 0]
        ret = []
        while up <= down and left <= right:
            ret.append(matrix[position[0]][position[1]])
            pos = get_next_pos(position, directions, curr_dir)
            if pos[0] < up:
                curr_dir = (curr_dir + 1) % 4
                left += 1
            elif pos[0] > down:
                curr_dir = (curr_dir + 1) % 4
                right -= 1
            elif pos[1] < left:
                curr_dir = (curr_dir + 1) % 4
                down -= 1
            elif pos[1] > right:
                curr_dir = (curr_dir + 1) % 4
                up += 1
            position = get_next_pos(position, directions, curr_dir)
        return ret
