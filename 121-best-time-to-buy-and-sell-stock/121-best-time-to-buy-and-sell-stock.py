class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_deal = 0
        min_price = prices[0]

        for i in range(1, len(prices)):
            if prices[i] - min_price > best_deal:
                best_deal = prices[i] - min_price

            if prices[i] < min_price:
                min_price = prices[i]

        return best_deal

            
                