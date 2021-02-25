"""

Given a balanced parentheses string S, compute the score of the string based on the following rule:

() has score 1
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.

 

Example 1:

Input: "()"
Output: 1


Example 2:

Input: "(())"
Output: 2


Example 3:

Input: "()()"
Output: 2


Example 4:

Input: "(()(()))"
Output: 6

 
Note:

S is a balanced parentheses string, containing only ( and ).
2 <= S.length <= 50






"""


class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stk = []
        for c in S:
            if c == '(':
                stk.append(c)
                continue
            val = 0
            while stk and stk[-1] != '(':
                val += stk[-1]
                stk.pop()
            if stk and stk[-1] == '(':
                stk.pop()
            if val == 0:
                stk.append(1)
            else:
                stk.append(val * 2)
        return sum(stk)
        