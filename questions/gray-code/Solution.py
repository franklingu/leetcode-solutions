"""

The gray code is a binary numeral system where two successive values differ in only one bit.
Given an integer n representing the total number of bits in the code, return any sequence of gray code.
A gray code sequence must begin with 0.
 
Example 1:

Input: n = 2
Output: [0,1,3,2]
Explanation:
00 - 0
01 - 1
11 - 3
10 - 2
[0,2,3,1] is also a valid gray code sequence.
00 - 0
10 - 2
11 - 3
01 - 1

Example 2:

Input: n = 1
Output: [0,1]

 
Constraints:

1 <= n <= 16


"""


class Solution:
    def grayCode(self, n: int) -> List[int]:
        ### method 1: dfs search
        # res = []
        # visited = set()
        # stk = [0]
        # while stk:
        #     curr = stk.pop()
        #     if curr in visited:
        #         continue
        #     res.append(curr)
        #     visited.add(curr)
        #     for idx in range(n):
        #         bit = (curr >> idx) & 1
        #         if bit == 0:
        #             neigh = curr | (1 << idx)
        #         else:
        #             neigh = curr & (~(1 << idx))
        #         if neigh not in visited:
        #             stk.append(neigh)
        # return res
        ### method 2: build the later half of sequence by reversing previous
        result = [0]
        for i in range(n):
            result += [x + 2**i for x in result[::-1]]
        return result