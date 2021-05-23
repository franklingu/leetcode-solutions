"""

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return the number of distinct solutions to the n-queens puzzle.
 
Example 1:


Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

Example 2:

Input: n = 1
Output: 1

 
Constraints:

1 <= n <= 9


"""


class Solution:
    def totalNQueens(self, n: int) -> int:
        def get_ld(col, row, n):
            m = min(col, row)
            col, row = col - m, row - m
            if row == 0:
                return n - col - 1
            return n - 1 + row
        
        def get_rd(col, row, n):
            m = min(row, n - col - 1)
            col, row = col + m, row - m
            if row == 0:
                return col
            return n - 1 + row
            
        
        def build_board(board, idx, n, cols, lds, rds, ret):
            if idx == n:
                ret[0] += 1
                return
            for i in range(n):
                if cols[i]:
                    continue
                ld = get_ld(idx, i, n)
                if lds[ld]:
                    continue
                rd = get_rd(idx, i, n)
                if rds[rd]:
                    continue
                board[idx][i] = 'Q'
                cols[i] = True
                lds[ld] = True
                rds[rd] = True
                build_board(board, idx + 1, n, cols, lds, rds, ret)
                board[idx][i] = '.'
                cols[i] = False
                lds[ld] = False
                rds[rd] = False
                
        
        board = [['.' for _ in range(n)] for _ in range(n)]
        cols = [False for _ in range(n)]
        lds = [False for _ in range(n + n - 1)]
        rds = [False for _ in range(n + n - 1)]
        ret = [0]
        build_board(board, 0, n, cols, lds, rds, ret)
        return ret[0]