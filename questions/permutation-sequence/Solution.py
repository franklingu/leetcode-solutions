"""
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
"""


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        facts = [0]
        fact = 1
        for i in range(1, n):
            fact *= i
            facts.append(fact)
        facts = facts[::-1]
        candidates = list(range(1, n + 1))
        ret = []
        k -= 1
        for i in range(n):
            if facts[i] != 0:
                index, k = divmod(k, facts[i])
            else:
                index, k = 0, 0
            ret.append(candidates[index])
            del candidates[index]
        return ''.join((str(e) for e in ret))
