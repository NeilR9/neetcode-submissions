class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        revPrice = sorted(prices, reverse=True)
        if len(prices) <= 1 or revPrice == prices:
            return 0
        
        maxPrice = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                maxPrice = max(maxPrice, prices[j] - prices[i])
        return maxPrice