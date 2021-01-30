"""

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.
Example:

X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

Explanation:
Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

"""


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def find_neighbor(board, curr, visited):
            deltas = [(-1, 0), (0, -1), (0, 1), (1, 0)]
            y, x = curr
            for yd, xd in deltas:
                yn, xn = y + yd, x + xd
                if not (0 <= yn < len(board)):
                    continue
                if not (0 <= xn < len(board[0])):
                    continue
                if (yn, xn) in visited:
                    continue
                if board[yn][xn] == 'O':
                    yield (yn, xn)
        
        if not board or not board[0]:
            return
        stack = []
        for i in [0, len(board) - 1]:
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    stack.append((i, j))
        for j in [0, len(board[0]) - 1]:
            for i in range(len(board)):
                if board[i][j] == 'O':
                    stack.append((i, j))
        visited = set()
        while stack:
            curr = stack.pop()
            visited.add(curr)
            for pos in find_neighbor(board, curr, visited):
                stack.append(pos)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    continue
                if (i, j) in visited:
                    continue
                board[i][j] = 'X'