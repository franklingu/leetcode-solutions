"""

None
"""


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        runner = 0
        curr = 0
        for i, c in enumerate(abbr):
            if c.isalpha():
                runner += curr
                curr = 0
                if runner >= len(word) or c != word[runner]:
                    return False
                runner += 1
            else:
                if curr == 0 and c == '0':
                    return False
                curr = curr * 10 + ord(c) - ord('0')
        runner += curr
        if runner != len(word):
            return False
        return True