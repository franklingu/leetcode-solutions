"""
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

Example:

Input: 13
Output: 6 
Explanation: Digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
"""


class Solution:
    def countDigitOne(self, n: int) -> int:
        cnt = 0
        mark = 1
        while n >= mark:
            c, r = divmod(n, (mark * 10))
            cnt += c * mark
            if r >= mark:
                cnt += min(r - mark + 1, mark)
            mark *= 10
        return cnt
        