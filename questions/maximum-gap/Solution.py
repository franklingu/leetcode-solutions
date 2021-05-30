"""

Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.
You must write an algorithm that runs in linear time and uses linear extra space.
 
Example 1:

Input: nums = [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.

Example 2:

Input: nums = [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.

 
Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 109


"""


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        elif len(nums) == 2:
            return abs(nums[0] - nums[1])
        mmin, mmax = min(nums), max(nums)
        if mmax == mmin:
            return 0
        buckets = [[] for _ in range(len(nums))]
        step = math.ceil((mmax - mmin) / (len(nums) - 1))
        for n in nums:
            bidx = (n - mmin) // step
            b = buckets[bidx]
            if len(b) == 0:
                b.append(n)
                b.append(n)
            else:
                b[0] = min(b[0], n)
                b[1] = max(b[1], n)
        prev = mmin
        ret = 0
        for b in buckets:
            if len(b) == 0:
                continue
            ret = max(ret, b[0] - prev)
            prev = b[1]
        return ret