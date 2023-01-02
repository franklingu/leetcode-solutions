"""

Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
You can use each character in text at most once. Return the maximum number of instances that can be formed.
 
Example 1:


Input: text = "nlaebolko"
Output: 1

Example 2:


Input: text = "loonbalxballpoon"
Output: 2

Example 3:

Input: text = "leetcode"
Output: 0

 
Constraints:

1 <= text.length <= 104
text consists of lower case English letters only.


"""


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        base = Counter('balloon')
        tr = {}
        for a in text:
            if a not in base:
                continue
            tr[a] = tr.get(a, 0) + 1
        multiple = len(text)
        for k in base.keys():
            if k not in tr:
                return 0
            multiple = min(multiple, tr[k] // base[k])
        return multiple
