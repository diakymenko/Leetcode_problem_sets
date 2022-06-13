class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_profit = 0
        min_value = prices[0]


        for i in range(1, len(prices)):
            if prices[i] > min_value:
                current_profit += prices[i] - min_value
                min_value = prices[i]
            else:
                min_value = prices[i]
        return current_profit