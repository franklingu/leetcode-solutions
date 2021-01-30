"""

According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.
 
Example 1:


Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

Example 2:


Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]

 
Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 25
board[i][j] is 0 or 1.

 
Follow up:

Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?


"""


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def find_live_neighbors(board, i, j):
            directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            num = 0
            for yd, xd in directions:
                y, x = i + yd, j + xd
                if not (0 <= y < len(board)):
                    continue
                if not (0 <= x < len(board[0])):
                    continue
                if board[y][x] & 1 == 1:
                    num += 1
            return num
        
        def should_live(board, i, j, live_neighbors):
            curr = board[i][j] & 1
            if curr == 1 and (live_neighbors == 2 or live_neighbors == 3):
                return True
            if curr == 0 and live_neighbors == 3:
                return True
            return False
        
        if not board or not board[0]:
            return
        for i, row in enumerate(board):
            for j, elem in enumerate(row):
                live_neighbors = find_live_neighbors(board, i, j)
                is_live = should_live(board, i, j, live_neighbors)
                if is_live:
                    board[i][j] = elem | 2
        for i, row in enumerate(board):
            for j, elem in enumerate(row):
                board[i][j] = (elem & 2) >> 1