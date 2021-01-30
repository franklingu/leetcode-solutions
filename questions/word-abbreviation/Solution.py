"""

None
"""


class Solution:
    def wordsAbbreviation(self, dict: List[str]) -> List[str]:
        def shorten(word, idx):
            return word if idx > len(word) - 3 else \
                   word[:idx] + str(len(word)-1-idx) + word[-1]
               
        res = [shorten(word, 1) for word in dict]
        pre = {word : 1 for word in dict}
        n = len(dict)
        for i in range(n):
            while True:
                duplicate = [j for j in range(i, n) if res[i] == res[j]]
                if len(duplicate) == 1: break
                for k in duplicate:
                    pre[dict[k]] += 1
                    res[k] = shorten(dict[k], pre[dict[k]])
        return res
        