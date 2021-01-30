"""

Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.


Note: 
You may assume k is always valid, 1 ≤ k ≤ n2.
"""


import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ## method 1, using heap
        hp = [(row[0], 0, i) for i, row in enumerate(matrix)]
        heapq.heapify(hp)
        for _ in range(k):
            curr, idx, row_idx = heapq.heappop(hp)
            idx += 1
            if idx < len(matrix[row_idx]):
                heapq.heappush(hp, (matrix[row_idx][idx], idx, row_idx))
        return curr