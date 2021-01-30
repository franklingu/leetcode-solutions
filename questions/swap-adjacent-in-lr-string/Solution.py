"""

In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR". Given the starting string start and the ending string end, return True if and only if there exists a sequence of moves to transform one string to the other.
 
Example 1:

Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
Output: true
Explanation: We can transform start to end following these steps:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX

Example 2:

Input: start = "X", end = "L"
Output: false

Example 3:

Input: start = "LLR", end = "RRL"
Output: false

Example 4:

Input: start = "XL", end = "LX"
Output: true

Example 5:

Input: start = "XLLR", end = "LXLX"
Output: false

 
Constraints:

1 <= start.length <= 104
start.length == end.length
Both start and end will only consist of characters in 'L', 'R', and 'X'.


"""


from collections import Counter


class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        # basic check, number of each elements must be the same
        if Counter(start) != Counter(end):
            return False
        i, j = 0, 0
        N = len(start)
        while i < N and j < N:
            while i < N and start[i] == 'X':
                i += 1
            while j < N and end[j] == 'X':
                j += 1
            if i == N and j == N:
                continue
            elif i == N or j == N:
                return False
            # L can be moved left and R can be moved right
            # and L and R cannot cross
            # so current element in start and end must be the same
            # L in start must be same position or right
            # R in start must be same position or left
            if start[i] != end[j]:
                return False
            elif start[i] == 'L' and i < j:
                return False
            elif start[i] == 'R' and i > j:
                return False
            i += 1
            j += 1
        return True
            