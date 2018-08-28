"""
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].
"""
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        def min_cost_climbing(cost, idx, track):
            l = len(cost)
            if idx >= l - 2:
                return cost[idx]
            if idx in track:
                return track[idx]
            s1 = cost[idx] + min_cost_climbing(cost, idx + 1, track)
            s2 = cost[idx] + min_cost_climbing(cost, idx + 2, track)
            if s1 < s2:
                track[idx] = s1
            else:
                track[idx] = s2
            return track[idx]

        track = {}
        s1 = min_cost_climbing(cost, 0, track)
        s2 = min_cost_climbing(cost, 1, track)
        return s1 if s1 < s2 else s2

