class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp = prices[0]
        profit = 0
        for p in prices:
            minp = min(p,minp)
            profit = max(profit,p-minp)
        return profit