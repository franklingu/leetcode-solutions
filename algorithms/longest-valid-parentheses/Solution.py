"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
"""

"""
Starting from left, keep count of opening - closing. If count is
bigger than 0, we do nothing; if count is smaller than 0, we reset;
if count is equal to 0, we found something that are valid and record
the length.
Then starting from right.
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        count, start, mm = 0, 0, 0
        for i, c in enumerate(s):
            if c == '(':
                count += 1
            else:
                count -= 1
            if count < 0:
                count = 0
                start = i + 1
            elif count == 0:
                mm = max(mm, i - start + 1)
        count, start = 0, 0
        for i, c in enumerate(reversed(s)):
            if c == ')':
                count += 1
            else:
                count -= 1
            if count < 0:
                count = 0
                start = i + 1
            elif count == 0:
                mm = max(mm, i - start + 1)
        return mm
