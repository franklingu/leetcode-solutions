"""

There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly or indirectly through the network.
A critical connection is a connection that, if removed, will make some servers unable to reach some other server.
Return all critical connections in the network in any order.
 
Example 1:


Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.

 
Constraints:

2 <= n <= 105
n - 1 <= connections.length <= 105
0 <= ai, bi <= n - 1
ai != bi
There are no repeated connections.


"""


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        def build_graph(connetions, n):
            graph = [[] for _ in range(n)]
            for u, v in connections:
                graph[u].append(v)
                graph[v].append(u)
            return graph
        
        def dfs(i, pre, graph, low, order, ret, index):
            order[i] = index[0]
            low[i] = index[0]
            index[0] = index[0] + 1
            for ne in graph[i]:
                if ne == pre:
                    continue
                if order[ne] is None:
                    dfs(ne, i, graph, low, order, ret, index)
                    low[i] = min(low[i], low[ne])
                    if low[ne] > order[i]:
                        ret.append([i, ne])
                else:
                    low[i] = min(low[i], order[ne])
                    
        
        graph = build_graph(connections, n)
        low = [None for _ in range(n)]
        order = [None for _ in range(n)]
        ret = []
        index = [0]
        for i in range(n):
            if order[i] is None:
                dfs(i, -1, graph, low, order, ret, index)
        return ret