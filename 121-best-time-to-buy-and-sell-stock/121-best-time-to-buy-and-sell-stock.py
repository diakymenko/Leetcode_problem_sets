class Solution:
    def maxProfit(self, prices: List[int]) -> int:
#         diff = 0
        
#         for i in range(len(prices)):
#             for j in range(i+1, len(prices)):
#                 if prices[j] - prices[i] > diff:
#                     diff = prices[j] - prices[i]
#         return diff
        diff = 0
        min_num = prices[0]
        max_num = 0


        for i in range(1, len(prices)):
            if prices[i] < min_num:
                min_num = prices[i]
            if prices[i] - min_num > diff:
                diff = prices[i] - min_num

        return diff

            
                