"""

An integer array original is transformed into a doubled array changed by appending twice the value of every element in original, and then randomly shuffling the resulting array.
Given an array changed, return original if changed is a doubled array. If changed is not a doubled array, return an empty array. The elements in original may be returned in any order.
 
Example 1:

Input: changed = [1,3,4,2,6,8]
Output: [1,3,4]
Explanation: One possible original array could be [1,3,4]:
- Twice the value of 1 is 1 * 2 = 2.
- Twice the value of 3 is 3 * 2 = 6.
- Twice the value of 4 is 4 * 2 = 8.
Other original arrays could be [4,3,1] or [3,1,4].

Example 2:

Input: changed = [6,3,0,1]
Output: []
Explanation: changed is not a doubled array.

Example 3:

Input: changed = [1]
Output: []
Explanation: changed is not a doubled array.

 
Constraints:

1 <= changed.length <= 105
0 <= changed[i] <= 105


"""


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []
        ret = []
        cnt = Counter(changed)
        sks = list(sorted(cnt.keys()))
        i = 0
        while i < len(sks):
            a = sks[i]
            if cnt[a] == 0:
                i += 1
                continue
            a2 = a + a
            if cnt.get(a2, 0) <= 0:
                return []
            ret.append(a)
            cnt[a] -= 1
            cnt[a2] -= 1
            if cnt[a] == 0:
                i += 1
        return ret
    