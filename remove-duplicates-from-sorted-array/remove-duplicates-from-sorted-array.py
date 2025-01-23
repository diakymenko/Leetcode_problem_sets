class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 1
        num = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] != num:
                num = nums[i]
                nums[idx] = nums[i]
                idx += 1
        return idx
                
                
            