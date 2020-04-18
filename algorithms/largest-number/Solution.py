"""
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.
"""

import functools

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(a, b):
            n1 = int(str(a) + str(b))
            n2 = int(str(b) + str(a))
            return n2 - n1
            
        ns = sorted(nums, key=functools.cmp_to_key(cmp))
        ret = ''.join((str(n) for n in ns))
        if ret and ret[0] == '0':
            return '0'
        return ret
