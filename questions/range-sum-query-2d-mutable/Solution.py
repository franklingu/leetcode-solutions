"""

None
"""


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        for row in matrix:
            for col in range(1, len(row)):
                row[col] += row[col-1]
        self.matrix = matrix

    def update(self, row: int, col: int, val: int) -> None:
        original = self.matrix[row][col]
        if col != 0:
            original -= self.matrix[row][col-1]
            
        diff = original - val
        
        for y in range(col, len(self.matrix[0])):
            self.matrix[row][y] -= diff

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        for x in range(row1, row2+1):
            sum += self.matrix[x][col2]
            if col1 != 0:
                sum -= self.matrix[x][col1-1]
        return sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)