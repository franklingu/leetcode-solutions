/**
 * Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
 *
 * Example 1:
 *
 * Input: [[1,1],[2,2],[3,3]]
 * Output: 3
 * Explanation:
 * ^
 * |
 * |        o
 * |     o
 * |  o
 * +------------->
 * 0  1  2  3  4
 * Example 2:
 *
 * Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
 * Output: 4
 * Explanation:
 * ^
 * |
 * |  o
 * |     o        o
 * |        o
 * |  o        o
 * +------------------->
 * 0  1  2  3  4  5  6
 */

/**
 * Definition for a point.
 * class Point {
 *     int x;
 *     int y;
 *     Point() { x = 0; y = 0; }
 *     Point(int a, int b) { x = a; y = b; }
 * }
 */
class Solution {
    public int maxPoints(Point[] points) {
        if (points.length < 2) {
            return points.length;
        }
        Map<String, Set<Integer>> track = new HashMap<String, Set<Integer>>();
        for (int i = 0; i < points.length; i++) {
            Point p1 = points[i];
            for (int j = i + 1; j < points.length; j++) {
                Point p2 = points[j];
                String key = getKey(p1, p2);
                Set<Integer> ps;
                if (track.containsKey(key)) {
                    ps = track.get(key);
                } else {
                    ps = new HashSet<Integer>();
                    track.put(key, ps);
                }
                ps.add(i);
                ps.add(j);
            }
        }
        int m = 0;
        for (String k : track.keySet()) {
            Set<Integer> s = track.get(k);
            if (m < s.size()) {
                m = s.size();
            }
        }
        return m;
    }

    String getKey(Point p1, Point p2) {
        int[] i = getSimple(p1.y - p2.y, p1.x - p2.x);
        int[] j;
        if (i[0] == 0) {
            j = new int[]{p1.y, 1};
        } else if (i[1] == 0) {
            j = new int[]{p1.x, 0};
        } else {
            j = getSimple((p1.y * i[1] - i[0] * p1.x), i[1]);
        }
        return String.format("%d|%d|%d|%d", i[0], i[1], j[0], j[1]);
    }

    int[] getSimple(int a, int b) {
        if (b == 0) {
            return new int[]{1, 0};
        } else if (a == 0) {
            return new int[]{0, 1};
        } else if (a < 0 && b < 0) {
            return getSimple(-a, -b);
        } else if (a >= 0 && b < 0) {
            a = -a;
            b = -b;
        }
        int g = Math.abs(gcd(a, b));
        if (g == 1) {
            return new int[]{a, b};
        } else {
            return getSimple(a / g, b / g);
        }
    }

    int gcd(int a, int b) {
        if (a == 0) {
            return Math.abs(b);
        } else if (b < 0 && a < 0) {
            b = -b;
            a = -a;
        } else if (b < 0) {
            b = -b;
            a = -a;
        }
        if (Math.abs(a) < Math.abs(b)) {
            return gcd(b % a, a);
        } else {
            return gcd(a % b, b);
        }
    }
}
