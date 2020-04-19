"""
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4
Example 2:

Input: [0,1]
Output: 0
"""

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == n:
            return m
        start = bin(m)[2:]
        diff = bin(m^n)[2:]
        if len(diff) >= len(start):
            return 0
        else:
            return int(start[:-len(diff)]+''.join(['0' for i in range(len(diff))]), 2)
        
