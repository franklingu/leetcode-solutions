"""
Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]


 Note:

 S string length is in [1, 10000].
 C is a single character, and guaranteed to be in string S.
 All letters in S and C are lowercase.
"""
class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        l, l1, s = len(S), 0, 1
        r = [None] * l
        for i, c in enumerate(S):
            if c == C:
                r[i] = 0
                l1 += 1
        while l1 < l:
            for i, n in enumerate(r):
                if n != 0:
                    continue
                if i - s >= 0 and r[i - s] is None:
                    r[i - s] = s
                    l1 += 1
                if i + s < l and r[i + s] is None:
                    r[i + s] = s
                    l1 += 1
            s += 1
        return r
