"""

Given an array A of integers, a ramp is a tuple (i, j) for which i < j and A[i] <= A[j].  The width of such a ramp is j - i.
Find the maximum width of a ramp in A.  If one doesn't exist, return 0.
 
Example 1:

Input: [6,0,8,2,1,5]
Output: 4
Explanation: 
The maximum width ramp is achieved at (i, j) = (1, 5): A[1] = 0 and A[5] = 5.


Example 2:

Input: [9,8,1,0,1,9,4,0,4,1]
Output: 7
Explanation: 
The maximum width ramp is achieved at (i, j) = (2, 9): A[2] = 1 and A[9] = 1.




 
Note:

2 <= A.length <= 50000
0 <= A[i] <= 50000




 


"""


class Solution(object):
    def maxWidthRamp(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 2:
            return 0
        pos = dict()
        for i, n in enumerate(A):
            if n not in pos:
                pos[n] = []
            pos[n].append(i)
        max_pos = dict()
        prev = -1
        for k in reversed(sorted(pos.keys())):
            max_pos[k] = max(prev, pos[k][-1])
            prev = max_pos[k]
        res = 0
        for k in pos.keys():
            res = max(max_pos[k] - pos[k][0], res)
        return res