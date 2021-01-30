"""

None
"""


class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.cols = [0] * n
        self.rows = [0] * n
        self.diagonal1 = 0
        self.diagonal2 = 0

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        delta = 1 if player == 1 else -1
        self.rows[row] += delta
        self.cols[col] += delta
        if row == col:
            self.diagonal1 += delta
        if row == self.n - col - 1:
            self.diagonal2 += delta
        if abs(self.rows[row]) == self.n:
            return player
        elif abs(self.cols[col]) == self.n:
            return player
        elif abs(self.diagonal1) == self.n:
            return player
        elif abs(self.diagonal2) == self.n:
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)