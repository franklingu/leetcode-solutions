"""

A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.
 
Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

 
Note:

S will have length in range [1, 500].
S will consist of lowercase English letters ('a' to 'z') only.

 

"""


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        tr = {}
        for i, a in enumerate(S):
            if a not in tr:
                tr[a] = [i, i]
            else:
                tr[a][1] = i
        rgs = list(tr.values())
        rgs.sort()
        merged = []
        for rg in rgs:
            if not merged:
                merged.append(list(rg))
                continue
            if merged[-1][1] >= rg[0]:
                merged[-1][1] = max(merged[-1][1], rg[1])
            else:
                merged.append(list(rg))
        return [rg[1] - rg[0] + 1 for rg in merged]