"""

None
"""


class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        N = len(words)
        for row in words:
            N = max(len(row), N)
        for i in range(N):
            for j in range(i + 1, N):
                c1, c2 = None, None
                try:
                    c1 = words[i][j]
                except IndexError:
                    pass
                try:
                    c2 = words[j][i]
                except IndexError:
                    pass
                if c1 != c2:
                    return False
        return True