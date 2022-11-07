"""

You are given an array trees where trees[i] = [xi, yi] represents the location of a tree in the garden.
You are asked to fence the entire garden using the minimum length of rope as it is expensive. The garden is well fenced only if all the trees are enclosed.
Return the coordinates of trees that are exactly located on the fence perimeter.
 
Example 1:


Input: points = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
Output: [[1,1],[2,0],[3,3],[2,4],[4,2]]

Example 2:


Input: points = [[1,2],[2,2],[4,2]]
Output: [[4,2],[2,2],[1,2]]

 
Constraints:

1 <= points.length <= 3000
points[i].length == 2
0 <= xi, yi <= 100
All the given points are unique.


"""


class Solution:
    def outerTrees(self, points: List[List[int]]) -> List[List[int]]:
        def cross(p1, p2, p3):
            return (p2[0]-p1[0])*(p3[1]-p1[1])-(p2[1]-p1[1])*(p3[0]-p1[0])

        start = min(points)
        points.pop(points.index(start))
        points.sort(key=lambda p: (atan2(p[1]-start[1], p[0]-start[0]), -p[1], p[0]))

        ans = [start]
        for p in points:
            ans.append(p)
            while len(ans) > 2 and cross(*ans[-3:]) < 0:
                ans.pop(-2)
        return ans