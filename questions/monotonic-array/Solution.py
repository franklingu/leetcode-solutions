"""
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j].  An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Return true if and only if the given array nums is monotonic.

 

Example 1:

Input: nums = [1,2,2,3]
Output: true
Example 2:

Input: nums = [6,5,4,4]
Output: true
Example 3:

Input: nums = [1,3,2]
Output: false
Example 4:

Input: nums = [1,2,4,5]
Output: true
Example 5:

Input: nums = [1,1,1]
Output: true
 

Note:

1 <= nums.length <= 50000
-100000 <= nums[i] <= 100000
"""

class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        inc, p = None, None
        for n in A:
            if p is not None and n > p:
                if inc is not None and not inc:
                    print(1)
                    return False
            if p is not None and n < p:
                if inc is not None and inc:
                    return False
            if p is not None and n > p:
                inc = True
            elif p is not None and n < p:
                inc = False
            else:
                pass
            p = n
        return True
