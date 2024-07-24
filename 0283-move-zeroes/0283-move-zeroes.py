class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                # without python magic
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp

                # python magic way to swap variables
                # nums[left], nums[right] = nums[right], nums[left]
                left += 1
        
        
#         left = 0
#         right = 0
        
#         while right < len(nums):
#             if nums[right] != 0:
#                 nums[left] = nums[right]
#                 left += 1
#             right += 1
#         while left < len(nums):
#             nums[left] = 0
#             left += 1
            
                

    
        
