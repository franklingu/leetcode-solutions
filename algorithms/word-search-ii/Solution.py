"""
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example:

Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]
 

Note:

All inputs are consist of lowercase letters a-z.
The values of words are distinct.
"""


class TrieNode:
    def __init__(self):
        self.track = {}
        self.end = False
        self.word = ''

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add_word(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.track:
                curr.track[ch] = TrieNode()
            curr = curr.track[ch]
        curr.end = True
        curr.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def find_neighbors(position, board, curr):
            deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for y_d, x_d in deltas:
                y, x = position[0] + y_d, position[1] + x_d
                if not (0 <= y < len(board)):
                    continue
                if not (0 <= x < len(board[0])):
                    continue
                if board[y][x] in curr.track:
                    yield (y, x)
        
        def begin_search(position, node, board):
            stack = [(position, set(), node)]
            ret = []
            while stack:
                position, prevs, curr = stack.pop()
                if curr.end:
                    ret.append(curr.word)
                for ne in find_neighbors(position, board, curr):
                    if ne in prevs:
                        continue
                    stack.append((ne, prevs.union(set([position])), curr.track[board[ne[0]][ne[1]]]))
            return ret
        
        trie = Trie()
        for word in words:
            trie.add_word(word)
        ret = set()
        for i, row in enumerate(board):
            for j, ch in enumerate(row):
                if ch not in trie.root.track:
                    continue
                tmp = begin_search((i, j), trie.root.track[ch], board)
                ret = ret.union(set(tmp))
        return list(ret)
