"""

You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.
We will send a signal from a given node k. Return the time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.
 
Example 1:


Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2

Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1

Example 3:

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1

 
Constraints:

1 <= k <= n <= 100
1 <= times.length <= 6000
times[i].length == 3
1 <= ui, vi <= n
ui != vi
0 <= wi <= 100
All the pairs (ui, vi) are unique. (i.e., no multiple edges.)


"""


import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        def build_graph(times):
            graph = {}
            for source, dest, weight in times:
                if source not in graph:
                    graph[source] = {}
                graph[source][dest] = weight
            return graph
        
        graph = build_graph(times)
        pq = [(0, K)]
        visited = set()
        while pq and len(visited) < N:
            time, node = heapq.heappop(pq)
            if node in visited:
                continue
            visited.add(node)
            for neighbor, weight in graph.get(node, {}).items():
                if neighbor in visited:
                    continue
                heapq.heappush(pq, (time + weight, neighbor))
        if len(visited) != N:
            return -1
        return time