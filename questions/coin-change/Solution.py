"""

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.
 
Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3
Output: -1

Example 3:

Input: coins = [1], amount = 0
Output: 0

Example 4:

Input: coins = [1], amount = 1
Output: 1

Example 5:

Input: coins = [1], amount = 2
Output: 2

 
Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104


"""


import collections

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ### method 1: BFS, model it as a graph problem
        # queue = collections.deque()
        # queue.append((0, 0))
        # visited = set()
        # while queue:
        #     curr, step = queue.popleft()
        #     if curr == amount:
        #         return step
        #     if curr in visited or curr > amount:
        #         continue
        #     visited.add(curr)
        #     for coin in coins:
        #         neighbor = curr + coin
        #         if neighbor in visited:
        #             continue
        #         queue.append((neighbor, step + 1))
        # return -1
        ### method 2: dp
        dp = [0] + [None] * amount
        for i in range(1, amount + 1):
            candidates = list(filter(lambda x: x is not None, [dp[i - c] if i - c >= 0 else None for c in coins]))
            dp[i] = min(candidates) + 1 if candidates else None
        return dp[amount] if dp[amount] is not None else -1