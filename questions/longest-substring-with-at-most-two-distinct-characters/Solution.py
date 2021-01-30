"""

None
"""


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        counter = {}
        max_cnt, start = 0, 0
        for i, c in enumerate(s):
            if c not in counter:
                counter[c] = 0
            counter[c] += 1
            while len(counter) > 2 and start <= i:
                counter[s[start]] -= 1
                if counter[s[start]] == 0:
                    del counter[s[start]]
                start += 1
            max_cnt = max(max_cnt, i - start + 1)
        return max_cnt