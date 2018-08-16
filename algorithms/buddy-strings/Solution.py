"""
Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.



Example 1:

Input: A = "ab", B = "ba"
Output: true
Example 2:

Input: A = "ab", B = "ab"
Output: false
Example 3:

Input: A = "aa", B = "aa"
Output: true
Example 4:

Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true
Example 5:

Input: A = "", B = "aa"
Output: false


Note:

0 <= A.length <= 20000
0 <= B.length <= 20000
A and B consist only of lowercase letters.
"""
class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        track1, track2 = {}, {}
        for c in A:
            if c not in track1:
                track1[c] = 0
            track1[c] += 1
        for c in B:
            if c not in track2:
                track2[c] = 0
            track2[c] += 1
        m = 1
        for c, n in track1.iteritems():
            if c not in track2:
                return False
            if n != track2[c]:
                return False
            m = max(m, n)
        cnt = 0
        for c1, c2 in zip(A, B):
            if c1 != c2:
                cnt += 1
            if cnt > 2:
                return False
        if cnt == 2:
            return True
        if cnt == 0 and m >= 2:
            return True
        return False
