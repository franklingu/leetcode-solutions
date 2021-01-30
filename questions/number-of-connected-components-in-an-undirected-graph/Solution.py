"""

None
"""


from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        connections = defaultdict(set)
        for v1, v2 in edges:
            connections[v1].add(v2)
            connections[v2].add(v1)
        cnt = 0
        visited = set()
        for i in range(n):
            if i in visited:
                continue
            cnt += 1
            stack = [i]
            while stack:
                curr = stack.pop()
                if curr in visited:
                    continue
                visited.add(curr)
                for ne in connections.get(curr, set()):
                    if ne in visited:
                        continue
                    stack.append(ne)
        return cnt