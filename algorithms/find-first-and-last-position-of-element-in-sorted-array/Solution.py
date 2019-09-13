'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''

'''
We can use bisect or the idea of bisect to find the left boundry and right boundry. Or
we can search both boundry at the same time by shrinking the range of low and high
'''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(lo, hi):
            if nums[lo] == target == nums[hi]:
                return [lo, hi]
            if nums[lo] <= target <= nums[hi]:
                mid = (lo + hi) // 2
                l, r = search(lo, mid), search(mid+1, hi)
                return max(l, r) if -1 in l+r else [l[0], r[1]]
            return [-1, -1]
        
        if not nums:
            return [-1, -1]
        return search(0, len(nums)-1)
    
    def searchRange2(self, nums: List[int], target: int) -> List[int]:
        import bisect
        left, right = bisect.bisect_left(nums, target), bisect.bisect_right(nums, target)
        if left == right:
            return [-1, -1]
        return [left, right - 1]
