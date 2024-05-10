class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # the idea is to sum up all positive returns 
        total = 0

        for i in range(1, len(prices)):
            if prices[i] - prices[i-1] > 0:
                total += prices[i] - prices[i-1]
        return total
        

                


