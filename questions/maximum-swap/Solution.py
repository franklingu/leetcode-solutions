'''
Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:
Input: 9973
Output: 9973
Explanation: No swap.
Note:
The given number is in the range [0, 108]
'''


'''
Convert num to a list of digits. Compare prev with current and if previous
is smaller than current, we found some violation. Starting from right to current
find the max, starting from left to current find the first value that is smaller
than max. Then we swap the two.
'''


class Solution:
    def maximumSwap(self, num: int) -> int:
        def find_max(num, target):
            md, mi = num[target + 1], target + 1
            for i in range(target + 1, len(num)):
                if num[i] >= md:
                    md = num[i]
                    mi = i
            return md, mi
        
        num = list(str(num))
        target = None
        for i in range(1, len(num)):
            if num[i] > num[i - 1]:
                target = i - 1
                break
        if target is not None:
            md, mi = find_max(num, target)
            for i in range(target + 1):
                if num[i] < md:
                    num[i], num[mi] = md, num[i]
                    break
        return int(''.join(num))
