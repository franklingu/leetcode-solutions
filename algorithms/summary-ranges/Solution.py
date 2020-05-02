"""
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:

Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
Example 2:

Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
"""


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        rgs = []
        for n in nums:
            if not rgs:
                rgs.append([n])
                continue
            last = rgs[-1]
            if last[-1] == n - 1:
                last = last + [n] if len(last) == 1 else [last[0], n]
                rgs[-1] = last
            else:
                rgs.append([n])
        ret = []
        for rg in rgs:
            if len(rg) == 1:
                ret.append(str(rg[0]))
            else:
                ret.append('{}->{}'.format(rg[0], rg[1]))
        return ret
