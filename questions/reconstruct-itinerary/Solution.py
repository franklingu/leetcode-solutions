"""

Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.
Note:

If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
One must use all the tickets once and only once.

Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]

Example 2:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.


"""


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        import collections
        targets = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a] += b,
        route = []
        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)
        visit('JFK')
        return route[::-1]


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for st, ed in tickets:
            graph[st].append(ed)
        for st in graph:
            graph[st].sort()
        final_path = []
        
        def visit(curr, path):
            if final_path:
                return
            path.append(curr)
            if not graph:
                for p in path:
                    final_path.append(p)
                return
            nes = graph.get(curr, [])
            for ne in nes:
                idx = graph[curr].index(ne)
                graph[curr].remove(ne)
                if len(graph[curr]) == 0:
                    del graph[curr]
                visit(ne, path)
                graph[curr].insert(idx, ne)
            path.pop()
                
        
        visit('JFK', [])
        return final_path
        