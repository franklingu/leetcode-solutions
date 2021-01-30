"""

Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.
Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.

 
Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?
Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.

"""


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        def get_num_of_ways(nums, target, track):
            if target < 0:
                return 0
            elif target == 0:
                return 1
            if target in track:
                return track[target]
            ss = 0
            for n in nums:
                ss += get_num_of_ways(nums, target - n, track)
            track[target] = ss
            return ss
        
        if target == 0:
            return 0
        track = {}
        return get_num_of_ways(nums, target, track)