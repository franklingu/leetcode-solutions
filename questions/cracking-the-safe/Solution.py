"""

There is a box protected by a password. The password is a sequence of n digits where each digit can be one of the first k digits 0, 1, ..., k-1.
While entering a password, the last n digits entered will automatically be matched against the correct password.
For example, assuming the correct password is "345", if you type "012345", the box will open because the correct password matches the suffix of the entered password.
Return any password of minimum length that is guaranteed to open the box at some point of entering it.
 
Example 1:

Input: n = 1, k = 2
Output: "01"
Note: "10" will be accepted too.

Example 2:

Input: n = 2, k = 2
Output: "00110"
Note: "01100", "10011", "11001" will be accepted too.

 
Note:

n will be in the range [1, 4].
k will be in the range [1, 10].
k^n will be at most 4096.

 

"""


class Solution:
    def crackSafe(self, n: int, k: int) -> str:        
        ans = "0" * (n - 1)
        visits = set()
        for x in range(k ** n):
            current = ans[-n+1:] if n > 1 else ''
            for y in range(k - 1, -1, -1):
                if current + str(y) not in visits:
                    visits.add(current + str(y))
                    ans += str(y)
                    break
        return ans