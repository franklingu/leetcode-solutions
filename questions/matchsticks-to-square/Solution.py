"""

You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.
Return true if you can make this square and false otherwise.
 
Example 1:


Input: matchsticks = [1,1,2,2,2]
Output: true
Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.

Example 2:

Input: matchsticks = [3,3,3,3,4]
Output: false
Explanation: You cannot find a way to form a square with all the matchsticks.

 
Constraints:

1 <= matchsticks.length <= 15
1 <= matchsticks[i] <= 108


"""


class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 4 != 0:
            return False
        target = s // 4
        if max(nums) > target:
            return False
        nums.sort()
        sides = [target for _ in range(4)]
        
        def can_fill_sides(idx):
            if idx == len(nums):
                return True
            stick = nums[idx]
            seen = set()
            for i in range(4):
                side = sides[i]
                if side in seen or side < stick:
                    continue
                seen.add(side)
                sides[i] = side - stick
                if can_fill_sides(idx + 1):
                    return True
                sides[i] = side
            return False
        
        return can_fill_sides(0)