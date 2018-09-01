"""
Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

Note:
The length of A and B will be between 1 and 10000.
"""
class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if B in A:
            return 1
        l = len(B) / len(A) + 2
        t = A * l
        try:
            r = t.index(B)
        except ValueError:
            return -1
        q, rm = divmod((r + len(B)), len(A))
        if rm == 0:
            return q
        return q + 1

