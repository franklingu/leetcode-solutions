"""

You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.
What is the maximum number of envelopes can you Russian doll? (put one inside other)
Note:
Rotation is not allowed.
Example:


Input: [[5,4],[6,4],[6,7],[2,3]]
Output: 3 
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).



"""


import bisect
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes:
            return 0
        envelopes.sort(key=lambda x:(x[0],-x[1]))
        h=[]
        for i, e in enumerate(envelopes,0):
            j = bisect.bisect_left(h, e[1])
            if j < len(h):
                h[j] = e[1]
            else:
                h.append(e[1])
        return len(h)
        