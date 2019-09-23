"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

![Image1](https://assets.leetcode.com/uploads/2018/10/12/histogram.png)


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

![Image2](https://assets.leetcode.com/uploads/2018/10/12/histogram_area.png)


The largest rectangle is shown in the shaded area, which has area = 10 unit.

 

Example:

Input: [2,1,5,6,2,3]
Output: 10
"""


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0
        for i, num in enumerate(heights):
            while stack and num < heights[stack[-1]]:
                idx = stack.pop()
                h = heights[idx]
                if stack:
                    prev_idx = stack[-1]
                else:
                    prev_idx = -1
                curr_area = h * (i - prev_idx - 1)
                area = max(area, curr_area)
            stack.append(i)
        if not stack:
            return area
        while stack:
            idx = stack.pop()
            h = heights[idx]
            if stack:
                prev_idx = stack[-1]
            else:
                prev_idx = -1
            curr_area = h * (len(heights) - prev_idx - 1)
            area = max(area, curr_area)
        return area
