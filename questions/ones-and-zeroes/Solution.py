"""

You are given an array of binary strings strs and two integers m and n.
Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.
A set x is a subset of a set y if all elements of x are also elements of y.
 
Example 1:

Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
{"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.

Example 2:

Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
Explanation: The largest subset is {"0", "1"}, so the answer is 2.

 
Constraints:

1 <= strs.length <= 600
1 <= strs[i].length <= 100
strs[i] consists only of digits '0' and '1'.
1 <= m, n <= 100


"""


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counter=[[s.count("0"), s.count("1")] for s in strs]
        
        @cache
        def dp(i,j,idx):
            if i<0 or j<0:
                return -math.inf
            
            if idx==len(strs):
                return 0
            
            return max(dp(i,j,idx+1), 1 + dp(i-counter[idx][0], j-counter[idx][1], idx+1))
        return dp(m,n,0)