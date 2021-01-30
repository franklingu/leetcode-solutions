"""

None
"""


# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, mat: 'BinaryMatrix') -> int:
        n, m = mat.dimensions()
        ret = -1
        x, y = 0, m - 1
        while y >= 0 and x < n:
            val = mat.get(x, y)
            if val == 0:
                x += 1
            else:
                ret = y
                y -= 1
        return ret