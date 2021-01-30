"""
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

 

 

Example 1:

![img1](https://assets.leetcode.com/uploads/2019/10/15/untitled-diagram-2.jpg)

Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true
Example 2:

![img2](https://assets.leetcode.com/uploads/2019/10/09/untitled-diagram-1.jpg)

Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false
 

Constraints:

2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point.
"""


class Solution:
    def checkStraightLine(self, coords: List[List[int]]) -> bool:
        def is_same_line(p1, p2, p3):
            return (p1[0] - p2[0]) * (p1[1] - p3[1]) == (p1[1] - p2[1]) * (p1[0] - p3[0])
        
        if len(coords) <= 2:
            return True
        for i, coord in enumerate(coords):
            if i < 2:
                continue
            if not is_same_line(coords[0], coords[1], coord):
                return False
        return True
