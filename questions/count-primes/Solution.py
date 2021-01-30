"""
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        candidates = [2]
        for i in range(3, n, 2):
            candidates.append(i)
        primes = set(candidates)
        for i, num in enumerate(candidates):
            if num not in primes:
                continue
            runner = num + num
            while runner <= n:
                if runner in primes:
                    primes.remove(runner)
                runner += num
        return len(primes)
