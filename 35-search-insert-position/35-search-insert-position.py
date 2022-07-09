class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        idx = 0
        
        if len(nums) == 1:
            if target > nums[0]:
                return 1
            else:
                return 0
        
        for i in range(1, len(nums)):
            if nums[i - 1] == target:
                return i - 1
            elif target > nums[-1]:
                return len(nums)
            if nums[i-1] <= target <= nums[i]:
                return i
            elif target < nums[i-1]:
                return i-1
            
        