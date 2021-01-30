"""

None
"""


class Vector2D:

    def __init__(self, v: List[List[int]]):
        self.idx1 = 0
        self.idx2 = 0
        self.v = v

    def next(self) -> int:
        ls = self.v[self.idx1]
        elem = ls[self.idx2]
        if self.idx2 == len(ls) - 1:
            self.idx2 = 0
            self.idx1 += 1
        else:
            self.idx2 += 1
        return elem

    def hasNext(self) -> bool:
        while self.idx1 < len(self.v) and self.idx2 >= len(self.v[self.idx1]):
            self.idx2 = 0
            self.idx1 += 1
        if self.idx1 >= len(self.v):
            return False
        if self.idx2 >= len(self.v[self.idx1]):
            return False
        return True


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()