class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        i = len(prices) - 2

        profit = max(0, prices[i + 1] - prices[i])
        maxPrice = max(prices[i], prices[i + 1])

        while i > 0:
            i -= 1
            profit = max(profit, maxPrice - prices[i])
            maxPrice = max(maxPrice, prices[i])

        return profit