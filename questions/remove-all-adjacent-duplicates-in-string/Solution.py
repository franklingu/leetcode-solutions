"""

Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.
We repeatedly make duplicate removals on S until we no longer can.
Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.
 
Example 1:

Input: "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".

 
Note:

1 <= S.length <= 20000
S consists only of English lowercase letters.


"""


class Solution:
    def removeDuplicates(self, S: str) -> str:
        stk = []
        for a in S:
            if stk and stk[-1] == a:
                stk.pop()
                continue
            stk.append(a)
        return ''.join(stk)