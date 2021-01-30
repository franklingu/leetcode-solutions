"""
Say you have an array for which the i-th element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example 1:

Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
"""



class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        def get_transactions(prices):
            if len(prices) < 2:
                return []
            ret = []
            start = prices[0]
            for i, price in enumerate(prices):
                if i == 0:
                    continue
                if price < prices[i - 1]:
                    if start < prices[i - 1]:
                        ret.append(start)
                        ret.append(prices[i - 1])
                    start = price
            if prices[-1] > start:
                ret.append(start)
                ret.append(prices[-1])
            return ret
        
        def remove_one_transaction(prices):
            merge_pos = 0
            cost = None
            for i, price in enumerate(prices):
                if i == 0:
                    continue
                if cost is None or cost > abs(prices[i] - prices[i - 1]):
                    merge_pos = i - 1
                    cost = abs(prices[i] - prices[i - 1])
            del prices[merge_pos:merge_pos + 2]
        
        def get_profit(prices):
            ret = 0
            for i in range(0, len(prices), 2):
                ret = ret + prices[i + 1] - prices[i]
            return ret
        
        prices = get_transactions(prices)
        while len(prices) // 2 > k:
            remove_one_transaction(prices)
        return get_profit(prices)
