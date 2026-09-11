class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        revPrice = sorted(prices, reverse=True)
        if len(prices) <= 1 or revPrice == prices:
            return 0
        left = 0
        right = 1
        maxProfit = 0
        while right < len(prices):
            if prices[right] - prices[left] < 0:
                left = right
                right += 1
            else:
                maxProfit = max(maxProfit, prices[right] - prices[left])
                right += 1
        return maxProfit