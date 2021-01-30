"""

Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.
Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.
 
Example 1:
Input: n = 12
Output: 21
Example 2:
Input: n = 21
Output: -1

 
Constraints:

1 <= n <= 231 - 1


"""


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        def find_next_greater(n1):
            prev = None
            for i in range(len(n1) - 1, -1, -1):
                curr = n1[i]
                if prev is None:
                    prev = curr
                    continue
                if curr >= prev:
                    prev = curr
                    continue
                mm, midx = prev, i + 1
                for j in range(i + 2, len(n1)):
                    tmp = n1[j]
                    if curr < tmp <= mm:
                        mm = tmp
                        midx = j
                break
            else:
                return -1
            n1[i], n1[midx] = n1[midx], n1[i]
            i1, i2 = i + 1, len(n1) - 1
            while i1 < i2:
                n1[i1], n1[i2] = n1[i2], n1[i1]
                i1 += 1
                i2 -= 1
            return int(''.join(n1))
        
        n1 = list(str(n))
        n2 = find_next_greater(n1)
        if n2 > 2147483647:
            return -1
        return n2