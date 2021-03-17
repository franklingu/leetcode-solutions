"""


Given a non-negative integer N, find the largest number that is less than or equal to N with monotone increasing digits.

(Recall that an integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.)

Example 1:

Input: N = 10
Output: 9


Example 2:

Input: N = 1234
Output: 1234


Example 3:

Input: N = 332
Output: 299


Note:
N is an integer in the range [0, 10^9].

"""


class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        def build_mono(a):
            r = [0 for _ in a]
            for i, n in enumerate(a):
                if i == 0:
                    r[i] = n
                    continue
                if n >= r[i - 1]:
                    r[i] = n
                    continue
                j = i - 1
                while j >= 0:
                    r[j] -= 1
                    if j > 0 and r[j] < r[j - 1]:
                        j -= 1
                    else:
                        break
                for k in range(j + 1, len(a)):
                    r[k] = 9
                break
            return r
        
        a = []
        while N > 0:
            q, r = divmod(N, 10)
            a.append(r)
            N = q
        a = a[::-1]
        return int(''.join([str(e) for e in build_mono(a)]))
        