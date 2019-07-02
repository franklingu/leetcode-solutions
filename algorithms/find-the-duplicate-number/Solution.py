'''
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
'''

'''
Two methods:
1. Start and end is 1 and n, mid is (start + end) // 2. Count numbers smaller than mid, equal to mid
and bigger than mid, if count of equal to mid is bigger than 1, we found it; if count smaller than
mid is bigger than half, the duplicate is in the first half; else later half. Continue shrink the
search space.
2. View nums[i] = j as a link in a linked list. Then we can get a detecting cycle in a linked list
problem. There must be a cycle as more than one link is pointing the duplicate. And we will definitely
reach the cycle as at least one must point to duplicate number's position.
'''


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # method 1: using a modified binary search
        # low, high = 1, len(nums) - 1
        # while low < high:
        #     mid = (low + high) // 2
        #     cnt1, cnt2, cnt3 = 0, 0, 0
        #     for n in nums:
        #         if low <= n < mid:
        #             cnt1 += 1
        #         elif n == mid:
        #             cnt2 += 1
        #         elif mid < n <= high:
        #             cnt3 += 1
        #     if cnt2 > 1:
        #         return mid
        #     if mid != low and cnt1 > mid - low:
        #         high = mid - 1
        #     elif cnt3 > high - mid:
        #         low = mid + 1
        # cnt1, cnt2 = 0, 0
        # for n in nums:
        #     if n == low:
        #         cnt1 += 1
        #     elif n == high:
        #         cnt2 += 1
        # return low if cnt1 > 1 else high
        # method 2: view the array as a linked list and detect cycle
        if len(nums) < 2:
            return -1
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast = 0
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
        return slow
