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
        min_num_idx = 0
        max_num_idx = 0

        for idx, num in enumerate(prices):
            if num < min_num:
                min_num = num
                min_num_idx = idx
                max_num = 0
            if num > max_num and idx > min_num_idx:
                max_num = num
                max_num_idx = idx
            if max_num - min_num > diff and min_num_idx < max_num_idx:
                diff = max_num - min_num
        return diff

            
                