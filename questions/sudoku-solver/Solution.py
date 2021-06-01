"""

Write a program to solve a Sudoku puzzle by filling the empty cells.
A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

The '.' character indicates empty cells.
 
Example 1:


Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:



 
Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.


"""


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def fill_board(board, i, j, rows, cols, blocks):
            if i >= len(rows) or j >= len(cols):
                return True
            ni, nj = i + 1, j
            if ni == len(rows):
                ni, nj = 0, j + 1
            if board[i][j] != '.':
                return fill_board(board, ni, nj, rows, cols, blocks)
            for n in range(1, 10):
                if n in rows[i]:
                    continue
                if n in cols[j]:
                    continue
                if n in blocks[(i // 3 * 3) + (j // 3)]:
                    continue
                board[i][j] = str(n)
                rows[i].add(n)
                cols[j].add(n)
                blocks[(i // 3 * 3) + (j // 3)].add(n)
                sub = fill_board(board, ni, nj, rows, cols, blocks)
                if sub:
                    return True
                board[i][j] = '.'
                rows[i].remove(n)
                cols[j].remove(n)
                blocks[(i // 3 * 3) + (j // 3)].remove(n)
            return False
            
        
        rows = [set() for _ in range(len(board))]
        cols = [set() for _ in range(len(board[0]))]
        blocks = [set() for _ in range(len(board))]
        for i, row in enumerate(board):
            for j, elem in enumerate(row):
                if elem != '.':
                    val = ord(elem) - ord('0')
                    rows[i].add(val)
                    cols[j].add(val)
                    blocks[(i // 3 * 3) + (j // 3)].add(val)
        fill_board(board, 0, 0, rows, cols, blocks)
                    