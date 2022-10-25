class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        count = 0
        for num in nums:
            if num == val:
                count +=1
        
        new_len = len(nums) - count
        pointer = 0
        idx = 0
        
        while pointer <= new_len - 1:
            if nums[idx] != val:
                nums[pointer] = nums[idx]
                pointer+=1
            idx+=1
        return pointer
            
            
        
           
                