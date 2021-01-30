'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

 
![Image](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg)


The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

 

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49

'''

'''
Classic two pointer problem
'''


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start, end = 0, len(heights) - 1
        mm = None
        while start < end:
            area = min(heights[start], heights[end]) * (end - start)
            if mm is None or area > mm:
                mm = area
            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1
        return mm
