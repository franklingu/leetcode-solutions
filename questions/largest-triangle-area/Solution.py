"""
You have a list of points in the plane. Return the area of the largest triangle that can be formed by any 3 of the points.

Example:
Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2
Explanation:
The five points are show in the figure below. The red triangle is the largest.

![fig](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/04/1027.png)

Notes:

3 <= points.length <= 50.
No points will be duplicated.
 -50 <= points[i][j] <= 50.
 Answers within 10^-6 of the true value will be accepted as correct.
"""
class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        def calcArea(p1, p2, p3):
            u = ((p2[0] - p1[0]) * (p3[0] - p1[0]) + (p2[1] - p1[1]) * (p3[1] - p1[1]))
            l1 = (((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5)
            l2 = (((p3[0] - p1[0]) ** 2 + (p3[1] - p1[1]) ** 2) ** 0.5)
            try:
                cosine = u / (l1 * l2)
            except ZeroDivisionError:
                return 0
            if abs(cosine) > 1:
                cosine = 1 if cosine > 0 else -1
            sine = (1 - cosine ** 2) ** 0.5
            return l1 * l2 * sine / 2

        m = 0
        for i, p1 in enumerate(points):
            for j, p2 in enumerate(points):
                if j <= i:
                    continue
                for p3 in points[j + 1:]:
                    a = calcArea(p1, p2, p3)
                    m = max(m, a)
        return m
