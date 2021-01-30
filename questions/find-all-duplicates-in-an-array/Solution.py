"""

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements that appear twice in this array.
Could you do it without extra space and in O(n) runtime?

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]

"""


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ret = []
        for i in range(len(nums)):
            j = abs(nums[i]) - 1
            if nums[j] <= 0 :
                ret.append(j + 1)
            nums[j] = -nums[j]
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = -nums[i]
        return ret