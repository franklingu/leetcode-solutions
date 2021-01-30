'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''

'''
Starting from right, find the breakpoint where current element is smaller
than previous element. Then from right to breakpoint find the minimum
value that is bigger than current element. Swap these two and reverse
all numbers from right to previous position.
'''


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        if len(nums) < 2:
            return
        target = None
        for index in range(len(nums) - 2, -1, -1):
            prev, curr = nums[index + 1], nums[index]
            if curr < prev:
                target = index
                break
        start, end = 0, len(nums) - 1
        if target is not None:
            for index in range(len(nums) - 1, target, -1):
                if nums[index] > nums[target]:
                    break
            nums[target], nums[index] = nums[index], nums[target]
            start = target + 1
        reverse(nums, start, end)
