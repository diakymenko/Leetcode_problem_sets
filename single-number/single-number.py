class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        count = 1
        nums.sort()
        num = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] != num and count == 1:
                return num
            elif nums[i] != num and count > 1:
                count = 1
                num = nums[i]
            else:
                count += 1
        return num

     

            