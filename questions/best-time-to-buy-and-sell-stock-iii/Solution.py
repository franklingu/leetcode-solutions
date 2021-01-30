"""

Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most two transactions.
Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
 
Example 1:

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.

Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

Example 4:

Input: prices = [1]
Output: 0

 
Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 105


"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
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
        while len(prices) // 2 > 2:
            remove_one_transaction(prices)
        return get_profit(prices)