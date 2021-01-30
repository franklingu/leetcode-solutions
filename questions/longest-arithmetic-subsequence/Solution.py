"""

Given an array A of integers, return the length of the longest arithmetic subsequence in A.
Recall that a subsequence of A is a list A[i_1], A[i_2], ..., A[i_k] with 0 <= i_1 < i_2 < ... < i_k <= A.length - 1, and that a sequence B is arithmetic if B[i+1] - B[i] are all the same value (for 0 <= i < B.length - 1).
 
Example 1:

Input: A = [3,6,9,12]
Output: 4
Explanation: 
The whole array is an arithmetic sequence with steps of length = 3.

Example 2:

Input: A = [9,4,7,2,10]
Output: 3
Explanation: 
The longest arithmetic subsequence is [4,7,10].

Example 3:

Input: A = [20,1,15,3,10,5,8]
Output: 4
Explanation: 
The longest arithmetic subsequence is [20,15,10,5].

 
Constraints:

2 <= A.length <= 1000
0 <= A[i] <= 500


"""


class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        mlen = 0
        track = []
        for i, n in enumerate(A):
            if i == 0:
                track.append({})
                mlen = 1
                continue
            tmp = {}
            for j in range(i):
                diff = n - A[j]
                tmp[diff] = track[j].get(diff, 1) + 1
                mlen = max(mlen, tmp[diff])
            track.append(tmp)
        return mlen