"""

Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.
If possible, output any possible result.  If not possible, return the empty string.
Example 1:

Input: S = "aab"
Output: "aba"

Example 2:

Input: S = "aaab"
Output: ""

Note:

S will consist of lowercase letters and have length in range [1, 500].

 

"""


import collections
import heapq

class Solution:
    def reorganizeString(self, S: str) -> str:
        counter = collections.Counter(S)
        hp = [(-val, key) for key, val in counter.items()]
        heapq.heapify(hp)
        ret = []
        while hp:
            prev = ret[-1] if ret else None
            mv1, mc1 = heapq.heappop(hp)
            if prev != mc1:
                ret.append(mc1)
                if mv1 < -1:
                    heapq.heappush(hp, (mv1 + 1, mc1))
                continue
            if not hp:
                return ''
            mv2, mc2 = heapq.heappop(hp)
            ret.append(mc2)
            if mv2 < -1:
                heapq.heappush(hp, (mv2 + 1, mc2))
            heapq.heappush(hp, (mv1, mc1))
        return ''.join(ret)