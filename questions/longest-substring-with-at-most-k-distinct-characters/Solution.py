"""

None
"""


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        counter = {}
        start = 0
        m_len = 0
        for i, c in enumerate(s):
            if c not in counter:
                counter[c] = 1
            else:
                counter[c] += 1
            while len(counter.keys()) > k:
                counter[s[start]] -= 1
                if counter[s[start]] == 0:
                    del counter[s[start]]
                start += 1
            m_len = max(m_len, i - start + 1)
        return m_len