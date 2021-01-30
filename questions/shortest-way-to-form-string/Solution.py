"""

None
"""


from collections import Counter

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        counter = Counter(source)
        count = 0
        start = 0
        for i, e in enumerate(target):
            if e not in counter:
                return - 1
            found = False
            while start < len(source):
                if found:
                    break
                if source[start] == e:
                    found = True
                start += 1
                if start >= len(source):
                    start = 0
                    count += 1
            if not found:
                return -1
        if start > 0:
            count += 1
        return count