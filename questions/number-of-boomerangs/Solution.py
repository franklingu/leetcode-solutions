"""

You are given n points in the plane that are all distinct, where points[i] = [xi, yi]. A boomerang is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).
Return the number of boomerangs.
 
Example 1:

Input: points = [[0,0],[1,0],[2,0]]
Output: 2
Explanation: The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]].

Example 2:

Input: points = [[1,1],[2,2],[3,3]]
Output: 2

Example 3:

Input: points = [[1,1]]
Output: 0

 
Constraints:

n == points.length
1 <= n <= 500
points[i].length == 2
-104 <= xi, yi <= 104
All the points are unique.


"""


class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def get_distance(p1, p2):
            return (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2
        
        def update_track(track, i, j, dist):
            if i not in track:
                track[i] = {}
            if dist not in track[i]:
                track[i][dist] = []
            track[i][dist].append(j)

        track = {}
        for i, p1 in enumerate(points):
            for j, p2 in enumerate(points):
                if j >= i:
                    continue
                dist = get_distance(p1, p2)
                update_track(track, i, j, dist)
                update_track(track, j, i, dist)
        l = 0
        for i, val in track.iteritems():
            for dist, ll in val.iteritems():
                l1 = len(ll)
                l += ((l1 - 1) * l1)
        return l