"""

Given integer array nums, return the third maximum number in this array. If the third maximum does not exist, return the maximum number.
 
Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation: The third maximum is 1.

Example 2:

Input: nums = [1,2]
Output: 2
Explanation: The third maximum does not exist, so the maximum (2) is returned instead.

Example 3:

Input: nums = [2,2,3,1]
Output: 1
Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.

 
Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1

 
Follow up: Can you find an O(n) solution?
"""


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m1 = m2 = m3 = None
        for n in nums:
            if m1 is None or n > m1:
                m3 = m2
                m2 = m1
                m1 = n
            elif n == m1:
                pass
            else:
                if m2 is None or n > m2:
                    m3 = m2
                    m2 = n
                elif n == m2:
                    pass
                else:
                    if m3 is None or n > m3:
                        m3 = n
        return m3 if m3 is not None else m1