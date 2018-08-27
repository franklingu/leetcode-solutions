"""
On a 2 dimensional grid with R rows and C columns, we start at (r0, c0) facing east.

Here, the north-west corner of the grid is at the first row and column, and the south-east corner of the grid is at the last row and column.

Now, we walk in a clockwise spiral shape to visit every position in this grid.

Whenever we would move outside the boundary of the grid, we continue our walk outside the grid (but may return to the grid boundary later.)

Eventually, we reach all R * C spaces of the grid.

Return a list of coordinates representing the positions of the grid in the order they were visited.



 Example 1:

 Input: R = 1, C = 4, r0 = 0, c0 = 0
 Output: [[0,0],[0,1],[0,2],[0,3]]


  ![Image](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/24/example_1.png)

  Example 2:

  Input: R = 5, C = 6, r0 = 1, c0 = 4
  Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]


   ![Image](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/24/example_2.png)

   Note:

   1 <= R <= 100
   1 <= C <= 100
   0 <= r0 < R
   0 <= c0 < C

"""
class Solution(object):
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        def change_dire(dire):
            if dire[0] == 0 and dire[1] == 1:
                return [1, 0]
            elif dire[0] == 1 and dire[1] == 0:
                return [0, -1]
            elif dire[0] == 0 and dire[1] == -1:
                return [-1, 0]
            else:
                return [0, 1]

        curr = [r0, c0]
        dire = [0, 1]
        step_b, acc = 2, 1
        ll1, ll2, final = 1, 1, R * C
        ret = [curr]
        while ll2 < final:
            if ll1 == step_b * step_b:
                acc += 1
                step_b += 1
            elif acc == step_b:
                dire = change_dire(dire)
                acc = 2
            else:
                acc += 1
            curr = [curr[0] + dire[0], curr[1] + dire[1]]
            # print(dire, curr, acc, step_b)
            ll1 += 1
            if curr[0] < 0 or curr[0] >= R or curr[1] < 0 or curr[1] >= C:
                continue
            ret.append(curr)
            ll2 += 1
        return ret

