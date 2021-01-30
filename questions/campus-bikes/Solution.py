"""

None
"""


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        distances = []
        for i, worker in enumerate(workers):
            for j, bike in enumerate(bikes):
                distances.append((abs(worker[0] - bike[0]) + abs(worker[1] - bike[1]), i, j))
        distances.sort()
        assigned = set()
        taken = set()
        track = [-1] * len(workers)
        for dist, i, j in distances:
            if i in assigned or j in taken:
                continue
            assigned.add(i)
            taken.add(j)
            track[i] = j
            if len(assigned) == len(workers):
                break
        return track