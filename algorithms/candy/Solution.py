'''
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

Example 1:

Input: [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
             The third child gets 1 candy because it satisfies the above two conditions.

'''

'''
Initialize all candies to be 1.
Run from left to right, if current is bigger than previous, set
current's candy to be bigger than previous.
And run from right to left, if current is biggern than previous,
set current's candy to be max of previous can + 1 and current candy.

Essentially greedy.
'''


class Solution:
    def candy(self, ratings: List[int]) -> int:
        nums = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i - 1] < ratings[i]:
                nums[i] = nums[i - 1] + 1
        for i in range(len(ratings) - 1, 0, -1):
            if ratings[i - 1] > ratings[i]:
                nums[i - 1] = max(nums[i] + 1, nums[i - 1])
        return sum(nums)
