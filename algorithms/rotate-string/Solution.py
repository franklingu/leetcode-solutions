"""
We are given two strings, A and B.

A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.

Example 1:
Input: A = 'abcde', B = 'cdeab'
Output: true

Example 2:
Input: A = 'abcde', B = 'abced'
Output: false
Note:

A and B will have length at most 100.

"""
class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        def is_same_after_rotate(A, B, i):
            j, l = 0, len(A)
            while j < l:
                idx = (i + l) % l
                if A[j] != B[idx]:
                    return False
                j += 1
                i += 1
            return True

        if A == B:
            return True
        t1, t2 = {}, {}
        for c in A:
            if c not in t1:
                t1[c] = 1
            else:
                t1[c] += 1
        for c in B:
            if c not in t2:
                t2[c] = 1
            else:
                t2[c] += 1
        if t1 != t2:
            return False
        for i, c in enumerate(reversed(B)):
            if c != A[0]:
                continue
            if is_same_after_rotate(A, B, -i - 1):
                return True
        return False

