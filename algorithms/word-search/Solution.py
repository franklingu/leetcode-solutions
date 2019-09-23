"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def find_neighbors(position, board, target):
            deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for y_d, x_d in deltas:
                y, x = position[0] + y_d, position[1] + x_d
                if not (0 <= y < len(board)):
                    continue
                if not (0 <= x < len(board[0])):
                    continue
                if board[y][x] == target:
                    yield (y, x)
        
        def begin_search(position, word, board):
            stack = [(position, set(), 1)]
            while stack:
                position, prevs, index = stack.pop()
                if index >= len(word):
                    return True
                target = word[index]
                for ne in find_neighbors(position, board, target):
                    if ne in prevs:
                        continue
                    stack.append((ne, prevs.union(set([position])), index + 1))
            return False
            
        if not word:
            return True
        for i, row in enumerate(board):
            for j, ch in enumerate(row):
                if ch != word[0]:
                    continue
                found = begin_search((i, j), word, board)
                if found:
                    return True
        return False
