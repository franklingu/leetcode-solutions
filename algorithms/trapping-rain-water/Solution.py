'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

![Image](https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png)

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''

'''
Use the idea of monotic stack and make sure the stack is always increasing.
If the new entry to be pushed into the stack is found, first try to calculate
the trapped rain by getting max area in between and then substract bars.

Do this for both from left to right and from right to left because for the
first round, everything after heightest bar will be ignored
'''


class Solution:
    def trap(self, heights: List[int]) -> int:
        stack = []
        area = 0
        for i in range(len(heights)):
            height = heights[i]
            if stack and heights[stack[-1]] > height:
                continue
            if stack:
                width = i - stack[-1] - 1
                height = heights[stack[-1]]
                tarea = width * height
                for j in range(stack[-1] + 1, i):
                    tarea -= heights[j]
                area += tarea
            stack.append(i)
        if not stack:
            return area
        index = stack[-1]
        stack = []
        for i in range(len(heights) - 1, index - 1, -1):
            height = heights[i]
            if stack and heights[stack[-1]] > height:
                continue
            if stack:
                width = stack[-1] - i - 1
                height = heights[stack[-1]]
                tarea = width * height
                for j in range(i + 1, stack[-1]):
                    tarea -= heights[j]
                area += tarea
            stack.append(i)
        return area
