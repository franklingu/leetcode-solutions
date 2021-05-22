"""
Given an array nums, partition it into two (contiguous) subarrays left and right so that:

Every element in left is less than or equal to every element in right.
left and right are non-empty.
left has the smallest possible size.
Return the length of left after such a partitioning.  It is guaranteed that such a partitioning exists.

 

Example 1:

Input: nums = [5,0,3,8,6]
Output: 3
Explanation: left = [5,0,3], right = [8,6]
Example 2:

Input: nums = [1,1,1,0,6,12]
Output: 4
Explanation: left = [1,1,1,0], right = [6,12]
 

Note:

2 <= nums.length <= 30000
0 <= nums[i] <= 106
It is guaranteed there is at least one way to partition nums as described.
"""

class Solution(object):
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        mx, ms = [], []
        for n in A:
            if not mx:
                mx.append(n)
            else:
                mx.append(max(mx[-1], n))
        for n in reversed(A):
            if not ms:
                ms.append(n)
            else:
                ms.append(min(ms[-1], n))
        ms = list(reversed(ms))
        for i, n in enumerate(mx):
            if i >= len(A) - 1:
                continue
            n2 = ms[i + 1]
            if n2 >= n:
                return i + 1
        return len(A)
