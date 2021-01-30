"""

You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.
Find out how many ways to assign symbols to make sum of integers equal to target S.
Example 1:

Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.

 
Constraints:

The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.


"""


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        ss = {}
        for n in nums:
            if not ss:
                ss[n] = 1
                ss[-n] = 1
                if n == 0:
                    ss[n] = 2
                continue
            tmp = {}
            for sn, cnt in ss.items():
                tmp[sn + n] = tmp.get(sn + n, 0) + cnt
                tmp[sn - n] = tmp.get(sn - n, 0) + cnt
            ss = tmp
        return ss.get(S, 0)