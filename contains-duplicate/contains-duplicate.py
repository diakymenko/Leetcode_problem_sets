class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        
        prev = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] == prev:
                return True
            prev = nums[i]
        return False