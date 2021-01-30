"""

Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.
 
Example 1:

Input: arr = [3,1,2,4]
Output: 17
Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.

Example 2:

Input: arr = [11,81,94,43,3]
Output: 444

 
Constraints:

1 <= arr.length <= 3 * 104
1 <= arr[i] <= 3 * 104


"""


class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        left, right = [], []
        track1, track2 = [], []
        for i, n in enumerate(A):
            while left and A[left[-1]] >= n:
                left.pop()
            track1.append(-1 if not left else left[-1])
            left.append(i)
        for i in range(len(A) - 1, -1, -1):
            n = A[i]
            while right and A[right[-1]] > n:
                right.pop()
            track2.append(len(A) if not right else right[-1])
            right.append(i)
        track2 = track2[::-1]
        res = 0
        for i, n in enumerate(A):
            res += n * (i - track1[i]) * (track2[i] - i)
        return res % 1000000007
        