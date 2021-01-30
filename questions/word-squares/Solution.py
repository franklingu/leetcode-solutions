"""

None
"""


import collections


class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        n = len(words[0])
        fulls = collections.defaultdict(list)
        for word in words:
            for i in range(n):
                fulls[word[:i]].append(word)
        def build(square):
            if len(square) == n:
                squares.append(square)
                return
            for word in fulls[''.join(list(zip(*square))[len(square)])]:
                build(square + [word])
        squares = []
        for word in words:
            build([word])
        return squares