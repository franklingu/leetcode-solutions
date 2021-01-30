"""

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
Return the max sliding window.
 
Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:

Input: nums = [1], k = 1
Output: [1]

Example 3:

Input: nums = [1,-1], k = 1
Output: [1,-1]

Example 4:

Input: nums = [9,11], k = 2
Output: [11]

Example 5:

Input: nums = [4,-2], k = 2
Output: [4]

 
Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length


"""


from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        q = deque()
        for index in range(0, k):
            while q and nums[index] >= q[0][0]:
                q.popleft()
            while q and nums[index] >= q[-1][0]:
                q.pop()
            q.append((nums[index], index))
        ret = []
        for index in range(k, len(nums)):
            ret.append(q[0][0])
            num = nums[index]
            if q[0][1] <= index - k:
                q.popleft()
            while q and num >= q[0][0]:
                q.popleft()
            while q and num >= q[-1][0]:
                q.pop()
            q.append((num, index))
        ret.append(q[0][0])
        return ret